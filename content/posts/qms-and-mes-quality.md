---
title: "QMS and MES: closing the quality loop"
short: "QMS and MES quality"
description: "A good MOM does everything a standalone QMS does, with the production context a QMS never has. Why a separate QMS is almost always the wrong choice, and how to close the quality loop."
published: 2026-09-15
category: education
art: badge
---

Quality often lives in more than one system. The problem comes when a defect found on the shopfloor never makes it into the process that's meant to stop it happening again. Sometimes that's because quality has been split between an MES on the line and a separate QMS in the office.

## What a standalone QMS does

A **QMS** (Quality Management System) handles quality processes across the business, over weeks and months, and across sites and suppliers:

- CAPA (corrective and preventive action)
- Customer and supplier complaints
- Audits and certifications
- Document control and training records
- Supplier quality and approvals

## A good MOM does all of that, and more

A good MES/MOM covers everything a standalone QMS does: CAPA, customer and supplier complaints, sampling, SPC, non-conformances and audits.

On top of that, it has something a QMS never has: the context. It knows which order, material, lot, machine and operator every result relates to, because it's running the production. And it can use the rest of the MOM data to trigger quality checks from other events, such as an order starting, a tool change, a new lot of material or a process parameter drifting. I cover that in [QMS vs LIMS vs MES](/post/qms-vs-lims-vs-mes).

**ERP** handles the business consequences of quality: stock status (available, blocked, in inspection), supplier returns, scrap cost and the money side of a complaint. Serious non-conformances escalate into ERP, where the cost, supplier and customer sides already live.

I covered shopfloor quality in [MES functionality: quality operations](/post/mes-functionality-quality), and SPC in [SPC on the shopfloor](/post/spc-on-the-shopfloor).

## Why a standalone QMS is almost always the wrong choice

- **It's a poor experience for the operator.** They run the order in MES, then switch to the QMS to record a check or a defect, with a different login, different screens, and the order details typed in again. It slows them down, and it's where mistakes creep in.
- **Context gets lost at the boundary.** The QMS only knows what the interface sends it. The measurements, the machine settings and the photo often stay behind.
- **Checks can't follow what's happening.** A QMS can't see a tool change or a new lot arrive, so it can't trigger the right check at the right moment.
- **Holds get out of step.** If quality blocks a lot in the QMS and the line doesn't know, the line will happily consume it.
- **You pay twice.** Licences, upgrades and an interface to maintain, for capability your MOM already has.

## Where the loop breaks

A typical story goes like this. An operator finds a defect. They record it in MES, scrap the part and carry on. A week later, quality runs a report in the QMS, spots a trend and raises a CAPA. The CAPA team asks for details. Nobody can remember which shift, which lot, which machine or which operator.

The information existed. It just didn't travel.

With quality inside the MOM, the loop looks different:

1. The non-conformance is recorded once, at the source, with full context: order, operation, lot, machine, operator, measurements and photo.
2. Rules decide what happens next. One-off scrap stays where it is. A repeat defect, a critical characteristic or a customer-impacting issue raises a CAPA automatically, and escalates into ERP where there's a cost, supplier or customer impact.
3. The investigation and actions work from the same record the operator created, so the team investigating sees exactly what happened on the line.
4. Actions that change the process come straight back to the line: a new inspection, a tighter limit, a revised instruction.

## If you already have a QMS

If a QMS is already in place, connect it directly to MES/MOM, so non-conformances arrive with their full context, and send stock status changes through ERP, because ERP must know what's blocked.

Whichever way it's wired, one rule applies: when a lot goes on hold, every system that could move or consume it must know immediately. Decide which system raises the hold, and make sure it reaches ERP, MES/MOM and any [WMS](/post/wms-vs-mes-inventory) in minutes, not at the next batch interface run.

## Don't forget the documents

Work instructions, specifications and inspection plans need approving, and the operator needs to see the approved revision for this order, not a copy someone saved locally in 2023.

The best option is a central document repository that every application can access. Each document is stored once, tagged by product, revision and operation, and read by MES/MOM, ERP and PLM alike. Nobody maintains two copies, and every system sees the same approved version.

## My view

A standalone QMS is almost always the wrong choice. A good MOM does everything it does, with the production context it will never have, and the operator works in one system instead of two. Escalate serious non-conformances into ERP for the business side, and you have a closed loop with nothing to stitch together.

If you run an MES that covers production only, it can feed a separate QMS, and that works. But it's a compromise, and a full MOM is the better overall solution.

When a CAPA concludes "retrain operators", how do you prove the retraining happened before that operator next ran the job? That's where [skills you can enforce](/post/skills-enforcement-shopfloor) close the loop.
