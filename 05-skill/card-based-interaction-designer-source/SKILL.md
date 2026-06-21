---
name: card-based-interaction-designer
description: design safe, structured card-based interaction systems for conversation, learning, culture, onboarding, workshops, change management, training, personal growth, family activities, and team reflection. Use when the user wants to create, review, revise, or package a deck of prompt cards, scenario cards, reflection cards, discussion cards, quiz cards, facilitation cards, or any gamified interaction tool. Also use when converting existing material such as policies, change plans, training notes, values, meeting notes, or personal-development topics into cards with safety checks, card taxonomy, facilitation guidance, and reusable output formats.
---

# Card-Based Interaction Designer

## Core principle

Design an interaction system, not just a list of questions. Start with purpose, audience, setting, power dynamics, disclosure level, and safety boundaries before writing or revising cards.

Prefer card formats that let people answer through choice, scenario, sorting, ranking, trade-off, or practical action. Avoid forcing confession, vulnerability, blame, embarrassment, or disclosure.

## Default workflow

1. Clarify the brief.
2. Classify the deck type.
3. Identify risk, disclosure level, and power dynamics.
4. Build the card taxonomy.
5. Generate or review a small sample first unless the user explicitly asks for a full deck.
6. Run a safety and usefulness review.
7. Revise flagged cards.
8. Produce the requested output format.
9. Add facilitation, pilot-test, and next-step guidance when useful.

If the user asks to review an existing deck, skip generation and perform a structured review first. If the user asks for print files, follow the relevant document, spreadsheet, slide, or PDF skill instructions outside this skill.

## Intake questions

Ask only the missing questions needed to proceed. Do not overload the user. The minimum required inputs are:

- Purpose: What should the cards help people do?
- Audience: Who will use them?
- Setting: Where and how will they be used?
- Output: What format is needed?

When relevant, also ask:

- Relationship dynamics: family, peers, managers and staff, strangers, mixed ages, leadership team, community group.
- Sensitivity: light, curious, reflective, workplace-safe, change-management, confidential.
- Deck size: 10, 25, 50, 75, or 100 cards.
- Facilitation: self-guided, lightly facilitated, strongly facilitated, anonymous, private reflection.
- Capture: no capture, anonymous themes, named actions, workshop notes, or follow-up report.

## Deck type decision tree

Classify the request before producing cards:

- Connection deck: conversation, belonging, icebreakers, family, community.
- Learning deck: training, retention, teach-back, concept checking.
- Reflection deck: coaching, journaling, personal growth, planning.
- Decision deck: prioritisation, trade-offs, strategy, values, options.
- Change deck: workplace change, adoption, uncertainty, barriers, support, next steps.
- Culture deck: team norms, leadership, behaviour, rituals, values.
- Workshop deck: facilitated group activity, breakout discussion, planning.

Use the classification to set tone, risk level, disclosure level, and facilitation mode.

## Disclosure levels

Default to the lowest level that can achieve the purpose.

- Level 0: no personal disclosure. Hypotheticals, scenarios, choices, ranking options.
- Level 1: preference. What would you choose? What works best for you?
- Level 2: experience. What have you seen work before?
- Level 3: reflection. What helps you when things change?
- Level 4: vulnerability. What feels hard, uncertain, or personal?
- Level 5: sensitive. Trauma, conflict, identity, grief, money, health, relationships. Avoid unless explicitly requested and appropriate.

Defaults:

- Family or social decks: Level 0 to 3.
- Workplace decks: Level 0 to 2.
- Change-management decks: Level 0 to 2, with Level 3 only in facilitated or private-reflection mode.

## Safety rules

Apply these rules to every deck:

- Passing is always allowed.
- No one has to explain why they passed.
- Make prompts answerable lightly.
- Keep teasing kind and opt-in.
- Do not rank people negatively.
- Challenge ideas or scenarios, not people.
- Use neutral framing such as “someone might” or “a team might” for sensitive workplace topics.
- Do not collect identifiable sensitive responses unless the user has a clear, ethical purpose.

