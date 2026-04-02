const axios = require('axios');

async function listCalendars() {
  const token = 'pit-596a4d77-06e7-4b60-89e6-b29eafeca86d';
  const locationId = 'p5wbVxxtAqPqnOsCqaTt';

  try {
    const response = await axios.get(`https://services.leadconnectorhq.com/calendars/?locationId=${locationId}`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Version': '2021-07-28',
        'Accept': 'application/json'
      }
    });

    console.log('--- GHL Calendars Found ---');
    if (response.data.calendars && response.data.calendars.length > 0) {
      response.data.calendars.forEach(cal => {
        console.log(`- Name: ${cal.name}`);
        console.log(`  ID: ${cal.id}`);
        console.log(`  Slug: ${cal.slug}`);
      });
    } else {
      console.log('No calendars found in this location.');
    }
  } catch (error) {
    console.error('Error fetching calendars:', error.response ? error.response.data : error.message);
  }
}

listCalendars();
