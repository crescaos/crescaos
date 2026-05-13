const fs = require('fs');
const path = require('path');

const files = [
  'public/diagnostic.html',
  'public/es/diagnostic.html'
];

const emojiMap = {
  // bizTypes
  'home_services': '&#x1F3E0;',
  'health_wellness': '&#x1F3E5;',
  'professional': '&#x1F4BC;',
  'trades': '&#x1F3D7;&#xFE0F;',
  'auto': '&#x1F697;',
  'other': '&#x1F4E6;',
  
  // bottleneck
  'missed_calls': '&#x1F4F5;',
  'leads_no_convert': '&#x1F50D;',
  'poor_followup': '&#x1F4E8;',
  'scheduling_chaos': '&#x1F4C5;',
  'no_visibility': '&#x1F4CA;',
  'disconnected_tools': '&#x1F6E0;&#xFE0F;',
  
  // responseTime
  'under_5min': '&#x26A1;',
  '5_30min': '&#x1F552;',
  '30min_2hr': '&#x1F558;',
  'same_day': '&#x1F4C5;',
  'next_day': '&#x1F4C6;',
  'no_process': '&#x1F937;'
};

const tierMap = {
  'critical': '&#x1F534;',
  'leaking': '&#x1F7E1;',
  'functional': '&#x1F7E2;',
  'strong': '&#x1F680;',
  '🚀': '&#x1F680;'
};

files.forEach(file => {
  const filePath = path.resolve(process.cwd(), file);
  if (!fs.existsSync(filePath)) return;
  
  let content = fs.readFileSync(filePath, 'utf8');
  
  // Fix bizTypes
  content = content.replace(/\{v:'home_services',\s+e:'.*?',/g, `{v:'home_services',    e:'&#x1F3E0;',`);
  content = content.replace(/\{v:'health_wellness',\s+e:'.*?',/g, `{v:'health_wellness',  e:'&#x1F3E5;',`);
  content = content.replace(/\{v:'professional',\s+e:'.*?',/g, `{v:'professional',     e:'&#x1F4BC;',`);
  content = content.replace(/\{v:'trades',\s+e:'.*?',/g, `{v:'trades',           e:'&#x1F3D7;&#xFE0F;',`);
  content = content.replace(/\{v:'auto',\s+e:'.*?',/g, `{v:'auto',             e:'&#x1F697;',`);
  content = content.replace(/\{v:'other',\s+e:'.*?',/g, `{v:'other',            e:'&#x1F4E6;',`);
  
  // Fix bottleneck
  content = content.replace(/\{v:'missed_calls',\s+e:'.*?',/g, `{v:'missed_calls',       e:'&#x1F4F5;',`);
  content = content.replace(/\{v:'leads_no_convert',\s+e:'.*?',/g, `{v:'leads_no_convert',   e:'&#x1F50D;',`);
  content = content.replace(/\{v:'poor_followup',\s+e:'.*?',/g, `{v:'poor_followup',      e:'&#x1F4E8;',`);
  content = content.replace(/\{v:'scheduling_chaos',\s+e:'.*?',/g, `{v:'scheduling_chaos',   e:'&#x1F4C5;',`);
  content = content.replace(/\{v:'no_visibility',\s+e:'.*?',/g, `{v:'no_visibility',      e:'&#x1F4CA;',`);
  content = content.replace(/\{v:'disconnected_tools',\s+e:'.*?',/g, `{v:'disconnected_tools', e:'&#x1F6E0;&#xFE0F;',`);
  
  // Fix responseTime
  content = content.replace(/\{v:'under_5min',\s+e:'.*?',/g, `{v:'under_5min', e:'&#x26A1;',`);
  content = content.replace(/\{v:'5_30min',\s+e:'.*?',/g, `{v:'5_30min',    e:'&#x1F552;',`);
  content = content.replace(/\{v:'30min_2hr',\s+e:'.*?',/g, `{v:'30min_2hr',  e:'&#x1F558;',`);
  content = content.replace(/\{v:'same_day',\s+e:'.*?',/g, `{v:'same_day',   e:'&#x1F4C5;',`);
  content = content.replace(/\{v:'next_day',\s+e:'.*?',/g, `{v:'next_day',   e:'&#x1F4C6;',`);
  content = content.replace(/\{v:'no_process',\s+e:'.*?',/g, `{v:'no_process', e:'&#x1F937;',`);

  // Fix tiers
  content = content.replace(/critical:\s+\{label:'.*?',/g, `critical:  {label:'&#x1F534; Critical — Revenue at Risk',`);
  content = content.replace(/leaking:\s+\{label:'.*?',/g, `leaking:   {label:'&#x1F7E1; Active Leak — Real Money Slipping',`);
  content = content.replace(/functional:\s+\{label:'.*?',/g, `functional: {label:'&#x1F7E2; Functional — Growth Ceiling',`);
  content = content.replace(/strong:\s+\{label:'.*?',/g, `strong:    {label:'&#x1F680; Solid — Ready to Scale',`);
  content = content.replace(/🚀:\s+\{label:'.*?',/g, `🚀:    {label:'&#x1F680; Solid — Ready to Scale',`);

  // Fix Spanish tier labels if in es/
  if (file.includes('/es/')) {
    content = content.replace(/critical:\s+\{label:'.*?',/g, `critical:  {label:'&#x1F534; Crítico — Ingresos en Riesgo',`);
    content = content.replace(/leaking:\s+\{label:'.*?',/g, `leaking:   {label:'&#x1F7E1; Fuga Activa — Pérdida de Dinero',`);
    content = content.replace(/functional:\s+\{label:'.*?',/g, `functional: {label:'&#x1F7E2; Funcional — Techo de Crecimiento',`);
    content = content.replace(/strong:\s+\{label:'.*?',/g, `strong:    {label:'&#x1F680; Sólido — Listo para Escalar',`);
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Fixed ${file}`);
});
