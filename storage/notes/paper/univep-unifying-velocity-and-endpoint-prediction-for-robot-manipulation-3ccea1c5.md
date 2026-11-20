# UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-19T13:36:23Z
- **First seen:** 2026-11-20
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 10.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.26103v1
- **PDF:** https://arxiv.org/pdf/2611.26103v1

## Summary / source snapshot

The authors analyze the different challenges of recovering actions from noise versus polishing clean actions in flow-matching robot policies. They introduce UniVEP, a framework that jointly trains velocity and endpoint prediction targets with consistency supervision to switch prediction types based on noise levels.

## Method / approach

Systematic comparison of velocity prediction, endpoint prediction, and velocity-weighted endpoint prediction across policies, benchmarks, and inference budgets, followed by joint training with consistency supervision that switches from endpoint recovery to velocity refinement as noise decreases.

## Reported contribution / result

Endpoint predictions remain more stable under high noise while velocity predictions offer more accurate corrections near clean actions, and UniVEP achieves high success rates with reduced inference steps on RoboTwin and LiLa-WAM.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It improves success rates and efficiency in simulated and real-world robot manipulation while cutting inference latency.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
