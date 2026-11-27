# $μ$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-25T15:56:47Z
- **First seen:** 2026-11-27
- **Topic matches:** AI and machine learning
- **Relevance score:** 3.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.34597v1
- **PDF:** https://arxiv.org/pdf/2611.34597v1

## Summary / source snapshot

The authors introduce a model predictive control framework called muMPC designed to decrease online computational burdens through learned Koopman-linearized dynamics. By precomputing specific maps and utilizing a fixed primal operator, the system enables efficient optimization and control-aware dynamics learning.

## Method / approach

Precomputing finite-horizon control-to-output maps to eliminate lifted-state trajectories, yielding an action-only Koopman-Compiled QP with fixed precomputed primal operators for primal-dual iterations using matrix-vector products and projections.

## Reported contribution / result

The approach achieves solve times as low as 23 microseconds on a desktop CPU and 24 milliseconds on a 168 MHz microcontroller, scaling to high-dimensional quadruped control, visual planning, and multi-robot collision-aware planning.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It significantly accelerates constrained model predictive control and visuomotor planning compared to competing methods across a variety of hardware platforms.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
