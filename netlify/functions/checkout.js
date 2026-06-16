const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const PRICING = {
  us: {
    capture: {
      setup: {
        amount: 150000,
        currency: 'usd',
        name: 'Cresca OS Capture System - Setup',
        description: 'Initial setup fee for the Capture plan.'
      }
    },
    growth: {
      setup: {
        amount: 300000,
        currency: 'usd',
        name: 'Cresca OS Growth System - Setup',
        description: 'Initial setup fee for the Growth plan.'
      }
    },
    revenue: {
      audit: {
        amount: 100000,
        currency: 'usd',
        name: 'Cresca OS Revenue Engine - Strategy Audit Deposit',
        description: 'Strategy Audit Deposit credited toward first payment.'
      }
    },
    custom: {
      audit: {
        amount: 100000,
        currency: 'usd',
        name: 'Cresca OS Custom Build - Strategy Audit Deposit',
        description: 'Strategy Audit Deposit credited toward first payment.'
      }
    }
  },

  'el-salvador': {
    starter: {
      setup: {
        amount: 30000,
        currency: 'usd',
        name: 'Cresca OS Starter Plan El Salvador - Initial Payment',
        description: 'Initial payment for the Starter plan.'
      }
    },
    growth: {
      setup: {
        amount: 80000,
        currency: 'usd',
        name: 'Cresca OS Growth Plan El Salvador - Initial Payment',
        description: 'Initial payment for the Growth plan.'
      }
    },
    pro: {
      audit: {
        amount: 50000,
        currency: 'usd',
        name: 'Cresca OS Pro Plan El Salvador - Audit Deposit',
        description: 'Pro Plan Audit Deposit credited toward first payment.'
      }
    },
    custom: {
      audit: {
        amount: 50000,
        currency: 'usd',
        name: 'Cresca OS Custom Build El Salvador - Audit Deposit',
        description: 'Custom Build Audit Deposit credited toward first payment.'
      }
    }
  }
};

exports.handler = async (event) => {
  const { plan, market = 'us', type = 'setup', email, name } = event.queryStringParameters || {};

  if (!process.env.STRIPE_SECRET_KEY) {
    console.error('Stripe Error: STRIPE_SECRET_KEY env var is not set on Netlify.');
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Payment system not configured. Missing STRIPE_SECRET_KEY.' }),
    };
  }

  // 1. Validate pricing details
  const marketData = PRICING[market];
  if (!marketData) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: `Invalid market: ${market}` }),
    };
  }

  const planData = marketData[plan];
  if (!planData) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: `Invalid plan: ${plan} for market: ${market}` }),
    };
  }

  const priceItem = planData[type];
  if (!priceItem) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: `Invalid type: ${type} for plan: ${plan} in market: ${market}` }),
    };
  }

  try {
    // 2. Resolve market-specific success and cancel redirect URLs
    const SUCCESS_URL = market === 'el-salvador'
      ? (process.env.STRIPE_SUCCESS_URL_SV || 'https://crescaos.com/el-salvador?checkout=success')
      : (process.env.STRIPE_SUCCESS_URL_US || process.env.STRIPE_SUCCESS_URL || 'https://crm.crescaos.com/widget/booking/OlqdoFrT1sgJ3f2nnaIa');

    const CANCEL_URL = market === 'el-salvador'
      ? (process.env.STRIPE_CANCEL_URL_SV || 'https://crescaos.com/el-salvador?checkout=cancel')
      : (process.env.STRIPE_CANCEL_URL_US || process.env.STRIPE_CANCEL_URL || 'https://crescaos.com/pricing');

    // 3. Create Stripe Checkout Session (one-time payment)
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      phone_number_collection: { enabled: true },
      customer_email: email || undefined,
      line_items: [
        {
          price_data: {
            currency: priceItem.currency,
            product_data: {
              name: priceItem.name,
              description: priceItem.description
            },
            unit_amount: priceItem.amount,
          },
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: SUCCESS_URL,
      cancel_url: CANCEL_URL,
      metadata: {
        plan: plan,
        market: market,
        type: type,
        amount_type: type,
        credit_policy: 'Credited toward first payment if client moves forward',
        customer_name: name || 'unknown',
        source: event.queryStringParameters.source || 'checkout',
        locale: event.queryStringParameters.locale || (market === 'el-salvador' ? 'es' : 'en')
      },
    });

    return {
      statusCode: 303,
      headers: { Location: session.url },
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
