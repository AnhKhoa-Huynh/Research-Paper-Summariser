# MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-05T17:50:35Z
- **First seen:** 2026-11-06
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 10.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.08372v1
- **PDF:** https://arxiv.org/pdf/2611.08372v1

## Summary / source snapshot

Momasplat is a novel-view demonstration augmentation framework designed for mobile manipulation to address policy sensitivity to camera viewpoint changes. The approach synthesizes full manipulation trajectories from unseen robot base poses by separately reconstructing the static scene and the manipulated object.

## Method / approach

Combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to reconstruct scenes and objects from standard multiview observations, render novel viewpoints, and generate synthetic demonstrations with transformed actions.

## Reported contribution / result

The authors claim that Momasplat more than doubles the average success rate of the strongest baseline, maintains non-trivial success at large base displacements where baselines fail, and reduces the need for large-scale real-world data collection.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It improves robot robustness to unseen base poses during mobile manipulation tasks, particularly by addressing dynamic object interactions that previous static scene approaches fail to re-render.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
