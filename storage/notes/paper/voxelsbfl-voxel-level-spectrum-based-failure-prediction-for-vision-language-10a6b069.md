# VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-17T09:18:38Z
- **First seen:** 2026-11-18
- **Topic matches:** Dexterous manipulation and embodied AI, Computer vision and 3D perception, NLP and language models
- **Relevance score:** 7.95
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.22453v1
- **PDF:** https://arxiv.org/pdf/2611.22453v1

## Summary / source snapshot

The authors propose VoxelSBFL, a black-box method that adapts spectrum-based fault localization to identify failure-associated workspace regions for vision-language-action models. By treating workspace voxels as units of analysis and utilizing recorded trajectories with execution outcomes, the approach scores unseen trajectories without needing internal model access.

## Method / approach

A black-box adaptation of Spectrum-Based Fault Localization where workspace voxels replace program elements, using binary tool-center-point trajectory coverage and execution outcomes to compute suspiciousness maps via established formulas.

## Reported contribution / result

VoxelSBFL achieves an overall macro ROC-AUC of 0.704, significantly outperforming eight action- and trajectory-based baselines, while sensitivity analyses demonstrate that performance varies based on spatial granularity and training-set size.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The findings support the use of spatial spectra for assessing vision-language-action execution and motivate future research into runtime monitoring, self-healing, and targeted policy improvement.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
