'use strict';
require('dotenv').config();

const express = require('express');
const cors    = require('cors');
const logger  = require('./utils/logger');

const webhookHandler = require('./api/webhook');

const app  = express();
const PORT = process.env.PORT || 3000;

// ── CORS ─────────────────────────────────────────────────────────────────────
const ALLOWED_ORIGINS = [
  'https://crescaos.com',
  'https://www.crescaos.com',
  // Local dev
  'http://localhost:3000',
  'http://localhost:5500',
  'http://127.0.0.1:5500',
  'http://localhost:8080'
];

app.use(cors({
  origin: (origin, callback) => {
    // Allow requests with no origin (e.g. server-to-server, curl)
    if (!origin) return callback(null, true);
    if (ALLOWED_ORIGINS.includes(origin)) return callback(null, true);
    logger.warn(`CORS blocked origin: ${origin}`);
    callback(new Error(`Origin ${origin} not allowed by CORS`));
  },
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: false
}));

// ── Body Parsing ──────────────────────────────────────────────────────────────
app.use(express.json({ limit: '1mb' }));

// ── Health Check ──────────────────────────────────────────────────────────────
app.get('/health', (_req, res) => {
  res.json({ ok: true, service: 'crescaos-website-backend' });
});

// ── Netlify Handler → Express Adapter ────────────────────────────────────────
// The existing webhook.js uses Netlify/Vercel's exports.handler signature.
// This adapter converts Express req/res into that format without rewriting
// any business logic.
async function netlifyAdapter(handler, req, res) {
  const event = {
    httpMethod:            req.method,
    headers:               req.headers,
    body:                  JSON.stringify(req.body),
    queryStringParameters: req.query || {},
    path:                  req.path
  };

  const result = await handler(event, {});

  res.status(result.statusCode || 200);

  // Apply any non-CORS headers returned by the handler
  if (result.headers) {
    Object.entries(result.headers).forEach(([key, value]) => {
      if (!key.toLowerCase().startsWith('access-control-')) {
        res.set(key, value);
      }
    });
  }

  try {
    res.json(JSON.parse(result.body));
  } catch {
    res.send(result.body);
  }
}

// ── Routes ───────────────────────────────────────────────────────────────────
app.options('/api/webhook', (_req, res) => res.sendStatus(200));

app.post('/api/webhook', async (req, res) => {
  try {
    logger.info('Railway → /api/webhook received', {
      origin: req.headers.origin,
      source: req.body && req.body.source
    });
    await netlifyAdapter(webhookHandler, req, res);
  } catch (err) {
    logger.error('Express webhook route error', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// ── 404 Catch-all ─────────────────────────────────────────────────────────────
app.use((req, res) => {
  res.status(404).json({ error: `Cannot ${req.method} ${req.path}` });
});

// ── Start ─────────────────────────────────────────────────────────────────────
app.listen(PORT, () => {
  logger.info(`CrescaOS Website Backend listening on port ${PORT}`);
});

module.exports = app;
