# Cresca OS Environment Variable Setup

This document outlines all environment variables required by the Cresca OS backend for correct operation on Netlify.

## Core Required Variables (Must have before Production)

These variables are strictly required. The backend will fail or be unable to authenticate without them.

| Variable | Description | Location Used | Expected Format |
| :--- | :--- | :--- | :--- |
| `STRIPE_SECRET_KEY` | Your Stripe live secret key for creating checkout sessions and verifying webhooks. | `api/checkout.js`, `api/stripe-webhook.js` | `sk_live_...` |
| `STRIPE_WEBHOOK_SECRET` | Secret used to verify that webhooks actually come from Stripe. | `api/stripe-webhook.js` | `whsec_...` |
| `GHL_ACCESS_TOKEN` | Your GoHighLevel API v2 Access Token. | `utils/ghl.js` | String |
| `GHL_LOCATION_ID` | Your GoHighLevel sub-account Location ID. | `utils/ghl.js` | String |

## Pipeline & Stage Variables (Have Fallbacks, but SHOULD be set)

These map leads to specific stages in your GoHighLevel pipelines. They currently have temporary fallbacks in the code to prevent breakage, but you should set these in Netlify to ensure they match your active GHL configuration.

| Variable | Description | Expected Format | Fallback in Code |
| :--- | :--- | :--- | :--- |
| `GHL_PIPELINE_ID` | Primary pipeline for standard leads. | String | `mPu4ZjliPtVnfAADBj0h` |
| `GHL_STAGE_ID` | Default stage for new standard leads. | String | `54daa97e-e0fd-45ba-b017-539e2e5e61df` |
| `GHL_AUDIT_PIPELINE_ID` | Pipeline for Paid Audits and checkouts. | String | `k9Ke4zv94rXG6WezViHR` |
| `GHL_AUDIT_STAGE_ID` | Stage for Discovery Calls / Audits. | String | `b621db30-363f-42e5-a0ed-4a00465d8363` |
| `GHL_SALE_LITE_ID` | Stage for Lite/Starter plan purchases. | String | `a0296611-9844-4c19-b344-e4d028c70c69` |
| `GHL_SALE_GROWTH_ID` | Stage for Growth plan purchases. | String | `bb4b9701-abc6-42cd-8690-0f4df07bd8ea` |
| `GHL_SALE_PRO_ID` | Stage for Pro/Elite plan purchases. | String | `9176acb4-3c14-46bf-b196-34682e4b0c34` |

## Redirection & Custom Fields

| Variable | Description | Location Used | Fallback in Code |
| :--- | :--- | :--- | :--- |
| `STRIPE_SUCCESS_URL` | Where users go after successful payment. | `api/checkout.js` | `https://crm.crescaos.com/widget/booking/OlqdoFrT1sgJ3f2nnaIa` |
| `STRIPE_CANCEL_URL` | Where users go if they cancel payment. | `api/checkout.js` | `https://crescaos.com/pricing` |

**Custom Fields (GHL_FIELD_*)**: The backend `webhook.js` supports mapping Growth Audit data to specific GHL Custom Fields (e.g., `GHL_FIELD_MONTHLY_LEADS`, `GHL_FIELD_LOST_REVENUE`). These are optional, but if you want that data to populate native fields instead of just notes, you must provide the GHL custom field IDs here.
