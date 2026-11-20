# Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-19T16:18:14Z
- **First seen:** 2026-11-20
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, NLP and language models
- **Relevance score:** 12.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.26341v1
- **PDF:** https://arxiv.org/pdf/2611.26341v1

## Summary / source snapshot

The authors propose an efficient framework called Reasoning on Call to address the high latency and token costs associated with using large multimodal models for long-horizon robot manipulation. The approach utilizes an online task-state monitor to coordinate a low-level policy and a high-level reasoning agent through event-triggered reviews.

## Method / approach

An online task-state monitor combines temporal visual observations with ordered interaction memory to estimate progress and predict successors, which guides event-triggered agent review for execution repair and plan revision.

## Reported contribution / result

On RMBench, the proposed framework improves the task success rate by 24.0 percentage points and reduces token consumption by 65.3% compared to the strongest agent-based baseline, while also outperforming the strongest policy-based baseline by 15.1 percentage points.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It enables efficient agent intervention and coordinated recovery across execution and planning for long-horizon robot manipulation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
