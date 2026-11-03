# KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-02T13:11:21Z
- **First seen:** 2026-11-03
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 14.3
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.03091v1
- **PDF:** https://arxiv.org/pdf/2611.03091v1

## Summary / source snapshot

The authors introduce KlaskTron-IL, an imitation learning benchmark featuring a multi-tier dataset and diagnostic baselines designed for contact-rich adversarial dynamics. They also demonstrate the zero-shot transfer of a trained behavioral cloning policy to the physical KlaskTron hardware platform.

## Method / approach

The authors collected 80k human demonstration timesteps directly on the physical robot, expanded them with 320k symmetry-augmented timesteps, and generated synthetic expert trajectories up to 5M steps using a PPO policy. They evaluated diagnostic baselines including behavioral cloning and generative adversarial imitation learning on the platform.

## Reported contribution / result

Standard imitation learning methods exhibit three characteristic failure modes under contact-rich adversarial dynamics, specifically a data scaling plateau for behavioral cloning, a weak-gradient discriminator in GAIL, and an asymmetric behavioral cloning prior and reward-density interaction.

## Limitations / evidence gaps

Commands used by the transferred policy must respect the actuator model's identification range of plus or minus 0.2 meters per second.

## Why it might matter

Policies trained on this benchmark can run unchanged on the physical robot due to a validated sim-to-real actuator model bridge, supporting zero-shot hardware transfer for contact-rich adversarial reinforcement learning.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
