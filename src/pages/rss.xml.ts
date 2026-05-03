import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';
import { getIssueNumber, getIssueSummary, getIssueTitle } from '../lib/issues';

const escapeXml = (value: string) =>
	value
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&apos;');

const getDate = (value: string | Date | undefined) => {
	if (value instanceof Date) return value;
	if (value) return new Date(value);
	return undefined;
};

export const GET: APIRoute = async ({ site }) => {
	const baseUrl = site ?? new URL('https://techmemo.cc');
	const issues = await getCollection('issues');
	const sortedIssues = issues.sort((a, b) => {
		const numA = parseInt(getIssueNumber(a) || '0');
		const numB = parseInt(getIssueNumber(b) || '0');
		return numB - numA;
	});
	const latestDate = sortedIssues.map((issue) => getDate(issue.data.date)).find(Boolean);

	const items = sortedIssues
		.map((issue) => {
			const title = `Issue #${getIssueNumber(issue)} - ${getIssueTitle(issue)}`;
			const description = getIssueSummary(issue);
			const url = new URL(`/issues/${issue.id}/`, baseUrl).toString();
			const date = getDate(issue.data.date);

			return `<item>
		<title>${escapeXml(title)}</title>
		<link>${escapeXml(url)}</link>
		<guid isPermaLink="true">${escapeXml(url)}</guid>
		<description>${escapeXml(description)}</description>${date ? `
		<pubDate>${date.toUTCString()}</pubDate>` : ''}
	</item>`;
		})
		.join('\n');

	const body = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
	<title>Tech Memo</title>
	<link>${escapeXml(new URL('/', baseUrl).toString())}</link>
	<description>Bản dịch tiếng Việt của các bản tin công nghệ hàng tuần.</description>
	<language>vi-VN</language>${latestDate ? `
	<lastBuildDate>${latestDate.toUTCString()}</lastBuildDate>` : ''}
${items}
</channel>
</rss>`;

	return new Response(body, {
		headers: {
			'Content-Type': 'application/rss+xml; charset=utf-8',
		},
	});
};
