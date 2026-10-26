---
title: "AI will transform your factory, if you give it the right data"
short: "AI on the shopfloor"
description: "AI can transform a factory when it has the right data and context to learn from. What a good data foundation looks like, and where AI already delivers."
published: 2023-07-22
updated: 2026-10-25
category: thought-leadership
art: mesh
---

AI will transform manufacturing. It can predict failures before they happen, find the settings that cut scrap and help every operator work like your best one. What it needs from you is the right data, with the right context.

Large language models show why. The technology is remarkable, but on its own it would be close to useless. What made it so capable was the internet: decades of text that people put online for it to learn from. Your shopfloor data plays the same role for your factory. Give AI accurate, contextualised data about your operation and it can do remarkable things with it. Without that data, it can tell you a lot about factories in general, and very little about yours.

## The slide everyone wants

A common goal on strategy slides is a single line: "Use AI to optimise the factory."

Behind that line sit all the things that make it work:

- Defined, documented processes
- An MES/MOM platform running those processes on the shopfloor
- Machines connected, with data collected automatically
- Data contextualised with the order, material, shift and reason
- A data platform that keeps it over time
- Dashboards people use, and baselines to measure against
- A team that trusts the numbers
- A use case and a hypothesis to test

AI is the line that delivers the biggest gains, and the lines above it are what make those gains possible. They aren't a queue to clear before AI gets a turn. The organisations getting the most from AI work on the whole list at once, and the AI and the data each move faster because of the other.

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

## Where generative AI delivers from day one

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

## Building operational AI and the foundation together

Most manufacturers are somewhere between paper-based and partially digital. AI that predicts and optimises operations grows with the foundation: defined processes, MES/MOM on the shopfloor, connected equipment and contextualised data built up over time. You don't wait for that to be finished. Start a model on the first line you connect, and let what it needs set the priorities for what to capture next. GenAI on documents and know-how can start straight away, so people see value early. [Time to truth](/post/time-to-truth) describes the stages.

## Where to start

Start with a question rather than a model: what decision would you make differently with perfect data about it? Then work backwards. What data would that take, and how much of it is accurate and in context today? The gap is the roadmap.

## My view

I'm genuinely excited about what AI will do for manufacturing. AI will fix your factory, provided you give it the right data and context, in the same way that large language models only became useful once they had the internet to learn from. The manufacturers who'll get the most from it are the ones building that foundation and their AI together, starting now: defined processes, MES/MOM on the shopfloor and contextualised data that builds up over time. Start GenAI on your documents today, and build the data that lets AI predict and optimise alongside it.

What's the one decision in your factory you'd most like AI to help with, and do you have the data for it yet?
