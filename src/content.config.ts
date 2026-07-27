import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

export const categories = ['ideas', 'builds', 'notes', 'after-hours'] as const;

const articles = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/articles' }),
  schema: ({ image }) =>
    z.object({
      title: z.string().min(4),
      description: z.string().min(20).max(220),
      published: z.coerce.date(),
      updated: z.coerce.date().optional(),
      category: z.enum(categories),
      series: z.string().optional(),
      seriesOrder: z.number().int().min(1).optional(),
      tags: z.array(z.string()).default([]),
      featured: z.boolean().default(false),
      featureOrder: z.number().int().min(1).optional(),
      draft: z.boolean().default(false),
      cover: image().optional(),
      coverAlt: z.string().optional(),
      visual: z.enum(['agent-flow', 'empathy', 'analysis', 'hub', 'town', 'travel', 'none']).default('none'),
    })
    .refine((data) => !data.cover || Boolean(data.coverAlt), {
      message: 'coverAlt is required whenever cover is provided.',
      path: ['coverAlt'],
    }),
});

export const collections = { articles };
