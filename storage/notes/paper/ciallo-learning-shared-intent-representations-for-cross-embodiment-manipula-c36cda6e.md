# CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-10T08:35:27Z
- **First seen:** 2026-11-11
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 7.6
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.13732v1
- **PDF:** https://arxiv.org/pdf/2611.13732v1

## Summary / source snapshot

The paper introduces CIALLO, an action codec designed to learn shared intent representations that bridge control interface differences across various robot embodiments. It uses an embodiment-conditioned decoder to map short-horizon behavioral intent to specific robot actions, enabling cross-embodiment knowledge transfer.

## Method / approach

CIALLO aligns actions, visual changes, and observation-grounded language in a shared intent space and adapts to new robots by updating only embodiment embeddings using short recordings. The authors instantiate a policy called Qwen-CIALLO by combining CIALLO with a Qwen3.5-4B backbone, and also evaluate finetuning the action decoder in simulation.

## Reported contribution / result

Qwen-CIALLO achieves a 76.7% average success rate across real SO-101 and single-arm Piper robots using 20 demonstrations per task, compared to 70.0% for fully finetuned pi_0. In simulation, the approach achieves 97.3% success on LIBERO and 52.7% on RoboTwin 2.0, with the LIBERO policy reaching 80.8% on LIBERO-Plus without further finetuning.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The proposed shared action codec serves as a transferable control interface that successfully separates embodiment calibration from task learning.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
