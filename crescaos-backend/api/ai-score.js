// api/ai-score.js
const logger = require('../utils/logger');
const { evaluateLead } = require('../utils/scoringModel');

/**
 * AI Scoring Endpoint.
 * Purposefully isolated if the frontend just wants to test a lead's score
 * without fully committing it to a database ingestion pipeline.
 */
module.exports = async (req, res) => {
  // CORS setup
  res.setHeader('Access-Control-Allow-Origin', '*'); 
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const leadData = req.body;

    if (!leadData) {
        return res.status(400).json({ error: 'Payload body missing.' });
    }

    logger.info('Initiating AI Scoring Logic for lead data request.');

    // Pass body into our scoring algorithm
    const result = evaluateLead(leadData);

    return res.status(200).json({
        success: true,
        analysis: result
    });

  } catch (err) {
      logger.error('Failed processing AI Score payload', err);
      return res.status(500).json({ error: 'Internal Server Error' });
  }
};
