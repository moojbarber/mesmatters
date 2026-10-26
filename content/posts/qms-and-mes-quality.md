---
title: "QMS and MES: closing the quality loop"
short: "QMS and MES quality"
description: "Enterprise QMS runs CAPA, audits and complaints. MES/MOM runs in-process quality. How they divide the work, where ERP fits, and how to connect them."
published: 2026-09-15
category: education
art: badge
---

Quality lives in more than one system. That's not a problem in itself. The problem is when a defect found on the shopfloor never makes it into the process that's meant to stop it happening again.

## Who does what

**QMS** (Quality Management System) handles enterprise quality processes. They run over weeks and months, and across sites and suppliers:

- CAPA (corrective and preventive action)
- Customer complaints
- Audits and certifications
- Document control and training records
- Supplier quality and approvals

**MES/MOM** handles quality at the point of production. In real time, against the order that's running:

- In-process inspections, triggered by what's actually being made
- SPC on critical characteristics
- Recording non-conformances at the source, with photos
- Holding and releasing lots
- Linking every result to the [as-built record](/post/ebom-mbom-as-built)

**ERP** handles the business consequences of quality. Stock status (available, blocked, in inspection), supplier returns, scrap cost, and quality inspections at goods receipt in many setups. Some manufacturers also run the full CAPA process in ERP, once the details have been passed across from the QMS or MOM platform.

I covered shopfloor quality in [MES functionality: quality operations](/post/mes-functionality-quality), and SPC in [SPC on the shopfloor](/post/spc-on-the-shopfloor).

## Where the loop breaks

A typical story goes like this. An operator finds a defect. They record it in MES/MOM, scrap the part, and carry on. A week later, quality runs a report, spots a trend, and raises a CAPA in the QMS. The CAPA team asks for details. Nobody can remember which shift, which lot, which machine, which operator.

The information existed. It just didn't travel.

Where a separate QMS is used, a connected loop looks different:

1. MES/MOM records the non-conformance with full context: order, operation, lot, machine, operator, measurements, photo.
2. Rules decide what happens next. One-off scrap stays in MES/MOM. A repeat defect, a critical characteristic or a customer-impacting issue raises a non-conformance or CAPA in the QMS automatically.
3. The QMS owns the investigation, root cause and action.
4. Actions that change the process come back to the shopfloor: a new inspection, a tighter limit, a revised instruction.

## Integration options

There's more than one way to wire this up.

**Through ERP.** MES/MOM posts quality results and blocked stock to ERP. The QMS reads from ERP. Simple, one hub, but you usually lose the rich detail. ERP carries the status and quantity, not the 40 measurements and the photo.

**Direct MES/MOM to QMS, with ERP for stock.** Non-conformances and inspection data go straight to the QMS with full context. Stock status changes still go through ERP, because ERP must know what's blocked. Where a QMS is already in place and quality is critical, this is the pattern I see working best.

**One platform.** A good MOM platform covers the QMS scope as well, so there's no separate QMS to connect. Check the depth: CAPA workflows, audits and document control should be genuinely usable, not token modules.

## Holds must be everywhere at once

One rule that applies whichever option you choose: when a lot goes on hold, every system that could move or consume it must know immediately.

If quality blocks a lot in the QMS but MES/MOM doesn't know, the line will happily consume it. If MES/MOM blocks it but the warehouse system doesn't, someone will ship it. Decide which system raises the hold, and make sure it propagates to ERP, MES/MOM and any [WMS](/post/wms-vs-mes-inventory) in minutes, not at the next batch interface run.

## Don't forget the documents

Document control sits in the MOM platform, or in the QMS where one is used. Work instructions, specifications and inspection plans are approved there. But the operator reads them in MES/MOM.

So the same revision question comes up as with PLM: the operator must see the approved revision for this order, not a copy someone saved locally in 2023. With a separate QMS, either publish from it to MES/MOM, or have MES/MOM reference it directly. Just don't maintain two copies.

## My view

A good MOM platform replaces the need for a separate QMS, and that's the option I'd choose. Running both means paying twice for the same capability, and losing context at the boundary. If a QMS is already in place, connect it directly, so non-conformances arrive with their full context.

With an MES that covers production only, feeding a QMS through one of the options above works well enough. But a full MOM is the better overall solution.

When a CAPA concludes "retrain operators", how do you prove the retraining happened before that operator next ran the job? That's where [skills you can enforce](/post/skills-enforcement-shopfloor) close the loop.
