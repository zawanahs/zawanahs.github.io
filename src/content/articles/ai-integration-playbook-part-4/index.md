---
title: "Mapping Claude into Existing Workflows"
description: "Redesign workflows around AI while keeping human review visible and stakeholder communication credible"
published: 2026-08-26
category: notes
series: ai-integration-playbook
tags: [prompt, decomposition, components]
draft: False
---

This part of the series shares use cases for building a repeatable process, run by a team, where Claude performs the specific steps. Making good choices to automate the right steps is key.

## Use Case #1: Extracting Business Requirements

Claude is great for taking in unstructured materials and returning a structured analysis. For example, it can take a business need "We need better reporting" into specific defined tasks that are actionable (eg. What report, for whom, how often, drawn from what data and in what format).

> Example: RFP Response Workflow
>
> "From the attached RFP and the email thread, extract every distinct requirement the client is asking us to address. For each, give a short label, the exact RFP section it comes from, whether our thread already has an answer, and any requirement that is ambiguous and needs clarification. Return it as a table."
>
> Use Projects as the Entry Point, have past winning proposals in the Knowledge Base, extraction format in the Standing Instructions, and create Skills to define the formatting steps.

Then verify the output by pressure-testing, to surface any hidden requirements.

> "Review the requirements you extracted. Which are ambiguous as written? Which could be interpreted two ways by our proposal team? Which imply a requirement the RFP states only indirectly?"


## Use Case #2: Research, Planning and Process Optimisation

A strong planning workflow uses Claude's **synthesis** with **code-executed analysis** so the plan relies on numbers that were computed.

Use Claude to synthesize varied sources to develop a plan -> gather considerations, structure the options, and layout the trade-offs. For current information beyond the trainind date cut-off, use web search and Research. Verification habits still apply.

Note: For judgment steps where humans need to be involved to weigh risk appetite or political reality, it should stay human because these are areas that Claude can't see. Use Claude for documented considerations that have to be weighed and structured.

For plans that include numbers, use Claude to compute them using code execution.

> "Using code execution on the attached ticket data, calculate quarterly volume growth and average tickets resolved per analyst. Then, from those figures, recommend the headcount needed to hold our current resolution time next quarter, and show the assumptions."


## Use Case #3: Solution Designing, Development & Iteration

Claude is meant to be a **design collaborator**. The value is in the loop: ideate, prototype, gather feedback, refine. 

Keeping the design context stable across iterations in the loop is what produces a solution. 

1. Ideation produces options
2. Prototype makes one of the options concrete
3. Feedback exposes what could be better
4. Refinement fixes/improves the product

This loop continues until the product is ready to be shipped.

> Example: Business Analytics Internal Dashboard
>
> Instead of building a dashboard, use Claude to produce it as a web artifact for the internal team. Build and refine until there is a working artifact for the team.

There are many other use cases other than the above, and it helps to think about the different workstreams in an organisation, and how to incorporate Claude in them.

## Mapping Claude's Role in a Workflow

Before redesigning workflows around Claude, it is crucial to assess which parts could be outsourced to AI and which to humans or both, then map it accordingly. 

There are 3 key criteria to assignment:
| Criteria | Explanation | Assessment |
| --- | --- | --- |
| Reversibility | Assess if the step can be undone if Claude gets it wrong. | Reversible steps -> tolerate more delegation. Irreversible steps -> need more human involvement |
| Stakes | What is the cost of the error at this step | High cost -> human-owned. Low cost -> can outsource to Claude |
| Accountability | Who is answerable for the outcome of this step | If human, leave human in the loop. |
> Note: Never map an irreversible or high-accountability step to AI.

Once we have mapped Claude's role in the workflow redesign, embed the right feature for each AI step :
- use SKILLs for repeatable procedure steps
- use code execution for data computation steps

Human-retained steps serve as explicit review gates.

Avoid falling prey to these errors:
- Halo delegation -> Handing the next step to AI because the previous step went well. Each stage or step needs to be judged on its own.
- Collapsing collaborative into automation -> While the step says "AI drafts, human reviews" and human review is not staffed, then there's no real reviewer in this step.
- Mapping the tool instead of the work -> It's not about mapping about a skill that is built, but rather, mapping of the work first, then decide on the features to use.

## Communicating Value & Limitations upfront

> Credibility is what underpins trust.

Credibility comes from accurate claims and this includes *communicating the limits of the tool alongside its value* to the organisation. 

The message has to be **calibrated** based on the audience's AI literacy:
- Technical stakeholder -> feature detail and failure modes
- Executive -> outcome, oversight, and risk considerations

Document the human oversight as stakeholders trust an AI workflow more when human checkpoints are explicit. "Fully automated" is almost never true.

