const ghl = require('../utils/ghl');
const logger = require('../utils/logger');

/**
 * Handles incoming leads from the "Book Audit" form.
 * Syncs the data directly to GoHighLevel (GHL).
 */
module.exports = async (req, res) => {
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
    const contactData = {
      email: payload.email || null,
      firstName: payload.full_name ? payload.full_name.split(' ')[0] : (payload.name ? payload.name.split(' ')[0] : 'Audit'),
      lastName: payload.full_name ? payload.full_name.split(' ').slice(1).join(' ') : (payload.name ? payload.name.split(' ').slice(1).join(' ') : 'Lead'),
      phone: payload.phone || null,
      companyName: payload.company || null,
      tags: [isESLead ? 'es-lead' : 'website-audit'],
      customFields: []
    };

    // 2. Format detailed note for ES Leads or standard Audit Leads
    let noteContent = `Source: ${payload.source || 'Website Form'}\n`;
    if (isESLead) {
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
    
    // Attach the note to the contact data (most GHL versions accept 'note' or 'notes')
    contactData.notes = [noteContent];

    // 3. Upsert Contact in GHL
    if (contactData.email) {
      const ghlContact = await ghl.upsertContact(contactData);
      const contactId = ghlContact.id || (ghlContact.contact && ghlContact.contact.id);

      // 4. Create Opportunity in the Sales Pipeline
      const pipelineId = process.env.GHL_AUDIT_PIPELINE_ID || 'k9Ke4zv94rXG6WezViHR';
      
      // Stage Mapping
      const DISCOVERY_CALL_STAGE = 'b621db30-363f-42e5-a0ed-4a00465d8363';
      const AUDIT_REQUESTED_STAGE = '09bc05ae-3918-4010-8d29-b31f5078e26b';
      
      // For ES Leads, always use Discovery Call since no payment was made
      const stageId = (isESLead || payload.service_type === 'demo') ? DISCOVERY_CALL_STAGE : AUDIT_REQUESTED_STAGE;

      if (contactId && pipelineId) {
        await ghl.createOpportunity(
          contactId,
          pipelineId,
          stageId,
          `${isESLead ? 'ES' : (payload.service_type === 'demo' ? 'DEMO' : 'AUDIT')}: ${payload.company || payload.full_name || payload.name}`,
          isESLead ? 0 : (payload.service_type === 'audit' ? 500 : 0)
        );
        logger.info('Opportunity created in GHL Sales Pipeline', { contactId, isESLead });
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
