---
title: "ERP, APS and MES scheduling: the plan versus the shift"
short: "APS vs MES scheduling"
description: "ERP plans, APS sequences and MES/MOM executes. Where scheduling belongs in each system, the options for connecting them, and how to keep the plan honest."
published: 2026-09-10
category: education
art: gantt
---

Every factory has a plan. Every factory also has what actually happened on the shift. The gap between the two is where a lot of money goes.

Scheduling sits across three systems, and the confusion usually starts with the word "schedule" meaning something different in each one.

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

## Do you need APS at all?

Honestly, often not. If you have a handful of lines, stable products and simple changeovers, ERP's scheduling plus a good dispatch list in MES/MOM gets you a long way.

APS earns its keep when sequencing is genuinely hard: sequence-dependent changeovers (light to dark colours, allergen-free before allergen), shared tools or moulds, multi-stage processes where one bottleneck drives everything, or hundreds of orders a day competing for the same resources.

Many ERP suites include APS capability, so it may be a module you already own rather than another system.

## Where the scheduling logic lives

This is the decision that matters. You have options:

- **ERP schedules, MES/MOM dispatches.** Simplest. ERP releases orders in priority order, MES/MOM shows them to the line and supervisors adjust on the day.
- **APS schedules via ERP.** ERP sends orders to APS, APS sequences them, the sequence comes back to ERP and down to MES/MOM. ERP stays the single path to the shopfloor.
- **APS schedules, with a direct link to MES/MOM.** ERP sends orders to APS. APS sends the sequence straight to MES/MOM and receives actuals straight back, so it can reschedule within the shift. ERP still gets order status and confirmations.
- **Short-interval scheduling in MES/MOM.** Some MES/MOM platforms include detailed scheduling for the shopfloor horizon. Good for plants where the main problem is the next 24 hours, not next week.

Each is valid. The direct APS link pays off when you reschedule several times a shift and the round trip through ERP is too slow. If you reschedule once a day, keep it simple.

What I'd avoid: two systems both believing they own the sequence. If APS publishes a schedule and supervisors re-sequence in MES/MOM, someone needs to decide whose version wins, and the other system must be told.

## The feedback loop is the point

A schedule is only as good as the data it's built on. And most plans are built on standard cycle times and setup times that nobody has checked in years.

MES/MOM knows the real numbers. Actual cycle times by product and machine. Actual changeover durations. Real availability after breakdowns and micro-stops. Real yield.

Feed those back, and the plan gets better every week. Ignore them, and the planners keep building schedules that the shopfloor knows are fiction. Then supervisors stop trusting the schedule and run the line from a whiteboard.

In my experience, that feedback loop is worth more than any optimisation algorithm. A simple scheduler with honest data beats a clever one working from fantasy standards.

## What the operator needs

Whatever sits upstream, the operator needs a clear answer to one question: what do I run next? Plus the reason, if it changed. A dispatch list in MES/MOM, sequenced by the plan, updated when the plan changes, with the materials and tooling status visible.

So, when did someone last compare your planned setup times to the actuals?
