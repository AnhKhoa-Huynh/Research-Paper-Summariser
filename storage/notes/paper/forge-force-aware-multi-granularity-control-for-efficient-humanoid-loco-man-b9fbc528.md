# FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-12T17:30:11Z
- **First seen:** 2026-11-13
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 10.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.17142v1
- **PDF:** https://arxiv.org/pdf/2611.17142v1

## Summary / source snapshot

The authors introduce FORGE, a control system designed for humanoid loco-manipulation that manages locomotion, balance, and manipulation through a coarse-to-fine command space. The approach utilizes a momentum observer, learned corrections, and a quasi-static virtual-target loop to enable contact awareness and stability without requiring full-body human motion trajectories.

## Method / approach

A force-aware multi-granularity control system utilizing a coarse-to-fine command space, a momentum observer with learned contact-force supervision, a quasi-static virtual-target loop for wrist target adaptation, a frozen locomotion prior, and asymmetric residual actions.

## Reported contribution / result

The system enables unified control stability, task-space tracking, quasi-static wrist-equivalent force estimation without wrist sensors, sustained contact squeezing force control, and downstream diffusion-policy execution for lifting tasks across payloads.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides a practical controller for humanoid robots that simultaneously delivers precision, stability, and contact awareness while reducing the complexity of teleoperated demonstration collection.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
