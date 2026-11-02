# $\\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-10-30T12:27:45Z
- **First seen:** 2026-11-02
- **Topic matches:** Human–robot interaction, Robotics and autonomy
- **Relevance score:** 7.8
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2610.41654v1
- **PDF:** https://arxiv.org/pdf/2610.41654v1

## Summary / source snapshot

The authors introduce a first-order humanoid control approach called ∇Mimic that utilizes exact simulator gradients instead of black-box optimization or surrogate models. By addressing gradient explosion and computational cost issues, the method achieves efficient whole-body motion tracking.

## Method / approach

The authors bound unbounded gradient samples using median-relative per-sample clipping at every backward step and reuse simulated windows via multistep regression onto gradient-derived action targets. They also use NablaEngine, a differentiable GPU simulation engine that computes analytic contact dynamics and adjoints as a single megakernel.

## Reported contribution / result

∇Mimic reaches a tracking score of 0.82 in 20 minutes and 0.874 in 1.8 hours on whole-body tracking of LAFAN1 clips, outperforming the standard SHAC baseline which fails due to exploding gradients.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides open-source infrastructure that makes exact-gradient first-order humanoid policy learning significantly faster and more sample-efficient than traditional zeroth-order or surrogate-based methods.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
