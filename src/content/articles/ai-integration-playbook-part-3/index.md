---
title: "AI Integration Playbook (Part 3)"
description: "A first-principles approach to redesigning workflows with AI"
published: 2026-08-24
category: notes
series: ai-integration-playbook
tags: [prompt, decomposition, components]
draft: True
---

This is Part 3 of the series where I distil the specifics of integrating LLMs into existing workflows. 

Part 1 of the series helps us decide the entry points, the capability layers to use, selecting the "brain" of the workflow, and how to manage context. Part 2 focuses on effective prompting strategies and iterating prompts diagnostically for more usable outputs. 

Part 3 is about evaluating and validating Claude's output systematically.

## Evaluating Accuracy, Completeness, and Fitness

#### 1. Evaluate output against 3 references

The evaluation framework is a check against 3 fixed references:
| No. | Reference | Assessment |
| --- | --- | --- |
| 1 | Requirements Set | Whether the output reflects what was asked. Confirm that each and every part of the requirements are met. |
| 2 | Source Material | Does the output match the specific source material? Trace specific claims back to the source (rather than trusting Claude) |
| 3 | Professional Standards in the Industry | Would the output pass based on industry standards? eg. Number without units, recommendation without reasoning, a citation that is not real would fail professional standards |
#### 2. Stakes calibration 

**Determine whether it's high-stakes work or low-stakes work before deciding how deeply to review across these criteria.** For zero-tolerance work like in Legal, Finance or Compliance, accuracy beats speed and every claim needs to be verified. On the other hand, low-stakes work like internal brainstorming could work with lighter review.

#### 3. 3-way triage

Once reviewed, sort the output into 3 different buckets and document the reasoning:

| Bucket | Verdict | When to Assign to this Bucket |
| --- | --- | --- |
| 1 | Ready to use | Output meets requirements, matches sources, clears professional standards. |
| 2 | Needs revision | Close, but a specific gap remains. Document the gap and iterate output. |
| 3 | Needs human override | The stakes, the errors, or uncertainty means that the output should not go out on Claude's draft. Escalate to a human. |
#### 4. Review completeness

> An output can be entirely accurate and still omit a factor that impacts a decision

Assess for whether the output is missing anything that could impact the decision that will be made off the output.

