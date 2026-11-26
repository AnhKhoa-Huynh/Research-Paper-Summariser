# RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-25T18:30:43Z
- **First seen:** 2026-11-26
- **Topic matches:** Dexterous manipulation and embodied AI, NLP and language models
- **Relevance score:** 8.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.34864v1
- **PDF:** https://arxiv.org/pdf/2611.34864v1

## Summary / source snapshot

The authors introduce RePace, an offline reasoning framework designed to accelerate human demonstrations used for fine-tuning vision-language-action policies. The method uses a pretrained language model to evaluate candidate retiming effects and select a speedup profile for each episode.

## Method / approach

RePace measures how different candidate speedup factors shorten the demonstration sequence and compares the resulting observation-action pairs. A pretrained language model then interprets these retiming effects using visual context and original motion to select a complete episode speedup profile based on the task instruction.

## Reported contribution / result

Experimental results on LIBERO and RoboCasa-Kitchen show that RePace outperforms baselines in overall task execution efficiency, while matching or exceeding acceleration baselines in success rate and completing successful trials faster across three tasks using a Franka Research 3 arm.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It enables vision-language-action policies to achieve faster execution speeds without requiring an additional speed-selection module at deployment time.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
