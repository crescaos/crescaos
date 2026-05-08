// crescaos-backend/utils/auditLogic.js

/**
 * Calculates the potential lost opportunities and revenue based on audit inputs.
 * Baseline Lead Value: $150 (Home Services Avg)
 */
const calculateAudit = (data) => {
  const LEAD_VALUE = 150;
  const { monthlyLeads, responseTime, missedCallsPerWeek, hasBookingSystem, adSpend } = data;

  let leads = parseInt(monthlyLeads) || 0;
  let marketingSpend = parseFloat(adSpend) || 0;
  let lossPercentage = 0;

  // 1. Response Time Impact (Speed to Lead)
  if (responseTime === 'longer') lossPercentage += 40;
  else if (responseTime === 'day') lossPercentage += 25;
  else if (responseTime === 'hour') lossPercentage += 15;
  
  // 2. Booking System Friction
  if (hasBookingSystem === 'no') lossPercentage += 15;

  // 3. Missed Calls (Direct Loss)
  const missedCallsPerMonth = (parseInt(missedCallsPerWeek) || 0) * 4.3;
  
  // Total Lost Leads
  const lostViaSystems = leads * (lossPercentage / 100);
  const totalLostLeads = Math.min(leads, lostViaSystems + missedCallsPerMonth);
  const monthlyRevenueLoss = totalLostLeads * LEAD_VALUE;

  // 4. Marketing Efficiency (Optional)
  const marketingLoss = marketingSpend * (lossPercentage / 100);

  return {
    lossPercentage: Math.min(lossPercentage + (leads > 0 ? (missedCallsPerMonth / leads * 100) : 0), 80).toFixed(0),
    totalLostLeads: totalLostLeads.toFixed(0),
    monthlyRevenueLoss: monthlyRevenueLoss.toLocaleString('en-US', { style: 'currency', currency: 'USD' }),
    annualRevenueLoss: (monthlyRevenueLoss * 12).toLocaleString('en-US', { style: 'currency', currency: 'USD' }),
    marketingLoss: marketingLoss > 0 ? marketingLoss.toLocaleString('en-US', { style: 'currency', currency: 'USD' }) : null,
    verdict: lossPercentage > 30 ? "Critical Loss" : "Optimization Required"
  };
};

module.exports = { calculateAudit };
