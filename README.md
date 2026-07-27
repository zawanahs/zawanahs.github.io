# Zawanah — personal site

A custom Astro publication for `zawanahs.github.io`, designed around Zawanah’s work as an AI Solutions Designer.

The site is intentionally Markdown-first. Writing and publishing an article does not require editing a page component.

## Local development

```bash
npm install
npm run dev
```

The development server prints the local URL. Use `npm run build` before publishing to run Astro’s checks and generate the static site.

## Publish an article

1. Create a URL-friendly folder in `src/content/articles/`, such as `why-good-agents-ask-questions/`.
2. Copy [`docs/ARTICLE_TEMPLATE.md`](docs/ARTICLE_TEMPLATE.md) into that folder and rename it `index.md`.
3. Keep the article's images in the same folder, then fill in the frontmatter and write the article in Markdown.
4. Preview with `npm run dev`.
5. Commit and push to the `main` branch. GitHub Actions builds and publishes the site.

The folder name becomes the article URL. For example:

```text
src/content/articles/why-good-agents-ask-questions/index.md
→ /articles/why-good-agents-ask-questions/
```

## Editorial controls

- `category` must be `ideas`, `builds`, `notes`, or `after-hours`.
- `series` is optional. Articles with the same value automatically get a series archive.
- `seriesOrder` controls the deliberate reading order inside a series.
- `tags` are reusable subjects. Every tag automatically gets its own archive at `/tags/tag-name/`.
- `featured: true` makes an article eligible for the homepage magazine hierarchy.
- `featureOrder: 1` is the cover story; higher numbers follow.
- `draft: true` shows an article locally but excludes it from the production build.
- `visual` chooses a built-in CSS cover while no custom cover image is supplied.
- `cover` and `coverAlt` can replace the built-in visual with an image stored alongside the article or in `src/assets/`.

## GitHub Pages setup

1. Create or use the repository named `zawanahs.github.io`.
2. Push this project to its `main` branch.
3. In GitHub, open **Settings → Pages** and set **Source** to **GitHub Actions**.
4. The workflow at `.github/workflows/deploy.yml` publishes every push to `main`.

The Astro site URL is currently `https://zawanahs.github.io`. When `zawanah.com` is ready, update `site` in `astro.config.mjs`, add a `public/CNAME` file containing `zawanah.com`, and configure the domain in GitHub Pages.

## Analytics

The site supports privacy-conscious Umami analytics without adding tracking code when it is not configured.

In the GitHub repository, create these **Actions variables**:

- `PUBLIC_ANALYTICS_SCRIPT_URL` — for Umami Cloud, `https://cloud.umami.is/script.js`
- `PUBLIC_ANALYTICS_WEBSITE_ID` — the website ID from the Umami dashboard
- `UMAMI_API_ENDPOINT` — for Umami Cloud, `https://api.umami.is/v1`

Create one **Actions secret**:

- `UMAMI_API_KEY` — a read-capable Umami Cloud API key; it is used only during the private GitHub build

Page paths are recorded automatically, so article, category, and series popularity can be compared. No analytics request is made when either variable is absent.

The deployment workflow refreshes `src/data/popular-articles.json` from the last 90 days of article pageviews before building, and also runs once daily. The homepage uses the three highest-viewed paths. Before analytics is configured or while the site has no traffic, featured articles are used as a fallback.

Never expose `UMAMI_API_KEY` as a `PUBLIC_` environment variable or fetch private analytics directly from browser code.

## Series and tags

Series and tags serve different purposes:

- A **series** is one intentional, ordered body of work, such as `nanoclaw` or `analyst-in-the-loop`. Use `seriesOrder` to control its reading sequence.
- A **tag** is a reusable subject, such as `agents`, `architecture`, or `leadership`. An article can have several tags and each tag automatically receives an archive page.

Do not automatically repeat a series name as a tag. Add it only when that same term is genuinely useful as a cross-series subject.

## Portrait

The circular `Z` is an intentional placeholder. Replace it after choosing a publishable portrait by adding the image to `public/images/` and updating the identity markup in `src/components/Header.astro` and `src/pages/about.astro`.
