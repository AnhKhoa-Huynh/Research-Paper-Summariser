# TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-05T12:01:12Z
- **First seen:** 2026-11-06
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning, NLP and language models
- **Relevance score:** 14.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.07881v1
- **PDF:** https://arxiv.org/pdf/2611.07881v1

## Summary / source snapshot

The authors introduce TactileLab, a scalable multimodal tactile simulation framework built on IsaacLab that models shear-sensitive contact dynamics using rigid-body simulation. Additionally, they propose a real-to-sim tactile translation method to enable sim-to-real policy deployment across heterogeneous robotic systems.

## Method / approach

The framework utilizes rigid-body simulation to estimate dense tangential motion at the contact interface, producing simulated tactile flow combined with a contact depth field, and introduces a policy architecture for processing proprioceptive and tactile observations along with a real-to-sim tactile translation pipeline.

## Reported contribution / result

Policies trained with simulated tactile flow learn efficiently at scale, exhibit emergent contact-aware behaviors, and can be successfully deployed in the real world for dual-arm and dexterous in-hand manipulation.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides an end-to-end sim-to-real framework for scalable tactile policy learning, overcoming the computational demands of soft-body simulation to enable shear-sensitive manipulation across diverse robotic systems.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
