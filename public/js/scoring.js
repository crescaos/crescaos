/**
 * Cresca OS — Funnel Scoring Engine
 * Computes Customer Acquisition Score (0-100) from funnel answers.
 */
window.CrescaScoring = (function () {

  // --- Weight Tables ---

  const RESPONSE_TIME_SCORES = {
    'under_5min':  30,
    '5_30min':     22,
    '30min_2hr':   15,
    'same_day':     8,
    'next_day':     3,
    'no_process':   0
  };

  const BOTTLENECK_SCORES = {
    'disconnected_tools': 28,
    'no_visibility':      24,
    'scheduling_chaos':   20,
    'leads_no_convert':   12,
    'poor_followup':       8,
    'missed_calls':        4
  };

  const REVENUE_SCORES = {
    'under_10k':  8,
    '10k_30k':   12,
    '30k_75k':   15,
    '75k_150k':  18,
    '150k_plus': 20
  };

  const BUSINESS_TYPE_SCORES = {
    'home_services':  15,
    'health_wellness': 17,
    'professional':   18,
    'trades':         14,
    'auto':           15,
    'other':          15
  };

  // --- Monthly Loss Estimators ---

  const AVG_JOB_VALUE = {
    'under_10k':  200,
    '10k_30k':    350,
    '30k_75k':    500,
    '75k_150k':   800,
    '150k_plus': 1200
  };

  const AVG_MONTHLY_LEADS = {
    'under_10k':  15,
    '10k_30k':    35,
    '30k_75k':    55,
    '75k_150k':   80,
    '150k_plus': 120
  };

  const LOSS_RATE = {
    'under_5min': 0.05,
    '5_30min':    0.15,
    '30min_2hr':  0.30,
    'same_day':   0.45,
    'next_day':   0.60,
    'no_process': 0.70
  };

  // --- Tier Thresholds ---

  function getTier(score) {
    if (score <= 40) return 'critical';
    if (score <= 65) return 'leaking';
    if (score <= 80) return 'functional';
    return 'strong';
  }

  // --- Bottleneck Human Label ---

  const BOTTLENECK_LABELS = {
    'missed_calls':       'missed calls and slow response time',
    'leads_no_convert':   'lead-to-booking conversion',
    'poor_followup':      'inconsistent follow-up',
    'scheduling_chaos':   'manual scheduling and booking chaos',
    'no_visibility':      'lack of visibility into what\'s working',
    'disconnected_tools': 'disconnected tools and manual processes'
  };

  // --- Public API ---

  return {
    /**
     * @param {Object} answers
     * @param {string} answers.businessType
     * @param {string} answers.revenueStage
     * @param {string} answers.bottleneck
     * @param {string} answers.responseTime
     * @returns {{ score: number, tier: string, monthlyLoss: number, bottleneckLabel: string }}
     */
    compute(answers) {
      const rt  = RESPONSE_TIME_SCORES[answers.responseTime]  ?? 0;
      const bn  = BOTTLENECK_SCORES[answers.bottleneck]       ?? 0;
      const rev = REVENUE_SCORES[answers.revenueStage]        ?? 10;
      const biz = BUSINESS_TYPE_SCORES[answers.businessType]  ?? 15;

      const score = Math.min(100, Math.max(0, rt + bn + rev + biz));
      const tier  = getTier(score);

      const leads    = AVG_MONTHLY_LEADS[answers.revenueStage] ?? 30;
      const jobValue = AVG_JOB_VALUE[answers.revenueStage]     ?? 400;
      const lossRate = LOSS_RATE[answers.responseTime]         ?? 0.40;
      const monthlyLoss = Math.round(leads * jobValue * lossRate);

      return {
        score,
        tier,
        monthlyLoss,
        bottleneckLabel: BOTTLENECK_LABELS[answers.bottleneck] ?? 'lead follow-up gaps'
      };
    },

    getTier,
    BOTTLENECK_LABELS
  };
})();
