# Beyond Feature Fusion: Sensor-Grounded Semantic-Spiking Learning for Robust Object Detection

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-25T18:10:24Z
- **First seen:** 2026-11-27
- **Topic matches:** Computer vision and 3D perception
- **Relevance score:** 3.0
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.34828v1
- **PDF:** https://arxiv.org/pdf/2611.34828v1

## Summary / source snapshot

The authors propose SPIRE, a sensor-grounded semantic-spiking framework designed for illumination-robust object detection using a single spike stream. By combining appearance views and cumulative temporal views, the approach integrates semantic cues with spike-derived properties to refine feature pyramids.

## Method / approach

The framework builds an appearance view via illumination adaptation and constructs cumulative views from progressively longer prefixes to supply rate maps, edge maps, and rate differences. It uses artificial neural network features and spike-derived initialization to set membrane potentials and firing thresholds, and applies local spike-count contrasts for supervision and feature correction.

## Reported contribution / result

On simulated VOC and COCO, SPIRE-D outperforms the strongest baseline by 4.00 to 5.50 AP50 points across four exposure settings, achieves 67.07 AP50 and 40.10 AP75 on real PKU-Vidar-DVS recordings, and uses 50.4 percent fewer MACs than SPFD.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It offers an illumination-robust approach for object detection under challenging exposure conditions using spike cameras.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
