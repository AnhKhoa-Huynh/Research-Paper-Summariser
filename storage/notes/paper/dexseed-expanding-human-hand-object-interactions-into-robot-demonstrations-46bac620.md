# DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-10T13:52:18Z
- **First seen:** 2026-11-11
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 10.95
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.14092v1
- **PDF:** https://arxiv.org/pdf/2611.14092v1

## Summary / source snapshot

The authors introduce DexSeed, a framework designed to generate low-cost, physically executable robot demonstrations for dexterous vision-language-action learning using human hand-object datasets. The approach expands source sequences by preserving grasps and utilizing physics simulation to produce valid robot interactions.

## Method / approach

The framework organizes source sequences by grasp mode with shared language descriptions, uses InteractionMesh-based retargeting and arm trajectory augmentation to adapt sequences to robot hands and varying geometries, and employs a reinforcement learning finger-control policy alongside arm tracking.

## Reported contribution / result

Experiments indicate improved contact fidelity during retargeting and more reliable whole-arm execution compared to evaluated baselines, with simulation and real-world deployment showing successful execution of language-specified grasps by a fine-tuned vision-language-action model.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It offers a low-cost method to leverage reusable human hand-object datasets for generating diverse robot demonstrations, supporting dexterous policy learning without relying entirely on costly teleoperated examples.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
