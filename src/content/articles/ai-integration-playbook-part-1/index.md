---
title: "AI Integration Playbook (Part 1)"
description: "A first-principles approach to redesigning workflows with AI"
published: 2026-08-19
category: notes
series: ai-integration-playbook
tags: [context-management, capability-layer, model]
draft: False
---

There are a lot of information out there about using AI in existing business processes and workflows but more often than not, I find the use cases almost too simplistic, and not scalable at an enterprise level.

In this series, I strive to extract key principles of integrating AI into existing business processes into a playbook to serve as a guide or roadmap when an organisation is planning on implementating AI into existing workflows. My starting point is Anthropic's foundational modules. 

## Behavioural Properties of Generative AI
Before even starting to work with Gen AI, it is important to understand how it behaves and so that once we know this, we would be able to manage our expectations when working with it, and then, learn how best to utilise it for our day-to-day work. 

1. Responses vary

The first behavioural property of Gen AI to understand is responses vary. There is no one correct output. The same prompt asked twice, will yield different outputs and no one is more correct than the other. This is simply how Gen AI works: that outputs are produced using probabilities (not from a fixed database).

As this is inherent in the tool itself, we need to **plan for variation in any workflow that depends on consistent outputs**, and **build review into the process**. 

2. Confident tone ≠ accuracy

Secondly, a confident tone does not signal accuracy. No matter how accurate the output is, the LLM can write with consistent fluency that sounds correct. In other words, a fabricated statistic can read as assuring as a verified statistic.

Due to this, we need to **build verification habits** in the workflow so that we don't put out erroneous information that could cost us monetary-wise or reputation-wise.

3. Context is a budget

Thirdly, context is a budget that we need to manage to work with Gen AI effectively. Every conversation has a working-memory limit. When the conversation approaches the limit, it automatically summarises earlier messages so that the session can continue. During this summarisation, details are compressed and that also means that some information may be lost. What is trimmed is based on the LLM's judgment. 

We need to **strategise how to work with context limits** when integrating them into our workflows. For example, when to restart a new conversation, when to summarise, when to persist in the conversation. 

4. Knowledge cutoff date

Fourthly, the LLM's knowledge has a cutoff date. **For recent information and data, we need to connect to a current source, or use web search**.

5. Varied outputs from configured procedures

Finally, configured procedures still produced varied outputs. Setting up a *Skill* to run the same procedure each time reduces output variance but does not eliminate it, even if it is well-configured.

Thus, **review needs to stay in the workflow** regardless of how carefully a skill is built. While configuration reduces variation, it doesn't remove the need to check the output.

> So, human review stays in all AI-integrated workflows (unless it pertains to low-risk decisions). Human review should include methods to verify outputs or claims made by the LLM. When working with LLMs, it is important to know how to work with its context limits.

Now that we have a clear understanding of how Gen AI behaves and how to work with it, next is applying the framework for making 4 decisions that need to be made before working with LLMs.

1. Which *entry point* to use (and interact with the LLM)
2. Which *capability features* to activate
3. Which *model* to select
4. How to *manage context* across a session

Deciding on the best one for the specific workflow would directly affect the quality ceiling of the output.

## Entry Point

There are 4 entry points : Chat, Projects, Artifacts, and Research Mode.

Projects are persistent workspaces that supports processes that:
1. Require the LLM **to know and perform recurring work or do something consistently** for every conversation (ie. have standing instructions that persist across all conversations with it). 
2. Have to refer specific documents or policies or reference files ie. a **knowledge base** to inform the output
3. Benefits from having **context from past conversations** related to a specific context (separate from other conversations) 

> Instead of explaining the background and context for every session, once it's in the standing instructions and knowledge base, the LLM would already have this context in place and can start every conversation with this in mind. 

For one-off conversations, the chat function works well.

Ask the LLM to create an artifact if what is required is a **deliverable in a specific output format** where receipients can open and read, instead of inline. 

Compared to a simple web search, use **Research** for multi-step searches or deep investigation across multiple sources and synthesis of findings.

Once the most suitable entry point is selected, we look at the capability layer, which determines what the LLM can do within that entry point. 

## Capability Layer

Beyond simple text generation, there are 4 features in the capability layer that support enterprise-level work:

1. **Project Context** provides *background knowledge* and context for the specific workstream.
   
2. **Skills** define *procedures or how a specific task should be executed consistently* each time. 

> Skills = reusable procedures. There are built-in skills for tasks: creating, editing, analyzing Excel spreadsheets, Word documents, ppt decks, and PDFs, but custom skills can be added using settings for task-specific workflows.
>
> Skills live at the account level (not inside any one Project) and they are invoked automatically when relevant in any conversation.
>
> Note:
> - Skills reduce variance but they do not eliminate it no matter how well the Skill is configured. So, human review remains in the workflow.
> - Skills require a trust evaluation. It has access to what Claude has access to during the session. Thus, before enabling a third party skill, review the source and permissions. Anthropic-provided skills and organization-approved skills are the low-risk starting point.
 
3. **Code execution** verifies computation and should be used when the result *must be correct*, and not probabilistic.

