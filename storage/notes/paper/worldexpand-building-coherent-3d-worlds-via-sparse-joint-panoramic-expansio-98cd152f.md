# WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-25T17:58:06Z
- **First seen:** 2026-11-28
- **Topic matches:** Computer vision and 3D perception
- **Relevance score:** 1.05
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.34810v1
- **PDF:** https://arxiv.org/pdf/2611.34810v1

## Summary / source snapshot

The authors introduce WorldExpand to build coherent 3D worlds from a single panorama by framing the process as the generation of sparse, complementary, and high-resolution panoramic observations. This approach addresses redundancy and accumulation errors found in traditional dense sequential generation methods.

## Method / approach

The method uses Coverage-Guided View Selection to identify informative target locations with scene-adaptive quadrants and warp-based coverage scores, alongside Joint Panoramic Diffusion to jointly synthesize four pose-grounded and cross-view-consistent panoramas using Gaussian-splatting-based geometric warps and a diagnostic-guided global-local attention schedule.

## Reported contribution / result

The authors claim that WorldExpand recovers content behind occluders and around distant corners, improves novel-view synthesis and downstream 3D reconstruction metrics, generalizes robustly to diverse in-the-wild scenes, and runs significantly faster than the state-of-the-art panoramic-video method while producing higher-resolution observations.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It concentrates the generation budget on informative scene regions, preserves fine-grained details required for 3D construction, and reduces the training and inference costs of high-resolution joint generation.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
