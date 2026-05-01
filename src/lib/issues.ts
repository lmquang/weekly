import type { CollectionEntry } from 'astro:content';

type IssueEntry = CollectionEntry<'issues'>;

const boilerplateKeywords = ['Bản tin này ghi lại', 'Đây là nơi ghi lại', 'Tạp chí này', 'mã nguồn mở'];
const maxSummaryLength = 220;

function cleanMarkdown(text: string) {
	return text
		.replace(/!\[[^\]]*\]\([^)]*\)/g, '')
		.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
		.replace(/[#*`>]/g, '')
		.replace(/\s+/g, ' ')
		.trim();
}

function getCompleteSentences(paragraphs: string[]) {
	return paragraphs
		.flatMap((paragraph) => paragraph.match(/[^.!?]+[.!?](?=\s|$)/g) ?? [])
		.map((sentence) => sentence.trim())
		.filter((sentence) => !/^["'”,，,.)]/.test(sentence));
}

function buildSummary(paragraphs: string[]) {
	const sentences = getCompleteSentences(paragraphs);
	const selectedSentences: string[] = [];

	for (const sentence of sentences) {
		const nextSummary = [...selectedSentences, sentence].join(' ').trim();
		if (nextSummary.length > maxSummaryLength) break;
		selectedSentences.push(sentence.trim());
	}

	return selectedSentences.join(' ') || sentences[0]?.trim() || paragraphs[0] || '';
}

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
	const topicTitle = title.split(':').at(-1)?.trim() ?? title;
	const mainSectionIndex = allLines.findIndex((line) => {
		const heading = line.trim().replace(/^##\s+/, '');
		return heading === title || heading === topicTitle;
	});
	const candidateLines = mainSectionIndex >= 0 ? allLines.slice(mainSectionIndex + 1) : allLines;
	const nextSectionIndex = candidateLines.findIndex((line) => line.startsWith('## '));
	const sectionLines = nextSectionIndex >= 0 ? candidateLines.slice(0, nextSectionIndex) : candidateLines;
	const paragraphs: string[] = [];
	let currentParagraph: string[] = [];

	for (const line of sectionLines) {
		const trimmedLine = line.trim();
		const isSeparator = trimmedLine === '';
		const isHeader = trimmedLine.startsWith('#');
		const isBoilerplate = boilerplateKeywords.some((keyword) => line.includes(keyword));
		const isImage = trimmedLine.startsWith('!');
		const isQuote = trimmedLine.startsWith('>');
		const isListItem = /^[-*]\s+/.test(trimmedLine) || /^\(?\d+[.)]\s+/.test(trimmedLine);

		if (isSeparator || isHeader || isBoilerplate || isImage || isQuote || isListItem) {
			if (currentParagraph.length > 0) {
				paragraphs.push(cleanMarkdown(currentParagraph.join(' ')));
				currentParagraph = [];
			}
			continue;
		}

		currentParagraph.push(trimmedLine);
	}

	if (currentParagraph.length > 0) {
		paragraphs.push(cleanMarkdown(currentParagraph.join(' ')));
	}

	const summary = buildSummary(paragraphs.filter(Boolean));
	return summary || 'Khám phá những tin tức công nghệ mới nhất trong số này.';
}

export function getIssueImage(issue: IssueEntry) {
	const imageMatch = issue.body?.match(/!\[[^\]]*\]\(([^)]+)\)/);
	return imageMatch?.[1];
}
