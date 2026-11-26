# M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-25T15:32:21Z
- **First seen:** 2026-11-26
- **Topic matches:** Dexterous manipulation and embodied AI, NLP and language models
- **Relevance score:** 8.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.34560v1
- **PDF:** https://arxiv.org/pdf/2611.34560v1

## Summary / source snapshot

The authors present a vision-language-action model that combines visual and wrench memories with predictive test-time adaptation for robotic manipulation. The approach integrates test-time training for visual history and a context gate for wrench history alongside online self-supervision to handle shifts in contact dynamics.

## Method / approach

The model uses test-time training to encode observation history in fast weights for visual memory, a context gate to control the use of wrench history during joint action and wrench denoising, and low-rank policy adapters updated via an auxiliary wrench prediction loss.

## Reported contribution / result

The authors claim that the proposed method achieves a mean success rate of 82.71% across eight tasks, representing a 31.46% absolute gain over the strongest baseline.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It addresses challenges in robotic manipulation involving multimodal memory and rapid adaptation to shifting contact dynamics.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