Avoid prompts that invite:

- Shame, gossip, blame, ranking people, confession, trauma, family conflict, body image, personal money issues, health disclosure, politics as debate, religion as debate, performance judgement, or private relationship details.

For workplace decks, also avoid:

- Forced positivity.
- “Why are people resisting?” framing.
- Questions that ask employees to disclose fear in front of managers.
- Questions that could be used for performance assessment.
- Prompts that imply consultation, HR, health and safety, or training obligations have been met when they have not.

## Power-dynamics check

For workplaces, teams, schools, community groups, or any mixed-authority setting, assess:

- Who has authority in the room?
- Can managers, teachers, leaders, or parents hear the answers?
- Is participation optional?
- Could answers affect reputation, trust, opportunity, grading, or employment?
- Should responses be anonymous or private?
- Should the activity be facilitated?

If risk is high, recommend anonymous, scenario-based, or private-reflection formats.

## Card architecture

Use references/card-types.md for the card type library.
Use references/domain-packs.md for domain-specific guidance.
Use references/safety-review.md for review and rewriting rules.
Use references/output-schemas.md for tables and data fields.
Use references/facilitation-patterns.md for instruction sheets and facilitator guides.
Use references/change-management-mode.md for change-specific decks.

Balance the deck. Suggested ratios:

- Family or social: 60% fun, 25% curious, 10% meaningful, 5% wildcard.
- Workplace change: 30% low-risk scenario, 25% practical support, 20% prioritisation, 15% reflection, 10% action.
- Training: 35% recall, 25% application, 20% scenario, 10% misconception check, 10% teach-back.
- Personal growth: 25% choice, 25% reflection, 20% values, 20% tiny action, 10% wildcard.

## Bad-card rewriting

When a card is risky, vague, boring, or cringe, rewrite it into a safer interaction pattern.

Examples:

Risky: “What are you afraid of with this change?”
Safer: “Pick the support that would make this change easier: clear instructions, time to practise, someone to ask, fewer surprises, or better examples.”

Risky: “Why do people resist new systems?”
Safer: “What usually makes a new system harder to adopt: unclear purpose, poor training, time pressure, old habits, or missing support?”

Vague: “How do you feel about AI?”
Safer: “Pick one AI use case you would trust first: summarising, drafting, checking, planning, or finding information. Why?”

## Required review scoring

When reviewing or generating a deck for real use, score or label each card for:

- Clarity.
- Engagement.
- Usefulness.
- Safety.
- Audience fit.
- Actionability, for workplace decks.

Flag cards as:

- Keep.
- Revise.
- Remove.
- Move to private reflection.
- Use only with facilitation.

## Output formats

Support any of these outputs:

- Brief only.
- Deck architecture only.
- Sample cards.
- Full card table.
- Safety-reviewed card table.
- Card copy for design templates.
- Instruction sheet.
- Facilitator guide.
- Pilot-test checklist.
- Icon or category map.
- Workshop agenda.
- Revision log.

When the user wants structured data, use the schema in references/output-schemas.md. Prefer tables, CSV-ready fields, or JSON when the user plans automation or print production.

## Existing deck review

If the user provides an existing deck:

1. Parse the cards.
2. Identify card types, categories, tone, and disclosure level.
3. Review safety, clarity, variety, and audience fit.
4. Flag weak, repetitive, risky, or unclear cards.
5. Rewrite flagged cards.
6. Recommend deck ratios, missing categories, facilitation rules, and pilot-test steps.

If the deck is in Markdown, CSV, or JSON, use scripts/review_card_deck.py when a quick deterministic summary is useful. Use judgment for qualitative review.

## Not-for-card warning

Say when the topic is better handled by another format, such as a private survey, 1:1 conversation, facilitated workshop, policy document, risk register, HR process, counselling support, or formal consultation.

Warn especially for active workplace conflict, performance issues, confidential restructuring, mental health disclosure, compensation, job security, or anything where answers could be used against people.
