#!/usr/bin/env python3
"""Check parity between original and translated weekly issues."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CHINESE_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002ebef]")
FRONTMATTER_PATTERN = re.compile(r"\A---\n(?P<body>.*?)\n---(?:\n|\Z)", re.DOTALL)
INLINE_TAGS_PATTERN = re.compile(r"^tags:\s*\[(?P<tags>.*)]\s*$", re.MULTILINE)
BLOCK_TAGS_PATTERN = re.compile(r"^tags:\s*\n(?P<tags>(?:\s+-\s*.+\n?)+)", re.MULTILINE)
DATE_PATTERN = re.compile(r"^date:\s*\S+\s*$", re.MULTILINE)
STANDALONE_ORDERED_MARKER_PATTERN = re.compile(r"^\d+\.$")
STANDALONE_MARKER_PATTERN = re.compile(r"^(?P<number>\d+)(?:\\\.|\.|、)$")


@dataclass(frozen=True)
class ChineseTextMatch:
	"""Chinese text occurrence in a translated issue."""

	line_number: int
	column_number: int
	character: str
	line: str


@dataclass(frozen=True)
class ImageCheckResult:
	"""Image parity result for one translated issue."""

	issue: str
	source_path: Path
	translation_path: Path
	source_images: tuple[str, ...]
	translation_images: tuple[str, ...]
	chinese_matches: tuple[ChineseTextMatch, ...]
	tag_errors: tuple[str, ...]
	markdown_errors: tuple[str, ...]

	@property
	def is_ok(self) -> bool:
		"""Return whether translation passes all checks."""
		return (
			not self.missing_images
			and not self.extra_images
			and not self.chinese_matches
			and not self.tag_errors
			and not self.markdown_errors
		)

	@property
	def missing_images(self) -> tuple[str, ...]:
		"""Return source images missing from translation, preserving duplicate counts."""
		remaining_translation_images = list(self.translation_images)
		missing: list[str] = []

		for image in self.source_images:
			try:
				remaining_translation_images.remove(image)
			except ValueError:
				missing.append(image)

		return tuple(missing)

	@property
	def extra_images(self) -> tuple[str, ...]:
		"""Return translation images absent from source, preserving duplicate counts."""
		remaining_source_images = list(self.source_images)
		extra: list[str] = []

		for image in self.translation_images:
			try:
				remaining_source_images.remove(image)
			except ValueError:
				extra.append(image)

		return tuple(extra)


def extract_images(markdown: str) -> tuple[str, ...]:
	"""Extract Markdown image targets from a document."""
	return tuple(match.group(1) for match in IMAGE_PATTERN.finditer(markdown))


def read_images(path: Path) -> tuple[str, ...]:
	"""Read a Markdown file and return image targets."""
	return extract_images(path.read_text(encoding="utf-8"))


def find_chinese_text(markdown: str) -> tuple[ChineseTextMatch, ...]:
	"""Find Han ideographs in a translated Markdown document."""
	matches: list[ChineseTextMatch] = []

	for line_number, line in enumerate(markdown.splitlines(), start=1):
		for match in CHINESE_PATTERN.finditer(line):
			matches.append(
				ChineseTextMatch(
					line_number=line_number,
					column_number=match.start() + 1,
					character=match.group(0),
					line=line.strip(),
				)
			)

	return tuple(matches)


def read_chinese_text(path: Path) -> tuple[ChineseTextMatch, ...]:
	"""Read a Markdown file and return Chinese text occurrences."""
	return find_chinese_text(path.read_text(encoding="utf-8"))


def extract_frontmatter_tags(markdown: str) -> tuple[str, ...]:
	"""Extract tags from top-level YAML frontmatter without a YAML dependency."""
	frontmatter = FRONTMATTER_PATTERN.match(markdown)
	if not frontmatter:
		return ()

	body = frontmatter.group("body")
	inline_match = INLINE_TAGS_PATTERN.search(body)
	if inline_match:
		return tuple(
			tag.strip().strip('"\'')
			for tag in inline_match.group("tags").split(",")
			if tag.strip().strip('"\'')
		)

	block_match = BLOCK_TAGS_PATTERN.search(body)
	if block_match:
		return tuple(
			line.split("-", 1)[1].strip().strip('"\'')
			for line in block_match.group("tags").splitlines()
			if line.strip().startswith("-") and line.split("-", 1)[1].strip().strip('"\'')
		)

	return ()


def validate_tags(markdown: str) -> tuple[str, ...]:
	"""Validate translated issue frontmatter tags for search metadata."""
	errors: list[str] = []

	frontmatter = FRONTMATTER_PATTERN.match(markdown)
	if not frontmatter:
		errors.append("missing YAML frontmatter at top of file")
		return tuple(errors)

	if not DATE_PATTERN.search(frontmatter.group("body")):
		errors.append("missing date in YAML frontmatter")

	tags = extract_frontmatter_tags(markdown)
	if not tags:
		errors.append("missing tags in YAML frontmatter")
		return tuple(errors)
	if len(tags) != 10:
		errors.append(f"expected 10 tags, found {len(tags)}")

	return tuple(errors)


def read_tag_errors(path: Path) -> tuple[str, ...]:
	"""Read a Markdown file and return tag metadata validation errors."""
	return validate_tags(path.read_text(encoding="utf-8"))


def validate_markdown(markdown: str) -> tuple[str, ...]:
	"""Validate Markdown patterns that render incorrectly after translation."""
	errors: list[str] = []
	in_quote_section = False

	for line_number, line in enumerate(markdown.splitlines(), start=1):
		stripped_line = line.strip()
		if stripped_line.startswith("## "):
			in_quote_section = stripped_line == "## Trích dẫn"

		marker = STANDALONE_MARKER_PATTERN.fullmatch(stripped_line)
		if in_quote_section and marker and not stripped_line.endswith("\\."):
			errors.append(
				f"line {line_number}: use quote marker `{marker.group('number')}\\.` "
				f"inside `## Trích dẫn`"
			)
		elif not in_quote_section and marker:
			errors.append(
				f"line {line_number}: remove standalone marker `{stripped_line}` "
				"outside `## Trích dẫn`"
			)

	return tuple(errors)


def read_markdown_errors(path: Path) -> tuple[str, ...]:
	"""Read a Markdown file and return Markdown validation errors."""
	return validate_markdown(path.read_text(encoding="utf-8"))


def add_frontmatter_date(markdown: str, current_date: str) -> str:
	"""Add date metadata to translated Markdown frontmatter if missing."""
	frontmatter = FRONTMATTER_PATTERN.match(markdown)
	if not frontmatter:
		return f"---\ndate: {current_date}\n---\n\n{markdown}"

	body = frontmatter.group("body")
	if DATE_PATTERN.search(body):
		return markdown

	return (
		f"{markdown[:frontmatter.start('body')]}"
		f"date: {current_date}\n"
		f"{body}"
		f"{markdown[frontmatter.end('body'):]}"
	)


def normalize_translation_markdown(markdown: str) -> str:
	"""Normalize translated Markdown markers to parser-friendly forms."""
	lines: list[str] = []
	in_quote_section = False

	for line in markdown.splitlines():
		stripped_line = line.strip()
		if stripped_line.startswith("## "):
			if stripped_line in {"## Ngôn luận", "## 言论"}:
				line = "## Trích dẫn"
				stripped_line = line
			elif stripped_line == "## 文摘":
				line = "## Trích đoạn"
				stripped_line = line
			in_quote_section = stripped_line == "## Trích dẫn"

		marker = STANDALONE_MARKER_PATTERN.fullmatch(stripped_line)
		if marker:
			number = marker.group("number")
			if in_quote_section:
				line = f"{number}\\."
			else:
				continue
		elif in_quote_section and stripped_line.startswith("—"):
			line = f"-- {stripped_line.removeprefix('—').strip()}"

		lines.append(line)

	return "\n".join(lines) + ("\n" if markdown.endswith("\n") else "")


def normalize_translation_file(path: Path, current_date: str) -> bool:
	"""Normalize one translated Markdown file in place. Return whether it changed."""
	markdown = path.read_text(encoding="utf-8")
	normalized_markdown = add_frontmatter_date(
		normalize_translation_markdown(markdown), current_date
	)
	if normalized_markdown == markdown:
		return False

	path.write_text(normalized_markdown, encoding="utf-8")
	return True


def normalize_issue(issue: str) -> str:
	"""Normalize user input like `390` or `issue-390` to `issue-390`."""
	issue = issue.removesuffix(".md")
	return issue if issue.startswith("issue-") else f"issue-{issue}"


def discover_issues(root: Path) -> list[str]:
	"""Discover source issues that have Vietnamese translation files."""
	source_dir = root / "docs"
	translation_dir = root / "docs-vi"
	issues: list[str] = []

	for source_path in sorted(source_dir.glob("issue-*.md")):
		issue = source_path.stem
		if (translation_dir / f"{issue}.md").exists():
			issues.append(issue)

	return issues


def check_issue(root: Path, issue: str) -> ImageCheckResult:
	"""Check image-count parity for one issue."""
	issue = normalize_issue(issue)
	source_path = root / "docs" / f"{issue}.md"
	translation_path = root / "docs-vi" / f"{issue}.md"

	if not source_path.exists():
		raise FileNotFoundError(f"Missing source file: {source_path}")
	if not translation_path.exists():
		raise FileNotFoundError(f"Missing translation file: {translation_path}")

	return ImageCheckResult(
		issue=issue,
		source_path=source_path,
		translation_path=translation_path,
		source_images=read_images(source_path),
		translation_images=read_images(translation_path),
		chinese_matches=read_chinese_text(translation_path),
		tag_errors=read_tag_errors(translation_path),
		markdown_errors=read_markdown_errors(translation_path),
	)


def print_result(result: ImageCheckResult, verbose: bool) -> None:
	"""Print one issue check result."""
	status = "OK" if result.is_ok else "FAIL"
	print(
		f"[{status}] {result.issue}: "
		f"source images={len(result.source_images)}, "
		f"translation images={len(result.translation_images)}"
	)

	if not result.is_ok or verbose:
		print(f"  source:      {result.source_path}")
		print(f"  translation: {result.translation_path}")

	if result.missing_images:
		print("  missing images:")
		for image in result.missing_images:
			print(f"    - {image}")
	if result.extra_images:
		print("  extra images:")
		for image in result.extra_images:
			print(f"    - {image}")
	if result.chinese_matches:
		print("  Chinese text found in translation:")
		for match in result.chinese_matches:
			print(
				f"    - line {match.line_number}, column {match.column_number}: "
				f"{match.character} in {match.line}"
			)
	if result.tag_errors:
		print("  tag metadata errors:")
		for error in result.tag_errors:
			print(f"    - {error}")
	if result.markdown_errors:
		print("  markdown errors:")
		for error in result.markdown_errors:
			print(f"    - {error}")

	if verbose:
		print("  source images:")
		for image in result.source_images:
			print(f"    - {image}")
		print("  translation images:")
		for image in result.translation_images:
			print(f"    - {image}")


def parse_args() -> argparse.Namespace:
	"""Parse command-line arguments."""
	parser = argparse.ArgumentParser(
		description="Check translated issue parity against original issue files."
	)
	parser.add_argument(
		"issues",
		nargs="*",
		help="Issue numbers or names to check, e.g. 390 or issue-390. Defaults to all translated issues.",
	)
	parser.add_argument(
		"--root",
		type=Path,
		default=Path.cwd(),
		help="Repository root. Defaults to current working directory.",
	)
	parser.add_argument(
		"--verbose",
		action="store_true",
		help="Print image URLs for each checked file.",
	)
	parser.add_argument(
		"--fix",
		action="store_true",
		help="Normalize translated Markdown marker characters before checking.",
	)
	return parser.parse_args()


def main() -> int:
	"""Run translation checks."""
	args = parse_args()
	root = args.root.resolve()
	issues = [normalize_issue(issue) for issue in args.issues] or discover_issues(root)
	current_date = date.today().isoformat()

	if not issues:
		print("No translated issues found.", file=sys.stderr)
		return 1

	results: list[ImageCheckResult] = []
	try:
		for issue in issues:
			if args.fix:
				translation_path = root / "docs-vi" / f"{issue}.md"
				if normalize_translation_file(translation_path, current_date):
					print(f"[FIXED] {translation_path}")
			result = check_issue(root, issue)
			results.append(result)
			print_result(result, args.verbose)
	except FileNotFoundError as error:
		print(error, file=sys.stderr)
		return 1

	failed = [result for result in results if not result.is_ok]
	if failed:
		print(f"\n{len(failed)} issue(s) failed translation check.", file=sys.stderr)
		return 1

	print(f"\nAll {len(results)} issue(s) passed translation check.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