> This is Claude's sandboxed computation environment where it writes and runs code internally, then returns the result.
>
> This matters because Claude generates prose by producing the more probably next sequence of text, so for computation, it would then produce plausible-looking numbers that may or may not be accurate. Thus, with Code Execution, it would provide a verified result by actually running the calculation.
>
> Use this for numeric output that will be used or reported (eg. calculations, projections, summaries of figures), data that needs to be transformed or cleaned (eg. date normalization, deduplication, field formatting), when output needs a chart or visualisation, or if output needs a downloadable file (ie. .xlsx, .pptx, .docx, .pdf)
   
4. **Memory** retains work-relevant facts across sessions so there's no need to re-enter project context each time in every session

> Memory is most useful when **actively curated**. Memory that's accurate last Q but hasn't been reviewed can be misleading. Maintain it by:
> - monthly reviewing stored memories
> - deleting or updating entries that no longer hold
> - keeping the stored set focused on information that genuinely recurs across sessions
>
> Scoping Memory:
> - by Project so memory contexts are separate for Client A vs Client B.
> - use Incognito mode to keep a session out of Memory and chat history. For example, for sensitive conversations or exploratory work with confidential inputs that shouldn't surface in history or Memory.
> - import Memory from other AI platforms or add key facts to Memory manually through memory settings, not add them into a Project's knowledge base.

Each of the layers are independent and should be used in combination based on the requirements of the task. For example, a one-off question would not need any of them, whereas a recurring analytical workflow may use all 4 of them.

#### Considerations for Capability Layer(s) required before rebuilding workflows

1. What parts of this task recur (or are repetitive)? -> Standing instructions & Skill
2. What material needs to be referenced across sessions? -> Knowledge base
3. Are there outputs that need to be computed correctly? -> Code Execution
4. What context needs to carry across sessions? -> Memory

Note: Standing instructions define how Claude behaves while the knowledge base define what Claude knows.

Now that the entry point is decided and capability layers are considered, next is deciding the brain of the workflow. Specifically, how well Claude does the task in question, and at what cost in speed. 

## Model

Different model tiers for the Claude family range from efficient-and-fast to thorough-and-capable. 

It is important to match well to avoid over-engineering routine work and under-resourcing high-stakes work.
| Model | Speed | Cost | When best to use |
| --- | --- | --- | --- |
| Fable 5 | Slow | Very High $10/$50 per-million-token | For the hardest, highest-stakes work: Long-horizon multi-step or multi-day autonomous tasks, ambiguous problems where choosing the wrong approach is expensive to revert, and work where getting it right matters more than turnaround time or per-token cost. Fable should not be the starting point but escalate from Opus when Opus falls short. Eg. large multi-system migrations, deep multi-source research synthesis, high-stakes strategic work |
| Opus | Moderate | High @ $5/$25 per-million-token | More advanced performance than Sonnet or Haiku. Meant for tasks that require nuanced judgment, complex multi-step reasoning, ambiguous inputs that require interpretation, any work where quality outranks speed. Eg. client-facing deliverables, complex document analysis, strategic planning, and high-stakes synthesis across multiple sources. |
| Sonnet | Moderate | Mid @ $2-3/$10-15 per-million-token | Balanced tier. Handles a range of professional tasks with strong quality across task types: drafting, synthesis, analysis, research assistance, and document review. For most of us, Sonnet is the **right starting point**. Switch up to Opus if quality falls short. If speed and volume is needed, then switch down to Haiku. |
| Haiku | Fast | Low @ $1/$5 per-million-token | Structured tasks: classification, extraction, formatting, straightforward summarisation, high-volume routine work. Eg. Task that runs at volume across hundreds of items in sequence. |

Start with Sonnet, assess if the task could work with Haiku, and if not, stick to Sonnet. Then escalate to stronger models when the current model falls short.

After selecting the workflow's brain, we need to consider how long it can do the task well, by managing its context.

## Context Management

Every conversation has a working-memory limit ie. the **context window**. When messages and uploaded documents accumulate, the context window will start filling up. As it reaches the limit, Claude will automatically summarise earlier messages to make room (Note: full history still remains available for reference). During the summarisation, some details can get lost. For example, when we give instructions to Claude in the first 10 mins, after a long session 90 mins later, it may forget those instructions said at the beginning of the conversation. 

Recognising **when** the conversation needs an intervention:
- Claude *stops following instructions* it followed correctly earlier in the session
- Responses *address only the most recent exchange* but not referencing earlier decisions or context.
- *Accuracy of replies drop* that are consistent with missing context earlier in the session.

When context has degraded, here are 3 ways to respond and when best to use each:
| Options | Action | Best use case |
| --- | --- | --- |
| Restart | Start a new conversation | When beginning a genuinely new task within the same workstream or when current session has drifted beyond recovery. Note that this loses the existing conversation thread but the Project's standing instructions and knowledge base still carry forward automatically. |
| Summarise | Get Claude to summarise the current state: decisions made, work in progress, and open questions. Next, paste this summary at the start of the new conversation as context. | Preserves thread continuity without carrying a degraded context window into the next session. |
| Persist | Saving information in the conversation that should be available across all future sessions to Memory or update the Project Knowledge base. | Saving it into Memory/Knowledge Base is more efficient than re-entering it repeatedly. |

Extended sessions on higher-tier models can reach the usage limit before the work is complete. For intensive tasks, it is more efficient to plan ahead than work around an uninterrupted session: 
- break large tasks into segments,
- save interim progress to the knowledge bases, 
- restart from summary than extending a single session indefinitely






