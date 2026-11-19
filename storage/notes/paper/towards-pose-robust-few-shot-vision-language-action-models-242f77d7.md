# Towards Pose-Robust Few-Shot Vision-Language-Action Models

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-18T12:54:16Z
- **First seen:** 2026-11-19
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 7.85
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.24360v1
- **PDF:** https://arxiv.org/pdf/2611.24360v1

## Summary / source snapshot

The authors state that few-shot vision-language-action policies fail when the camera-to-base extrinsic changes due to a bumped tripod or moved robot base. To address this, they introduce WACO, a framework that uses the robot arm and static scene to estimate shifts and canonicalize the inputs for robust policy execution.

## Method / approach

WACO estimates both camera and robot base shifts from a single RGB-D frame by using the robot arm as a metric calibration target and the static scene as a world anchor, without requiring ground-truth extrinsics or extra data, and fine-tunes the unmodified policy.

## Reported contribution / result

WACO consistently outperforms the standard few-shot recipe and prior viewpoint-robust methods across simulated and real-world tasks, raising shifted success rates and recovering most of the performance gap compared to a ground-truth oracle.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It establishes a new state of the art among methods that use no perturbed training data and require no test-time calibration, significantly improving robot manipulation success under spatial shifts.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
