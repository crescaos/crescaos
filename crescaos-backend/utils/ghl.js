const axios = require('axios');
const logger = require('./logger');

/**
 * Utility for interacting with the GoHighLevel (GHL) API v2.
 */
class GHLClient {
  constructor() {
    this.accessToken = process.env.GHL_ACCESS_TOKEN;
    this.locationId = process.env.GHL_LOCATION_ID;
    this.baseUrl = 'https://services.leadconnectorhq.com';
  }

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
          'Version': '2021-07-02',
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
    
    // Check if contact exists by email
    try {
      const search = await this.request('GET', `/contacts/?locationId=${this.locationId}&email=${contactData.email}`);
      
      if (search && search.contacts && search.contacts.length > 0) {
        // Update existing
        const contactId = search.contacts[0].id;
        return this.request('PUT', `/contacts/${contactId}`, {
          ...contactData,
          locationId: this.locationId
        });
      } else {
        // Create new
        return this.request('POST', '/contacts/', {
          ...contactData,
          locationId: this.locationId
        });
      }
    } catch (error) {
      logger.error('Failed to upsert contact', error);
      throw error;
    }
  }

  /**
   * Creates an opportunity in a specific pipeline/stage.
   */
  async createOpportunity(contactId, pipelineId, stageId, title, value = 0) {
    logger.info('Creating opportunity in GHL', { contactId, pipelineId, stageId });
    
    return this.request('POST', '/opportunities/', {
      pipelineId,
      locationId: this.locationId,
      contactId,
      name: title,
      status: 'open',
      stageId,
      monetaryValue: value
    });
  }
}

module.exports = new GHLClient();
