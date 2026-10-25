---
title: "APS vs ERP scheduling: when ERP is enough, and where MES fits"
short: "APS vs ERP scheduling"
description: "ERP plans, APS sequences against real capacity, and MES/MOM dispatches and feeds back actuals. When ERP scheduling is enough, and where each one fits."
published: 2026-09-10
category: education
art: gantt
---

Every factory has a plan. Every factory also has what actually happened on the shift. The gap between the two is where a lot of money goes.

Most of the scheduling debate is really about ERP and APS. ERP plans; APS sequences against real capacity. MES/MOM mostly takes the orders once they've been scheduled and dispatches them, with some basic short-interval scheduling of its own.

The confusion usually starts with the word "schedule" meaning something different in each one.

## Different horizons, different jobs

**ERP** plans in weeks and months. MRP works out what to make and buy, and when, against demand. It mostly assumes infinite capacity, or uses rough-cut checks. Output: planned and released production orders with due dates.

**APS** (Advanced Planning and Scheduling) sequences in days and hours. It takes those orders and builds a finite-capacity schedule: which order on which machine, in what sequence, respecting changeovers, tooling, labour and material availability.

**MES/MOM** dispatches in minutes. It tells the line what to run *now*, records what actually happened, and reacts when reality doesn't match the plan: a breakdown, a quality hold, a missing component, an absent operator.

| | ERP | APS | MES/MOM |
| --- | --- | --- | --- |
| Horizon | Weeks to months | Days to hours | Shift to minutes |
| Capacity | Mostly infinite | Finite, constraint-based | Real, as it is right now |
| Output | Orders and due dates | Sequenced schedule | Dispatched jobs, actuals |
| Key question | What and when? | In what order, where? | What next, and what happened? |

## When is ERP scheduling enough?

More often than people expect. With a handful of lines, stable products and simple changeovers, ERP's scheduling plus a dispatch list in MES/MOM can cover most needs.

APS earns its keep when sequencing is genuinely hard: sequence-dependent changeovers (light to dark colours, allergen-free before allergen), shared tools or moulds, multi-stage processes where one bottleneck drives everything, or hundreds of orders a day competing for the same resources.

Many ERP suites include APS capability, so it may be a module you already own rather than another system.

## Where the scheduling logic lives

There are several ways to split the work:

- **ERP schedules, MES/MOM dispatches.** Simplest. ERP releases orders in priority order, MES/MOM shows them to the line and supervisors adjust on the day.
- **APS schedules via ERP.** ERP sends orders to APS, APS sequences them, the sequence comes back to ERP and down to MES/MOM. ERP stays the single path to the shopfloor.
- **APS schedules, with a direct link to MES/MOM.** ERP sends orders to APS. APS sends the sequence straight to MES/MOM and receives actuals straight back, so it can reschedule within the shift. ERP still gets order status and confirmations.
- **Short-interval scheduling in MES/MOM.** Some MES/MOM platforms include detailed scheduling for the shopfloor horizon. Good for plants where the main problem is the next 24 hours, not next week.

Each is valid. The direct APS link suits plants that reschedule several times a shift, where the round trip through ERP is too slow. Plants that reschedule once a day often use the simpler options.

Whichever option you choose, one system needs to own the sequence. If APS publishes a schedule and supervisors re-sequence in MES/MOM, the other system has to be told.

## The feedback loop

A schedule is only as good as the data it's built on. And most plans are built on standard cycle times and setup times that nobody has checked in years.

MES/MOM knows the real numbers. Actual cycle times by product and machine. Actual changeover durations. Real availability after breakdowns and micro-stops. Real yield.

Fed back, those numbers improve the plan over time. Without them, planners keep building schedules from outdated standards, and supervisors tend to stop trusting the schedule and run the line from a whiteboard.

## Where MES/MOM fits

MES/MOM doesn't need to be your planning system. Its job is dispatch and feedback. It shows the line what to run next from the scheduled orders, and reports what actually happened so the next plan is better.

Whatever sits upstream, the operator needs a clear answer to one question: what do I run next? Plus the reason, if it changed. A dispatch list in MES/MOM, sequenced by the plan, updated when the plan changes, with the materials and tooling status visible.

## My view

What I'd avoid is two systems both believing they own the sequence. In my experience, the feedback loop is worth more than any optimisation algorithm. A simple scheduler with honest data beats a clever one working from fantasy standards.

So, when did someone last compare your planned setup times to the actuals?
