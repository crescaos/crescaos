/**
 * Cresca OS — Funnel Analytics Tracker
 * Fires events at key conversion moments.
 * GTM-ready via dataLayer. Meta Pixel hook prepared (one-line activation).
 */
window.CrescaTrack = (function () {

  function push(event, props) {
    try {
      // GTM / dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event, ...props, timestamp: Date.now() });

      // Console (dev only — remove in prod or gate behind a debug flag)
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        console.log('[CrescaTrack]', event, props || '');
      }

      // ── Meta Pixel hook (activate when fbq is available) ──────────────
      // Uncomment when Pixel is live:
      // if (typeof fbq === 'function') {
      //   const pixelMap = {
      //     'results_reached': () => fbq('track', 'Lead'),
      //     'cta_clicked':     () => fbq('track', 'InitiateCheckout'),
      //     'booking_started': () => fbq('track', 'Schedule'),
      //   };
      //   if (pixelMap[event]) pixelMap[event]();
      // }

    } catch (err) {
      // Never block the funnel over a tracking error
    }
  }

  return {
    /** User clicks the welcome screen CTA */
    funnelStart()                   { push('cas_funnel_start', {}); },

    /** User reaches the Results screen (Step 9) */
    resultsReached(score, tier)     { push('cas_results_reached', { score, tier }); },

    /** User clicks a primary CTA on the Results screen */
    ctaClicked(type)                { push('cas_cta_clicked', { cta_type: type }); }, // 'calendar' | 'whatsapp'

    /** GHL calendar postMessage fires "booking_confirmed" */
    bookingStarted()                { push('cas_booking_started', {}); },

    /** Step completed */
    stepCompleted(step, stepName)   { push('cas_step_completed', { step, stepName }); },

    /** Diagnostic data sent to backend */
    webhookFired(score)             { push('cas_webhook_fired', { score }); },
  };
})();

// Listen for GHL calendar confirmation postMessage
window.addEventListener('message', function (e) {
  if (e.data && (e.data.type === 'booking_confirmed' || e.data === 'booking_confirmed')) {
    window.CrescaTrack.bookingStarted();
  }
});
