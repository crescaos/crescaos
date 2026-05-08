# Cresca OS Localization Stabilization Audit & Remediation

This document tracks the standardization of language switching, script loading, and legal/footer paths across the public Cresca OS landing pages.

## Scope
- `diagnostic.html`
- `es/diagnostic.html`
- `privacy.html`
- `terms.html`
- `es/privacy.html`
- `es/terms.html`
- `thank-you.html`
- `es/thank-you.html`

## Remediation Checklist

### 1. Script Injection (`/js/language-manager.js`)
- [ ] `diagnostic.html`
- [ ] `es/diagnostic.html`
- [ ] `privacy.html`
- [ ] `terms.html`
- [ ] `es/privacy.html`
- [ ] `es/terms.html`
- [ ] `thank-you.html`
- [ ] `es/thank-you.html`

### 2. Footer Link Standardisation (Absolute Paths)
- [ ] `diagnostic.html`
- [ ] `es/diagnostic.html`
- [ ] `privacy.html`
- [ ] `terms.html`
- [ ] `es/privacy.html`
- [ ] `es/terms.html`
- [ ] `thank-you.html`
- [ ] `es/thank-you.html`

### 3. Language Switcher Configuration
- [ ] `diagnostic.html` (-> `es`)
- [ ] `es/diagnostic.html` (-> `en`)
- [ ] `privacy.html` (-> `es`)
- [ ] `es/privacy.html` (-> `en`)
- [ ] `terms.html` (-> `es`)
- [ ] `es/terms.html` (-> `en`)
- [ ] `thank-you.html` (-> `es`)
- [ ] `es/thank-you.html` (-> `en`)

## Verification Results

| Page | Switcher Redirects? | LocalStorage Updated? | No Console Errors? |
| :--- | :---: | :---: | :---: |
| `diagnostic.html` | | | |
| `es/diagnostic.html` | | | |
| `privacy.html` | | | |
| `terms.html` | | | |
| `es/privacy.html` | | | |
| `es/terms.html` | | | |
| `thank-you.html` | | | |
| `es/thank-you.html` | | | |

## Issues Found & Resolved
- [Initial audit: Identified missing `language-manager.js` on diagnostic pages]
