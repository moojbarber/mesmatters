---
title: "Digital twins run on shopfloor data. MES/MOM is where it comes from"
short: "MES/MOM and digital twins"
description: "A digital twin is only as good as the data feeding it. MES/MOM is the key source of real-time, contextualised shopfloor data that keeps a twin honest."
published: 2026-10-16
updated: 2026-10-20
category: thought-leadership
art: bins
---

Digital twins are one of the most exciting ideas in manufacturing right now. Test a change virtually before you touch the line. Plan capacity on a model that behaves like the real factory. Spot problems before they happen.

But a twin is only as good as the data feeding it. And for most of what happens in a factory, that data comes from MES/MOM.

## What is a digital twin?

A digital twin is a virtual model of a physical asset, process or entire factory, kept in sync with the real thing through live data, and used to understand, predict or optimise how it behaves.

There are different flavours. A twin of a single machine, used by engineers to model wear or tune performance. A twin of a production process, used to test changes before making them. A twin of a whole factory, used to plan layouts, capacity and investments.

Most serious definitions share three ingredients:

- **A model** of the physical thing: its structure, behaviour and constraints.
- **A live connection** that keeps the model in step with reality.
- **A purpose**: simulation, prediction or optimisation that helps someone make a better decision.

MES/MOM isn't the model, and it doesn't do the simulation. What it does is supply much of the live connection, in a form the model can actually use.

## Why MES/MOM matters to a twin

Think about what a well-implemented [MES/MOM](/post/what-is-mes-and-why-is-it-important-in-manufacturing) knows at any moment:

- Every line and machine, and its current state: running, stopped, in changeover
- Which order is running where, and how far through it is
- Every lot of material, where it is, what state it's in and what it was made from
- Every quality result, linked to the product and process conditions at the time
- The condition and maintenance status of each asset
- Who is working where, and what they're qualified to do

That's real-time operational data, already in context. Not just "machine 7 stopped", but which order was running, on which shift, with which material, for how long and why. A twin needs exactly that to stay true to the factory it represents.

Sensors and historians give a twin the physics: temperatures, pressures, speeds. PLM gives it the product and process design. MES/MOM gives it the operational reality: what's being made, where, by whom, how well, and what got in the way.

## What the twin adds on top

Where a digital twin goes further is the model and the simulation. Running what-if scenarios before you change anything in the real world:

- What happens to throughput if we add a second shift on Line 2?
- Where's the new bottleneck if we speed up the filler by 10%?
- Should we buy another press, or fix the changeovers on the ones we've got?
- What does next month's schedule look like if this order slips a week?

That's where I find the future genuinely exciting. Data-driven decisions about investments, layouts and schedules, tested virtually first, instead of argued over in a meeting.

## Simulation is only as good as the data behind it

A simulation built on assumed cycle times, estimated downtime and a theoretical capacity model will give you very confident, very wrong answers.

The value comes from a twin that's fed by reality. Actual cycle times by product. Actual downtime patterns by machine and shift. Actual scrap rates. Actual changeover durations.

Which brings us back to the data foundation. MES/MOM, historians, connected equipment and data platforms feeding the twin with a live, accurate, contextualised picture. Build that, and simulation becomes trustworthy. Skip it, and your twin is a very attractive guess.

## Get the data flowing before you build the twin

I'm wary of digital twin projects that start with the visualisation. The 3D model looks impressive in the boardroom. But if the data behind it is typed in at the end of each shift, it's a nice picture of a factory that doesn't really exist.

Start with the data source you probably already need: MES/MOM capturing what's actually happening, accurately and in context. Then build the twin on top of it, aimed at a real decision you need to make.

Is there a decision coming up in your factory that you'd love to test virtually before committing to it?
