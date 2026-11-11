# From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-10T16:17:48Z
- **First seen:** 2026-11-11
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy
- **Relevance score:** 7.6
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.14274v1
- **PDF:** https://arxiv.org/pdf/2611.14274v1

## Summary / source snapshot

This paper investigates the difference between predictive utility and decision utility when manipulating deformable linear objects. The authors introduce a geometry-grounded policy called Geometry-Pointer-Flow to compare how different representations of physical context affect forward prediction versus executed control.

## Method / approach

The authors utilize Geometry-Pointer-Flow, a policy separating grasp-location selection from motion generation, and evaluate physical context represented by ground-truth parameters, estimated parameters, and learned interaction-history representations across simulation trials and hardware experiments.

## Reported contribution / result

While ground-truth and estimated parameters improve forward prediction, estimated parameters provide no detectable one-step control gain, whereas history-conditioned Geometry-Pointer-Flow reduces executed error by 9.9% relative to the geometry-only variant.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The findings demonstrate that physical context should be evaluated based on the decisions it supports rather than solely by predictive accuracy.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
