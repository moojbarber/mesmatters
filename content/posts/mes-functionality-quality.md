---
title: "MES functionality: quality operations"
short: "Quality operations"
description: "In-process quality in MES/MOM: control plans, variables and defects, SPC, automated inspections and holds, and how quality data ties back to every order."
published: 2023-06-29
updated: 2026-10-25
category: education
art: spc
series: functionality
order: 3
---

Manufacturers need to know the quality of what they make, as they make it. Poor quality means scrap and rework, and if it reaches a customer it can mean penalties or a recall. Customers are also tightening tolerances and pushing initiatives such as zero defects.

Quality costs come straight off the margin, so it pays to measure them and improve continuously. MES/MOM supports that by capturing quality data at the point of production, in the context of the order and the material.

## What quality means on the shopfloor

Manufacturers define quality control plans, which say which inspections to perform and when. Inspections are often shared across materials, but the specifications usually vary by material.

A specification sets the acceptable range for a measurement. If a length should be 100mm, the acceptable range might be 98mm to 103mm. Inspections are carried out on one or more samples taken from the line, and record two kinds of result.

### Variables

Variables are measured in units, such as dimensions or weight. They can be measured across several samples, and at several positions on the same sample.

Where a machine has several outputs, samples can come from each one. On an injection moulding machine, for example, a tool may produce parts from several cavities at once. Recording the cavity lets quality problems be traced to the exact position in the tool, not just the machine. More in [MES functionality: tooling](/post/mes-functionality-tooling).

Statistical process control (SPC) uses samples to judge whether a process is stable and capable, so not every item needs inspecting. More in [SPC on the shopfloor](/post/spc-on-the-shopfloor).

### Defects

Defects, sometimes called attributes, are issues that can't be measured on a scale, such as a dent or a scratch. A single product can have several, and each is usually graded by severity, with critical defects at the top. The grades decide whether the product is good or defective: one critical defect makes it defective, while a single minor one may not.

When recording defects, be clear whether you're counting defects or defective parts, and whether the sample size is fixed or variable. That decides which SPC chart to use:

::block spc-chart-types

Some MES platforms let the inspector mark defects on a picture of the product, so the location is recorded as well.

## How quality data is captured

Results can be entered by hand, but many MES platforms collect them directly from metrology equipment such as scales and gauges. Some equipment exports results to a file, which MES imports automatically. Both reduce typing and improve accuracy.

Some tests destroy the sample. Destructive testing adds to scrap, and so affects the quality part of OEE. More in [What is OEE?](/post/what-is-oee)

## Where quality checks happen

Quality connects closely to the other MES functions, which is why context matters so much.

**Incoming materials.** Inspections on supplier deliveries, by batch or by serial number. When the material is later consumed, MES/MOM links the inspection to the traceability record. If a problem is found later, or by a customer, genealogy leads back to the supplier lot and its results. Material that's out of tolerance may be returned, or accepted at a discount.

**In-line production.** MES/MOM already knows the order and the material, so the operator doesn't have to enter them. It can prompt the right check, with the right specification, as soon as it's due. It can also adjust the number of checks to the actual run time, so downtime doesn't trigger unnecessary checks, and report on compliance with the control plan.

**Lab checks.** Samples sent to an on-site lab, or to an external one, need labelling and tracking. MES/MOM can print the label and link the result back to the order. A dedicated LIMS manages the lab itself; more in [LIMS and MES](/post/lims-and-mes).

**Automated inspections.** Inspection equipment can export results for MES to compare against the specification. Vision systems, increasingly using AI, detect defects and often reject the part automatically. MES/MOM records the result either way.

**Inventory and warehouse inspections.** Checks recorded against a specific container or pallet, for example before shipping, or when someone spots a problem. These form part of the traceability record too.

**Asset inspections.** Some platforms also support checks on equipment and tools.

## Core quality functions

**Quality control plans.** MES/MOM defines and manages the plan, and makes sure the right inspections are carried out at each step.

**Performing inspections.** Results are visible in real time, so problems are dealt with as they arise. A clear, visual screen for the operator matters a lot. When a specification is breached or a critical defect is found, the operator should be told straight away, and given the chance to record the cause.

**Out of specification and out of control.** An out-of-spec result falls outside the specification limits. An out-of-control result falls outside the statistical control limits, signalling that the process is drifting even if parts are still within specification. Watching both catches problems early.

**SPC.** Statistical analysis of sampled results shows how capable the process is, and flags drift before it produces scrap.

**Metrology connections.** Direct links to gauges and measuring equipment improve accuracy and save time.

**Holds.** Suspect material is put on hold and blocked from being consumed or shipped. The hold needs to be visible in every system that could move the material.

**Non-conformances.** When problems are found, MES/MOM can raise a non-conformance with full context. Some platforms manage the follow-up actions themselves; others pass serious or repeat issues to a QMS for investigation and CAPA.

**Documents.** Document management is usually a quality function, and MES products handle it in different ways.

## From SPC to predictive quality

SPC has been catching drifting processes for decades, long before anyone called it AI. The principle is the same: learn what normal looks like, then flag what isn't.

Predictive quality goes a step further. Machine learning predicts whether a part or batch will pass inspection before it's inspected, based on process parameters, material lots, tool condition and history. When it works, you can act while the product is still on the line.

It only works if quality results are linked to the production and process data around them. More in [AI, ML and GenAI on the shopfloor](/post/ai-ml-genai-on-the-shopfloor).

## MES/MOM and QMS

MES/MOM and a QMS cover different parts of quality. MES/MOM runs quality at the point of production, with in-process checks and holds tied to the order and the lot. A QMS runs the quality system across the business, including CAPA, audits, complaints and controlled documents.

Some manufacturers run in-process quality entirely in MES/MOM and use a QMS for the wider system. Others with simpler needs manage with MES/MOM alone. The full comparison is in [QMS vs LIMS vs MES](/post/qms-vs-lims-vs-mes), and the connections between them in [QMS and MES](/post/qms-and-mes-quality).

## What it delivers

- **Problems caught earlier:** drift spotted on the line, not at final inspection.
- **Less scrap and rework:** fewer defects, and faster root cause when they happen.
- **Audit-ready records:** results captured with full context as the work is done.
- **Fewer escapes to customers:** holds that actually stop suspect material moving.

## My view

Quality data is most valuable when it sits on the same platform as production and inventory. That's what lets a check be triggered by what's actually running, and a result follow the material wherever it goes.

This article is part of the [MES functionality series](/post/mes-functionality-guide). Related: [Your traceability probably isn't as good as you think](/post/manufacturing-traceability).

How many of your quality checks are still recorded on paper?
