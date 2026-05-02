const axios = require('axios');
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../.env') });

const WEBHOOK_URL = 'http://localhost:3000/api/webhook'; // Assuming local server or I can call the function directly

// Mocking the webhook function request/response
const webhook = require('../api/webhook');

async function runTests() {
  console.log("🧪 Starting Growth Audit Verification...\n");

  const testLeads = [
    {
      name: "Standard Lead (No Optional)",
      payload: {
        full_name: "Standard John",
        email: "standard@test.com",
        monthly_leads: 50,
        response_time: "day",
        missed_calls: 10,
        has_booking: "no",
        source: "Growth Audit Wizard"
      }
    },
    {
      name: "Advanced Lead (Full Data)",
      payload: {
        full_name: "Advanced Jane",
        email: "advanced@test.com",
        website: "https://janedesign.co",
        monthly_leads: 100,
        response_time: "longer",
        missed_calls: 5,
        has_booking: "no",
        ad_spend: 5000,
        source: "Growth Audit Wizard"
      }
    }
  ];

  for (const test of testLeads) {
    console.log(`📡 Testing: ${test.name}...`);
    try {
      // We simulate the req/res for the serverless function
      const req = { method: 'POST', body: test.payload };
      const res = {
        status: (code) => ({
          json: (data) => console.log(`   ✅ Response (${code}):`, JSON.stringify(data, null, 2)),
          end: () => {}
        })
      };
      
      await webhook(req, res);
    } catch (e) {
      console.error(`   ❌ Failed:`, e.message);
    }
    console.log("\n");
  }
}

// Since I can't easily start the server and call it via HTTP in this environment without a port, 
// I am calling the exported function logic directly.
runTests();
