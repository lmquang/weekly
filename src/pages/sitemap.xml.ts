import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';

const escapeXml = (value: string) =>
	value
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&apos;');

export const GET: APIRoute = async ({ site }) => {
	const baseUrl = site ?? new URL('https://weekly.locus.run');
	const issues = await getCollection('issues');
	const urls = [
		new URL('/', baseUrl).toString(),
		new URL('/issues/', baseUrl).toString(),
		...issues.map((issue) => new URL(`/issues/${issue.id}/`, baseUrl).toString()),
	];

	const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((url) => `\t<url><loc>${escapeXml(url)}</loc></url>`).join('\n')}
</urlset>`;

	return new Response(body, {
		headers: {
			'Content-Type': 'application/xml; charset=utf-8',
		},
	});
};
