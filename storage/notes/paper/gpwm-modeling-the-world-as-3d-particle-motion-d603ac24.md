# GPWM: Modeling the World as 3D Particle Motion

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-05T17:24:36Z
- **First seen:** 2026-11-06
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 7.4
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.08338v1
- **PDF:** https://arxiv.org/pdf/2611.08338v1

## Summary / source snapshot

The authors introduce GPWM, a generative particle world model designed to predict 3D scene evolution by forecasting the motion of particles and rigid bodies. This approach operates directly in 3D physical space across various materials and robotic interactions using a unified object-aware multi-resolution transformer architecture.

## Method / approach

The authors employ an object-aware multi-resolution transformer that combines flow matching with diffusion forcing, trained and evaluated on a 25.5-million-frame corpus named ParticleWorlds.

## Reported contribution / result

The authors claim that GPWM outperforms the best prior learned-dynamics baseline across six physical domains by reducing prediction error by 31 percent on average, and that a single unified model largely outperforms per-domain baselines.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The authors claim this model enables contact-rich planning by serving as a generative prior over joint actuator-object motion, allowing goal-directed manipulation without reference action trajectories or goal-specific policies.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
