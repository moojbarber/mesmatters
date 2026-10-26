---
title: "Shopfloor applications explained: what each one does, and why"
short: "Shopfloor applications explained"
description: "Production, quality, inventory, maintenance, connected worker and AI: what each shopfloor application does, and one platform versus several."
published: 2026-10-14
category: education
art: hexgrid
guide: true
---

"Shopfloor applications" covers a lot of ground. OEE tools, quality systems, traceability, maintenance, digital work instructions, checklists, energy monitoring, AI assistants. Each one is sold as the answer to something.

Most of them are genuinely useful. The question is which problem you're actually trying to solve, and whether you're solving it in a way that will still make sense in five years.

This guide goes through the main shopfloor applications by the job they do. At the end there's a table to match the problem you have to the application that fixes it.

## What counts as a shopfloor application?

Anything used at the point of work, by the people doing the work, in real time. Operators, supervisors, quality technicians, maintenance engineers and logistics.

That's different from ERP, which runs the business from the office, and from SCADA, which controls the equipment itself. Shopfloor applications sit in between, at level 3 of [ISA-95](/post/isa-95-explained). Collectively, that layer is MES/MOM.

## Production

**Production execution and monitoring.** Getting the right order onto the right line, starting and stopping it, and recording good counts, scrap and downtime, ideally straight from the equipment. The production order is the context everything else hangs off. This is the core of MES, and for many manufacturers their first step. See [Production monitoring](/post/mes-functionality-production).

**OEE and performance.** Availability, performance and quality on the bottleneck, calculated from automatic data rather than end-of-shift estimates. Most people are genuinely surprised when they first see their micro-stops. See [What is OEE?](/post/what-is-oee) and [KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee).

**Scheduling and dispatch.** ERP plans the orders. On the shopfloor, the job is fine-tuning the sequence and showing the line what to run next, and adjusting when a machine goes down. Complex sequencing may need APS on top. See [Production scheduling](/post/mes-functionality-scheduling).

## Quality

**In-process quality.** Inspection plans and checks triggered by what's actually running, with measurements and defects recorded against the order and material. Holds when something is wrong. See [Quality operations](/post/mes-functionality-quality).

**SPC.** Control charts at the line, so operators see a process drifting before it makes scrap. Inspection tells you a part is bad; SPC tells you it's about to be. See [SPC on the shopfloor](/post/spc-on-the-shopfloor).

**Electronic batch and device records.** In regulated industries, the record that proves you made it correctly, enforced as you go and reviewed by exception. See [MES/MOM in regulated industries](/post/mes-in-regulated-industries).

## Inventory and traceability

**Inventory and material tracking.** Labelled units, lots, serials and containers, consumed and created against orders as it happens, with labels printed at the line. See [Inventory management](/post/mes-functionality-inventory).

**Line-side logistics.** Replenishment requests based on real consumption or kanban signals, with a clean handover from the warehouse. See [Warehouse management](/post/mes-functionality-logistics).

**Traceability.** Genealogy forwards and backwards, plus the tooling, operators, quality results and process parameters behind every lot. In a recall, the difference between minutes and a weekend in spreadsheets. See [Your traceability probably isn't as good as you think](/post/manufacturing-traceability).

## Maintenance and assets

**Maintenance.** Fault reporting from the screen operators already use, work orders, planned and condition-based maintenance, and autonomous maintenance by operators, on the same downtime data production uses. See [Maintenance](/post/mes-functionality-maintenance).

**Tooling.** Tool life counted from real production, with cavities and readiness tracked alongside. No tool or no setter, and the job doesn't start. See [Tooling](/post/mes-functionality-tooling).

**Energy.** Consumption linked to the machine and order that caused it, including what machines draw while idle. See [Energy](/post/mes-functionality-energy).

## The people on the line

This is the part of the shopfloor that's changing fastest, because the workforce is. Experienced people are retiring, and their replacements stay for less time.

**Digital work instructions.** Presented automatically for the job that's running, always the latest version, step by step, with confirmations captured as you go. Not a PDF on a tablet. See [Digital work instructions that know what's running](/post/digital-work-instructions).

