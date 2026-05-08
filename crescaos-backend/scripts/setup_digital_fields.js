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
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  }
});

async function setupDigitalFields() {
  console.log("🚀 Registering Optional Growth Fields in GHL...");

  const fields = [
    { name: 'Business Website', dataType: 'TEXT', model: 'contact' },
    { name: 'Monthly Ad Spend', dataType: 'NUMERIC', model: 'contact' },
    { name: 'Marketing Channels', dataType: 'TEXT', model: 'contact' },
    { name: 'Digital Audit Note', dataType: 'LARGE_TEXT', model: 'contact' }
  ];

  for (const field of fields) {
    try {
      const res = await ghl.post(`/locations/${GHL_LOCATION_ID}/customFields`, field);
      console.log(`✅ Created Field: ${field.name} (${res.data.customField.id})`);
    } catch (e) {
      if (e.response && (e.response.status === 409 || e.response.status === 400)) {
        console.log(`ℹ️ Field might already exist: ${field.name}`);
      } else {
        console.error(`❌ Failed to create field ${field.name}:`, e.response ? e.response.data : e.message);
      }
    }
  }

  console.log("\n🎉 GHL Field Registration Complete!");
}

setupDigitalFields();
