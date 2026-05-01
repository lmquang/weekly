import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';
import { getIssueNumber, getIssueSearchText, getIssueSummary, getIssueTitle } from '../lib/issues';

export const GET: APIRoute = async () => {
	const issues = await getCollection('issues');
	const searchIssues = issues
		.sort((a, b) => parseInt(getIssueNumber(b) || '0') - parseInt(getIssueNumber(a) || '0'))
		.map((issue) => ({
			number: getIssueNumber(issue),
			title: getIssueTitle(issue),
			summary: getIssueSummary(issue),
			tags: issue.data.tags ?? [],
			searchText: getIssueSearchText(issue),
			url: `/issues/${issue.id}`,
		}));

	return new Response(JSON.stringify(searchIssues), {
		headers: {
			'Content-Type': 'application/json; charset=utf-8',
			'Cache-Control': 'public, max-age=3600',
		},
	});
};
