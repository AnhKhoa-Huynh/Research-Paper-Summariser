# La-JEPA: Compact Robot Policies with Latent World Modeling

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-05T15:16:38Z
- **First seen:** 2026-11-06
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 7.65
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.08156v1
- **PDF:** https://arxiv.org/pdf/2611.08156v1

## Summary / source snapshot

The authors introduce La-JEPA, a compact world-action model for robotics that uses a policy transformer trained from scratch within a pretrained V-JEPA encoder feature space. It matches or exceeds the performance of much larger models across multiple benchmarks while running significantly faster.

## Method / approach

Training a compact policy transformer from scratch in the feature space of a pretrained V-JEPA 2.1 encoder to jointly predict future features and actions during training, followed by generating only actions at inference.

## Reported contribution / result

La-JEPA achieves state-of-the-art performance among policies without embodied pretraining on RoboTwin 2.0 and LIBERO-Plus while using fewer parameters, running faster than Fast-WAM, and achieving real-robot success comparable to pi0.5.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It suggests that robot foundation models may benefit from architectures specifically designed for control rather than those inherited from generative tasks.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
