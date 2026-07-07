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
3. Add YAML frontmatter metadata at the very top with 10 topical `tags`.
4. **Transcreate** the content into Vietnamese using the Premium Style.
5. Preserve Markdown syntax: headings, lists, links, images, emphasis, inline code, and tables.
6. Keep product names, person names, repository names, and URLs unchanged.
7. Re-read for tonal flow—ensure the Vietnamese has a natural "rhythm" and sounds like a tech memo for experts.
8. Run the translation post-process and parity validation for the issue: `python3 scripts/check_translation.py --fix <issue-number>`. Fix any remaining validation failure before finishing.

## Translation Rules

- **Faithful yet Fluid:** Do not just translate words; translate the inquiry and the "vibe".
- **File Location:** Always use `docs-vi/issue-<number>.md`.
- **Metadata Tags:** Every full translated issue must start with YAML frontmatter containing only `tags`. Choose exactly 10 useful tags based on the issue's main topics, mixing English and Vietnamese search terms where helpful. Prefer useful search terms like `ai`, `trí tuệ nhân tạo`, `lập trình`, `phần cứng`, `startup`, `internet`, `bảo mật`, `cloud`, `robot`, `thiết kế`, `mã nguồn mở`. Avoid generic tags like `weekly`, `news`, or `technology` unless the issue is specifically about those concepts.
- **Metadata Format:** Use this exact shape before the H1 title:

  ```md
  ---
  tags: ["ai", "trí tuệ nhân tạo", "lập trình", "programming", "cloud", "đám mây", "startup", "internet", "bảo mật", "security"]
  ---

  # <translated topic title>
  ```
- **H1 Title Cleanup:** Remove generic newsletter prefixes from the translated H1. If the source or draft title has the form `科技爱好者周刊（第 N 期）：<topic>` or `Tuần báo công nghệ (Số N): <topic>`, output only `# <topic>`. Example: `# Tuần báo công nghệ (Số 380): Tại sao mọi người lại chọn "Lợi nhuận không đối xứng"` becomes `# Tại sao mọi người lại chọn "Lợi nhuận không đối xứng"`.
- **Technical Terms:** Keep widely used English terms (API, Agent, LLM, Watermark, Framework, Prompt, Deploy, Render) as is.
- **Omit Intro Paragraph:** Skip the introductory paragraph that follows the H1 title (the one containing project links, contribution info, recruitment service, and email contact). The translation should start directly with the first section (usually "## 封面图" or "## Ảnh bìa") after the H1 title.
- **Omit "Looking Back" Section:** Skip the final section titled "## 往年回顾" or "## Nhìn lại năm xưa". The translation should end before this section.
- **Section Names:** Translate `## 文摘` as `## Trích đoạn`. Translate `## 言论` as `## Trích dẫn` so the site can render quote cards.
- **Natural Transitions:** Use smooth Vietnamese transitions (e.g., "Thực tế là...", "Đáng nói ở chỗ...", "Vậy nên...") instead of stiff literal translations.
- **Standalone Number Markers:** If the source uses standalone Chinese section markers like `1、`, `2、` outside the `## Trích dẫn` section, omit those marker-only lines. They add visual noise and are not needed by the site parser.
- **Quote Markers:** Inside `## Trích dẫn`, use escaped standalone quote markers as `1\.`, `2\.`, etc. This displays as `1.`, avoids accidental Markdown lists, and lets the site turn each quote/source pair into a quote card.
- **Post-process Required:** Always run `python3 scripts/check_translation.py --fix <issue-number>` after writing the translated file. This standardizes section names, standalone markers, and quote markers before validation.


## Quality Check

- Is the tone thoughtful and exploratory?
- Are there any em dashes? (Should be none).
- Does a full translated issue start with YAML frontmatter containing 10 useful `tags` include both English and Vietnamese terms?
- Are standalone marker-only lines outside `## Trích dẫn` omitted?
- Are `## Trích dẫn` markers written as escaped `1\.`, `2\.`, etc.?
- Does the H1 omit generic issue prefixes and keep only the topic title?
- Does it sound like a "memo" for tech experts?
- Is the file saved in `docs-vi/issue-<number>.md`?
- Is the Markdown structure intact?
- Does `python3 scripts/check_translation.py --fix <issue-number>` pass? The translated file must preserve the same number of Markdown images as the source.
