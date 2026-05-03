import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const issues = defineCollection({
	loader: glob({ pattern: '**/issue-*.md', base: "./docs-vi" }),
	schema: z.object({
		title: z.string().optional(),
		date: z.union([z.string(), z.date()]).optional(),
		tags: z.array(z.string()).optional(),
	}),
});

export const collections = { issues };
