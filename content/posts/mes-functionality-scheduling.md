---
title: "MES functionality: production scheduling"
short: "Production scheduling"
description: "How production orders flow from ERP into MES/MOM, how schedulers sequence and release them, and when a dedicated APS is worth adding."
published: 2023-05-10
updated: 2026-10-25
category: education
art: gantt
series: functionality
order: 2
---

Production scheduling turns a plan into work the shopfloor can run. MES/MOM plays a central part in that, by giving schedulers and operators a live view of what's planned and what's actually happening.

The initial schedule usually comes from ERP. ERP looks at customer demand and stock levels, works out which semi-finished and finished goods need making, and creates production orders with a first view of priority. Those orders are then passed to MES/MOM, where the sequence and the equipment can be fine-tuned. How much scheduling an MES offers varies widely between products.

Where scheduling itself is complex, a dedicated APS (advanced planning and scheduling) system may be added.

## Who does what

| | ERP | MES/MOM | APS |
| --- | --- | --- | --- |
| **Main job** | Create orders from demand and stock | Sequence and execute orders | Build detailed, constraint-based schedules |
| **Horizon** | Weeks to months | Shifts to minutes | Days to hours |
| **Capacity** | Mostly simplified | Real, as it is now | Finite, with constraints |
| **Output** | Orders and due dates | Dispatched jobs and actuals | Optimised sequence |

The full comparison, including the options for connecting them, is in [APS vs ERP scheduling](/post/aps-vs-mes-scheduling).

## How scheduling works in MES/MOM

### Downloading orders from ERP

MES/MOM receives production orders from ERP, with the routing and bill of materials behind each one. That keeps the schedule aligned with the materials and resources it needs. You'll hear production orders called works orders or manufacturing orders, depending on the product and the industry. More on the data involved in [Your ERP master data isn't ready for MES](/post/erp-master-data-for-mes).

### Viewing and adjusting the schedule

Schedulers see the schedule in real time and can change the sequence or move orders between machines. Where the sequence must be followed, it can also be locked, so operators can't run orders out of order.

### Allocating resources

MES/MOM allocates equipment, people, materials and tooling to orders, and prevents conflicts. A tool, for example, can only be on one order at a time. More in [MES functionality: tooling](/post/mes-functionality-tooling).

### Releasing orders to the shopfloor

Once the schedule is agreed, orders are released to the line. Operators see what's next, with its priority and any instructions, and other teams such as maintenance and tooling can plan around it. When the schedule changes, operators see it straight away, with no paperwork to reprint.

## Do you need an APS?

Not every manufacturer needs one. An APS is for more advanced scheduling with complex constraints. Where production is stable and changeovers don't drive the sequence, the scheduling in ERP, or an extra ERP module, alongside MES/MOM is often sufficient.

An APS earns its place when sequencing becomes the hard problem:

- Shared bottlenecks that many orders compete for
- Sequence-dependent changeovers, such as light to dark colours or allergen-free before allergen
- Large numbers of orders changing every day
- Tools or moulds shared across several machines

## Why a live schedule matters

A printed schedule is out of date almost as soon as it's printed. A live schedule shows when a machine goes down or an order runs late, so the planner knows straight away rather than at the end of the shift.

It also works the other way. MES/MOM records actual cycle times and changeover durations, and feeding those back makes each new plan more realistic. More in [Takt time vs cycle time vs lead time](/post/takt-time-vs-cycle-time-vs-lead-time).

## What it delivers

- **Visibility and control:** schedulers see delays as they happen, and operators see changes as soon as they're made.
- **Better use of resources:** workloads are balanced and conflicts over equipment or tools are avoided.
- **On-time delivery:** problems surface early enough to recover, which protects lead times and customer commitments.
- **Agility:** rush orders and disruptions can be absorbed without rebuilding the plan by hand.

## Things to check

Scheduling capability varies a lot between MES products. Some build it into the core application, while others provide it separately, through their own module or a partner's tool. Where it's separate, an interface carries schedule changes between systems, so check how quickly changes flow in each direction.

## My view

In my experience, a schedule built on actual cycle times rather than old standards does more for the floor than a cleverer algorithm.

This article is part of the [MES functionality in depth](/paths/mes-functionality) learning path. Related: [The smart factory tech stack](/post/smart-factory-tech-stack).

When did your schedule last survive a whole shift unchanged?
