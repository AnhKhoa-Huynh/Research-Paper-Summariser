# DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-23T16:05:37Z
- **First seen:** 2026-11-24
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 8.8
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.30907v1
- **PDF:** https://arxiv.org/pdf/2611.30907v1

## Summary / source snapshot

The authors introduce a 3D latent-action world model designed to learn continuous action representations from human manipulation demonstrations using point-cloud observations. This model aims to provide a unified framework that enables zero-shot robotic manipulation across different embodiments without requiring embodiment-specific action decoders.

## Method / approach

The authors employ a contrastive objective to learn consistent motion representations across embodiments from point-cloud observations of retargeted human demonstrations, using the resulting unified latent action space for model-predictive control and recovering executable robot commands from predicted geometric motion.

## Reported contribution / result

The authors claim the model achieves 90%, 92%, and 60% success on reaching, grasping, and placing respectively, and an 86% success rate across 50 trials for zero-shot real-world manipulation with an unseen dexterous hand.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The authors claim this approach highlights the potential of geometry-grounded latent actions as a unified and transferable interface for world-model-based robotic manipulation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
