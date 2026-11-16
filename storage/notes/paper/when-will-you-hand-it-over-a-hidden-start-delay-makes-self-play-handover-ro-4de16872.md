# When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-13T18:04:37Z
- **First seen:** 2026-11-16
- **Topic matches:** Human–robot interaction, Robotics and autonomy
- **Relevance score:** 8.6
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.18491v1
- **PDF:** https://arxiv.org/pdf/2611.18491v1

## Summary / source snapshot

The authors demonstrate that standard cooperative self-play handover policies fail when interacting with unfamiliar partners due to rigid timing expectations. To address this, they introduce hidden start-delay randomisation, which improves generalization to unseen partners without requiring partner retraining.

## Method / approach

Alternating PPO self-play in a physics-based parcel handover task between a Unitree G1 and a learned giver, paired interventions, and hidden start-delay randomisation (HSD).

## Reported contribution / result

Standard self-play handovers drop significantly in success rate with unfamiliar partners, but adding hidden start-delay randomisation raises success with unseen scripted partners from 31% to 80% while reducing high-force contact.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides a simple one-line rule to make self-play handover policies robust to unfamiliar partners without requiring human data or retraining the partner.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
