---
title: "AI Integration Playbook"
description: "A first-principles approach to redesigning workflows with AI"
published: 2026-08-19
category: notes
series: ai-integration-playbook
tags: [ccaof, prompt]
draft: True
---

While I have read and studied Anthropic's videos on AI integration, I want to be able to easily articulate and present a clear roadmap of how to implement this. I believe that to truly understanding something is to be able to apply the. Messy, and infirmation is everywhere. Start my basal information from Anthropic's modules, and this will be where my core knowledge is from, on top of some reliable youtube videos. 

It would be ignorant to assume I know how to do it wihtout being able to explain clearly at an ELI5 level. So here, I attempt to break it down step by step.

Here's a series of step-by-step of how I would approach towards thinking about integrating AI into existing business processes.

## Behavioural Properties of Generative AI
Before even starting to work with Gen AI, it is important to understand how it behaves and so that once we know this, we would be able to manage our expectations when working with it, and then, learn how best to utilise it for our day-to-day work. 

The first behavioural property of Gen AI to understand is responses vary. There is no one correct output. The same prompt asked twice, will yield different outputs and no one is more correct than the other. This is simply how Gen AI works: that outputs are produced using probabilities (not from a fixed database).

As this is the inherent in the tool itself, we need to **plan for variation in any workflow that depends on consistent outputs**, and **build review into the process**. 

Secondly, a confident tone does not signal accuracy. No matter how accurate the output is, the LLM can write with consistent fluency that sounds correct. In other words, a fabricated statistic can read as assuring as a verified statistic.

Due to this, we need to **build verification habits** in the workflow so that we don't put out erroneous information that could cost us monetary-wise or reputation-wise.

Thirdly, context is a budget that we need to manage to work with Gen AI effectively. Every conversation has a working-memory limit. When the conversation approaches the limit, it automatically summarises earlier messages so that the session can continue. During this summarisation, details are compressed and that also means that some information may be lost. What is trimmed is based on the LLM's judgment. 

We need to **strategise how to work with context limits** when integrating them into our workflows. For example, when to restart a new conversation, when to summarise, when to persist in the conversation. 

Fourthly, the LLM's knowledge has a cutoff date. **For recent information and data, we need to connect to a current source, or use web search**.

Finally, configured procedures still produced varied outputs. Setting up a *Skill* to run the same procedure each time reduces output variance but does not eliminate it, even if it is well-configured.

Thus, **review needs to stay in the workflow** regardless of how carefully a skill is built. While configuration reduces variation, it doesn't remove the need to check the output.

> So, human review stays in all AI-integrated workflows (unless it is not related to a high-risk business decision). Human review should include methods to verify outputs or claims made by the LLM. When working with LLMs, it is important to know how to work with its context limits.

Now that we have a clear understanding of how Gen AI behaves and how to work with it, next is applying the framework for making 4 decisions that need to be made before working with LLMs.

1. Which entry point to use (and interact with the LLM)
2. Which capability features to activate
3. Which model to select
4. How to manage context across a session

Deciding on the best one for the specific workflow would directly affect the quality ceiling of the output.

## Entry Point

There are 4 entry points : Chat, Projects, Artifacts, and Research Mode.



## Capability Layer


## Model


## Context Management




