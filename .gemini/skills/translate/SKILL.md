---
name: translate
description: >
  Translate weekly-news Markdown documents in `docs/issue-*.md` into Vietnamese.
  Use when asked to translate one issue, multiple issues, or specific sections of the
  technology newsletter while preserving Markdown structure, links, images, numbering,
  and technical meaning.
---

# Translate Weekly News To Vietnamese

Translate source newsletter files in `docs/issue-*.md` into natural Vietnamese with the exploratory and thoughtful style of Paul Graham (as seen in Dwarves Foundation memos).

## When To Use

- Receive a request to translate `docs/issue-*.md`
- Receive a request to translate one section of an issue into Vietnamese
- Receive a request to localize weekly tech-news content for Vietnamese readers

## Source Pattern

Expect input documents with a stable structure:

- H1 title with issue number
- Intro paragraph with project links
- Repeating section headings such as `## 封面图`, `## 科技动态`, `## 文章`, `## 工具`, `## AI 相关`
- Markdown images, numbered lists, inline links, and short commentary paragraphs

## Translation Goal

Produce Vietnamese text that reads like a thoughtful essay or a memo. The content should feel like an exploration of ideas rather than just a literal translation.

## Writing Style & Tone (Paul Graham Style v3.0)

- **Exploratory & Candid:** Write as if you are discovering the insights along with the reader. Use a tone that is informal yet intellectually rigorous.
- **Natural & Active Voice:** Prioritize active voice. Avoid unnecessary passive structures (e.g., instead of "Data is saved by...", use "The system saves..."). Limit the use of "được", "bị", "bởi".
- **Rhythmic Flow:** Match Paul Graham's simplicity and crispness. Use short, punchy sentences for key points and well-structured medium-to-long sentences for explanations.
- **Community Jargon & Transcreation:** Use modern Vietnamese tech jargon (e.g., "chạy code", "deploy", "render", "prompt"). Adapt metaphors to fit the Vietnamese cultural context where appropriate.
- **Language Purity:** Avoid heavy or outdated Sino-Vietnamese (Hán-Việt) terms. Prefer pure Vietnamese for a warmer, more engaging feel (e.g., use "khám phá" instead of "thăm dò").
- **Sentence Structure:** **STRICTLY: Do not use the em dash (—).** Use commas, parentheses, or start a new sentence.
- **Perspective:** Use a first-person voice that is authoritative yet humble. Share the "why" and "how" behind trends.

## Workflow

1. Inspect the target file and identify whether the task is full-document translation or section-only translation.
2. Create a translated sibling file in the specialized directory: `docs-vi/issue-<number>.md`.
3. **Transcreate** the content into Vietnamese using the Premium Style.
4. Preserve Markdown syntax: headings, lists, links, images, emphasis, inline code, and tables.
5. Keep product names, person names, repository names, and URLs unchanged.
6. Re-read for tonal flow—ensure the Vietnamese has a natural "rhythm" and sounds like a tech memo for experts.

## Translation Rules

- **Faithful yet Fluid:** Do not just translate words; translate the inquiry and the "vibe".
- **File Location:** Always use `docs-vi/issue-<number>.md`.
- **Technical Terms:** Keep widely used English terms (API, Agent, LLM, Watermark, Framework, Prompt, Deploy, Render) as is.
- **Natural Transitions:** Use smooth Vietnamese transitions (e.g., "Thực tế là...", "Đáng nói ở chỗ...", "Vậy nên...") instead of stiff literal translations.


## Quality Check

- Is the tone thoughtful and exploratory?
- Are there any em dashes? (Should be none).
- Does it sound like a "memo" for tech experts?
- Is the file saved in `docs-vi/issue-<number>.md`?
- Is the Markdown structure intact?


