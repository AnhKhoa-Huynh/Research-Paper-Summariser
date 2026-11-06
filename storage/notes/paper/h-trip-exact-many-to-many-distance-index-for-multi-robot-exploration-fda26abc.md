# H-TRIP: Exact Many-to-Many Distance Index for Multi-Robot Exploration

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-05T15:03:10Z
- **First seen:** 2026-11-06
- **Topic matches:** Swarm and multi-agent robotics, Robotics and autonomy
- **Relevance score:** 10.2
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.08139v1
- **PDF:** https://arxiv.org/pdf/2611.08139v1

## Summary / source snapshot

The authors introduce H-TRIP, an exact distance index designed for multi-robot exploration based on Kleene algebra over the min-plus semiring for growing occupancy grids. The approach uses a spatial hierarchy and rank-one edge insertions to efficiently compute many-to-many shortest paths.

## Method / approach

Partitioning the known map into a spatial hierarchy with fixed boundary ports, decomposing unknown-to-free revelations into rank-one min-plus edge insertions, propagating decreased port-to-port summaries up ancestor chains, and applying a shared hierarchical lift.

## Reported contribution / result

Sequential insertions preserve exact shortest-path distances on the grid, and dense many-to-many queries are up to two orders of magnitude faster than sequential breadth-first searches.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It accelerates in-loop queries during multi-robot exploration runs on growing occupancy graphs compared to co-scheduled baseline searches.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
