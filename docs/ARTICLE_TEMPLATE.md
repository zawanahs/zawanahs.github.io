---
title: "Your article title"
description: "A clear one- or two-sentence description used on article cards, search results, and link previews."
published: 2026-07-15
category: ideas
series: optional-series-name
seriesOrder: 1
tags: [first-tag, second-tag]
featured: false
draft: true
visual: none
---

Open with the reason this was worth writing. Give the reader a specific situation, question, or observation rather than a broad introduction.

## A useful section heading

Write in ordinary Markdown. Paragraphs become article copy automatically.

- Lists work.
- **Bold** and *italic* work.
- [Links](https://example.com) work.

> Blockquotes receive their own editorial treatment.

## Adding an image with a caption

Keep the image in the same folder as `index.md`, then add its accessible description and visible caption together:

```md
![A concise description of the image](./image-name.webp "Figure 1: The visible caption")
```

The website automatically centres the image and renders the quoted text as its caption.

## Publishing checklist

- Replace the placeholder title, description, date, and category.
- Remove `series` if this is a standalone article.
- Remove `seriesOrder` if this is a standalone article; otherwise use it to control reading order within the series.
- Set `draft: false` when the article is ready to publish.
- Choose a built-in visual: `agent-flow`, `empathy`, `analysis`, `hub`, `town`, `travel`, or `none`.
- To feature it, set `featured: true` and add a unique `featureOrder`.
- Run `npm run build` before pushing.
