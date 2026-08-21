---
title: "AI Integration Playbook (Part 1)"
description: "A first-principles approach to redesigning workflows with AI"
published: 2026-08-19
category: notes
series: ai-integration-playbook
tags: [ai-workflows, prompt]
draft: True
---

There are a lot of information out there about using AI in existing business processes and workflows but more often than not, the use cases are almost too simplistic, and not scalable at an enterprise level.

In this series, I strive to extract key principles of integrating AI into existing business processes into a playbook to serve as a guide or roadmap when an organisation is planning on implementating AI into existing workflows. My starting point is Anthropic's foundational modules. 

## Behavioural Properties of Generative AI
Before even starting to work with Gen AI, it is important to understand how it behaves and so that once we know this, we would be able to manage our expectations when working with it, and then, learn how best to utilise it for our day-to-day work. 

1. Responses vary

The first behavioural property of Gen AI to understand is responses vary. There is no one correct output. The same prompt asked twice, will yield different outputs and no one is more correct than the other. This is simply how Gen AI works: that outputs are produced using probabilities (not from a fixed database).

As this is inherent in the tool itself, we need to **plan for variation in any workflow that depends on consistent outputs**, and **build review into the process**. 

2. Confident tone \(\ne \) accuracy

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

Beyond simple text generation, there are 3 features in the capability layer that support enterprise-level work:

1. **Project Context** provides *background knowledge* and context for the specific workstream.
   
2. **Skills** define *procedures or how a specific task should be executed consistently* each time. 
   
3. **Code execution** verifies computation and should be used when the result *must be correct*, and not probabilistic.
   
4. **Memory** retains work-relevant facts across sessions so there's no need to re-enter project context each time in every session

what should be in instructions context and what should be in memory. 




## Model


## Context Management





