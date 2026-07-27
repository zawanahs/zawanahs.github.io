import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';

const websiteId = process.env.PUBLIC_ANALYTICS_WEBSITE_ID;
const apiKey = process.env.UMAMI_API_KEY;
const endpoint = (process.env.UMAMI_API_ENDPOINT || 'https://api.umami.is/v1').replace(/\/$/, '');
const windowDays = Number(process.env.POPULAR_WINDOW_DAYS || 90);
const outputPath = resolve('src/data/popular-articles.json');

if (!websiteId || !apiKey) {
  console.log('Popularity sync skipped: Umami credentials are not configured.');
  process.exit(0);
}

const endAt = Date.now();
const startAt = endAt - windowDays * 24 * 60 * 60 * 1000;
const url = new URL(`${endpoint}/websites/${websiteId}/metrics/expanded`);
url.searchParams.set('startAt', String(startAt));
url.searchParams.set('endAt', String(endAt));
url.searchParams.set('type', 'path');
url.searchParams.set('limit', '500');

const response = await fetch(url, {
  headers: { Accept: 'application/json', 'x-umami-api-key': apiKey },
});

if (!response.ok) throw new Error(`Umami popularity sync failed with ${response.status}.`);

const metrics = await response.json();
const articles = metrics
  .filter((metric) => metric.name?.startsWith('/articles/'))
  .map((metric) => ({
    path: metric.name.endsWith('/') ? metric.name : `${metric.name}/`,
    views: Number(metric.pageviews || 0),
  }))
  .sort((a, b) => b.views - a.views)
  .slice(0, 12);

await mkdir(dirname(outputPath), { recursive: true });
await writeFile(outputPath, `${JSON.stringify({ generatedAt: new Date().toISOString(), windowDays, articles }, null, 2)}\n`);
console.log(`Popularity data updated with ${articles.length} article paths.`);
