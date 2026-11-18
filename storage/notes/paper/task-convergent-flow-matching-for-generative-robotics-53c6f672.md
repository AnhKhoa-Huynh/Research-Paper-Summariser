# Task Convergent Flow Matching for Generative Robotics

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-17T11:25:23Z
- **First seen:** 2026-11-18
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 9.3
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.22609v1
- **PDF:** https://arxiv.org/pdf/2611.22609v1

## Summary / source snapshot

The authors propose a task-centric inference-time refinement framework for flow matching policies to ensure that generated robot motions lead to desired task outcomes. The approach uses parallel physics-based rollouts and interval-wise Lipschitz bounds to verify task convergence funnels.

## Method / approach

Parallel physics-based rollouts, interval-wise Lipschitz bounds for continuous-time funnel satisfaction verification, and derivative-free Covariance Matrix Adaptation Evolution Strategy constrained to radial quantile bands.

## Reported contribution / result

Refinement raises success rates from 31.3% to 88.5% on PushT and from 77.0% to 86.0% on three-cube stacking, while a learned funnel lowers the average maximum loss of achieved progress by 19% relative to constraining chunk endpoints alone.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It addresses the limitation where generative policies produce plausible motions that fail to ensure consistent progress toward a task outcome, preventing action chunks from stalling or undoing earlier changes.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
