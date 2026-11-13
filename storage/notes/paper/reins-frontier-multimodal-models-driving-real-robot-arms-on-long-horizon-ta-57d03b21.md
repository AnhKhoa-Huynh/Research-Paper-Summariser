# Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-12T11:05:11Z
- **First seen:** 2026-11-13
- **Topic matches:** Human–robot interaction, Dexterous manipulation and embodied AI, Robotics and autonomy, NLP and language models
- **Relevance score:** 11.05
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.16632v1
- **PDF:** https://arxiv.org/pdf/2611.16632v1

## Summary / source snapshot

The authors introduce Reins, a harness designed to enable off-the-shelf frontier multimodal models to operate dual-arm robots on long-horizon manipulation tasks. Utilizing 3D perception tools, atomic actions, and a continuous narrator instance, the system allows models to execute tasks successfully with natural-language prompts and no task-specific code.

## Method / approach

An off-the-shelf model operates a dual-arm robot using 3D perception tools and atomic actions that report contact and grip, chaining actions with conditional constraints, while a second model instance acts as a narrator to continuously monitor camera feeds and report changes.

## Reported contribution / result

With the Reins harness and natural-language prompts, GPT-6.1 Sol achieves an 88% success rate on real episodes across five tasks, whereas without the harness it fails every shell game and takes eight times as long.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It demonstrates that frontier multimodal models can drive real robot arms on complex, long-horizon, contact-rich manipulation tasks zero-shot when equipped with appropriate perception and action harnesses.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
