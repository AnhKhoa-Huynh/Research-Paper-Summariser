# Reference-Model-Guided Distributed MPC for UAV Swarm Formation Flying Under Switching Directed Graphs

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-25T15:21:09Z
- **First seen:** 2026-11-27
- **Topic matches:** Swarm and multi-agent robotics
- **Relevance score:** 3.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.34540v1
- **PDF:** https://arxiv.org/pdf/2611.34540v1

## Summary / source snapshot

This paper presents a reference-model-guided distributed model predictive control framework designed for UAV swarm formation flying under switching directed graphs and limited communication. The authors validate the proposed approach through both simulation and real-world flight experiments on a fully distributed multi-UAV platform.

## Method / approach

A local reference model uses neighbor relative-position information to guide an onboard model predictive control controller, combined with a Kalman filter for motion prediction, disturbance-observer-based feedforward compensation, and control barrier function-based obstacle-avoidance constraints.

## Reported contribution / result

The framework successfully maintains swarm formation and handles obstacles while reducing communication bandwidth demands and adapting to switching directed graphs.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It offers strong scalability for large-scale UAV swarms by eliminating the need to exchange predicted trajectories and operating without external global localization.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
