# TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-19T16:53:19Z
- **First seen:** 2026-11-20
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI
- **Relevance score:** 8.8
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.26405v1
- **PDF:** https://arxiv.org/pdf/2611.26405v1

## Summary / source snapshot

The authors propose TacInno to address the issue of inconsistent gains when integrating tactile sensing into vision-language-action models. The approach isolates tactile changes unexplained by vision and actions, using this residual as a supervision target during training.

## Method / approach

A TacInno tokenizer compresses future tactile changes into a discrete code conditioned on visual observations and executed actions, while the TacInno-VLA policy learns to predict this code without adding inference-time modules.

## Reported contribution / result

TacInno-VLA achieved average success rates of 87.5% across six simulation tasks and 70.5% across four real-world tasks, outperforming the strongest visuo-tactile baseline by 10.7 and 9.0 percentage points, respectively.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The results demonstrate the effectiveness of tactile innovation as a supervision signal for contact-rich manipulation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
