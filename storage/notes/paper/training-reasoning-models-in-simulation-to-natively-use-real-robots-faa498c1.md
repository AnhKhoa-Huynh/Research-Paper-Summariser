# Training Reasoning Models in Simulation to Natively Use Real Robots

- **Type:** paper
- **Source:** arXiv
- **Published:** 2026-11-13T18:59:02Z
- **First seen:** 2026-11-16
- **Topic matches:** Dexterous manipulation and embodied AI, Robotics and autonomy, AI and machine learning, NLP and language models
- **Relevance score:** 7.3
- **Evidence:** gemini from abstract
- **Original link:** http://arxiv.org/abs/2611.18562v1
- **PDF:** https://arxiv.org/pdf/2611.18562v1

## Summary / source snapshot

The authors demonstrate that an open-weight reasoning model can be trained for native robot control using reinforcement learning exclusively in simulation. The resulting system successfully transfers its learned skills to real-world hardware and novel tasks without requiring human demonstrations.

## Method / approach

The authors introduce a Post-training Engine for Agentic Robotics (PEAR) to train a 27B reasoning model at scale using robot-use reinforcement learning (RURL) on simulated tasks from LIBERO and RoboDojo.

## Reported contribution / result

Training via RURL enables the model to achieve a 60% success rate on a real dual-arm robot and 74.4% on LIBERO, while showing increased robustness to task variations compared to baseline and fine-tuned vision-language-action models.

## Limitations / evidence gaps

Not specified in source

## Why it might matter

The approach demonstrates that open-weight reasoning models can achieve competitive robot-control performance through simulation-based reinforcement learning, offering a viable path for foundation-model post-training in robotics.

## Personal notes

- [ ] Read full source
- [ ] Save to reading list

> Research assistant output is not a fact-checked literature review. Verify claims in the original paper or reporting.
