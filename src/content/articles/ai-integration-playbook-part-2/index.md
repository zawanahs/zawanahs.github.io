---
title: "Prompting, Decomposition, and Creating Better First Drafts"
description: "How to structure prompts, decompose complex tasks, and iterate outputs effectively"
published: 2026-08-24
category: notes
series: ai-integration-playbook
tags: [prompt, decomposition, components]
draft: False
---

Part 1 of this series was about understanding the nature of Gen AI, deciding on the entry points and the capability layers to use for task workflows, selecting the Claude model that best fit the task(s), and managing context while working with it.

Part 2 looks at the structure and strategies for prompting and executing tasks, and how to iterate diagnostically when the output falls short. 

## Components of an Effective and Professional Prompt

> Prompting is a communication discipline with learnable structure

| No. | Components | Details and Purpose | Examples |
| --- | --- | --- | --- |
| 1 | Role | Who do you want Claude to be for this task? By having Claude assume a role, it would **set the vocabulary, the depth and the assumptions** that Claude brings into the conversation | Financial Analyst, Editor, Policy Reviewer |
| 2 | Context | Background that Claude cannot possibly know unless it was given. With this, Claude would **provide more specific and relevant outputs** | The situation, audience, prior decisions, source material |
| 3 | Task | The **specific action** that we need Claude to do, **stated as a clear instruction**. | Summarise, compare, draft, identify etc. |
| 4 | Constraints | Boundaries set to keep the output usable without heavy editing. | Length of output, the tone, what to include, what to avoid |
| 5 | Output Format | Defines the shape of the result | Table, bulleted list, a 3 paragraph memo, a draft email |

Not every prompt needs all of these 5 components. It's about knowing which component(s) a task requires.

> To be competent here is to make it a habit to explicitly share with the model the 5 components of the task (rather than assuming Claude will infer it).

Any information that is only in my head or outside the connected source is a *context gap* which is usually the reason a prompt underperforms.

Most of the time, I work with complex, multi-step tasks, which require more than a single effective prompt. Packing this request into a single prompt would produce shallow work at each step. The solution is **decomposition** ie. breaking a complex task into a sequence that Claude can execute well.

## Task Decomposition for Complex Requests

> Decomposition: Splitting a multi-part problem into discrete, ordered steps, then running them in sequence

Each step should produce a *checkable intermediate result* so the work at each step is auditable. Breaking it down into a multi-step auditable process helps to answer how the final recommendation is reached. If the intermediate results are not up to expectations, then it can be iterated first before going through the entire pipeline. 

#### Decompose into a single sequential conversation or several independent conversations?

Keep **sequential steps that build on each other in one conversation**, so each step sees the prior results. 

Move to a separate conversation when **a step is genuinely independent or when conversation has grown long enough that early context is degrading** (make this judgment based on context management skills shared in Part 1).

For example, a communications manager needs to summarise a policy change into: an internal announcement, an FAQ for staff, and a short briefing for executives. These are 3 different deliverables based off one foundation.

In this case, extract the key changes from the policy document first, review to confirm the extraction is complete. Then, draft the 3 different deliverables on top of it. Sequence the shared, high-stakes extraction first before drafting the deliverables in parallel. This prevents propagating mistakes from extraction into any of the 3 deliverables.

## First Drafts are not Perfect

After prompting, the first output is rarely perfect. Systematically diagnose which specific component fall short to iterate and achieve a more usable output. 

Common symptoms of output that fall short and how to fix them:

| Output Deficiency | Cause | Solution |
| --- | --- | --- |
| Generic and off-base | Context is thin | Add more background and context that lives in your head into Claude |
| Answered the wrong questions or wrong action taken by Claude | Task verb is ambiguous | Sharpen and be clear about the instruction to Claude |
| Wrong length, tone, format or shape | Constraint or Format is missing | Include expected format, tone, length and constraints |
| Output is close but one section is not right |  | Iterate on that section only and don't discard the draft that is mostly already right |

While iterating prompts for the specific components that are missing from the outputs, **recognising diminishing returns after each iteration is part of the skill**. When further prompting yields less than a quick manual edit, stop iterating. The goal is a usable result, not the perfect output. 

## Nature of Tasks

The emphasis for each component depends on the nature of tasks on these 2 axes: specificity and creativity.

|Task Type| Nature of Task | Prompting Strategy|
|---|---|---|
| Analysis| Tight constraints and explicit criteria ie. Low creative latitude; high specification| Prompt Claude what to measure and against what standard, and how to handle ambiguity|
|Research| Clear scope and source discipline ie. Low creative latitude; high specification and citations included | Define the question, the boundaries, and whether current sources are required. Explicitly ask for citations so claims are checkable|
|Drafting| Audience, tone, and format needs to be specified and allow Claude to find the phrasing ie. Medium creative latitude; high specification| Control the shape of the draft, and let Claude fill it|
|Brainstorming| Loose constraints and high latitude| Over-specifying kills the divergence we're after. Provide goal and boundaries, then volume and range before narrowing down|

At this stage, each workstream would have effectively designed prompt(s) specific to the nature of the tasks.

Next, we look at evaluating and valuating Claude's output in systematically in Part 3.




