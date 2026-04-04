const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const ghl = require('../utils/ghl');
const logger = require('../utils/logger');

/**
 * Handles incoming webhooks from Stripe after successful checkout.
 */
module.exports = async (req, res) => {
  // CORS Preflight
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).end();

  const signature = req.headers['stripe-signature'];
  const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let event;

  try {
    // 1. Verify Webhook Authenticity
    event = stripe.webhooks.constructEvent(
      req.body, // In Netlify, we need raw body. If parsed, use Buffer.from(JSON.stringify(req.body))
      signature,
      endpointSecret
    );
  } catch (err) {
    logger.error('Stripe Webhook Verification Failed', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

    // 2. Process the Event
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    
    logger.info('Processing Successful Stripe Checkout', { sessionId: session.id });

    const isAudit = session.metadata.type === 'audit';
    const plan = session.metadata.plan || 'none';

    // 3. Extract Customer Info
    const contactData = {
      email: session.customer_details.email,
      firstName: session.customer_details.name.split(' ')[0] || session.metadata.customer_name.split(' ')[0] || '',
      lastName: session.customer_details.name.split(' ').slice(1).join(' ') || session.metadata.customer_name.split(' ').slice(1).join(' ') || '',
      phone: session.customer_details.phone || '',
      tags: ['stripe-purchase', plan !== 'none' ? plan : '', isAudit ? 'paid-audit' : ''].filter(Boolean)
    };

    try {
      // 4. Create/Update Contact in GHL
      const contact = await ghl.upsertContact(contactData);
      const contactId = contact.id || (contact.contact ? contact.contact.id : null);

      // 5. Dynamic Map Plan to GHL Stage
      const stageMapping = {
        'lite': process.env.GHL_SALE_LITE_ID || 'a0296611-9844-4c19-b344-e4d028c70c69',
        'growth': process.env.GHL_SALE_GROWTH_ID || 'bb4b9701-abc6-42cd-8690-0f4df07bd8ea',
        'pro': process.env.GHL_SALE_PRO_ID || '9176acb4-3c14-46bf-b196-34682e4b0c34',
        'discovery': process.env.GHL_DISCOVERY_STAGE_ID || 'b621db30-363f-42e5-a0ed-4a00465d8363' // Discovery Call
      };

      const pipelineId = process.env.GHL_AUDIT_PIPELINE_ID || 'k9Ke4zv94rXG6WezViHR';
      
      // If it's an audit or no specific plan, move to Discovery Call stage
      const stageId = (isAudit || plan === 'none') ? stageMapping['discovery'] : (stageMapping[plan] || stageMapping['lite']);

      if (contactId) {
        await ghl.createOpportunity(
          contactId,
          pipelineId,
          stageId,
          isAudit ? 'PAID AUDIT: Full Systems Analysis' : `PROJECT START: ${plan.toUpperCase()} ($500 Deposit Paid)`,
          session.amount_total / 100
        );
        logger.info('Stripe Deposit successfully synced to GHL', { email: contactData.email, plan, isAudit });
      }

    } catch (error) {
      logger.error('Failed to sync Stripe purchase to GHL', error);
      return res.status(500).json({ error: 'Failed to process purchase automation' });
    }
  }

  res.status(200).json({ received: true });
};
