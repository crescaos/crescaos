const ghl = require('../utils/ghl');
const logger = require('../utils/logger');

/**
 * Handles incoming leads from the "Book Audit" form.
 * Syncs the data directly to GoHighLevel (GHL).
 */
module.exports = async (req, res) => {
  // CORS Headers for Production
  res.setHeader('Access-Control-Allow-Origin', '*'); 
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // CORS Preflight
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const payload = req.body;
    logger.info('Incoming Audit Form Submission', { payload });

    // 1. Map Form Payload to GHL Contact Data
    const isESLead = payload.source === 'El Salvador Intake Form';
    const isAuditWizard = payload.source === 'Growth Audit Wizard' || payload.source === 'Growth Audit Wizard (ES)';
    
    // Normalize names from the wizard (full_name) vs the form (firstName/lastName)
    let firstName = payload.firstName || '';
    let lastName = payload.lastName || '';
    if (payload.full_name) {
      const parts = payload.full_name.trim().split(' ');
      firstName = parts[0];
      lastName = parts.slice(1).join(' ');
    }

    const contactData = {
      firstName: firstName || 'Audit',
      lastName: lastName || 'Lead',
      tags: [isESLead ? 'es-lead' : 'growth-audit'],
      customFields: []
    };
    
    if (payload.email) contactData.email = payload.email.toLowerCase();
    if (payload.phone) contactData.phone = payload.phone;
    if (payload.company || payload.business_name) contactData.companyName = payload.company || payload.business_name;

    // 2. Format detailed note for ES Leads or standard Audit Leads
    let noteContent = `Source: ${payload.source || 'Website Form'}\n`;
    
    if (isAuditWizard) {
      if (payload.website) contactData.customFields.push({ key: 'website', value: payload.website });
      
      // Map to custom fields from environment
      if (payload.monthly_leads) contactData.customFields.push({ id: process.env.GHL_FIELD_MONTHLY_LEADS, value: payload.monthly_leads });
      if (payload.response_time) contactData.customFields.push({ id: process.env.GHL_FIELD_RESPONSE_TIME, value: payload.response_time });
      if (payload.followup_freq) contactData.customFields.push({ id: process.env.GHL_FIELD_FOLLOWUP_FREQ, value: payload.followup_freq });
      if (payload.booking_system) contactData.customFields.push({ id: process.env.GHL_FIELD_BOOKING_SYSTEM, value: payload.booking_system });
      if (payload.missed_calls) contactData.customFields.push({ id: process.env.GHL_FIELD_MISSED_CALLS, value: payload.missed_calls });
      if (payload.loss_percentage) contactData.customFields.push({ id: process.env.GHL_FIELD_LOSS_PERCENT, value: payload.loss_percentage });
      if (payload.lost_revenue) contactData.customFields.push({ id: process.env.GHL_FIELD_LOST_REVENUE, value: payload.lost_revenue });
      
      // Optional Advanced Fields
      if (payload.website) contactData.customFields.push({ id: process.env.GHL_FIELD_WEBSITE, value: payload.website });
      if (payload.ad_spend) contactData.customFields.push({ id: process.env.GHL_FIELD_AD_SPEND, value: payload.ad_spend });

      noteContent += `--- Growth Audit Results ---\n`;
      if (payload.loss_percentage) noteContent += `Total Interaction Loss: ${payload.loss_percentage}%\n`;
      if (payload.lost_revenue) noteContent += `Monthly Revenue Opportunity: $${payload.lost_revenue.toLocaleString()}\n`;
      
      if (payload.ad_spend) {
        const adWaste = (parseFloat(payload.ad_spend) * (parseFloat(payload.loss_percentage) / 100)) || 0;
        noteContent += `--- Marketing ROI Snapshot ---\n`;
        noteContent += `Avg Monthly Ad Spend: $${payload.ad_spend}\n`;
        noteContent += `Estimated Wasted Ad Spend: $${adWaste.toFixed(2)}/mo\n`;
      }

      noteContent += `\n--- Operational Profile ---\n`;
      if (payload.monthly_leads) noteContent += `Monthly Leads: ${payload.monthly_leads}\n`;
      if (payload.missed_calls) noteContent += `Missed Calls/Week: ${payload.missed_calls}\n`;
      if (payload.response_time) noteContent += `Avg Response Time: ${payload.response_time}\n`;
      if (payload.has_booking) noteContent += `Has Booking System: ${payload.has_booking}\n`;
      if (payload.website) noteContent += `Website: ${payload.website}\n`;
      
    } else if (isESLead) {
      if (payload.plan) noteContent += `Selected Plan: ${payload.plan.toUpperCase()}\n`;
      noteContent += `Role: ${payload.role || 'N/A'}\n`;
      noteContent += `Employees: ${payload.employees || 'N/A'}\n`;
      if (payload.revenue) noteContent += `Annual Revenue: ${payload.revenue}\n`;
      if (payload.website) noteContent += `Website: ${payload.website}\n`;
      if (payload.needs) noteContent += `Biggest Needs: ${payload.needs}\n`;
    } else {
      if (payload.website) contactData.customFields.push({ key: 'website', value: payload.website });
      if (payload.bottleneck) noteContent += `Bottleneck: ${payload.bottleneck}\n`;
      if (payload.leads_monthly) noteContent += `Monthly Leads: ${payload.leads_monthly}\n`;
    }
    
    // 3. Upsert Contact in GHL
    if (contactData.email) {
      const ghlContact = await ghl.upsertContact(contactData);
      const contactId = ghlContact.id || (ghlContact.contact && ghlContact.contact.id);

      // 3b. Create Note on the contact (GHL API v2 requires a separate /notes call)
      if (contactId && noteContent) {
        try {
          await ghl.request('POST', `/contacts/${contactId}/notes`, {
            userId: '',
            body: noteContent
          });
          logger.info('Note added to GHL contact', { contactId });
        } catch (noteErr) {
          logger.warn('Note creation failed (non-critical)', noteErr.message);
        }
      }

      // 4. Create Opportunity in the Sales Pipeline
      const pipelineId = process.env.GHL_PIPELINE_ID || 'mPu4ZjliPtVnfAADBj0h';
      const stageId = process.env.GHL_STAGE_ID || '54daa97e-e0fd-45ba-b017-539e2e5e61df';

      if (contactId && pipelineId) {
        await ghl.createOpportunity(
          contactId,
          pipelineId,
          stageId,
          `${isESLead ? 'ES' : (isAuditWizard ? 'AUDIT' : 'LEAD')}: ${payload.company || payload.full_name || payload.firstName}`,
          isAuditWizard ? (payload.lost_revenue || 0) : 0
        );
        logger.info('Opportunity created in GHL Sales Pipeline', { contactId, isAuditWizard });
      }
    }

    return res.status(200).json({
      success: true,
      message: 'Lead received and synced to GHL.'
    });

  } catch (err) {
    logger.error('Failed to sync Audit Lead to GHL', err);
    // return 200 to prevent form errors on the frontend, but log the failure
    return res.status(200).json({ success: true, warning: 'Synced with delay' });
  }
};
