# Compressed Orientation Reachability Maps for Sub-Second Robotic Needle Entry Point Planning

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-10-29T11:57:41Z
- **First seen:** 2026-11-01
- **Topic matches:** General
- **Relevance score:** 1.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2610.39879v1
- **PDF:** https://arxiv.org/pdf/2610.39879v1

## Summary / source snapshot

This paper presents an Orientation-Based Reachability Map framework to overcome computational bottlenecks in robotic percutaneous liver interventions. By precomputing kinematic feasibility and utilizing a Just-In-Time compiled runtime pipeline, the approach achieves sub-second entry point planning while maintaining high geometric fidelity.

## Method / approach

The authors precompute the kinematic feasibility of a 6 Degrees of Freedom serial manipulator across workspace positions and encode orientation feasibility into an 83 MB map, paired with a Just-In-Time compiled runtime pipeline that replaces live optimization with array lookups.

## Reported contribution / result

Planning latency was reduced from 13.5-26.9 seconds to 0.289-0.349 seconds per target, while achieving a mean convex hull volume overlap ratio of 0.933 and a mean alpha-shape volume ratio of 0.976 compared to the baseline.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The framework enables sub-second entry point planning and offers an efficient computational approach for robotic needle insertion in percutaneous liver ablation, supporting real-time intraoperative adaptation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
