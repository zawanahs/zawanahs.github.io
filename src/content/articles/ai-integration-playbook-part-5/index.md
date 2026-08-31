---
title: "Mapping Claude into Existing Workflows"
description: "Redesign workflows around AI while keeping human review visible and stakeholder communication credible"
published: 2026-08-26
category: notes
series: ai-integration-playbook
tags: [prompt, decomposition, components]
draft: FalseS
---

This part of the series is about configuration and knowledge management. 

> Configuration is leverage: setup once, and we benefit from every conversation after

Setting up a Project, with standing instructions, and curated knowledge base supports a team with more consistent and quality answers. **Maintaining the setup regularly at a monthly cadence** is important so the quality of output remain *high and usable* (and not degraded).

## Configuration Slots

Choosing the right mechanism for the right need makes the difference between a project that runs more smoothly than not.
| Mechanism | About | Details |
| --- | --- | --- |
| Standing Instructions | Behaviour of the LLM | Include tone, format, verification habits. |
| Knowledge Base | Facts for the work | Documents, policies, and reference files that the model should draw on. |
| Skills | Procedures | Repeatable procedures that Claude should follow consistently for a kind of task. Note: Skills live at the account level and is reusable across any Project that requires it. |
| Scoped Memory | For continuity | Context for the Project. Doesn't bleed between different projects or workstreams. |

## Connectors

A connector allows the LLM to **reach an authorised external system** eg. searching Google Drive for a document or finding a relevant email. **Manage what is accessible by the LLM** rather than connecting everything.

Every connector has a **defined boundary** and knowing this upfront helps manage expectations of what the LLM can and cannot do. 

Note: 
- Connect only those vetted by the organisation
- Understand the connectors' capability boundary

## Knowledge Base

The uploaded knowledge base needs to be treated with the same care and update as the connected source: keep it *current, relevant, and free of duplicates*. 

## Standing Instructions

Write:
- verification behaviours/ guardrail guidance - e.g. cite the source document for every factual claim, say "I don't know" rather than guessing when the documents do not cover something.
- format defaults
- tone

Every conversation in the project will inherit them. So the first draft is closer to the final deliverable. 

Precision is important because vague instructions will silently fail. For example, "Be professional" is vague compared to "Use a formal register, define any acronym on first use, and keep paragraphs under 5 sentences". 

> Test it by asking whether 2 people will read it the same way

## Configurations are Living Assets

**Scheduling maintenance** is the way to go to prevent standing instructions, knowledge base, and skills to drift towards stale configuration.

1. Set a **monthly review cadence** to assess:
  - If current standing instructions still *match* the current process
  - If knowledge base is *free of superseded documents*
  - If the *right Skills* are enabled

> The alternative is output quality slowly degrading rendering the output less usable

2. Skills versioning:
  - Anthropic-built/ organization-provisioned Skills update automatically
  - Own custom-uploaded Skills change only when it is re-uploaded

3. Memory lifecycle:
  - Memory is a working file to be reviewed periodically.
  - Edit or delete entries that are stale, and export as backup before a major change.
  - When a Project's memory has accumulated *enough outdated context to mislead*, a **full reset is needed**. *Accuracy of what is stored is more important than volume*.

