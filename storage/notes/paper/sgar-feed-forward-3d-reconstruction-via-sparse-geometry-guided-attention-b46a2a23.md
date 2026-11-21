# SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-19T17:46:57Z
- **First seen:** 2026-11-21
- **Topic matches:** Computer vision and 3D perception
- **Relevance score:** 3.0
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.26493v1
- **PDF:** https://arxiv.org/pdf/2611.26493v1

## Summary / source snapshot

The authors propose the Sparse Geometric Attention Reconstruction (SGAR) method to address the quadratic computational growth of dense global attention in feed-forward 3D models. By utilizing a lightweight learned module that selects patch tokens based on predicted cross-view 3D proximity, SGAR replaces dense attention with efficient geometric-similarity-guided sparse attention.

## Method / approach

A lightweight learned key selection module is integrated into feed-forward models to predict cross-view 3D proximity of tokens, allowing each patch token to attend only to a small, targeted set of patch tokens from other views.

## Reported contribution / result

The authors claim that SGAR is the fastest among current state-of-the-art dense and sparse methods and the most accurate among sparse methods, operating up to 12 times faster than dense attention at 1,000 views while maintaining stable pose accuracy and superior geometry reconstruction completeness.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It enables feed-forward 3D reconstruction models to scale to larger settings by overcoming the computational bottleneck of dense global attention without sacrificing accuracy.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
