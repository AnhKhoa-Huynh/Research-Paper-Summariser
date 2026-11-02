# RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-10-30T12:01:49Z
- **First seen:** 2026-11-02
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 7.85
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2610.41625v1
- **PDF:** https://arxiv.org/pdf/2610.41625v1

## Summary / source snapshot

The authors introduce RTPolicy, a multi-view visuomotor policy designed for efficient robotic manipulation on edge devices. The approach combines view-aware feature fusion and visual compression to reduce computational overhead while maintaining necessary visual information for action generation.

## Method / approach

Combines view-aware feature fusion with visual compression to generate a compact token representation, which then conditions a flow-matching action generator utilizing the robot state and flow time.

## Reported contribution / result

RTPolicy achieves a mean success rate of 52.26 percent across 50 tasks on the RoboTwin 2.0 evaluation and sustains real-time inference at 32.9 Hz on the RDK S600 edge platform.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides a low-latency, real-time multi-view visuomotor policy suitable for closed-loop robotic manipulation and asynchronous streaming inference on resource-constrained edge devices.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
