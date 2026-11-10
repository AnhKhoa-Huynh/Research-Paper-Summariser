# World In-Context Learning for Agentic Robot Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-09T18:59:45Z
- **First seen:** 2026-11-10
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 10.9
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.12885v1
- **PDF:** https://arxiv.org/pdf/2611.12885v1

## Summary / source snapshot

The authors introduce World In-Context Learning (WICL) and its implementation, RoboScript, to address the distribution coupling limitations of traditional action policies. By allowing a frozen model to rehearse tasks in a simulation world and store feedback in context rather than weights, the approach achieves strong task transfer and high success rates across evaluated benchmarks.

## Method / approach

RoboScript implements WICL by taking a single demonstration, rehearsing the task through simulation, freezing the acquired knowledge into a Task Memory, and deploying it on new scenes with data isolation matching real robot constraints.

## Reported contribution / result

RoboScript achieves an 83.4% mean success rate across 50 tasks in RoboTwin 2.0 with one demonstration per task and no gradient updates, outperforming the strongest trained action policy by over 20 points.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The proposed paradigm demonstrates that with a world in the loop, a robot can learn manipulation tasks effectively in its context, generalizing across visual distributions and transferring to physical dual-arm robots.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
