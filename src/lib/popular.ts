import type { Article } from './content';
import { articleHref } from './content';
import popularity from '../data/popular-articles.json';

const popularityData = popularity as {
  generatedAt: string | null;
  windowDays: number;
  articles: Array<{ path: string; views: number }>;
};

export function getPopularArticles(articles: Article[], limit = 3) {
  const ranked = popularityData.articles
    .map(({ path }) => articles.find((article) => articleHref(article) === path))
    .filter((article): article is Article => Boolean(article));

  const fallback = [...articles]
    .filter((article) => !ranked.some((item) => item.id === article.id))
    .sort((a, b) => {
      if (a.data.featured !== b.data.featured) return a.data.featured ? -1 : 1;
      return (a.data.featureOrder ?? 99) - (b.data.featureOrder ?? 99)
        || b.data.published.valueOf() - a.data.published.valueOf();
    });

  return [...ranked, ...fallback].slice(0, limit);
}
