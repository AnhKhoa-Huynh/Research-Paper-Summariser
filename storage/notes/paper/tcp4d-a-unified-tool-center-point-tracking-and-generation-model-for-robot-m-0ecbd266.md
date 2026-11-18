# TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-17T17:59:42Z
- **First seen:** 2026-11-18
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 10.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.23143v1
- **PDF:** https://arxiv.org/pdf/2611.23143v1

## Summary / source snapshot

The authors introduce TCP4D, a unified model that uses a shared 4D scene representation for both tracking observed tool-center-point motion and generating future trajectories in robot manipulation. The framework employs an embodiment-agnostic action space to recover poses and states from monocular video while facilitating cross-embodiment data augmentation.

## Method / approach

The tracker utilizes monocular video inputs and initial 2D queries to recover metric SE(3) TCP poses, gripper states, scene geometry, and camera parameters via a shared 4D scene representation. The generator samples local features along these tracks, combining them with observations and language instructions to forecast future TCP states, supplemented by a cross-embodiment augmentation pipeline.

## Reported contribution / result

The tracker achieves absolute trajectory errors of 7.60 mm on DROID and 16.07 mm on RoboLab, while the generator achieves a 69.19% mean success rate on RoboTwin and outperforms baseline policy models on two real-world tasks.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It enables robust robot action recovery and trajectory generation from RGB videos while supporting efficient cross-embodiment adaptation and data augmentation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
