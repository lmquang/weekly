#!/usr/bin/env python3
"""Check parity between original and translated weekly issues."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


@dataclass(frozen=True)
class ImageCheckResult:
	"""Image parity result for one translated issue."""

	issue: str
	source_path: Path
	translation_path: Path
	source_images: tuple[str, ...]
	translation_images: tuple[str, ...]

	@property
	def is_ok(self) -> bool:
		"""Return whether source and translation image URLs match."""
		return not self.missing_images and not self.extra_images

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
	return parser.parse_args()


def main() -> int:
	"""Run translation checks."""
	args = parse_args()
	root = args.root.resolve()
	issues = [normalize_issue(issue) for issue in args.issues] or discover_issues(root)

	if not issues:
		print("No translated issues found.", file=sys.stderr)
		return 1

	results: list[ImageCheckResult] = []
	try:
		for issue in issues:
			result = check_issue(root, issue)
			results.append(result)
			print_result(result, args.verbose)
	except FileNotFoundError as error:
		print(error, file=sys.stderr)
		return 1

	failed = [result for result in results if not result.is_ok]
	if failed:
		print(f"\n{len(failed)} issue(s) failed image-count check.", file=sys.stderr)
		return 1

	print(f"\nAll {len(results)} issue(s) passed image-count check.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
