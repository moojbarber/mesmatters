---
title: "Lot vs batch vs serial traceability: how granular do you need to be?"
short: "Lot vs batch vs serial"
description: "Lot, batch, serial and time-based traceability explained: how granular you need to be, whether lot and batch differ, and how to choose per product."
published: 2026-10-06
category: education
art: tiles
---

"We need full traceability" is one of the most common requirements in any MES/MOM project. It's also one of the least specific. Full at what level? Every batch of resin, or every individual part?

The answer changes the cost of the project and the work operators do every shift. So it's worth deciding deliberately.

## How you can trace

**Lot (or batch) traceability.** A quantity of material shares one identifier: a lot of resin from a supplier, or a batch from a mixer. You know which lots went into which lots. Most manufacturers trace at this level.

**Serial traceability.** Every individual item has its own identifier, usually a printed or engraved barcode or a data matrix. You know exactly which components went into exactly which unit. Common for high-value and regulated products.

**Time-based traceability.** In continuous processes, material doesn't arrive in neat lots. You trace by time window instead, using the actual lead time through the line to work out which input was in which output. It's how extrusion and many continuous food lines do it.

Many manufacturers use a mix, such as serialised finished goods built from lot-tracked components.

## Lot vs batch: is there a difference?

The two words are often used interchangeably, and in many factories that's fine. But there's a useful distinction.

A **batch** is a quantity made in one production run, usually under one order and one recipe. It's a production term, most common in process industries.

A **lot** is a quantity that shares one identity for traceability, whether you made it or bought it. A supplier's delivery of resin is a lot. A batch you produce becomes a lot once it's identified and stored.

The two don't always line up one to one. A large batch might be split into several lots for packing or release, and a lot of finished goods might be blended from more than one batch. In US pharmaceutical regulations, for example, a lot can be a whole batch or an identified portion of one.

What matters is that your MES/MOM can record both, and the links between them, so that you can trace from any lot back to the batches and raw material lots that went into it.

## Side by side

| | Lot | Serial | Time-based |
| --- | --- | --- | --- |
| **Identifies** | A quantity sharing one ID | Each individual item | A window of production |
| **Typical use** | Raw materials, batches, most consumables | High-value or regulated products | Continuous processes |
| **Recall scope** | Every item in the affected lots | Exactly the affected units | Everything in the affected time window |
| **Labelling effort** | Moderate | High: every item marked and scanned | Low on the line, but needs accurate timing |
| **Data volume** | Moderate | High | Moderate |

## Choosing the right level

Ask these for each material and product:

- **What do customers or regulators require?** Medical devices and aerospace parts often need serial-level records. Food usually needs lot-level, done fast.
- **What does a recall cost?** If one bad component means recalling a whole week's production, finer traceability pays for itself quickly.
- **Will you service the product?** Field failures trace back through the serial number to the [as-built record](/post/ebom-mbom-as-built). See [Service data back to engineering](/post/service-data-back-to-engineering).
- **Can the process support it?** Serialising thousands of small parts a minute needs marking and scanning at line speed. Sometimes lot level with tight lot sizes is the practical answer.

## What makes traceability good

The level of granularity is only half the story. The difference between adequate and excellent traceability is what you capture alongside the genealogy: the tooling used, quality results at every stage, the operator, the machine, and the process parameters at the time.

That's what turns a recall from quarantining a week of production into identifying exactly which units contain the suspect material. More in [Your traceability probably isn't as good as you think](/post/manufacturing-traceability).

## Where it lives

ERP usually tracks lots at the level the business needs, often with backflushing. The detailed genealogy, especially serial-level and time-based, is MES/MOM's job, because it's there when the material is actually consumed. Lot quantities need to be recorded as they happen, not calculated from the BOM afterwards.

If a complaint landed on your desk this afternoon, how long would it take to find every affected unit?
