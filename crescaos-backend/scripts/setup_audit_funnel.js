const axios = require('axios');
require('dotenv').config();

const GHL_ACCESS_TOKEN = process.env.GHL_ACCESS_TOKEN;
const GHL_LOCATION_ID = process.env.GHL_LOCATION_ID;

if (!GHL_ACCESS_TOKEN || !GHL_LOCATION_ID) {
  console.error("❌ GHL_ACCESS_TOKEN or GHL_LOCATION_ID missing in .env");
  process.exit(1);
}

const ghl = axios.create({
  baseURL: 'https://services.leadconnectorhq.com',
  headers: {
    'Authorization': `Bearer ${GHL_ACCESS_TOKEN}`,
    'Version': '2021-07-02',
    'Content-Type': 'application/json'
  }
});

async function setupAuditFunnel() {
  console.log("🚀 Starting CRESCA Growth Audit Setup...");

  try {
    // 1. Create Custom Fields
    console.log("📝 Creating Custom Fields...");
    const fields = [
      { name: 'Monthly Leads', dataType: 'TEXT', model: 'contact' },
      { name: 'Response Time', dataType: 'TEXT', model: 'contact' },
      { name: 'Follow-up Frequency', dataType: 'TEXT', model: 'contact' },
      { name: 'Booking System', dataType: 'TEXT', model: 'contact' },
      { name: 'Missed Calls Per Week', dataType: 'NUMERIC', model: 'contact' },
      { name: 'Loss Percentage', dataType: 'NUMERIC', model: 'contact' },
      { name: 'Lost Revenue', dataType: 'NUMERIC', model: 'contact' }
    ];

    for (const field of fields) {
      try {
        // GHL V2 uses customFields (no hyphen) and requires model property
        const res = await ghl.post(`/locations/${GHL_LOCATION_ID}/customFields`, field, {
          headers: { 'Version': '2021-07-28' }
        });
        console.log(`✅ Created Field: ${field.name} (${res.data.customField.id})`);
      } catch (e) {
        if (e.response && (e.response.status === 409 || e.response.status === 400)) {
          console.log(`ℹ️ Field might already exist or name conflict: ${field.name}`);
        } else {
          console.error(`❌ Failed to create field ${field.name}:`, e.response ? e.response.data : e.message);
        }
      }
    }

    console.log("\n⚠️ NOTE: GHL V2 API does not support automated Pipeline creation.");
    console.log("👉 Please create the 'CRESCA Growth Audit' pipeline MANUALLY in Settings > Pipelines.");

    console.log("🎉 CRESCA Growth Audit Setup Complete!");
  } catch (error) {
    console.error("❌ Fatal Error during setup:", error.response ? error.response.data : error.message);
  }
}

setupAuditFunnel();
