require('dotenv').config({ path: '../.env' });
const axios = require('axios');

async function getUsers() {
    try {
        const response = await axios.get(`https://services.leadconnectorhq.com/users/?locationId=${process.env.GHL_LOCATION_ID}`, {
            headers: {
                'Authorization': `Bearer ${process.env.GHL_ACCESS_TOKEN}`,
                'Version': '2021-07-28',
                'Accept': 'application/json'
            }
        });
        const users = response.data.users.map(u => ({
            id: u.id,
            name: u.name,
            email: u.email
        }));
        console.log(JSON.stringify(users, null, 2));
    } catch (e) {
        console.error('Error fetching users:', e.response ? e.response.data : e.message);
    }
}
getUsers();
