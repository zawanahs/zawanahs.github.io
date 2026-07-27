import type { CollectionEntry } from 'astro:content';
import { getCollection } from 'astro:content';

export type Article = CollectionEntry<'articles'>;

export const categoryLabels = {
  ideas: 'Ideas',
  builds: 'Builds',
  notes: 'Notes',
  'after-hours': 'After Hours',
} as const;

export async function getPublishedArticles() {
  const entries = await getCollection('articles', ({ data }) => import.meta.env.DEV || !data.draft);
  return entries.sort((a, b) => b.data.published.valueOf() - a.data.published.valueOf());
}

export function articleSlug(article: Article) {
  return article.id
    .replace(/\\/g, '/')
    .replace(/\.(md|mdx)$/, '')
    .replace(/\/index$/, '');
}

export function articleHref(article: Article) {
  return `/articles/${articleSlug(article)}/`;
}

export function seriesLabel(series?: string) {
  if (!series) return undefined;
  const labels: Record<string, string> = {
    nanoclaw: 'NanoClaw',
    'analyst-in-the-loop': 'Analyst in the Loop',
    'ccar-f': 'CCAR-F',
    'learning-cca-f': 'CCA-F Notes',
    'building-with-hermes': 'Building with Hermes',
  };
  if (labels[series]) return labels[series];
  return series
    .split('-')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

export function formatDate(date: Date) {
  return new Intl.DateTimeFormat('en-SG', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  }).format(date);
}

export function tagHref(tag: string) {
  return `/tags/${encodeURIComponent(tag.toLowerCase())}/`;
}
