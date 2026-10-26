---
title: "What is MES/MOM? A guide to MES and manufacturing operations management"
short: "What is MES/MOM?"
description: "MES runs production. MOM runs the whole operation, from production and quality to inventory and maintenance, on the same data. What each one covers."
published: 2022-08-01
updated: 2026-10-25
category: education
art: hexcore
start: 1
---

MES and MOM are often used interchangeably, on vendor websites and in conversation. Strictly, they describe different scopes, and the difference matters most when you decide what to buy.

This guide explains what each term means, and what MES/MOM does for a factory.

## MES: the production pillar

MES stands for manufacturing execution system. It's the original term, and still the one most people search for.

At its core, MES is about **production execution**: getting the right order onto the right line, then recording what actually happened. In practice that means:

- Receiving the production schedule from ERP, and fine-tuning the sequence on the shopfloor
- Starting and stopping production orders, including changeovers and setup
- Recording good counts and downtime, ideally straight from the equipment
- Calculating [OEE](/post/what-is-oee) and the measures that sit underneath it
- Guiding operators with digital work instructions
- Sending confirmations back to ERP, with actuals rather than estimates

For a factory running on paper travellers and end-of-shift spreadsheets, real-time production data on its own changes how the plant runs. Short stops that were never recorded become visible for the first time.

## MOM: the whole operation

MOM stands for manufacturing operations management. The term exists because the scope grew beyond production.

ISA-95, the international standard for how business and shopfloor systems fit together, splits manufacturing operations into four areas. MOM covers all four:

- **[Production](/post/mes-functionality-production):** executing orders, counts, scrap, downtime and OEE.
- **[Quality](/post/mes-functionality-quality):** inspection plans, in-line checks, SPC, non-conformance and holds.
- **[Inventory](/post/mes-functionality-inventory):** consumption, labelling, work in progress, [logistics](/post/mes-functionality-logistics) and traceability.
- **[Maintenance](/post/mes-functionality-maintenance):** asset care, from autonomous maintenance by operators to planned work.

The broadest platforms go further, into tooling, energy, labour and skills, and connected worker capabilities such as checklists and shift handover. The full list is in the [MES functionality guide](/post/mes-functionality-guide).

| | MES | MOM |
| --- | --- | --- |
| **Scope** | Production execution | Production, quality, inventory and maintenance |
| **Main users** | Operators and production supervisors | Everyone in operations, including quality, logistics, maintenance and planning |
| **Answers** | What did we make, and how well? | What's happening across the whole operation, and why? |
| **Data** | Counts, scrap, downtime, OEE | The same, connected to inspections, material, traceability and asset condition |

More on the difference in [MES vs MOM](/post/mes-vs-mom).

## Why scope matters: shared data

The practical difference between an MES and a MOM platform is whether everyone in operations works from the same data.

Many concerns overlap between departments. Production and maintenance both care about downtime. If they record it in separate systems, meetings can start with a debate about whose numbers are right. Quality needs to know what's being made, and from which batch of raw material. Inventory needs to know whether that batch has passed inspection before it moves. Planning needs to know a line is down before the schedule goes stale.

The operator sits in the middle. They run the order, perform the quality check, consume the material and do the autonomous maintenance, often within the same ten minutes.

When all of that lives on one platform:

- The downtime production sees is the downtime maintenance sees
- Quality checks are triggered by what's actually being produced, with no re-keying of order or material details
- Traceability links every lot to its inspection results and the process parameters at the time
- The operator works in one application, with one login

## One platform or several?

The alternative is a separate product for each pillar, integrated together: an OEE tool for production, a quality system, inventory in ERP or a WMS, and a CMMS for maintenance.

Separate systems can offer more depth in one area, and each can be bought on its own timeline. A complex warehouse may need a WMS, and a heavy asset business a full EAM.

The trade-offs:

- **Context is lost at each boundary.** Integrations usually pass only a subset of the data, so the quality system may not know which order was running.
- **Integrations need maintaining.** They take time to build and need retesting whenever either side upgrades.
- **Operators may juggle applications.** Different logins and screens for related tasks.
- **Data can diverge.** Two systems can hold different versions of the same downtime or stock.

## Where MES/MOM sits

MES/MOM sits at level 3 of the [ISA-95 model](/post/isa-95-explained). ERP sits above it, running the business: orders, finance, procurement and planning. The automation layer sits below it: PLCs and the machines themselves.

Orders and master data flow down. Actual consumption, counts, scrap and quality results flow back up, aggregated to the level ERP needs. MES/MOM doesn't compete with ERP. ERP receives validated actuals rather than backflushed estimates, which makes its data better. More in [MES vs ERP](/post/mes-vs-erp) and [How MES takes complexity out of your ERP](/post/mes-simplifies-erp).

## Life before MES/MOM

Most factories already have some form of MES/MOM. It just isn't software.

It's paper travellers and whiteboards, Excel spreadsheets, a departmental database someone built years ago, and ERP screens pushed onto the shopfloor where they were never designed to be. Each piece manages part of the operation, but none of them talk to each other. The knowledge that holds it together lives in people's heads.

## What MES/MOM delivers

- **Real-time visibility.** What's running and what's stopped on every line, now rather than at the end of the shift.
- **Error-proofed processes.** MES/MOM validates as work happens: the wrong material can't be consumed, and a missed check gets flagged.
- **Traceability and compliance.** Forward and backward traceability, with the audit trail built in rather than assembled after a complaint.
- **Better ERP data.** Actuals rather than assumptions, synchronised at the right level of detail.

Who benefits, role by role, is covered in [Who benefits from MES?](/post/who-benefits-from-mes) and the [role explorer](/roles/).

## The foundation for AI

AI and machine learning need accurate, contextualised data collected over time. A machine signal that says "stopped" means little on its own. MES/MOM turns it into "Line 7 stopped at 14:23 during order 4521, on night shift, for 12 minutes, because of a jam at station 2, for the third time in 48 hours." That's data a model can learn from.

The broader the scope, the richer the context. Quality results linked to process parameters and maintenance history are the data that predictive quality and predictive maintenance are built on. More in [AI will transform your factory, if you give it the right data](/post/ai-needs-shopfloor-data)

## Which term should you use?

Use whichever your audience understands. MES is still the more common search term.

On this site, **MES** means production execution and **MOM** means the whole operation. **MES/MOM** refers to the category. When buying, the scope matters more than the label: ask whether you're getting the production pillar, or a platform that puts production, quality, inventory and maintenance on the same data.

## My view

I've used the terms interchangeably myself for years, but the distinction is worth being deliberate about. The most expensive mistake I see is drifting into four or five point solutions because each one solved a single problem quickly. Dedicated systems should be deliberate choices about depth. A cheap stop-gap is rarely cheap by the time it's integrated.

Which one is your factory actually running on today?
