import type { CollectionEntry } from 'astro:content';

type IssueEntry = CollectionEntry<'issues'>;

const boilerplateKeywords = ['Bản tin này ghi lại', 'Tạp chí này', 'mã nguồn mở'];

export function getIssueNumber(issue: IssueEntry) {
	return issue.id.match(/\d+/)?.[0] ?? '';
}

export function getIssueTitle(issue: IssueEntry) {
	if (issue.data.title) return issue.data.title;

	const h1Match = issue.body?.match(/^#\s+(.+)$/m);
	return h1Match ? h1Match[1].trim() : `Số ${getIssueNumber(issue)}`;
}

export function getIssueSummary(issue: IssueEntry) {
	const title = getIssueTitle(issue);
	const allLines = (issue.body ?? '').split('\n');
	const mainSectionIndex = allLines.findIndex((line) => line.trim() === `## ${title}`);
	const lines = (mainSectionIndex >= 0 ? allLines.slice(mainSectionIndex + 1) : allLines).filter(
		(line) => line.trim() !== ''
	);
	const contentLines = lines.filter((line) => {
		const isHeader = line.startsWith('#');
		const isBoilerplate = boilerplateKeywords.some((keyword) => line.includes(keyword));
		const isImage = line.startsWith('!');
		return !isHeader && !isBoilerplate && !isImage;
	});

	const summaryText = contentLines
		.join(' ')
		.replace(/!\[[^\]]*\]\([^)]*\)/g, '')
		.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
		.replace(/[#*`]/g, '')
		.replace(/\s+/g, ' ')
		.trim();

	const sentences = summaryText.match(/[^.!?]+[.!?](\s|$)/g) ?? [summaryText];
	const summary = sentences.length >= 2 ? `${sentences[0]}${sentences[1]}`.trim() : sentences[0].trim();

	return summary || 'Khám phá những tin tức công nghệ mới nhất trong số này.';
}

export function getIssueImage(issue: IssueEntry) {
	const imageMatch = issue.body?.match(/!\[[^\]]*\]\(([^)]+)\)/);
	return imageMatch?.[1];
}
