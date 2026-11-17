# ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-16T18:59:37Z
- **First seen:** 2026-11-17
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, NLP and language models
- **Relevance score:** 8.8
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.21607v1
- **PDF:** https://arxiv.org/pdf/2611.21607v1

## Summary / source snapshot

The authors investigate whether frontier-scale representations can improve robot learning by connecting a massive 552B vision-language model backbone to a trainable action diffusion transformer. They systematically evaluate this scale against smaller models across sample efficiency, generalization, and precise manipulation.

## Method / approach

The authors introduce ScaleVLA, which connects a 552B DeepSeek-V4.1-Flash backbone to a trainable action DiT, and systematically compare it with VLMs ranging from 2B to 552B under a shared training setup.

## Reported contribution / result

ScaleVLA achieves higher sample efficiency with 10 demonstrations outperforming a 2B backbone trained with 50, reaches a 45.1% LIBERO-PRO success rate for generalization, improves real-world charger insertion success from 4/10 to 9/10, and maintains a median latency of 216 ms per action chunk.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The findings suggest that frontier vision-language models can serve as powerful representational foundations for efficient and generalizable robot policies.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
