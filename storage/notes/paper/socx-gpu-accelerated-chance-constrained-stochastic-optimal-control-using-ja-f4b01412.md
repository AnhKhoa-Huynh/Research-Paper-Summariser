# socx: GPU-Accelerated Chance-Constrained Stochastic Optimal Control using JAX

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-10-29T16:50:11Z
- **First seen:** 2026-11-01
- **Topic matches:** General
- **Relevance score:** 1.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2610.40427v1
- **PDF:** https://arxiv.org/pdf/2610.40427v1

## Summary / source snapshot

The authors introduce socx, a GPU-accelerated JAX solver designed for lifted convex reformulations of linear stochastic optimal control problems involving chance constraints. By leveraging problem structure, the method decomposes the task into independent linear-quadratic tracking problems and Euclidean projections that run in parallel before coupling.

## Method / approach

Distributed optimization that reduces the problem into independent linear-quadratic tracking problems and Euclidean projections onto sets, which are solved in parallel and coupled using constraints.

## Reported contribution / result

The solver achieves speed-ups of up to 98 times over MOSEK and up to 2224 times over SCS, handles horizons up to N=1120, and avoids the out-of-memory errors experienced by MOSEK at N=320.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It enables significantly faster and larger-scale solutions for stochastic optimal control under chance constraints compared to existing solvers like MOSEK and SCS.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
