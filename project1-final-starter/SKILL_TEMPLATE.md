# SKILL_TEMPLATE.md

Copy this into:

~~~text
.agents/skills/project1-portfolio-polish/SKILL.md
~~~

Then customize the description, inputs, workflow, constraints, and output format.

~~~md
---
name: project1-portfolio-polish
description: Polish a Week 2 AIM 5012 portfolio skeleton into a Project 1 portfolio while preserving beginner-friendly HTML/CSS, visible AI workflow evidence, useful Week 2 visual details, one simple interaction, and browser verification.
---

# Project 1 Portfolio Polish

Use this skill when the student asks to polish the Week 2 portfolio website
into a stronger Project 1 submission.

## Read first

- README.md
- PROJECT_BRIEF.md
- STYLE_DIRECTION.md
- TEST_PLAN.md
- index.html
- style.css
- PROMPTS.md
- Provided Week 2 demo or reference folder, if the student gives one

## Workflow

1. Inspect the current Week 2 portfolio before editing.
2. If a Week 2 demo/reference is provided, inspect its index.html and style.css.
3. Summarize what the site already has and what Project 1 still needs.
4. Identify useful existing visual features to keep, such as gold image/card accents, hover/focus states, status-strip layout, spacing, shadows, and responsive card behavior.
5. Return a small polish plan and wait for student approval.
6. Edit index.html first.
7. Edit style.css second: keep or restore useful Week 2 visual details.
8. Require browser tests after visible changes.
9. Ask the student to update PROMPTS.md.

## Constraints

- Keep HTML and CSS beginner-friendly.
- Do not add frameworks, build tools, package managers, or advanced JavaScript.
- Do not rewrite the whole page.
- Preserve visible AI workflow evidence.
- Include or preserve one small testable interaction.

## Output before editing

Return:

- Current Week 2 site
- Project 1 polish goals
- Proposed edit order
- Approval question
- Browser test checklist
~~~
