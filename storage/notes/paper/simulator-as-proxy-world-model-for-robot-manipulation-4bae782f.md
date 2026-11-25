# Simulator-as-Proxy World Model for Robot Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-24T15:14:07Z
- **First seen:** 2026-11-25
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 12.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.32786v1
- **PDF:** https://arxiv.org/pdf/2611.32786v1

## Summary / source snapshot

The authors introduce SimPWM, a framework that combines a calibrated camera, a rule-based simulator, and a video model to represent and render robot manipulation scenes from a first frame. They test the assumption that video world models actually follow the simulated proxy states by evaluating perturbed actions and observing inconsistencies between the video output and the simulation.

## Method / approach

Given a calibrated camera, the system represents the robot using its 3D model and interacted objects as 3D points from the first frame alone, uses a rule-based simulator with no trained parameters to move them based on actions, and renders the result using a video model.

## Reported contribution / result

The arm reliably follows the proxy across base video models, while simulated objects reduce missed pick-ups and their effectiveness in video generation depends heavily on the specific base video model used.

## Limitations / evidence gaps

The simulator carries items like cloth and rope rigidly, and the video model sometimes ignores the simulated state or infers grasps purely from arm motion.

## Why it might matter

It provides a way to test whether video world models actually condition their outputs on simulated proxies or simply ignore them, helping to evaluate the reliability of simulator-as-proxy approaches in robotic manipulation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
