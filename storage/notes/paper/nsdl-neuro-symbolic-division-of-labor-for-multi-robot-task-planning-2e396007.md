# NSDL: Neuro-Symbolic Division of Labor for Multi-Robot Task Planning

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-12T11:47:48Z
- **First seen:** 2026-11-13
- **Topic matches:** Swarm and multi-agent robotics, Robotics and autonomy, NLP and language models
- **Relevance score:** 10.9
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.16671v1
- **PDF:** https://arxiv.org/pdf/2611.16671v1

## Summary / source snapshot

The authors propose NSDL, a neuro-symbolic approach for multi-robot task planning that divides responsibilities between a vision-language model and a deterministic solver. The model generates a plan sketch from visual and textual inputs, which the solver then expands into a complete executable joint plan.

## Method / approach

A small vision-language model writes judgments as a plan sketch and utilizes a detector and a solver as tools, with the model trained with the solver in the loop.

## Reported contribution / result

NSDL outperforms end-to-end planners and formalize-then-plan baselines on the VIKI-L2 and LOCUS-Bench benchmarks, with ordering and scheduling errors nearly eliminated.

## Limitations / evidence gaps

Remaining failures are attributed to misjudged states, and missed goals are mostly those the model never lists.

## Why it might matter

It demonstrates that combining vision-language models for scene-based judgments with deterministic solvers for computational planning effectively improves multi-robot task planning performance.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
