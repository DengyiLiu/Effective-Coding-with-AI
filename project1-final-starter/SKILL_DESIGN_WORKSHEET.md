# SKILL_DESIGN_WORKSHEET.md

Use this worksheet before writing or editing a SKILL.md file.

A skill is useful when the same workflow will happen more than once. Today,
the recurring workflow is:

~~~text
Polish my Week 2 portfolio into a stronger Project 1 portfolio.
~~~

Keep the first version narrow. One good job is better than ten vague jobs.

## Seven design decisions

1. Recurring task: What exact Week 2-to-Project 1 workflow should this skill support?
2. Audience: Who will use the skill?
3. Trigger: What user request should make the AI use it?
4. Inputs: Which files should AI read first?
5. Workflow: What steps should AI follow before editing?
6. Constraints: What should AI avoid?
7. Output format: What should AI return so the student can review it?

## Weak vs stronger trigger

Weak:

~~~text
Helps with websites.
~~~

Stronger:

~~~text
Polish a Week 2 AIM 5012 portfolio skeleton into a Project 1 portfolio while
preserving beginner-friendly HTML/CSS, visible AI workflow evidence, one
simple interaction, and browser verification.
~~~

## Suggested student skill

Create this file in your own project:

~~~text
.agents/skills/project1-portfolio-polish/SKILL.md
~~~

Keep it instruction-only for Week 3. Add references or scripts later only if
the skill becomes too large or needs deterministic checks.

## Validation prompt

After writing the skill, start a fresh AI request and ask:

~~~text
Read .agents/skills/project1-portfolio-polish/SKILL.md.
Do not edit my files yet.
Tell me when you would use this skill, what files you would inspect first,
and what output you would return before editing.
~~~
