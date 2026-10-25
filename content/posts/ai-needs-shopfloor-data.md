---
title: "AI won't fix your factory. Data will."
short: "AI on the shopfloor"
description: "AI that predicts and optimises operations learns from shopfloor data. What a good data foundation looks like, and where AI already delivers."
published: 2023-07-22
updated: 2026-10-25
category: thought-leadership
art: mesh
---

AI can genuinely transform manufacturing. But AI that predicts and optimises a factory learns from that factory's data, and in most plants that data is incomplete or missing its context.

Large language models are a useful comparison. They learned from decades of text that people put online. Without that material, even the most advanced model would have nothing to learn from. A factory works the same way: its shopfloor data is what AI learns from. Without it, AI can tell you a lot about factories in general, and very little about yours.

## The slide everyone wants

A common goal on strategy slides is a single line: "Use AI to optimise the factory."

Behind that line sits a long list of prerequisites:

- Defined, documented processes
- An MES/MOM platform running those processes on the shopfloor
- Machines connected, with data collected automatically
- Data contextualised with the order, material, shift and reason
- A data platform that keeps it over time
- Dashboards people use, and baselines to measure against
- A team that trusts the numbers
- A use case and a hypothesis to test

AI is the last line. Many organisations want to invest in it before the processes and data that let it succeed, while still struggling to record downtime reasons accurately.

## AI isn't a black box

AI finds patterns in data. Machine learning trains an algorithm to predict an outcome from what it has seen before. You need a clear question and data to learn from, then you train and test the model. It's statistics at scale: useful and powerful, but dependent on what goes in.

A model fed with end-of-shift manual entries and backflushed consumption will produce confident-looking predictions on a weak foundation.

## What a good data foundation looks like

**Granular.** Individual stops rather than shift totals, and individual measurements rather than daily averages.

**Automatic where possible.** Counts and machine states come straight from the equipment. People record what only people know, such as the reason for a stop.

**Contextualised.** "Machine stopped" means little on its own. The same event with the line, order, product and reason attached is something a model can learn from. More in [Raw machine data is worthless](/post/contextualised-manufacturing-data).

**Connected across departments.** Predictive quality needs process parameters and inspection results in one place. Predictive maintenance needs machine condition alongside what was being produced. When production, quality, inventory and maintenance live in separate systems, some of that context is lost at each integration. This is where MOM's broader scope matters. See [MES vs MOM](/post/mes-vs-mom).

## Where AI already delivers

AI and statistical methods have been part of MES/MOM for longer than many people realise. Statistical process control has detected drifting processes for decades, and condition-based maintenance uses algorithms to spot patterns that come before a failure.

Newer applications are real too:

- **Process parameter optimisation.** Using history to find the settings that minimise scrap for a product and material.
- **Predictive quality.** Predicting whether a part will pass inspection before it's inspected.
- **Anomaly detection.** Spotting unusual patterns in production data that people would miss.
- **Generative AI for people.** Asking questions of operational data in plain English, or generating shift summaries. Examples in [Practical GenAI for the shopfloor](/post/practical-genai-for-the-shopfloor).

Each depends on good data, collected over time, with context.

## Where generative AI doesn't have to wait

Generative AI is different from AI that learns from operational data. Large language models arrive already trained, so they don't need years of a factory's own data to be useful. They also work well on information most factories already have, however messy: SOPs, work instructions, equipment manuals, maintenance work orders, shift logs and free-text comments.

Typical uses:

- **Search with understanding.** Documents are indexed by meaning, so a question like "how do we clear a jam on the capper?" returns an answer drawn from the relevant passages, with a link to the source. This is usually called retrieval-augmented generation (RAG).
- **Turning text into data.** A model can read years of free-text maintenance notes and extract the asset and the failure mode, or classify operator comments into consistent downtime reasons. That helps build the data foundation.
- **Digitising paper.** Photos of handwritten logbooks and scanned checklists can be read and turned into records.
- **Questions in plain English.** Even a partial data set becomes more useful when people can ask about it directly.

The limits:

- **It can't recover what was never captured.** If short stops weren't recorded, no model will find them.
- **It's only as current as its sources.** An outdated SOP produces an outdated answer.
- **It can sound right and be wrong.** Answers should be grounded in your own documents, show their source, and be reviewed by a person when they matter.
- **Acting is different from answering.** Once AI recommends or takes actions on live operations, data quality and guardrails matter again. More in [Agentic AI and MCP](/post/agentic-ai-mcp-manufacturing).

## The path for operational AI

Most manufacturers are somewhere between paper-based and partially digital. For AI that predicts and optimises operations, the route goes through the foundation: defined processes, MES/MOM on the shopfloor, connected equipment and contextualised data built up over time. GenAI pilots on documents and know-how can run alongside that work, so people see value early. [Time to truth](/post/time-to-truth) describes the stages.

## Where to start

Start with a question rather than a model: what decision would you make differently with perfect data about it? Then work backwards. What data would that take, and how much of it is accurate and in context today? The gap is the roadmap.

## My view

I believe AI can genuinely transform manufacturing, but only if the basics are right first. I've sat through many conferences where everyone talks about AI, and then the question about MES/MOM strategy, or how shopfloor data is collected, meets silence or a slide about a pilot. AI won't fix your factory. The data foundation makes it possible, and then AI makes it much better. Skip the foundation for operational AI and you're likely to be back at the start in two years, with an expensive pilot to explain.

What's the one decision in your factory you'd most like AI to help with, and do you have the data for it yet?
