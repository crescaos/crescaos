const axios = require('axios');
const logger = require('./logger');

/**
 * Utility for interacting with the GoHighLevel (GHL) API v2.
 */
class GHLClient {
  constructor() {
    this.baseUrl = 'https://services.leadconnectorhq.com';
  }

  // Read credentials at request time, not import time
  get accessToken() { return process.env.GHL_ACCESS_TOKEN; }
  get locationId()  { return process.env.GHL_LOCATION_ID; }

  /**
   * Helper to make authenticated requests to GHL
   */
  async request(method, endpoint, data = null) {
    if (!this.accessToken || !this.locationId) {
      logger.error('GHL Credentials Missing in Environment Variables.');
      return null;
    }

    try {
      const config = {
        method,
        url: `${this.baseUrl}${endpoint}`,
        headers: {
          'Authorization': `Bearer ${this.accessToken}`,
          'Version': '2021-07-28',
          'Content-Type': 'application/json'
        }
      };
      if (data) {
        config.data = data;
      }
      const response = await axios(config);
      return response.data;
    } catch (error) {
      logger.error(`GHL API Error [${endpoint}]:`, error.response ? error.response.data : error.message);
      throw error;
    }
  }

  /**
   * Creates or updates a contact in GHL.
   */
  async upsertContact(contactData) {
    logger.info('Upserting contact in GHL', { email: contactData.email });
    
    try {
      // Check if contact exists by email
      const search = await this.request('GET', `/contacts/?locationId=${this.locationId}&email=${contactData.email}`);
      
      if (search && search.contacts && search.contacts.length > 0) {
        const existing = search.contacts[0];
        const contactId = existing.id;
        
        // Merge tags to prevent duplicates
        const existingTags = existing.tags || [];
        const mergedTags = Array.from(new Set([...existingTags, ...(contactData.tags || [])]));

        // Build safe payload to avoid overwriting existing GHL values with empty/null fields
        const updatePayload = {
          email: contactData.email || existing.email,
          firstName: contactData.firstName || existing.firstName || '',
          lastName: contactData.lastName || existing.lastName || '',
          phone: contactData.phone || existing.phone || '',
          tags: mergedTags,
          locationId: this.locationId
        };
        
        logger.info('Updating existing GHL contact', { contactId, email: contactData.email });
        const result = await this.request('PUT', `/contacts/${contactId}`, updatePayload);
        return { contact: result, status: 'updated' };
      } else {
        logger.info('Creating new GHL contact', { email: contactData.email });
        const result = await this.request('POST', '/contacts/', {
          ...contactData,
          locationId: this.locationId
        });
        return { contact: result, status: 'created' };
      }
    } catch (error) {
      logger.error('Failed to upsert contact', error);
      throw error;
    }
  }

  /**
   * Queries existing opportunities associated with a specific contact.
   */
  async getOpportunities(contactId) {
    logger.info('Retrieving existing GHL opportunities for contact', { contactId });
    try {
      const response = await this.request('GET', `/opportunities/search?locationId=${this.locationId}&contactId=${contactId}`);
      return response && response.opportunities ? response.opportunities : [];
    } catch (error) {
      logger.error('Failed to retrieve opportunities', error);
      return [];
    }
  }

  /**
   * Creates an opportunity in a specific pipeline/stage.
   */
  async createOpportunity(contactId, pipelineId, stageId, title, value = 0, notes = '') {
    logger.info('Creating opportunity in GHL', { contactId, pipelineId, stageId });
    
    const payload = {
      pipelineId,
      locationId: this.locationId,
      contactId,
      name: title,
      status: 'open',
      stageId,
      monetaryValue: value
    };
    
    if (notes) {
      payload.notes = notes;
    }
    
    return this.request('POST', '/opportunities/', payload);
  }
}

module.exports = new GHLClient();
