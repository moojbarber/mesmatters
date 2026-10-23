---
title: "Raw machine data is worthless. Context is what makes it useful"
short: "Contextualised data"
description: "A machine signal that says 'stopped' tells you nothing. How MES/MOM turns raw data into contextualised information, and where context gets lost between systems."
published: 2026-05-07
category: thought-leadership
art: flow2
---

Data, data, data.

If there's one phrase that captures what a smart factory is really about, it's that. PLCs, sensors, historians and IIoT platforms all generate enormous amounts of it.

But data on its own is worthless. What matters is the context around it.

## A signal is not information

At the bottom of the stack you've got raw machine data. A PLC sends a signal every time a machine cycles. A temperature sensor reports every second. A proximity switch fires when a product passes.

This data is accurate. It's real-time. And it's completely meaningless on its own.

A signal that says "machine stopped" tells you nothing useful. When did it stop? For how long? Was it during a run or between orders? What was being made? Who was on shift? Why did it stop?

## Context turns a signal into something you can act on

The same event, contextualised:

> Machine 3 on Line 7 stopped at 14:23 during production order 4521, while making material X, on shift B. The stop lasted 12 minutes. The reason was a jam at station 2. It's the third time that reason has occurred in 48 hours.

Same signal. Completely different value.

Contextualised data is data that's been enriched with the who, what, when, where, why and how. That's what makes it useful for analysis, decisions and, eventually, AI.

## From signal to decision

The journey looks like this:

1. **Raw signal.** The machine stopped.
2. **Contextualised data.** Which machine, order, product, shift, reason and duration.
3. **KPIs.** OEE, availability, scrap rate, MTBF, energy per piece.
4. **Dashboards.** What's happening now, and what happened last shift, last week, last month.
5. **Decisions.** Replace the tool causing 40% of rejects on Machine 3. Change the maintenance interval on Line 7. Look at why Friday nights underperform.

Each step adds meaning. And each step depends on the one before it. You can't calculate a trustworthy OEE from signals nobody has put in context.

## Where context comes from

On the shopfloor, context comes from the system that knows what's *supposed* to be happening: the production order, the material, the routing, the operator, the quality plan.

That's [MES/MOM](/post/what-is-mes-and-why-is-it-important-in-manufacturing). It's the central hub of contextualised operational data, sitting between ERP above and the machines below. It takes the raw signal and attaches everything around it.

## Where context gets lost

This is where I get opinionated.

The broader the scope of MES/MOM, the richer the context. Production, quality, inventory and maintenance overlap constantly:

- A quality failure links to the production order, the raw material lot and the process parameters at the time.
- A machine stop matters to production, maintenance and planning.
- Material consumption ties to equipment performance and yield.
- A tool change explains a shift in dimensions on the parts that followed.

When those live in one application, every piece of data carries all of that context automatically.

When they're spread across separate systems and integrated, you lose some of it at every boundary. You can't pass everything through an integration, so you pass a subset. The quality system knows a sample failed, but not what the machine was doing. The CMMS knows a fault was logged, but not that the line was mid-changeover.

Integrating separate applications nearly always loses some context. A well-designed unified namespace or integration layer can carry more of it, but someone has to model that context and keep it consistent. In a single platform it's there by default. I compare the approaches in [Code, build, stitch or configure](/post/build-vs-buy-mes).

## Context is what AI really needs

Everyone wants AI on the shopfloor. Very few have the data to feed it.

Machine learning models learn from patterns. Give them context-free signals and the patterns they find are shallow. Give them stops linked to products, shifts, materials, maintenance history and quality outcomes, and they can start to find causes, not just correlations.

That's why I see MES/MOM as the foundation for AI, not a competitor to it. It creates the contextualised data set that makes AI worth doing.

## Where the data lives after that

Not all data lives in MES/MOM forever. High-frequency signals often sit in a historian. Analytics and AI teams often work from a data lake or data platform that pulls from MES/MOM, ERP and other sources. I explain how those fit together in [Historians, data lakes and data fabric](/post/manufacturing-data-platforms).

But the context is created at the point of work. If it isn't captured there, no data platform downstream can invent it later.

How much of the data in your factory today would pass the "Machine 3 on Line 7" test?
