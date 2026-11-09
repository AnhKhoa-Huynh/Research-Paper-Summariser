# Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-06T18:44:33Z
- **First seen:** 2026-11-09
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning
- **Relevance score:** 8.8
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.09864v1
- **PDF:** https://arxiv.org/pdf/2611.09864v1

## Summary / source snapshot

The authors propose Grasp-TAGS, a task-aware grasp selection framework designed to improve goal-conditioned large-object rearrangement for mobile manipulators. The approach trains a unified reinforcement learning policy across various initial grasp configurations and distills the critic into a lightweight utility network to rank candidate grasps prior to physical contact.

## Method / approach

Training a unified PPO-based reinforcement learning policy across multiple initial grasp configurations and distilling the learned critic into a lightweight grasp utility network that ranks candidate grasps using the candidate grasp configuration and goal information.

## Reported contribution / result

Grasp-TAGS achieves an average success rate of 89.84 percent compared to 79.87 percent for the best-performing single-grasp policies, and reduces final orientation errors across all evaluated objects.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

It provides a method to select grasps that account for downstream manipulation performance in loco-manipulation tasks, improving rearrangement success rates and reducing orientation errors compared to fixed or random grasp selection.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
