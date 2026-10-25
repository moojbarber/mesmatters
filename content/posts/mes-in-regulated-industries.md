---
title: "MES/MOM in regulated industries such as pharma and medical devices"
short: "Regulated industries"
description: "What changes when regulators and customers audit your shopfloor. Electronic batch records, device records, first article inspection, PPAP and traceability."
published: 2026-09-23
category: education
art: document
---

In some industries, making a good product isn't enough. You have to *prove* you made it correctly, every time, often years later, to an auditor who wasn't there.

That changes what you need from MES/MOM. The core functions are the same: orders, materials, quality, equipment, people. But the evidence requirements are much stricter, and the cost of getting it wrong is a recall or a regulator's warning letter.

Four regulated sectors, and how each shapes MES/MOM. I covered food separately in [The biggest barriers to MES success in food manufacturing](/post/food-manufacturing-mes-barriers).

## Pharmaceuticals and biotech

The heart of it is the **batch record**. Every step, every material, every weight, every check, every signature. On paper, a batch record can run to hundreds of pages, and reviewing it takes days.

An **electronic batch record (EBR)** in MES/MOM changes that:

- The recipe enforces the sequence, so steps can't be skipped
- Weights and measurements come from connected scales and instruments, not handwriting
- Deviations are flagged as they happen, not found during review
- QA can use **review by exception**, checking only what went outside the normal path

Electronic records and signatures must meet **FDA 21 CFR Part 11** in the US and **EU GMP Annex 11** in Europe: secure, attributable, audit-trailed, and validated. Data integrity principles (often summarised as ALCOA+) apply to everything.

Validation is the big project overhead. Which brings me to a cautionary point: the more you customise, the more you validate. Here, [configure, don't customise](/post/configure-dont-customise) is a matter of compliance cost, not just good practice.

## Medical devices

Device makers need a complete record of how each device or batch was built. In the US, the FDA's Quality Management System Regulation (QMSR) has incorporated **ISO 13485** by reference since 2 February 2026, so the US now follows the same standard most manufacturers elsewhere already use.

For MES/MOM, that means:

- Serial or lot-level genealogy for every device and critical component
- Proof that operators were trained and qualified for the operation, at the time
- Equipment calibration status checked before use
- Labelling linked to the as-built record, including unique device identification (UDI) where it applies

Complaints and field issues must trace back to the build record quickly. I cover that end of the chain in [Service data back to engineering](/post/service-data-back-to-engineering).

## Aerospace and defence

Aerospace is built on **AS9100**, and its customers expect serialised traceability that can last for the life of an aircraft. Decades.

Things that matter on the shopfloor:

- **First article inspection** (FAI, typically to AS9102) when a part is new, changed or moved to a new process
- **Configuration control**: building to exactly the right revision, which makes the [PLM, ERP and MES](/post/plm-erp-mes-digital-thread) link critical, often with a direct PLM connection for drawings and characteristics
- **Special processes** such as heat treatment and welding, with qualified people and validated parameters
- **Counterfeit part prevention** and full supplier traceability for critical components

Operators frequently need the drawing at the workstation. Paper travellers with handwritten stamps are still common in aerospace, and they're a major source of escapes and audit findings.

## Automotive

Automotive suppliers work to **IATF 16949**, plus specific requirements from each OEM. The emphasis is on preventing defects at volume:

- **PPAP** (production part approval) before supply starts, and control plans that define every check
- **Error-proofing** at the station: right part, right torque, right sequence, enforced rather than checked afterwards
- **Traceability** of safety-critical components to the vehicle, so a recall can be targeted to specific VINs instead of a whole model year
- **Rapid containment**: when a defect is found, knowing within minutes which parts are suspect and where they are

The volumes are high and the margins thin, so traceability has to be automatic. Nobody hand-records lot numbers at 60 units an hour.

## What they have in common

Strip away the acronyms and four principles repeat:

- **Enforce, don't just record.** The system should stop the wrong thing happening, not merely log it.
- **Capture at the source.** Data from the instrument or the scan, not typed from memory.
- **Link everything to the unit or lot.** Materials, people, equipment, results.
- **Make the record reviewable.** Quickly, by exception, years later.

Those are good principles in any industry. Regulation just removes the option to skip them.

If an auditor arrived tomorrow and picked a unit you shipped two years ago, how long would it take you to produce its complete record?
