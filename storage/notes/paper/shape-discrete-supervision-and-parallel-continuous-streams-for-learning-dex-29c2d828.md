# SHAPE: Discrete Supervision and Parallel Continuous Streams for Learning Dexterous Manipulation from Egocentric Human Data

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-18T15:14:26Z
- **First seen:** 2026-11-19
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 8.1
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.24585v1
- **PDF:** https://arxiv.org/pdf/2611.24585v1

## Summary / source snapshot

The authors introduce SHAPE, a vision-language-action model designed to learn dexterous manipulation skills from egocentric human recordings rather than task-specific robot demonstrations. The approach employs discrete supervision of end-effector chunks through the backbone alongside parallel flow-matching streams for executable end-effector and joint actions.

## Method / approach

The model uses discrete action tokens of end-effector chunks as an auxiliary task for the backbone alongside a shared flow-matching expert that outputs parallel end-effector and joint streams.

## Reported contribution / result

Discrete supervision assists in learning from human data by driving backbone gradients and shaping action-informative representations, while joint readout excels at fine-grained control with robot demonstrations and inverse kinematics-based end-effector readout excels at human-to-robot transfer.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It enables a dexterous robot to leverage cheaper egocentric human recordings for pretraining and direct skill learning without requiring task-specific robot data.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
