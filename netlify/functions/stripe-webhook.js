const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const ghl = require('./utils/ghl');
const logger = require('./utils/logger');

const headers = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, stripe-signature'
};

// Case-insensitive header lookup helper
const getHeader = (headers, key) => {
  const lowerKey = key.toLowerCase();
  for (const k of Object.keys(headers)) {
    if (k.toLowerCase() === lowerKey) return headers[k];
  }
  return null;
};

/**
 * Handles incoming webhooks from Stripe after successful checkout.
 */
exports.handler = async (event, context) => {
  // CORS Preflight
  if (event.httpMethod === 'OPTIONS') return { statusCode: 200, headers, body: '' };
  if (event.httpMethod !== 'POST') return { statusCode: 405, headers, body: '' };

  const signature = getHeader(event.headers, 'stripe-signature');
  const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let stripeEvent;

  try {
    // 1. Verify Webhook Authenticity
    // In Netlify, event.body is already a string (raw body) if it's text/plain or application/json.
    // However, if the body is base64 encoded by Netlify, we need to decode it.
    const rawBody = event.isBase64Encoded ? Buffer.from(event.body, 'base64').toString('utf8') : event.body;

    stripeEvent = stripe.webhooks.constructEvent(
      rawBody,
      signature,
      endpointSecret
    );
  } catch (err) {
    logger.error('Stripe Webhook Verification Failed', err.message);
    return { statusCode: 400, headers, body: `Webhook Error: ${err.message}` };
  }

  // 2. Process the Event
  if (stripeEvent.type === 'checkout.session.completed') {
    const session = stripeEvent.data.object;
    
    logger.info('Processing Successful Stripe Checkout', { sessionId: session.id });

    const plan = session.metadata.plan || 'none';
    const market = session.metadata.market || 'us';
    const type = session.metadata.type || 'setup';
    const amountType = session.metadata.amount_type || type;
    const creditPolicy = session.metadata.credit_policy || 'none';

    // 3. Extract Customer Info
    const contactData = {
      email: session.customer_details.email,
      firstName: session.customer_details.name.split(' ')[0] || (session.metadata.customer_name && session.metadata.customer_name.split(' ')[0]) || '',
      lastName: session.customer_details.name.split(' ').slice(1).join(' ') || (session.metadata.customer_name && session.metadata.customer_name.split(' ').slice(1).join(' ')) || '',
      phone: session.customer_details.phone || '',
      tags: [
        'stripe-purchase', 
        'stripe-checkout-completed', 
        plan !== 'none' ? plan : '', 
        market ? `market-${market}` : '', 
        type === 'audit' ? 'audit-deposit' : 'setup-payment'
      ].filter(Boolean)
    };

    try {
      // 4. Create/Update Contact in GHL
      const upsertResult = await ghl.upsertContact(contactData);
      const contact = upsertResult.contact;
      const contactId = contact.id || (contact.contact ? contact.contact.id : null);
      const contactStatus = upsertResult.status;
      logger.info('GHL Contact processing complete', { email: contactData.email, contactId, status: contactStatus });

      // 5. Dynamic Map Plan to GHL Stage
      const stageMapping = {
        'lite': process.env.GHL_SALE_LITE_ID || 'a0296611-9844-4c19-b344-e4d028c70c69',
        'starter': process.env.GHL_SALE_STARTER_ID || process.env.GHL_SALE_LITE_ID || 'a0296611-9844-4c19-b344-e4d028c70c69',
        'capture': process.env.GHL_SALE_CAPTURE_ID || process.env.GHL_SALE_LITE_ID || 'a0296611-9844-4c19-b344-e4d028c70c69',
        'growth': process.env.GHL_SALE_GROWTH_ID || 'bb4b9701-abc6-42cd-8690-0f4df07bd8ea',
        'pro': process.env.GHL_SALE_PRO_ID || '9176acb4-3c14-46bf-b196-34682e4b0c34',
        'discovery': process.env.GHL_AUDIT_STAGE_ID || process.env.GHL_STAGE_ID || 'b621db30-363f-42e5-a0ed-4a00465d8363' // Discovery Call (matches Netlify: GHL_AUDIT_STAGE_ID)
      };

      if (!process.env.GHL_SALE_LITE_ID) logger.warn('Missing GHL_SALE_LITE_ID env var, using fallback');
      if (!process.env.GHL_SALE_GROWTH_ID) logger.warn('Missing GHL_SALE_GROWTH_ID env var, using fallback');
      if (!process.env.GHL_SALE_PRO_ID) logger.warn('Missing GHL_SALE_PRO_ID env var, using fallback');
      if (!process.env.GHL_AUDIT_STAGE_ID && !process.env.GHL_STAGE_ID) logger.warn('Missing GHL_AUDIT_STAGE_ID and GHL_STAGE_ID env var, using fallback');

      const pipelineId = process.env.GHL_AUDIT_PIPELINE_ID || process.env.GHL_PIPELINE_ID || 'k9Ke4zv94rXG6WezViHR';
      if (!process.env.GHL_AUDIT_PIPELINE_ID && !process.env.GHL_PIPELINE_ID) logger.warn('Missing GHL_AUDIT_PIPELINE_ID and GHL_PIPELINE_ID env var, using fallback');
      
      // If it's an audit or no specific plan, move to Discovery Call stage
      const stageId = (type === 'audit' || plan === 'none') ? stageMapping['discovery'] : (stageMapping[plan] || stageMapping['lite']);

      if (contactId) {
        // 6. Webhook Idempotency Check (Check GHL Opportunities first)
        const opportunities = await ghl.getOpportunities(contactId);
        const duplicateOpportunity = opportunities.find(opp => 
          (opp.notes && opp.notes.includes(session.id)) || 
          (opp.name && opp.name.includes(session.id))
        );

        if (duplicateOpportunity) {
          logger.info('Duplicate opportunity creation skipped (Stripe Session already processed)', { 
            sessionId: session.id, 
            opportunityId: duplicateOpportunity.id 
          });
        } else {
          const notes = `Stripe Session ID: ${session.id}
Plan: ${plan}
Market: ${market}
Type: ${type}
Payment Category: ${type === 'audit' ? 'audit_deposit' : 'setup_payment'}
Credit Policy: ${creditPolicy}
Amount Paid: $${session.amount_total / 100} ${session.currency.toUpperCase()}
Checkout Timestamp: ${new Date(session.created * 1000).toISOString()}`;

          const oppTitle = type === 'audit'
            ? `PAID AUDIT: ${plan.toUpperCase()} Strategy Audit ($${session.amount_total / 100} Deposit Paid)`
            : `PROJECT START: ${plan.toUpperCase()} ($${session.amount_total / 100} Setup Paid)`;

          await ghl.createOpportunity(
            contactId,
            pipelineId,
            stageId,
            oppTitle,
            session.amount_total / 100,
            notes
          );
          logger.info('Stripe Deposit successfully synced to GHL (Opportunity Created)', { 
            email: contactData.email, 
            plan, 
            sessionId: session.id 
          });
        }
      } else {
        logger.error('Failed to sync Stripe purchase: contactId is undefined', { email: contactData.email });
      }

    } catch (error) {
      logger.error('Failed to sync Stripe purchase to GHL', error);
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'Failed to process purchase automation' }) };
    }
  }

  return { statusCode: 200, headers, body: JSON.stringify({ received: true }) };
};
