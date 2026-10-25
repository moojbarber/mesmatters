---
title: "How MES takes complexity out of your ERP"
short: "How MES simplifies ERP"
description: "ERP wasn't built to run a shopfloor. Where the line between MES and ERP should sit, and how moving execution into MES/MOM simplifies ERP and improves its data."
published: 2023-08-02
updated: 2026-10-25
category: advice
art: bridge
---

Many manufacturers try to run more and more of the shopfloor through ERP. It seems logical: one system, one set of data. In practice it often adds complexity to ERP, through customisation and workarounds, without giving the shopfloor what it needs.

Putting manufacturing execution into MES/MOM, alongside ERP, usually simplifies ERP and improves the data it holds. This article explains why.

## What each system is built for

ERP manages and integrates the core business: finance, sales, purchasing, planning and inventory valuation. It gives the organisation one platform for business data, and it's the backbone of most manufacturers. More in [What is ERP?](/post/what-is-erp)

MES/MOM is built to run manufacturing operations. It captures data from the shopfloor as things happen, and guides operators through the work. It sits between ERP and the equipment. More in [What is MES/MOM?](/post/what-is-mes)

| | ERP | MES/MOM |
| --- | --- | --- |
| **Main job** | Run the business | Run the shopfloor |
| **Level of detail** | Orders and costs | Every event and measurement |
| **Time scale** | Days and weeks | Seconds and minutes |
| **Main users** | Office teams | Operators and supervisors |
| **Data volume** | Moderate, transactional | High, from machines and the line |

## Why ERP struggles on the shopfloor

ERP is excellent at business processes, but it isn't designed for the granular, real-time detail the shopfloor needs. Forcing it to cope usually means custom code and workarounds, which make ERP harder to maintain and upgrade.

User experience suffers too. ERP screens are designed mainly for office users, not for an operator wearing gloves at a machine.

The shopfloor is fast-moving, with many machines and people working together. Capturing what happens there, from machine status to material consumed by lot, needs a system built for real time. That's the job MES/MOM is designed for.

## The shift towards a focused ERP

Expectations of ERP have changed. Gartner's idea of "composable ERP" describes ERP as a strong core that integrates with specialist applications, rather than trying to do everything itself.

That creates room for MES/MOM to take on shopfloor execution. Moving those functions out of ERP can simplify ERP deployments and roll-outs, and lower its cost of ownership.

It also means choosing the right application for each area. Some vendors offer both ERP and MES/MOM, and many manufacturers successfully run ERP from one vendor and MES/MOM from another. Either way, the integration between them deserves careful attention:

- **Building and maintaining the interface.** Orders, master data, confirmations, consumption and stock movements all have to flow reliably, in both directions, for years.
- **Upgrades.** Every upgrade on either side means retesting the integration, and the two roadmaps won't always line up.
- **Ownership when something breaks.** When a confirmation goes missing, someone has to own the problem end to end.
- **Master data alignment.** Materials, BOMs, routings and units of measure have to mean the same thing in both systems.

Standard integrations from a single vendor can remove much of that effort. Where the systems come from different vendors, standard interfaces and an experienced integration partner do the same job. More in [integration patterns](/post/isa95-integration-patterns) and [Your ERP master data isn't ready for MES](/post/erp-master-data-for-mes).

## MES removes the need for ERP extensions

Bridging ERP's shopfloor gaps often means custom extensions. They're costly to build and maintain, and they add risk at every upgrade.

With MES/MOM alongside ERP, both systems can run closer to their standard functionality. Where a manufacturing process does need something specific, MES/MOM is the natural place for it, because it owns that process. MES/MOM platforms are usually designed to be configured for different processes, which makes changes quicker than in ERP. See [Configure, don't customise](/post/configure-dont-customise).

## ERP keeps the data it needs, and often gets better data

A common worry is that ERP loses visibility of production volumes or quality results once MES/MOM is in place. In practice ERP keeps at least the same information it had before, because MES/MOM keeps it up to date.

MES/MOM handles the high-volume, detailed data, and sends ERP what it needs, often aggregated, which also reduces the transaction load on ERP.

The quality of ERP data usually improves:

- **Actuals rather than estimates.** MES/MOM posts actual consumption and output, rather than backflushed standard quantities.
- **More accurate costing.** Real machine time and material usage replace estimates, so product costs reflect what actually happened.
- **Timely updates.** Production is confirmed as it happens, rather than keyed in at the end of a shift.
- **Supplier quality.** Inspection results on incoming material can flow back to ERP, for example where they affect what a supplier is paid.

## An analogy: the menu and the fitness app

Reading the calories on a restaurant menu is like ERP on the shopfloor. It's useful, high-level information, and for some people that's enough.

Logging everything you eat and tracking trends over time is like MES/MOM. It works at a far greater level of detail.

ERP can tell you that you made 1,000 widgets yesterday. MES/MOM can tell you that widget 847 failed its quality check at 14:32, and what needs to happen next. Manufacturing execution happens in seconds and minutes, which is why the shopfloor needs a system built for it.

## Where to draw the line

A few questions help decide where a function belongs:

- Who uses it: people in the office, or people on the shopfloor?
- How fresh does the data need to be: overnight, or right now?
- Does it need context from the machine or the operator?
- Does it need more detail than the business needs for costing and planning?

The more answers point to the shopfloor, the more the function belongs in MES/MOM. More in [MES vs ERP](/post/mes-vs-erp).

## My view

I'm a fan of ERP. ERP and MES/MOM complement each other: ERP provides the plan, and MES/MOM executes it and feeds back the reality. What I'd avoid is asking ERP to run the shopfloor. You'd never use an MES to do the job of an ERP, so why use an ERP to do the job of an MES? Getting that boundary right simplifies ERP and gives it better data.

How much custom code in your ERP exists only to handle the shopfloor?
