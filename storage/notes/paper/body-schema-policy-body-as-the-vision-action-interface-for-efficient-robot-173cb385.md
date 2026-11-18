# Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-17T12:52:14Z
- **First seen:** 2026-11-18
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 11.4
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.22713v1
- **PDF:** https://arxiv.org/pdf/2611.22713v1

## Summary / source snapshot

The authors introduce Body Schema Policy, an imitation learning approach that integrates a kinematic tree-based latent body schema into the vision-action interface for robots. This design allows individual body parts to retrieve specific visual evidence to condition action denoising efficiently.

## Method / approach

The method uses a latent body schema placing joint and link tokens on the robot's kinematic tree with learned screw motions carrying features between links, and employs body-queried vision where each body part retrieves its own visual evidence to condition action denoising.

## Reported contribution / result

The authors claim that BSP returns action chunks faster than compared policies, achieves compact visual readouts without spatial supervision, matches the Ψ_0 humanoid foundation model with significantly fewer parameters, and nearly doubles Diffusion Policy's success across multiple simulated and real-world tasks.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides an efficient inductive bias inspired by human body schemas, enabling robots to perform whole-body loco-manipulation with drastically fewer parameters and higher success rates than existing baselines.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
