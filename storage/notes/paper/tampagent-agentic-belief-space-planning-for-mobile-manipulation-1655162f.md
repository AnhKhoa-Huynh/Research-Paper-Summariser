# TAMPAgent: Agentic Belief-Space Planning for Mobile Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-02T18:32:18Z
- **First seen:** 2026-11-03
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, NLP and language models
- **Relevance score:** 11.4
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.03584v1
- **PDF:** https://arxiv.org/pdf/2611.03584v1

## Summary / source snapshot

The authors propose TAMPAgent, a framework that combines Large Vision-Language Models with Task and Motion Planning to handle mobile manipulation in partially observable environments. The approach uses an extensible tool API and belief-space planning to generate executable motion plans and update belief histories in a closed loop.

## Method / approach

The framework endows a Large Vision-Language Model agent with a belief-space planning model operating over perception, planning, and control tools. The agent formulates partial task plans, uses classical search algorithms to complete them, extracts geometric constraints, binds parameters via the tool API, and executes the resulting motion plan while continuously updating its belief history.

## Reported contribution / result

TAMPAgent significantly outperforms direct tool-calling agentic baselines across complex household mobile manipulation tasks on Rainbow Y1 and Unitree G1 platforms.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It demonstrates that integrating Task and Motion Planning constraint satisfaction into agentic planning loops is essential for operating in unstructured, partially observable environments.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
