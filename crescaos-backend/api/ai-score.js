// api/ai-score.js
const logger = require('../utils/logger');
const { evaluateLead } = require('../utils/scoringModel');

const headers = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type'
};

/**
 * AI Scoring Endpoint.
 * Purposefully isolated if the frontend just wants to test a lead's score
 * without fully committing it to a database ingestion pipeline.
 */
exports.handler = async (event, context) => {
  // CORS setup
  if (event.httpMethod === 'OPTIONS') return { statusCode: 200, headers, body: '' };
  
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method Not Allowed' }) };
  }

  let leadData;
  try {
    leadData = event.body ? JSON.parse(event.body) : null;
  } catch (parseError) {
    logger.error('Failed to parse event body', parseError);
    return { statusCode: 400, headers, body: JSON.stringify({ error: 'Invalid JSON body' }) };
  }

  try {
    if (!leadData) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: 'Payload body missing.' }) };
    }

    logger.info('Initiating AI Scoring Logic for lead data request.');

    // Pass body into our scoring algorithm
    const result = evaluateLead(leadData);

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        success: true,
        analysis: result
      })
    };

  } catch (err) {
      logger.error('Failed processing AI Score payload', err);
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'Internal Server Error' }) };
  }
};
