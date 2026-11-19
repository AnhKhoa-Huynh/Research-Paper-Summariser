# $Z$-sight: Unifying Vision-Language-Action and Latent World Modeling

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-18T18:59:38Z
- **First seen:** 2026-11-19
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 8.3
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.24940v1
- **PDF:** https://arxiv.org/pdf/2611.24940v1

## Summary / source snapshot

The authors introduce a unified robot foundation model named Z-sight that integrates vision-language-action capabilities with generative latent world modeling. By predicting the future directly within the visual token space of the vision-language model, the system jointly denoises future spatial tokens and actions without requiring pixel reconstruction.

## Method / approach

The approach utilizes a mixture-of-transformers architecture coupling a foresight expert and a continuous action expert with a vision-language model, trained on human video and robot trajectories.

## Reported contribution / result

The authors claim that Z-sight achieves an 81.9% success rate on SIMPLE and 73.3% across six Unitree G1 tasks at a processing speed of 110 ms per chunk.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The model provides a way to combine future prediction and action generation efficiently in a native feature space without the heavy costs associated with video generators.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
