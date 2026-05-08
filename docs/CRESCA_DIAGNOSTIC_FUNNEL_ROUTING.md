# Cresca OS Diagnostic Funnel Routing & Tracking

## Overview
This document outlines the architecture for the Cresca OS Diagnostic Funnel routing and UTM tracking preservation. The system is designed to gracefully transfer leads from standard marketing pages into an interactive diagnostic funnel, preserving marketing attribution (UTM tags) throughout the entire journey, and ultimately syncing this rich data into GoHighLevel (GHL).

## Key Components

### 1. UTM Preservation Script
**File**: `public/js/language-manager.js` (Appended logic)
**Purpose**: Automatically captures any URL query parameters (e.g., `?utm_source=facebook&utm_medium=cpc`) present on a user's initial landing page and appends them to all internal Call-To-Action (CTA) links that point to the `/diagnostic.html` or `/es/diagnostic.html` funnel.

**How it works**:
- The script executes on `DOMContentLoaded`.
- It parses `window.location.search`.
- It selects all `<a>` tags with an `href` pointing to `diagnostic.html`.
- It safely appends the missing search parameters using the `URL` API, ensuring parameters are passed when the user clicks the CTA.

### 2. Diagnostic Funnel Payload Capture
**Files**: `public/diagnostic.html` (EN), `public/es/diagnostic.html` (ES)
**Purpose**: Captures both user-submitted data and passive tracking metadata.

**Captured State**:
- **Marketing Attribution**: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`.
- **Navigation Context**: `source_page` (current URL), `referrer` (previous page), `landing_page` (first page visited in session).
- **Diagnostic Data**: Business Name, Type, Revenue Stage, Bottleneck, Response Time, and dynamically calculated Score and Tier.

When the user completes the funnel, the frontend bundles this state into a JSON payload and `POST`s it to the `/api/webhook` endpoint.

### 3. Backend Webhook Processing
**File**: `crescaos-backend/api/webhook.js`
**Purpose**: Acts as the middleware between the frontend funnel and GoHighLevel.

**Execution Flow for Diagnostic Leads**:
1. Identifies the lead type by checking `payload.source === 'Diagnostic Funnel'`.
2. Normalizes `firstName` and `lastName` from the single `name` input field.
3. Tags the contact with `diagnostic-funnel` and dynamically applies `en-lead` or `es-lead` based on the frontend language payload.
4. Generates a highly structured Note containing the diagnostic results (Score, Monthly Loss, Bottleneck) and full tracking attribution (UTMs, Referrer).
5. Upserts the contact and pushes the note to the contact's timeline in GHL.

## Updates Made During Transition
- Mass replaced `book-audit.html` references with `diagnostic.html` across all 20+ English and Spanish frontend pages.
- Replaced Legacy Book Audit logic with the interactive Diagnostic Funnel calculation matrix.
- Enabled multi-language backend logic inside `webhook.js` without breaking the existing Audit Wizard or ES Lead intakes.

## Adding New Links
When adding new CTAs to the website that point to the diagnostic funnel, simply use:
```html
<a href="/diagnostic.html">Get Started</a>
```
Or for Spanish:
```html
<a href="/es/diagnostic.html">Comenzar</a>
```
The preservation script will automatically hook into these links and pass UTM parameters seamlessly.

## Backend Environment Variables
The webhook relies on the following environment variables to authenticate and map data to GoHighLevel:

- `GHL_ACCESS_TOKEN` / `GHL_API_KEY`: Authentication for GHL APIs.
- `GHL_LOCATION_ID`: The specific sub-account location ID in GHL.
- `GHL_PIPELINE_ID`: The pipeline ID where new opportunities should be created. **Must be**: `mPu4ZjiIPtVnfAADBj0h`
- `GHL_STAGE_ID`: The ID of the specific stage within the pipeline. This must be pulled directly from the GHL pipeline API response or network tab for the correct stage. Do not guess this ID.
- `GHL_FIELD_*`: Various custom field IDs used for mapping specific diagnostic data points (e.g., `GHL_FIELD_MONTHLY_LEADS`, `GHL_FIELD_LOST_REVENUE`).

These variables must be set in your production backend environment (e.g., Railway). No hardcoded credentials or IDs should be committed to the repository.
