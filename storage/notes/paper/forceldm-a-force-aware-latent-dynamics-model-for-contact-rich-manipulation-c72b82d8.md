# ForceLDM: A Force-aware Latent Dynamics Model for Contact-Rich Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-02T15:31:54Z
- **First seen:** 2026-11-03
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 14.1
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.03294v1
- **PDF:** https://arxiv.org/pdf/2611.03294v1

## Summary / source snapshot

The authors propose ForceLDM, a force-aware latent dynamics model designed to improve robot policy learning for contact-rich manipulation tasks. The approach uses knowledge distillation to train a student network on current observations to reason about upcoming physical dynamics, guided by a teacher network leveraging privileged future signals.

## Method / approach

A teacher network extracts future dynamic features using privileged future force/torque and optical flow signals, which are then distilled into a student network trained exclusively on current observations, combined with a curriculum-based progressive noise injection strategy.

## Reported contribution / result

ForceLDM outperforms state-of-the-art baselines across five real-world contact-rich manipulation tasks while generalizing effectively to novel objects and remaining robust to environmental perturbations.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It addresses the limitations of vision-only policies in contact-rich manipulation by effectively modeling future interaction dynamics and forces without requiring future sensory inputs during deployment.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
