async function listAllPipelines() {
  const GHL_ACCESS_TOKEN = 'pit-596a4d77-06e7-4b60-89e6-b29eafeca86d';
  const GHL_LOCATION_ID = 'p5wbVxxtAqPqnOsCqaTt';

  try {
    const response = await fetch(`https://services.leadconnectorhq.com/opportunities/pipelines?locationId=${GHL_LOCATION_ID}`, {
      headers: {
        'Authorization': `Bearer ${GHL_ACCESS_TOKEN}`,
        'Version': '2021-07-28'
      }
    });

    const data = await response.json();
    console.log('All Pipelines Found:', data.pipelines.length);
    data.pipelines.forEach(p => {
      console.log(`Pipeline: ${p.name} (ID: ${p.id})`);
      p.stages.forEach(s => console.log(`  - ${s.name} (ID: ${s.id})`));
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

listAllPipelines();
