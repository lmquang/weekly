#!/usr/bin/env python3
"""Update translated issue dates from upstream GitHub commit dates."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


FRONTMATTER_PATTERN = re.compile(r"\A---\n(?P<body>.*?)\n---(?:\n|\Z)", re.DOTALL)
DATE_PATTERN = re.compile(r"^date:\s*\S+\s*$", re.MULTILINE)
REPO = "ruanyf/weekly"
PUBLISH_TIMEZONE = timezone(timedelta(hours=7))


def github_request(url: str) -> tuple[list[dict[str, object]], str | None]:
	"""Fetch one GitHub API page and return JSON data plus next page URL."""
	headers = {
		"Accept": "application/vnd.github+json",
		"User-Agent": "weekly-date-check",
	}
	if token := os.environ.get("GITHUB_TOKEN"):
		headers["Authorization"] = f"Bearer {token}"

	request = Request(url, headers=headers)
	with urlopen(request, timeout=30) as response:
		links = response.headers.get("Link", "")
		data = json.load(response)

	next_url = None
	for part in links.split(","):
		section = part.strip()
		if section.endswith('rel="next"'):
			next_url = section.split(";", 1)[0].strip("<>")
			break

	return data, next_url


def upstream_publish_date(issue: str) -> str:
	"""Return oldest upstream commit date for an issue source file."""
	path = f"docs/{issue}.md"
	url = f"https://api.github.com/repos/{REPO}/commits?sha=master&path={path}&per_page=100"
	commits: list[dict[str, object]] = []

	while url:
		data, url = github_request(url)
		commits.extend(data)

	if not commits:
		raise RuntimeError(f"No upstream commits found for {path}")

	commit = commits[-1]["commit"]
	author = commit["author"]
	published_at = datetime.fromisoformat(author["date"].replace("Z", "+00:00")).astimezone(
		PUBLISH_TIMEZONE
	)
	return published_at.date().isoformat()


def set_frontmatter_date(markdown: str, issue_date: str) -> str:
	"""Set date metadata in Markdown frontmatter."""
	frontmatter = FRONTMATTER_PATTERN.match(markdown)
	if not frontmatter:
		return f"---\ndate: {issue_date}\n---\n\n{markdown}"

	body = frontmatter.group("body")
	if DATE_PATTERN.search(body):
		body = DATE_PATTERN.sub(f"date: {issue_date}", body, count=1)
	else:
		body = f"date: {issue_date}\n{body}"

	return f"{markdown[:frontmatter.start('body')]}{body}{markdown[frontmatter.end('body'):]}"


def update_issue(path: Path) -> bool:
	"""Update one translated issue date. Return whether file changed."""
	issue_date = upstream_publish_date(path.stem)
	markdown = path.read_text(encoding="utf-8")
	updated = set_frontmatter_date(markdown, issue_date)
	if updated == markdown:
		print(f"[OK] {path.name}: {issue_date}")
		return False

	path.write_text(updated, encoding="utf-8")
	print(f"[UPDATED] {path.name}: {issue_date}")
	return True


def main() -> int:
	"""Update dates for given issue files, or all translated issues."""
	root = Path.cwd()
	paths = [root / "docs-vi" / f"issue-{arg.removeprefix('issue-').removesuffix('.md')}.md" for arg in sys.argv[1:]]
	if not paths:
		paths = sorted((root / "docs-vi").glob("issue-*.md"))

	try:
		for path in paths:
			if not path.exists():
				raise FileNotFoundError(path)
			update_issue(path)
	except (FileNotFoundError, HTTPError, URLError, RuntimeError) as error:
		print(error, file=sys.stderr)
		return 1

	return 0


if __name__ == "__main__":
	raise SystemExit(main())
