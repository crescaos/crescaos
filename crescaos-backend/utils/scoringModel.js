// utils/scoringModel.js

/**
 * Basic heuristic AI Scoring Model.
 * Evaluates a lead's data completeness and signals business intent.
 * 
 * @param {Object} lead - Contact data object
 * @returns {Object} { score: Number, status: String, reasons: Array }
 */
const evaluateLead = (lead) => {
  let score = 0;
  const reasons = [];

  // Parse lead object
  const { email, phone, name, source, company } = lead;

  // 1. Core Contact Info (Heavily weighted)
  if (email && email.trim() !== '') {
    score += 25;
    
    // Check for business email vs free email (gmail, yahoo, hotmail, etc.)
    const freeProviders = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com'];
    const domain = email.split('@')[1];
    if (domain && !freeProviders.includes(domain.toLowerCase())) {
        score += 20; // Extra points for B2B signals
        reasons.push("Business email detected.");
    } else {
        reasons.push("Free/Consumer email provider detected.");
    }
  } else {
    reasons.push("Missing email address.");
  }

  if (phone && phone.trim() !== '') {
    // Check for basic phone validity (e.g., minimum length for a phone number)
    if (phone.replace(/\D/g, '').length >= 10) {
      score += 25;
      reasons.push("Valid phone number format.");
    } else {
      score += 10; // Found but questionable format
      reasons.push("Phone number seems malformed.");
    }
  } else {
    reasons.push("Missing phone number.");
  }

  // 2. Identity & Association
  if (name && name.trim() !== '') {
    score += 10;
  }
  
  if (company && company.trim() !== '') {
    score += 20; // Direct B2B signal
    reasons.push("Company name provided.");
  }

  // Categorize based on score
  let tag = 'Cold';
  if (score >= 75) {
      tag = 'Hot';
  } else if (score >= 45) {
      tag = 'Warm';
  }

  // Cap score at 100
  score = Math.min(score, 100);

  return {
      score,
      tag,
      reasons
  };
};

module.exports = { evaluateLead };
