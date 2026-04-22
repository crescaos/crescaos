const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  const { plan, type, email, name } = event.queryStringParameters || {};
  
  try {
    // Public Booking Link for your GHL Calendar
    const SUCCESS_URL = "https://crm.crescaos.com/widget/booking/OlqdoFrT1sgJ3f2nnaIa";
    const CANCEL_URL = "https://crescaos.com/pricing";

    let targetPlan = plan || 'none';
    const country = event.headers['x-country']; // Geo-located automatically by Netlify 

    // Prevent US/CA from cheating by reverting El Salvador tiers to US tiers
    if (['US', 'CA'].includes(country)) {
      if (targetPlan === 'sv-inicial') targetPlan = 'capture';
      if (targetPlan === 'sv-growth') targetPlan = 'growth';
    }

    // Set dynamic setup amounts
    let depositAmount = 50000; 
    if (targetPlan === 'capture') depositAmount = 150000;      // $1,500
    else if (targetPlan === 'growth') depositAmount = 300000;  // $3,000
    else if (targetPlan === 'sv-inicial') depositAmount = 30000; // $300
    else if (targetPlan === 'sv-growth') depositAmount = 80000;  // $800

    const isAudit = type === 'audit';
    const productName = isAudit ? 'Business Systems Audit - Deposit' : `Cresca OS - ${targetPlan.toUpperCase()} Setup`;
    const productDesc = isAudit 
      ? 'Comprehensive business flow analysis and optimization roadmap.' 
      : `Initial setup fee for the ${targetPlan} plan.`;

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      phone_number_collection: {
        enabled: true,
      },
      customer_email: email || undefined,
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: productName,
              description: productDesc,
            },
            unit_amount: depositAmount,

          },
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: SUCCESS_URL,
      cancel_url: CANCEL_URL,
      metadata: {
        plan: targetPlan,
        type: type || 'purchase',
        customer_name: name || 'unknown'
      }
    });

    return {
      statusCode: 303,
      headers: {
        Location: session.url,
      },
      body: JSON.stringify({ url: session.url }),
    };
  } catch (error) {
    console.error('Stripe Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
