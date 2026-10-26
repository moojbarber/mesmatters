---
title: "OEE vs OOE vs TEEP: which measure answers which question"
short: "OEE vs OOE vs TEEP"
description: "OEE, OOE and TEEP use the same losses against different amounts of time. What each one measures, how to calculate them, and when to use which."
published: 2026-08-05
category: education
art: rings
---

OEE gets most of the attention. It answers one specific question: how well did we use the time we *planned* to run?

Ask a different question, such as how much capacity is hiding in the hours we don't run at all, and you need a different measure. That's where OOE and TEEP come in.

## They all share the same core

All three multiply availability, performance and quality. Performance and quality are calculated exactly the same way in each. What changes is the time you measure availability against.

I explain the calculation itself in [What is OEE?](/post/what-is-oee). This article is about the time base.

## Three time bases

Think of a week as a stack of time:

- **Calendar time.** Every hour there is: 24 hours a day, 7 days a week.
- **Operating time.** The hours the factory is open and staffed.
- **Planned production time.** Operating time minus planned stops such as breaks, meetings, trials and planned maintenance.

Each measure uses a different layer as its baseline.

| Measure | Availability measured against | Question it answers | Typical use |
| --- | --- | --- | --- |
| **OEE** | Planned production time | How well do we run when we plan to run? | Daily improvement on the line |
| **OOE** (overall operations effectiveness) | Operating time | How well do we use the hours we're open, planned stops included? | Challenging planned stops |
| **TEEP** (total effective equipment performance) | Calendar time | How much of the asset's total possible time is productive? | Capacity planning and investment decisions |

Because the baseline grows each time, the numbers fall as you go down the table. A line can show a healthy OEE and a much lower TEEP, simply because it only runs two shifts a day, five days a week.

## A quick example

Take a line that's open 80 hours a week, has 8 hours of planned stops, and runs 60 of the remaining 72 hours. Assume performance and quality are both 90%.

- **OEE availability** = 60 ÷ 72 = 83%. OEE = 0.83 × 0.9 × 0.9 = 67%
- **OOE availability** = 60 ÷ 80 = 75%. OOE = 0.75 × 0.9 × 0.9 = 61%
- **TEEP availability** = 60 ÷ 168 = 36%. TEEP = 0.36 × 0.9 × 0.9 = 29%

Same line, same week. Three very different numbers, each one right for its question.

## When to use which

**Use OEE** for day-to-day improvement. It's what operators and supervisors can influence directly, and it's the measure most people recognise. Measure it on the bottleneck.

**Use OOE** when you suspect planned stops have crept up. Long breaks, overrunning meetings, generous changeover allowances and planned maintenance during peak demand all hide inside OEE's baseline. OOE exposes them.

**Use TEEP** when someone asks for a new line or another big capital investment. A low TEEP with a decent OEE often means the capacity already exists, in the hours you don't currently run. Before you buy a new machine, ask whether adding a shift would do the job.

## Getting the data right

All three depend on the same thing: accurate time data. You need to know when the line was running, stopped, in a planned stop or not scheduled at all, and you need the reasons. Recorded from memory at the end of a shift, none of these measures is worth much. Captured automatically by [MES/MOM](/post/mes-functionality-production) from the equipment, they all fall out of the same data.

[ISO 22400](/post/manufacturing-kpis-beyond-oee) defines manufacturing KPIs formally, and is worth using if you compare figures across sites.

What's your TEEP, and has anyone ever asked?
