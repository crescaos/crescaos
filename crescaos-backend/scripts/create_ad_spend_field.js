const axios = require('axios');
require('dotenv').config();

const GHL_ACCESS_TOKEN = process.env.GHL_ACCESS_TOKEN;
const GHL_LOCATION_ID = process.env.GHL_LOCATION_ID;

const ghl = axios.create({
  baseURL: 'https://services.leadconnectorhq.com',
  headers: {
    'Authorization': `Bearer ${GHL_ACCESS_TOKEN}`,
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  }
});

async function createAdSpendField() {
  try {
    const res = await ghl.post(`/locations/${GHL_LOCATION_ID}/customFields`, {
      name: 'Monthly Ad Spend',
      dataType: 'NUMERICAL',
      model: 'contact'
    });
    console.log(`✅ Created Field: Monthly Ad Spend (${res.data.customField.id})`);
  } catch (e) {
    console.error("❌ Failed to create field:", e.response ? e.response.data : e.message);
  }
}

createAdSpendField();