**Checklists and tasks.** Start-up checks and safety sign-offs, triggered at the right moment and recorded with the context.

**Shift handover.** Built from what actually happened, with the supervisor adding what only a person knows. See [Shift handover is a process](/post/digital-shift-handover).

**Skills.** Qualifications checked at the point of work, so the system stops the wrong person starting the wrong job rather than reporting it afterwards. See [Skills you can enforce](/post/skills-enforcement-shopfloor).

Together these are usually called connected worker. I'm a big believer in it. I'd just build it into the operational platform rather than buy it as another app. See [Connected worker: one app, not five](/post/connected-worker-one-app-not-five).

## AI on the shopfloor

**Operator copilots and knowledge assistants.** Plain-English answers about procedures, alarms and past faults, at the point of work.

**Shift summaries.** Drafted from the data for a supervisor to review.

**Visual inspection support.** Image recognition flagging likely defects for the operator to confirm, so judgement stays with the person.

**Predictive maintenance and predictive quality.** Models trained on condition data, failure history, process parameters and operating context.

Every one of these depends on the applications above. AI needs the order, the material, the recent stops and the approved procedure. That context lives in MES/MOM. See [AI for the frontline](/post/ai-for-frontline-workers) and [Practical GenAI for the shopfloor](/post/practical-genai-for-the-shopfloor).

## Match the problem to the application

| If your problem is... | Start with | Read |
| --- | --- | --- |
| Nobody trusts the downtime numbers | Automatic stop detection and reason capture | [Production monitoring](/post/mes-functionality-production) |
| Output is lower than it should be, and you don't know why | OEE on the bottleneck | [What is OEE?](/post/what-is-oee) |
| Scrap is found at final inspection, too late | In-process checks and SPC | [SPC on the shopfloor](/post/spc-on-the-shopfloor) |
| A recall would mean quarantining a week of production | Lot-level traceability | [Traceability](/post/manufacturing-traceability) |
| ERP stock never matches what's on the floor | Inventory tracking at the line | [Inventory management](/post/mes-functionality-inventory) |
| Lines wait for material | Consumption-based replenishment | [WMS, MES and ERP](/post/wms-vs-mes-inventory) |
| Production and maintenance argue about what stopped | Maintenance on the same data as production | [Maintenance](/post/mes-functionality-maintenance) |
| Changeovers wait for the tool or the setter | Tool management and readiness | [Tooling](/post/mes-functionality-tooling) |
| New starters take months to get it right | Digital work instructions | [Digital work instructions](/post/digital-work-instructions) |
| The night shift starts blind | Structured, data-driven handover | [Shift handover](/post/digital-shift-handover) |
| Unqualified people end up on critical jobs | Skills enforcement | [Skills you can enforce](/post/skills-enforcement-shopfloor) |
| You can't see energy below the site meter | Energy by machine and order | [Energy](/post/mes-functionality-energy) |
| Batch record review takes days | Electronic batch records | [Regulated industries](/post/mes-in-regulated-industries) |
| The shopfloor still runs on paper | Remove the paper that hurts most first | [Going paperless](/post/paperless-manufacturing) |

## One platform or several?

You can buy most of these as separate products. An OEE tool here, a checklist app there, a standalone quality system, a CMMS.

That has real advantages. Each department gets a tool that's very good at its job, and you can start where the pain is biggest. Modern integration options, from standard APIs and point-to-point interfaces to a unified namespace, make connecting them easier than it used to be.

The trade-off shows up as the problems overlap. Quality needs to know what's running. Inventory needs to know whether a lot passed inspection. Maintenance needs production's downtime. The operator needs one screen, not five logins. Every boundary becomes an interface to own and retest, and some context gets lost at each one.

## My view

On one platform those overlaps are already handled, because everything shares the same data model. That's why my own preference is a MOM platform, which replaces the need for a standalone QMS or CMMS. Pick the problem that hurts most, and solve it on a platform that can grow into the rest. I set out all four approaches, including coding or building your own, in [Code, build, stitch or configure](/post/build-vs-buy-mes).

Which row of that table describes your biggest problem right now?
