const axios = require('axios');
require('dotenv').config(); // Loads crescaos-backend/.env

async function test() {
  const token = process.env.GHL_ACCESS_TOKEN;
  const locationId = process.env.GHL_LOCATION_ID;

  try {
    const response = await axios({
      method: 'GET',
      url: `https://services.leadconnectorhq.com/contacts/?locationId=${locationId}&query=test@crescaos.com`,
      headers: {
        'Authorization': `Bearer ${token}`,
        'Version': '2021-07-28',
        'Content-Type': 'application/json'
      }
    });
    console.log("Success:", response.data);
  } catch (err) {
    console.error("GET Error:", err.response ? err.response.data : err.message);
  }

  try {
    const response = await axios({
      method: 'POST',
      url: `https://services.leadconnectorhq.com/contacts/`,
      headers: {
        'Authorization': `Bearer ${token}`,
        'Version': '2021-07-28',
        'Content-Type': 'application/json'
      },
      data: {
        firstName: "Test",
        email: "test@crescaos.com",
        locationId: locationId
      }
    });
    console.log("POST Success:", response.data);
  } catch (err) {
    console.error("POST Error:", err.response ? err.response.data : err.message);
  }
}

test();
