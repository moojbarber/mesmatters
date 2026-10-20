---
title: "AI, ML and GenAI on the shopfloor: what each one actually does"
short: "AI, ML and GenAI explained"
description: "AI, machine learning and generative AI get used interchangeably. They shouldn't be. What each one is, where it earns its keep in a factory, and what it needs."
published: 2026-10-16
category: thought-leadership
art: mesh
---

AI is on every conference agenda, every vendor roadmap and every executive's wish list. And the terms get thrown around as if they all mean the same thing.

They don't. If you're going to spend money on any of them, it's worth knowing which is which.

## Let's align on some terminology

**Artificial intelligence (AI)** is the broad category. Any system that performs tasks that would normally need human intelligence: recognising patterns, making decisions, predicting outcomes.

**Machine learning (ML)** is a subset of AI. You train an algorithm on historical data so it can predict an outcome from new data, faster and more consistently than a person could. The key word is *train*. You need a data set and a model, and you train, test and refine it before you trust it. It's not magic. It's statistics at scale.

**Generative AI (GenAI)** is a different subset. Large language models that generate text, images, code and other content. This is what most people mean when they say "AI" today. GenAI doesn't predict from your operational data in the same way. It generates content from patterns learned across enormous amounts of training data.

So when someone says "we're doing AI on the shopfloor", the first question is: which kind?

## Machine learning: older than you think

Machine learning and statistical methods have been in MES/MOM for longer than most people realise.

**Statistical process control (SPC)** has been spotting drifting processes for decades. It's not branded as AI, but it's the same family of thinking: learn what normal looks like, then flag what isn't.

**Predictive maintenance** uses algorithms to find patterns in vibration, temperature, current or cycle counts that come before a failure. Proven, practical, and paying back in factories today. I cover the data it needs in [Predictive maintenance needs data you aren't collecting yet](/post/predictive-maintenance-data).

The newer ML applications need more maturity, but they're very real:

- **Process parameter optimisation.** Finding the speeds, temperatures and pressures that minimise scrap for each product and material.
- **Predictive quality.** Predicting whether a part or batch will pass inspection before it's inspected, so you can act while it's still on the line.
- **Anomaly detection.** Flagging unusual combinations of signals that no person watching a dashboard would catch.
- **Vision inspection.** Cameras and trained models spotting defects consistently, often running at the edge, right at the machine.

## Generative AI: useful in different ways

GenAI's sweet spot is helping people, not controlling machines. Some genuinely practical examples:

- **Asking questions in plain English.** "Write a one-page summary of OEE on Line 4 over the last 12 months for the CI manager, and flag anything unusual."
- **Configuring systems.** "Set up a new packing line in the packing department, and ask me what you need to know."
- **A knowledge assistant.** "How do I calculate Cpk?" or "What is this screen telling me?"
- **Shift summaries.** What ran, what stopped and what's waiting, written up for the incoming crew.

I go through more of these in [Practical GenAI for the shopfloor](/post/practical-genai-for-the-shopfloor).

## Agentic AI: the next step

You'll also hear a lot about agentic AI. These are systems that don't just answer a question but plan and carry out a task: gathering information, deciding what to do, acting through other software, and learning from the result.

It's exciting. It's also the top of the maturity curve, because an agent acting on your factory needs very good data and very clear guardrails. I explain it for operations leaders in [Agentic AI and MCP, explained](/post/agentic-ai-mcp-manufacturing).

## What all three need

Every one of these depends on data. Good, granular, contextualised data, collected over time.

ML can't learn patterns from shift totals typed in at 6am. GenAI can't summarise a shift accurately if the shift's data is scattered across paper, Excel and three systems. An agent can't safely act on information it can't trust.

That's why I keep saying AI is the last step, not the first. On the shopfloor, [MES/MOM](/post/what-is-mes-and-why-is-it-important-in-manufacturing) is where most of that data is created and given its context: which order, which material, which machine, which shift, and why.

## A practical way to start

Don't start with the technology. Start with a decision you'd like to make better.

- Which failure would you most like to see coming?
- Which quality defect costs you most?
- Which report do people spend hours building every week?
- Which question do new starters ask most often?

Then ask whether you have the data that decision needs, at the right granularity, with the right context. If you do, there's probably an AI use case worth piloting. If you don't, you've just found your first project, and it isn't an AI project.

Which of these three is closest to what your business is asking for right now?
