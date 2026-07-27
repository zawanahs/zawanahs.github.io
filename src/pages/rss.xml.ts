import rss from '@astrojs/rss';
import { articleHref, getPublishedArticles } from '../lib/content';
import { SITE } from '../lib/site';

export async function GET() {
  const articles = await getPublishedArticles();
  return rss({
    title: SITE.title,
    description: SITE.description,
    site: SITE.url,
    items: articles.map((article) => ({
      title: article.data.title,
      description: article.data.description,
      pubDate: article.data.published,
      link: articleHref(article),
    })),
  });
}
