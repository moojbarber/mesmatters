---
slug: "the-future-of-smart-manufacturing-harnessing-the-power-of-mes-intelligence"
legacyUrl: "https://www.mesmatters.com/post/the-future-of-smart-manufacturing-harnessing-the-power-of-mes-intelligence"
published: "2023-07-22T10:00:00.000Z"
updated: "2026-10-17T09:00:00.000Z"
author: "Matthew Barber"
---

Anyone who knows me knows I believe AI can genuinely transform manufacturing.

But only if you get the basics right first.

I've sat through countless conferences where everyone is obsessed with AI. Then I ask about their MES/MOM strategy, or how they're collecting data from the shopfloor to feed those AI ambitions, and I get... nothing. Silence. A slide about a pilot.

Think about ChatGPT, Claude or Gemini for a moment. The models are remarkable. But they learned from the internet: decades of text, data and knowledge that people put online. Take the internet away and the most advanced model in the world has nothing to learn from. It's redundant.

Your factory works the same way. Shopfloor data is your factory's internet. AI is the technology that sits on top of it. Without that data, AI can tell you a lot about factories in general, and very little about yours.

So let me put my position plainly. AI won't fix your factory. Your data foundation makes it possible. And then AI will make it much, much better.

## The slide everyone wants

There's a slide I use when I teach this subject. It says one thing: "Use AI to optimise your factory."

Simple, right?

Then I zoom out. Above that one line is a very long list of things you need first:

- Defined, documented processes
- An MES/MOM platform running those processes on the shopfloor
- Machines connected, with data collected automatically
- That data contextualised: which order, which material, which shift, which reason
- A data platform that holds it over time
- Dashboards people actually use, and baselines to measure against
- Training, buy-in, and a team that trusts the numbers
- A use case, a hypothesis and a model

AI is the tiny last line at the bottom.

Most people want to invest in that last line before the data architecture, the applications and the processes that let it succeed. They're still struggling to get basic downtime reasons recorded accurately, but their expectations are already at AI level.

## AI isn't a black box

AI doesn't magic up answers. It finds patterns in data.

Machine learning, specifically, is a way to train an algorithm to predict an outcome based on what it's seen before. You need a clear question and data to learn from. Then you train the model, test it and refine it. It's statistics at scale. Useful, powerful statistics. But statistics all the same.

Which means the quality of what comes out depends entirely on what goes in.

Feed a model manual end-of-shift entries, estimated scrap figures and backflushed consumption from ERP, and you'll get confident-looking predictions built on sand.

## What a good foundation looks like

A good data foundation has a few properties. None of them are glamorous.

**It's granular.** You need individual stops, not shift totals. Individual measurements, not daily averages.

**It's automatic where it can be.** Machine counts and states come straight from the equipment. People record the things only people know, like the reason for a stop.

**It's contextualised.** A signal that says "machine stopped" is worthless on its own. One that says which line, which order, which product, which shift and why, for how long and how often, is something a model can learn from. I've written about this in more detail in [Raw machine data is worthless](/post/contextualised-manufacturing-data).

**It's connected across departments.** This is where MOM matters. Predictive quality needs process parameters, inspection results and material lots in the same place. Predictive maintenance needs machine condition alongside what was being produced at the time. If production, quality, inventory and maintenance each live in their own system, much of that context is lost at the integration boundaries before any model sees it.

## Where AI is already earning its keep

Here's the part people forget. AI and machine learning have been in MES/MOM for longer than most realise.

Statistical process control has spotted drifting processes for decades. Condition-based and predictive maintenance use algorithms to detect patterns that come before a failure. Neither is new. Both are proven.

The newer applications are real too. The technology behind them is ready. What's lagging is the number of applications built to take advantage of it:

- **Process parameter optimisation.** Using history to find the speeds, temperatures and pressures that minimise scrap for a given product and material.
- **Predictive quality.** Predicting whether a part will pass inspection before it's inspected.
- **Anomaly detection.** Spotting unusual patterns in production data that no human would catch.
- **Generative AI for people.** Asking questions of your operational data in plain English, generating shift summaries, or explaining what a screen is showing. I cover practical examples in [Practical GenAI for the shopfloor](/post/practical-genai-for-the-shopfloor).

Each of these depends on the same thing. Good data, collected over time, with context.

## Where generative AI doesn't have to wait

Everything above is about AI that learns from your operational data: predicting failures, optimising parameters, spotting anomalies. That kind of AI really does need the foundation first.

Generative AI is different, and it's worth being precise about why.

Large language models arrive already trained. They learned language, and a surprising amount about engineering and manufacturing, before they ever reach your factory. So they don't need years of your own data to be useful. And they work on the kind of information every factory has in abundance, however messy: SOPs, work instructions, equipment manuals, maintenance work orders, free-text downtime comments, shift logs, quality reports, supplier certificates, emails.

Here's how they get value from it:

- **Search with understanding.** Documents are split into passages and indexed by meaning, not just keywords. When someone asks "how do we clear a jam on the capper?", the system retrieves the most relevant passages and the model answers from them, with a link back to the source. This is usually called retrieval-augmented generation (RAG). It works on documents as they are today.
- **Turning text into data.** A model can read ten years of free-text maintenance notes and pull out the asset, the failure mode, the part replaced and the likely cause. Or classify thousands of operator comments into consistent downtime reasons. That turns messy history into structured data you can analyse, and it helps build the foundation rather than waiting for it.
- **Reading what was never digital.** Photos of handwritten logbooks, scanned travellers and paper checklists can be read and digitised.
- **Asking questions of the data you do have.** Even a partial data set becomes more useful when people can ask about it in plain English instead of waiting for a report.

So GenAI pilots can, and often should, run alongside the foundation work rather than after it. Aim them at knowledge problems: finding answers in manuals, troubleshooting from maintenance history, drafting reports, onboarding new starters.

Be clear about the limits, though:

- **It can't recover what was never captured.** If nobody recorded the three-second stops, no model will find them.
- **It's only as current as its sources.** Index the 2019 version of an SOP and it will confidently give you the 2019 answer.
- **It can sound right and be wrong.** Ground every answer in your own documents, show the source, and keep a person reviewing anything that matters.
- **Acting is different from answering.** The moment AI starts recommending or taking actions on live operations, the quality, timeliness and context of the operational data matter again, and so do guardrails.

## You can't skip the steps for operational AI

Everyone wants to be at the top of the [maturity model](/post/smart-manufacturing-maturity-model). Predictive, autonomous, AI-enabled. Very few are.

Most manufacturers I speak to are somewhere between paper-based and partially digital. That's not a criticism. It's a starting point. For AI that predicts and optimises operations, the path goes through the middle, not around it.

Get the processes defined. Put MES/MOM on the shopfloor. Connect the equipment. Build up clean, contextualised data. Then point AI at the problems that matter most.

Do it in that order and AI amplifies everything you've built. Run GenAI pilots on your documents and know-how in parallel, so people see value early and you learn what works. But skip the foundation for operational AI and you'll be back at the start in two years, with a very expensive pilot to explain.

## So where should you start?

Not with a model. With a question: what decision would you make differently if you had perfect data about it?

Then work backwards. What data would that take? Where does it come from today? How much of it is accurate, automatic and in context?

That gap is your roadmap. And for most factories, the first steps on it look a lot more like MES/MOM than AI.

What's the one decision in your factory you'd most like AI to help with, and do you have the data for it yet?
