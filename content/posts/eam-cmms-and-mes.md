---
title: "EAM, CMMS and MES: who owns the maintenance work order?"
short: "EAM, CMMS and MES"
description: "Maintenance data sits in EAM, CMMS, ERP and MES/MOM. Where each one's job starts and stops, and the integration options that keep downtime data consistent."
published: 2026-09-17
category: education
art: wheel
---

Production and maintenance both care about the same machine. They just look at it differently. Production sees an asset that should be running. Maintenance sees an asset that needs looking after so it *keeps* running.

When those two views live in different systems with no link between them, you get two versions of the truth about downtime. And an argument in every morning meeting.

## The systems involved

**EAM** (Enterprise Asset Management) and **CMMS** (Computerised Maintenance Management System) manage assets over their whole life. The difference is mostly scale: EAM covers the full lifecycle and the financials across many sites; CMMS is the lighter, maintenance-team-focused version. I compare the two in more detail in [CMMS vs EAM vs MES](/post/cmms-vs-eam-vs-mes). Both handle:

- The asset register and hierarchy
- Preventive maintenance plans and schedules
- Maintenance work orders, labour and history
- Spare parts and maintenance stores

**ERP** often provides the EAM capability itself, or owns the financial side: asset values, depreciation, purchasing of spares, maintenance cost.

**MES/MOM** knows what the asset is doing right now. Run hours, cycle counts, downtime and its reasons, speed losses, the product being made, and what the operator just reported.

I covered the shopfloor side in [MES functionality: maintenance](/post/mes-functionality-maintenance). This one's about the boundary.

## The overlap

Here's where the two worlds collide:

- **Downtime.** MES/MOM records that the machine stopped, for how long, and the reason. Maintenance needs exactly that to plan and to measure MTBF and MTTR.
- **Usage-based maintenance.** "Service every 50,000 cycles" needs a counter. MES/MOM has it. EAM/CMMS has the plan.
- **Breakdown requests.** An operator spots a problem. Where do they raise it? Ideally on the screen they already use.
- **Planned maintenance windows.** Maintenance wants the machine. Production wants to run. Somebody has to schedule both.

## Integration options

**Through ERP.** MES/MOM sends downtime and counters to ERP, where the maintenance module (or an EAM connected to ERP) acts on them. One hub. Works well when ERP already runs maintenance and the trigger frequency is low, say daily counter updates.

**Direct MES/MOM to EAM/CMMS, with ERP for cost and parts.** MES/MOM sends counters, conditions and breakdown requests straight to the EAM/CMMS, which raises the work order. Planned maintenance windows come back to MES/MOM so the schedule reflects them. ERP still handles spares purchasing and costs. This suits plants with frequent, condition-based triggers.

**Maintenance inside MES/MOM.** For many plants, especially smaller ones, MES/MOM's own maintenance functionality is enough: operator-raised requests, simple PM schedules, autonomous maintenance checklists and downtime analysis in one place. No integration at all.

**Hybrid by asset criticality.** Critical, complex assets are managed in full EAM. Simpler line equipment and operator-level care are handled in MES/MOM. Clear rules decide which asset lives where.

None of these is universally right. I'd ask one question first: who actually raises and closes most of your maintenance tasks, technicians or operators?

## Rules that hold in every option

**One system owns downtime reasons.** Usually MES/MOM, because that's where the stop is recorded as it happens. If maintenance re-codes downtime in EAM, feed it back. Otherwise production and maintenance will report different numbers, and both will be right according to their own system.

**One system owns the work order.** Raising a request can happen anywhere. But the work order, its status and its history belong in one place.

**Operators don't log into a second system.** If raising a breakdown means leaving MES/MOM and opening the CMMS, operators will shout across the shop instead. The request should start where they already work. I make the same argument in [connected worker: one app, not five](/post/connected-worker-one-app-not-five).

**Maintenance windows are visible to production.** A planned stop that the schedule doesn't know about is just unplanned downtime with extra paperwork.

## Where this goes next

[Predictive maintenance](/post/predictive-maintenance-data) depends on exactly this link. The models need machine conditions and production context from MES/MOM, and they need somewhere to send their predictions that results in a work order. Without the integration, a prediction is just an alert nobody acts on.

## My view

A good MOM platform replaces the need for a CMMS: requests, work orders, preventive maintenance and downtime in one place. Running a MOM and a CMMS side by side makes little sense. Where an EAM is needed for asset lifecycle and capital planning, use the rules above so MOM still owns downtime, and production and maintenance tell the same story.

An MES that covers production only can feed a CMMS instead, using the same rules. But a full MOM is the better overall solution.

So, look at last month's top five downtime causes in your MES. Now look at your maintenance system. Do they tell the same story?
