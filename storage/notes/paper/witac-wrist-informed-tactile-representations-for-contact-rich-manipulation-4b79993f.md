# WiTac: Wrist-Informed Tactile Representations for Contact-Rich Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-16T13:08:09Z
- **First seen:** 2026-11-17
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI
- **Relevance score:** 12.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.21057v1
- **PDF:** https://arxiv.org/pdf/2611.21057v1

## Summary / source snapshot

The authors propose WiTac, a pretrained encoder designed to fuse touch signals, hand motion, and wrist views for contact-rich manipulation. They claim this early fusion approach grounds tactile features in visual context to improve downstream policy performance.

## Method / approach

Pretraining on nearly 300 hours of SharpaDex data to deeply fuse tactile signals with hand motion and wrist views before action generation, and conditioning downstream vision-language-action policies on the resulting representations.

## Reported contribution / result

Conditioning VLA policies on WiTac improves task success over vision-only base policies by 28.8% and 15.0% on average, and outperforms a wrist-free tactile encoder by 18.8% and 7.5%, across four contact-rich manipulation tasks.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It demonstrates that fusing touch and wrist vision prior to policy injection can better ground tactile features and significantly improve success rates in contact-rich manipulation tasks.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
