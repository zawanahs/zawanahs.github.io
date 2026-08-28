---
title: "Mapping Claude into Existing Workflows"
description: "Redesign workflows around AI while keeping human review visible and stakeholder communication credible"
published: 2026-08-26
category: notes
series: ai-integration-playbook
tags: [prompt, decomposition, components]
draft: True
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



