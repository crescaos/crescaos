const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  const { plan, type, email, name } = event.queryStringParameters || {};
  
  try {
    // Public Booking Link for your GHL Calendar
    const SUCCESS_URL = "https://link.crescaos.com/widget/booking/OlqdoFrT1sgJ3f2nnaIa";
    const CANCEL_URL = "https://crescaos.com/pricing";

    const isAudit = type === 'audit';
    const productName = isAudit ? 'Business Systems Audit - Deposit' : `Cresca OS - ${plan ? plan.toUpperCase() : 'Project'} Deposit`;
    const productDesc = isAudit 
      ? 'Comprehensive business flow analysis and optimization roadmap.' 
      : `Initial setup deposit for the ${plan || 'selected'} plan. Credits toward first month.`;

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
            unit_amount: 50000, // $500.00
          },
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: SUCCESS_URL,
      cancel_url: CANCEL_URL,
      metadata: {
        plan: plan || 'none',
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
