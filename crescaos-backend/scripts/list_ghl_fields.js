const axios = require('axios');
require('dotenv').config();
const fs = require('fs');

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

async function listFields() {
  try {
    const res = await ghl.get(`/locations/${GHL_LOCATION_ID}/customFields`);
    fs.writeFileSync('ghl_fields_new.json', JSON.stringify(res.data.customFields, null, 2));
    console.log("✅ Custom fields saved to ghl_fields_new.json");
  } catch (e) {
    console.error("❌ Failed to list fields:", e.response ? e.response.data : e.message);
  }
}

listFields();
