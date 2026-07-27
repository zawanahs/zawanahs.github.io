import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { unified } from '@astrojs/markdown-remark';
import remarkEmoticons from './src/lib/remarkEmoticons.mjs';
import remarkFigureCaptions from './src/lib/remarkFigureCaptions.mjs';
import remarkTypography from './src/lib/remarkTypography.mjs';

export default defineConfig({
  site: 'https://zawanahs.github.io',
  output: 'static',
  integrations: [mdx(), sitemap()],
  markdown: {
    processor: unified({ remarkPlugins: [remarkEmoticons, remarkTypography, remarkFigureCaptions] }),
    shikiConfig: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
    },
  },
});
