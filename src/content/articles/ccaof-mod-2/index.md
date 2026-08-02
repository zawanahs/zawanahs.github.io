---
title: "Prompting and Task Execution"
description: "A communication discipline that starts with 5 components"
published: 2026-07-27
category: notes
series: ccaof
tags: [ccaof, prompt]
---

## Prompting is a communication discipline with learnable structure

There are 5 components of a strong professional prompt :

**1. Role**

> Who do you want Claude to be for this task

For example, a financial analyst, an editor, a policy reviewer. The difference with having Claude assume a role is that it would **set the vocabulary, the depth, and assumptions** that Claude brings to the conversation.

**2. Context**

This is about providing the *background* that **Claude cannot possibly know unless you provided it**. For example, the audience, the situation, prior decisions, source material.

**3. Task**

This is the **specific action** that we need Claude to do, stated as a clear instruction: "Summarise", "compare", "draft", "identify". Typically, there is a primary verb that is **unambiguous**.

**4. Constraints**

These are the boundaries that we set, to keep the output from Claude usable without heavy editing. For example, the length, the tone, what to include, what to leave out, what to avoid.

**5. Output format**

This defines the shape of the result - it could be a table, a bulleted list, a 3 paragraph memo, a draft email. Stating the format upfront saves an iteration. 

> Note: Not every prompt **needs** all 5. It's about knowing which components a given task requires.

Competency here is about having the **habit of surfacing each component** and **making it explicit**, rather than assuming Claude will infer it. So anything that lives only in my head or outside the connected source is a *context gap* and this is usually the reason a prompt underperforms. 


## What about complex requests? Decomposition.

Some requests are too large to specify in a single instruction. 

When a task has several distinct stages, packing it into one prompt would produce shallow work at every stage. Decomposition is breaking a complex request into a sequence Claude can execute well. 

> Decomposition : splitting a multi-part problem into discrete, ordered steps, then running them in sequence (as opposed to asking for everything all at once)

For example, in a vendor evaluation:
1. Derive the criteria
2. Score vendors
3. Raise trade-offs
4. Recommend

At each step, it is wise to produce a *checkable intermediate result*. This is so that we could catch any problems with the particular step that produced the result, before continuing onto the next one. This makes the work auditable and understanding how the recommendation was reached.

> <u>A single conversation vs several conversations</u>
>
> Keep **sequential steps that build on each other in one conversation**, so each step sees the prior results. 
> 
> Move to a separate conversation when a **step is genuinely independent or when conversation has grown long enough** that early context is degrading (a judgment call based on context management skills). 

## Decomposing a parallel case

If there are 3 deliverables coming from one foundational work, *sequence* the shared extraction first.

For example, when announcing changes in policies to different stakeholder audiences:
1. Extract substantive changes from the policy document, and what each one means in practice
2. Confirm the extraction is complete and accurate before building anything on top of it
3. Draft the staff announcement from the confirmed change list, tuned to a general audience
4. Draft the FAQ, anticipating questions staff will likely ask about those changes
5. Draft the executive briefing, compressed to focus on decisions and impact

Steps 1 and 2 build the verified foundation that the 3 different deliverables draw on. **Sequence the shared, high-stakes extraction first** and let the parallel drafts follow. 

## Iterating prompts to improve output

The first draft is rarely perfect. When the output disappoints, don't rewrite the whole prompt but rather, read the output to diagnose which component fell short, then fix it.

> A weak prompt is when everything is left implicit. 

Output deficiencies are prompt diagnostics. **Each disappointment points back to a specific component**. So apply *targeted revisions* instead of wholesale rewriting.

|Output deficiency | Cause and Solution |
|---|---|
| Generic and off-base | Context is thin. Solution: Add more background and context that lives in your head into Claude |
| Answered the wrong question or wrong action taken by Claude | Task verb is ambiguous. Solution: Sharpen and be clear about the instruction to Claude |
| Wrong length, tone, format, or shape | A constraint or format is missing. Solution: Include expected format, tone, length and constraints |

> **Recognising diminishing returns** is part of the skill. The end goal is a usable result, not a perfect prompt.

## Adapting strategy by task type

The emphasis of each component changes with the nature of the task. Consider the balance of specificity (ie. constraints) and creative latitude of each task.

|Task Type| Nature of Task | Prompting Strategy|
|---|---|---|
| Analysis| Tight constraints and explicit criteria ie. Low creative latitude; high specification| Prompt Claude what to measure and against what standard, and how to handle ambiguity|
|Research| Clear scope and source discipline ie. Low creative latitude; high specification and citations included | Define the question, the boundaries, and whether current sources are required. Explicitly ask for citations so claims are checkable|
|Drafting| Audience, tone, and format needs to be specified and allow Claude to find the phrasing ie. Medium creative latitude; high specification| Control the shape of the draft, and let Claude fill it|
|Brainstorming| Loose constraints and high latitude| Over-specifying kills the divergence we're after. Provide goal and boundaries, then volume and range before narrowing down|






