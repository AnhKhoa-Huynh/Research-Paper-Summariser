# Nested Field-of-View Barriers for Teleoperated Multi-Robot Relay Chains

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-03T15:37:16Z
- **First seen:** 2026-11-04
- **Topic matches:** Swarm and multi-agent robotics, Robotics and autonomy
- **Relevance score:** 10.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.05074v1
- **PDF:** https://arxiv.org/pdf/2611.05074v1

## Summary / source snapshot

The authors propose a shared-autonomy framework that utilizes a chain of autonomous robots to maintain a line-of-sight communication relay for a teleoperated leader in communication-denied environments. By implementing nested hard-soft visibility constraints using Control Barrier Functions, the system resolves the conflict between maintaining strict connectivity and allowing follower mobility.

## Method / approach

The approach employs visibility-based Control Barrier Functions to enforce connectivity geometrically, with each agent computing control inputs locally via a quadratic program. It utilizes nested hard-soft visibility constraints consisting of a strict full field-of-view constraint for connectivity guarantees and a contracted field-of-view constraint as a relaxed behavioral objective.

## Reported contribution / result

The authors prove the feasibility of local quadratic programs and the forward invariance of the connected, collision-free set under the distributed controller. Evaluations on simulated kinematic integrators and Crazyflie quadrotors show that the framework keeps links closer to the connected set and requires less follower movement compared to a baseline.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The framework enables the teleoperation of mobile robots in communication-denied environments by resolving the conflict between maintaining strict connectivity guarantees and preserving robot mobility.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
