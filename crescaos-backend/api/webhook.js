// api/webhook.js
const logger = require('../utils/logger');

/**
 * Handles incoming webhooks directly from GoHighLevel.
 * Deployed under Vercel Serverless Functions context.
 */
module.exports = async (req, res) => {
  // 1. Enable CORS & Handle Preflight requests explicitly
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // 2. Validate Request Method
  if (req.method !== 'POST') {
    return res.status(405).json({
      error: 'Method Not Allowed',
      message: 'This endpoint only accepts POST requests from webhooks.'
    });
  }

  try {
    const payload = req.body;

    // Optional: Log raw payload for debugging GHL schema changes
    logger.info('Incoming Webhook Received', { payload });

    // 3. Extract core contact data (Adjust properties to match GHL Webhook schema)
    const leadData = {
      id: payload.id || payload.contact_id || null,
      name: payload.first_name ? `${payload.first_name} ${payload.last_name || ''}`.trim() : (payload.name || payload.contact_name),
      email: payload.email || null,
      phone: payload.phone || null,
      source: payload.source || payload.trigger || 'GHL Webhook',
      company: payload.company_name || payload.company || null,
      tags: payload.tags || []
    };

    // 4. Safely check if we got minimum parsing info
    if (!leadData.email && !leadData.phone && !leadData.id) {
       logger.warn('Webhook payload parsed but no actionable contact data found.', { leadData });
    } else {
       logger.info('Lead Data parsed successfully from webhook.', { leadData });
    }

    // [Future Step] Send to scoring algorithm, internal DB, or Slack alert here.

    // 5. Always return a 200 Fast Response to GHL to prevent webhooks backing up
    return res.status(200).json({
      success: true,
      message: 'Webhook received & processed successfully.',
      data: leadData
    });

  } catch (err) {
    logger.error('Failed to process GHL Webhook payload', err);
    // Vercel serverless catches 5xx, returning 500
    res.status(500).json({ error: 'Internal Server Error processing the payload' });
  }
};
