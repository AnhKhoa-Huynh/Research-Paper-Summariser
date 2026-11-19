# DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-18T18:03:14Z
- **First seen:** 2026-11-19
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 7.9
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.24836v1
- **PDF:** https://arxiv.org/pdf/2611.24836v1

## Summary / source snapshot

The authors introduce DiWALI, a framework designed to learn and improve diffusion policies using a world model trained on both human and robot play. The approach infers latent actions from action-free demonstrations via an inverse dynamics model and grounds them in robot commands to reduce reliance on action-labeled robot data.

## Method / approach

The framework infers latent actions from consecutive frames using an inverse dynamics model, grounds them in robot commands via a separately trained decoder, and trains skill policies over latent actions that are further improved with reinforcement learning in imagination.

## Reported contribution / result

Policies trained solely from human demonstrations substantially outperform baselines trained with robot demonstrations on the CALVIN benchmark, and incorporating human play into world model training yields stronger policies after fine-tuning.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It demonstrates that human experience can support both manipulation skill acquisition and policy improvement, thereby reducing reliance on scarce action-labeled robot data.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
