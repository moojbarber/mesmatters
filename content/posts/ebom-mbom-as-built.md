---
title: "EBOM, MBOM, as-built: who owns the BOM at each stage"
short: "Who owns the BOM"
description: "A bill of materials changes shape four times between engineering and shipment. Which system owns it at each stage, and where MES/MOM fits."
published: 2026-09-02
category: education
art: stack
---

Ask five people in a factory what "the BOM" is and you'll get five slightly different answers. They're all right. They're just talking about different stages of the same thing.

A bill of materials changes shape as it moves from design to a finished product. Each stage has a different owner, and a lot of integration arguments come from not agreeing who owns which one.

## Stage 1: the engineering BOM

The **EBOM** describes the product as designed. It's structured by function: the assemblies and parts an engineer thinks in. It lives in **PLM**, alongside the CAD models and specifications.

What it usually doesn't include: packaging, glue, labels, or the fact that two sub-assemblies are made in different plants.

## Stage 2: the manufacturing BOM

The **MBOM** describes the product as it will be *built*. Same product, restructured around the process:

- Sub-assemblies grouped by where they're built, not by function
- Consumables, packaging and labels added
- Phantom kits for parts picked together
- Plant-specific variants where two sites build it differently

For configurable products, the MBOM is often a **150% BOM**. It holds every possible option and variant in one structure, more than any single product would ever use, with rules that decide which parts apply to which configuration.

In most manufacturers, the MBOM lives in **ERP**, alongside the routing. That makes sense. ERP needs it to plan, purchase and cost.

There's an option here. Some manufacturers build the MBOM in a manufacturing process planning module that sits with PLM, then release it to ERP. Others receive the EBOM into ERP and restructure it there. Both work. What matters is that there's one owner, and everyone knows who it is.

## Stage 3: the order BOM

When ERP releases a production order, it takes a copy of the MBOM for that order, at the revision that's effective on that date, for that quantity. That copy is the **order BOM**.

For configurable products, this is where the 150% BOM is resolved into a **100% BOM**: exactly the parts needed for the configuration the customer ordered, and nothing else. The order BOM is a 100% BOM.

This is what goes to **MES/MOM**. Not the master MBOM. The specific list of components and quantities for this order.

It can change after release. A planner substitutes an alternative component. A shortage forces a different lot size. That's normal, and it's one reason ERP usually stays in the middle. It has to account for those changes anyway, for cost and stock.

## Stage 4: the as-built record

The **as-built** record is what was actually used. Which lot of component A, which serial number of sub-assembly B, which operator fitted it, at what torque, with which measurements recorded.

This is MES/MOM's job. Nobody else is there when it happens. The as-built record is the foundation of your [traceability](/post/manufacturing-traceability) and, for serialised products, the genealogy you'll need years later when a field failure comes back. More on that in [Service data back to engineering](/post/service-data-back-to-engineering).

## Who owns what

| Stage | Describes | Usual owner | Typical consumers |
| --- | --- | --- | --- |
| EBOM | The product as designed | PLM | ERP, sometimes MES/MOM directly |
| MBOM | The product as it will be built | ERP (or PLM process planning) | Planning, purchasing, costing |
| Order BOM | What this order should use | ERP | MES/MOM |
| As-built | What this order actually used | MES/MOM | ERP (consumption), quality, service, engineering |

## Where it goes wrong

**Nobody owns the MBOM.** Engineering thinks manufacturing engineering owns it. Manufacturing engineering thinks it's ERP's master data team. It drifts. It's an [ERP master data problem](/post/erp-master-data-for-mes) long before it's an MES problem.

**The as-built is reconstructed from the order BOM.** If MES/MOM just backflushes what the order said it should use, you don't have an as-built record. You have a copy of the plan. That's fine for some products. It's useless when you need to know which customers got the suspect lot.

Some ERPs do record an as-built, but it's based on the materials ERP issued to the order, with no confirmation that what was issued is what was actually consumed. Material gets swapped at the line, part-used packs are finished first, a lot runs out halfway through. That's where MES/MOM helps: it records what was actually used, as it's used, by scanning the lot or serial at the point of consumption.

**MES/MOM is asked to own the MBOM.** It happens when ERP's BOM is too coarse for the shopfloor, so someone builds the "real" BOM in MES. Be wary of this. You now have two masters, and they will disagree. Fix the MBOM in ERP instead, or add the missing detail as operation-level data rather than a parallel BOM.

**Revisions drift apart.** The order BOM says revision C. The drawing on the operator's screen says revision D, because it was pulled as "latest" from a shared drive. Every document the operator sees should be tied to the revision on the order.

## Where a direct PLM link fits

Some manufacturers send selected engineering data straight from PLM to MES/MOM: drawings, models, critical characteristics. It doesn't change BOM ownership. The order BOM still comes from ERP. The direct link adds context the operator needs to build and check it. For documents and drawings, a central document repository is usually the better option: every document stored once, tagged by product, revision and operation, and read by every system, so there's no need for a direct link at all. I cover the options in [PLM, ERP and MES: where the digital thread actually runs](/post/plm-erp-mes-digital-thread).

So, here's a test. Pick a finished product shipped last month. Can you show its EBOM revision, the MBOM it was planned against, the order BOM, and the exact lots and serials that went into it? If any one of those takes a day of digging, that's your gap.
