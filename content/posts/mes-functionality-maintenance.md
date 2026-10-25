---
title: "MES functionality: maintenance"
short: "Maintenance"
description: "Why maintenance belongs on the same platform as production: shared downtime data, and when a separate CMMS or EAM still makes sense."
published: 2026-05-14
category: education
art: gates
series: functionality
order: 7
---

Maintenance rarely gets much attention until something breaks. By then you've lost capacity, disrupted the schedule and you're scrambling to fix something that could probably have been prevented.

Downtime is usually the biggest loss in [OEE](/post/what-is-oee). For most manufacturers it's the single largest area for improvement. That makes maintenance one of the most valuable pillars of MOM, and one of the most overlooked.

## What maintenance covers in MES/MOM

- **Equipment and asset hierarchy.** Sites, areas, lines, machines and their components, structured so data rolls up properly.
- **Fault reporting.** Operators raise issues from the screen they already use, linked to the machine and the order that was running.
- **Work orders.** Corrective, preventive and condition-based, with tasks, parts and sign-off.
- **Planned maintenance.** By time, by cycle count, or by condition, scheduled around production rather than against it.
- **Autonomous maintenance.** Cleaning, lubrication, inspections and checks carried out by operators.
- **Maintenance KPIs.** MTBF (mean time between failures) and MTTR (mean time to repair) by asset, line and reason.

## Production and maintenance need the same data

This is the main reason I believe maintenance belongs in MOM.

Production and maintenance both care about downtime. If production records stops in one system and maintenance logs faults in another, they'll disagree about what happened. How can you have a productive morning meeting when the two teams can't even agree on how long the machine was stopped?

When both work in the same platform:

- The stop production sees is the fault maintenance sees, with the same duration and reason.
- Maintenance can see the production schedule and plan repair windows around it.
- Production can see upcoming planned work and prepare for it.
- Every repair is linked to the stops it fixed, so you can tell whether it worked.

## Operators are part of maintenance now

Day-to-day asset care is increasingly the operator's job. That's a good thing. Operators notice problems first.

But it means operators need, in the same place they run production:

- Their autonomous maintenance tasks, at the right time
- The upcoming planned maintenance on their equipment
- Issues already logged against their assets, so they don't log them twice
- A fast way to raise a new fault, with photos if needed

If that sits in a separate CMMS, it's another login and another screen. Most of the time, it simply won't get used.

## When a dedicated CMMS or EAM makes sense

I'm not saying you never need one.

A full EAM (Enterprise Asset Management) system makes sense for asset-heavy businesses with advanced needs: complex spare parts management, reliability engineering, linear assets, regulatory asset records across many sites.

My advice:

- Choose an MES/MOM with maintenance capabilities for most manufacturers.
- Only choose a dedicated CMMS or EAM if you have advanced use cases that genuinely need it. If you do, draw the boundary carefully, so operators and production still see downtime and maintenance status in MES/MOM.

## The step towards predictive maintenance

Getting maintenance onto the same data as production is also the foundation for condition-based and predictive maintenance. Models need failure history, condition data and operating context together. I cover the journey in [Predictive maintenance needs data you aren't collecting yet](/post/predictive-maintenance-data).

This article is part of the [MES functionality series](/post/mes-functionality-guide).

Do your production and maintenance teams agree on last week's downtime?
