# DeCoNav-Act: Benchmarking Collective Physical Capability in Multi-Robot Mobile Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-24T14:24:37Z
- **First seen:** 2026-11-25
- **Topic matches:** Dexterous manipulation and embodied AI, Swarm and multi-agent robotics, Robotics and autonomy
- **Relevance score:** 15.45
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.32683v1
- **PDF:** https://arxiv.org/pdf/2611.32683v1

## Summary / source snapshot

The authors introduce DeCoNav-Act, a benchmark designed to evaluate language-guided multi-robot mobile manipulation within a shared physics simulation. The benchmark tests both parallel workloads and physical dependencies through 500 tasks to assess collective physical capability.

## Method / approach

The authors evaluate sensor-grounded adaptations of ASPIRE, RAX, and their own agent CoMoMa using language models such as GPT-5.6-luna and GPT-6.1-sol across 350 homogeneous and 150 heterogeneous tasks verified by joint reference execution.

## Reported contribution / result

With GPT-5.6-luna, no method completes a task, a maximum of 8.8% of dependencies are reached, and no handoffs are completed from pre-handoff states; with GPT-6.1-sol, CoMoMa establishes the condition in 26.5% of trials, but only 4.1% succeed.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It addresses the limitation of existing benchmarks that rarely test whether physical states resulting from multi-robot task allocation and skill sequencing are actually usable by teammates.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
