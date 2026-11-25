# Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-24T17:32:00Z
- **First seen:** 2026-11-25
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 10.95
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.33010v1
- **PDF:** https://arxiv.org/pdf/2611.33010v1

## Summary / source snapshot

The authors investigate whether current robotic manipulation policies can successfully operate in scenes containing reflections by introducing a benchmark called RoboDojo-Mirror. They evaluate multiple policies and find that mirror conditions consistently reduce success rates due to spatial mislocalization and phantom targeting rather than just physical collisions.

## Method / approach

The authors introduce RoboDojo-Mirror, a benchmark built on RoboDojo that compares a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop conditions across five different policies, complemented by real-robot experiments with $\pi_{0.5}$ and FastWAM.

## Reported contribution / result

Every mirror condition reduces aggregate success rates by 10.8 to 56.7 percentage points across policies, reaching 62.5 points on the mirrored tabletop, with 50 to 88 percent of failures occurring without recorded robot-panel contact.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

These findings reveal a shared vulnerability to reflective environments across diverse robot policies and motivate reflection-aware evaluation of embodied intelligence.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
