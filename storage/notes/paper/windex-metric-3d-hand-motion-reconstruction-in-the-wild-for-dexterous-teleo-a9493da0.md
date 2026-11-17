# WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-16T14:14:54Z
- **First seen:** 2026-11-17
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 8.55
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.21143v1
- **PDF:** https://arxiv.org/pdf/2611.21143v1

## Summary / source snapshot

The authors introduce WinDEX to address limitations in metric-scale hand motion reconstruction from in-the-wild egocentric videos for robotic teleoperation and policy learning. The system combines geometric-temporal optimization, a fisheye-native network, distilled models, and low-cost stereo-inertial capture to achieve efficient and accurate hand tracking.

## Method / approach

The authors integrate geometric-temporal optimization with visual-inertial SLAM, a fisheye-native network called WinDEX-Net utilizing calibrated stereo and temporal context, distilled models for offline reconstruction and causal streaming, and low-cost CyberCap stereo-inertial capture to form a large training dataset.

## Reported contribution / result

The authors claim offline reconstruction runs at 43.61 FPS and causal streaming at 171 FPS, achieving state-of-the-art accuracy on held-out data with a 14.5-pixel in-the-wild reprojection error and a 37.29 mm world-frame joint error.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The authors claim the approach achieves significantly higher task success rates for reinforcement learning policies compared to prior methods and enables real-time arm-hand teleoperation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
