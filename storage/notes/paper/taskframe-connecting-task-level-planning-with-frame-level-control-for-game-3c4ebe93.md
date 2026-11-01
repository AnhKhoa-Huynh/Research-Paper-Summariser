# TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-10-29T15:31:37Z
- **First seen:** 2026-11-01
- **Topic matches:** AI and machine learning, NLP and language models
- **Relevance score:** 1.4
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2610.40276v1
- **PDF:** https://arxiv.org/pdf/2610.40276v1

## Summary / source snapshot

The authors introduce TaskFrame, a hierarchical framework designed to bridge high-level task reasoning with low-latency action control for game agents. The approach divides the architecture into a vision-language task planner and a causal Transformer controller, achieving competitive instruction decomposition and higher combat success rates in Minecraft.

## Method / approach

A vision-language task planner decomposes goals into atomic instructions using supervised learning and dependency-aware GRPO, while a causal Transformer controller predicts discrete keyboard-mouse actions and continuous camera motion using cached goal embeddings and observations across a three-stage training process.

## Reported contribution / result

The agent is competitive with general-purpose vision-language models on instruction decomposition and achieves a higher combat success rate than the evaluated baselines in Minecraft closed-loop evaluation.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It addresses the computational profile conflicts between high-level task reasoning and low-latency action control needed to build general game agents in rapidly changing visual environments.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
