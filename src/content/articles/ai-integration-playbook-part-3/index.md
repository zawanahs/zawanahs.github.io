---
title: "Systematically Evaluating Claude's Output"
description: "A review framework for spotting hallucinations, calibrating risk and deciding when human judgment must stay in the loop"
published: 2026-08-24
category: notes
series: ai-integration-playbook
tags: [prompt, decomposition, components]
draft: False
---

This is Part 3 of the AI Integration Playbook series where I distil the specifics of integrating AI into existing business processes. 

Part 1 of the series helps us decide the entry points, the capability layers to use, selecting the "brain" of the workflow, and how to manage context. Part 2 focuses on effective prompting strategies and iterating prompts diagnostically for more usable outputs. 

Part 3 is about evaluating and validating Claude's output systematically to be confident while being accountable for the final output.

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

Assess for whether the output is missing anything that could impact the decision(s) that will be made off the output.

## Failure Patterns: Hallucinations, Inconsistencies & Bias

In Part 1, we understand that LLMs can write with a confident tone even if it's a fabricated statistic. Learning to identify and spot specific failure patterns helps to prevent reliance on false information. 

| Failure Patterns | Signals | Examples |
| --- | --- | --- |
| Hallucination | **Plausible but unsupported claims**: Statements that sound reasonable but with *no basis in the source or in fact*. **Fabricated specifics**: Invented statistics, dates, names, quotations, or citations. Being specific can read as authority. **Confident tone masking uncertainty**: A guess and well-ground fact can come across in the same assured tone. | Claude can claim to have taken an action it cannot actually take. Eg. "I've emailed that to your team". Note: *Treat any claimed external action as unverified until you confirm it happened*. "Approximately 63% of mid-market SaaS firms adopted at least 1 AI tool in 2025" may sound accurate, but needs cited sources. If no citations, means it's just a confident guess. "This clause is enforceable in this state." sounds assuring but legal enforceability is jurisdiction-specific and date-sensitive, so requires evidence of these. |
| Inconsistencies and Bias | **Internal contradictions**: Especially in long outputs, a claim early on can conflict with the one later. Typically in long documents. **Confirmation bias in framing**: If the prompt *implicitly has a preferred answer, the output may lean toward it*. Look out for outputs that agree with you too readily on a question that should be open. | A 10-page market analysis needs a consistency pass, not just a paragraph-by-paragraph read. |

The best way to prevent these is to employ verification techniques within the prompt first.

## Fact-Checking and Grounding Techniques

Use these as a checklist when prompting to generate outputs that are less likely to have hallucinations, inconsistencies or bias:

1. **Prompt for Verifiability**
  - Telling Claude explicitly that **admitting uncertainty is acceptable** -> A model under pressure to answer is more likely to fill the gap by inventing something.
  - **Restrict to provided sources** -> Instruct Claude to answer only from the materials supplied and to flag anything that the materials do not cover. So instead of open-ended generation, it's bounded retrieval (like RAG).
  - Require **auditable citations** -> Ask for specific source and location for each claim made in a way that can be easily reviewed.

2. Grounding Techniques
  - Quote first, then analyse -> For long documents, ask Claude to **extract supporting quotes first, before drawing conclusions**. This grounds the analysis in pulled quotes making the reasoning and errors more visible.
  - Best-of-N comparison -> **Re-run the same request, then compare**. For parts that agree, we can have more confidence in it and where they diverge, they require a more detailed review
  - **Validating against authoritative sources** -> Check against a trusted external reference rather than a second Claude response.


## Threshold for Human Review

While Claude can produce decent drafts which are then iterated to build the final output, there are tasks where it is non-negotiable that a human needs to be in the loop before the final output. 

Know the thresholds for human review in advance and build this into policy is better than only stepping in when something goes wrong. 

| Threshold | Assessment |
| --- | --- |
| Stakes | **High-cost errors** need human review no matter how confident the output is. |
| Reversibility | An **irreversible step** (eg. a client deiverable, a filed report) need human review. |
| Audience | **External, executive, and regulatory audiences** increase the review requirements. |
| Regulatory exposure | **Regulated content** carries obligations. |
Reviewing the drafts before the final deliverable includes ensuring that it meets the professional standards of the industry or domain, and consideration of the type of audience.

## Editing and Adapting Output for Audience

Check for:
- **Clarity** -> Claude can be thorough and the edits to be made are for precision with the audience in mind.
- **Tone** -> Match the tone of the output to the relationship and occasion with respect to the audience.
- **Formatting** -> Shape the output into how it should be read by the audience. For example:
  - For Executives - Executive summary that leads with the decision and impact on key metrics.
  - For a Working Team - Detailed report and methods
  - For External Clients - Clean with controls over what is disclosed and how information is framed

## Output Formats

Format of the output depends on the purpose of the results:
| Output Format | Purpose |
| --- | --- |
| Inline | For quick and contextual reponse in chat |
| Artifacts | For separate editable block that is meant to be refined and reused. Typically when a deliverable is expected. |
| Structured Formats | For data eg. tables and defined schemas that downstream tools can consume directly |

#### Code execution vs Prose
Code execution runs the calculation and returns a computed and checkable result vs prose generation can produce a plausible-looking figure. 

Note: *The guarantee is that humans can read, verify and rerun the calculation but the code need not be necessarily correct*. So while code execution is deterministic, since Claude writes the code, the logic can contain a bug.


#### Curate inputs to shape output

If inputs are organised, outputs are more likely to be organised. 

Have structured and well-labelled source material (so the role of each input is explicit), deduplicate sources (so Claude is not synthesising multiple copies of the same material), and prune any materials that are not relevant to the question (noise in the input translates to noise in the output).

