---
title: "MES functionality: inventory management on the shopfloor"
short: "Inventory management"
description: "How MES/MOM manages stock on the shopfloor: lots, serials, containers and handling units, validated consumption, labels, WIP and traceability."
published: 2023-07-12
updated: 2026-10-25
category: education
art: bins
series: functionality
order: 4
---

Inventory is the physical material in the factory. Most plants track it in ERP at a summary level, but the shopfloor needs far more detail: which lot is at which machine, and exactly what went into each order.

This article covers how MES/MOM manages inventory once it reaches production. Warehousing and the movement of material to and from the line are covered in [MES functionality: warehouse management and logistics](/post/mes-functionality-logistics).

## Types of material

Inventory usually falls into these groups:

- **Raw materials**, received from suppliers
- **Semi-finished materials**, made in one process and consumed in the next, with their own material number
- **Finished goods**, ready to ship
- **Packaging and consumables**, often tracked more loosely

## How inventory is identified

The terms vary by industry and even by customer, but the principles are the same.

**Inventory.** A uniquely labelled quantity of material in a location, such as a pallet of cans, a reel of cable, a box of screws or a tote of meat. The identifier is usually printed as a barcode, so it can be scanned on a handheld device whenever it's moved or consumed.

**Serial items.** Inventory with a quantity of one. Typical for higher-value items, and for products that need detailed traceability or servicing after sale, such as a car or a printed circuit board. More common in discrete manufacturing, often with the identifier engraved or etched on.

**Lot.** An identifier for a group of inventory. Production lots often change by shift or by order, so ten pallets from the same order might share one lot number. Supplier lots matter too: a sample from the lot is often inspected, and if it passes, the whole lot is accepted.

Sometimes the lot is the most detailed identifier available. If 250 kg arrives as ten unlabelled 25 kg bags under one supplier lot, traceability stops at the lot. Relabelling each bag at goods-in makes each one traceable on its own.

**Batch.** A quantity made in a single vessel or run, common in process industries. A vat of cookie dough is mixed as one batch, and the batch number follows the dough into packing. The difference between lots and batches is explained in [Lot vs batch vs serial traceability](/post/lot-vs-serial-traceability).

**Handling unit.** Several pieces of inventory plus packaging, labelled as one transferable unit. Scanning the handling unit label moves everything on it in one transaction.

**Containers.** Physical assets that hold inventory, such as bins, racks, trolleys or oven carriers. Tracking them matters when they need cleaning or inspection after use, carry RFID tags, are restricted to certain materials, or hold material that can't carry a label of its own, for example through an oven.

## Inventory on the shopfloor

Logistics delivers material to the right place in production: directly to the machine, or to a supermarket nearby.

### Supermarkets

A supermarket is a stocked area on the shopfloor holding fast-moving materials and materials for upcoming orders, usually one location per material. Supermarkets are typically loaded from the back and picked from the front, so material is used first in, first out (FIFO).

::block supermarket-flow

Keeping a supermarket close to production shortens the trip to the machine and keeps line-side stock to a minimum, which keeps the shopfloor clean and tidy.

### Silos and kitting

Some materials sit in silos at the line, topped up periodically and drawn from as needed, such as plastic pellets feeding injection moulding machines.

Others are kitted: collected in advance of an order on a trolley or in a container. Electronics assembly is a good example, where reels of components are loaded onto a trolley in set positions and attached to the placement machine.

## Consuming inventory

Once material is at the line, it can be consumed into the process. Inventory can also be pre-allocated to orders, for example to link a semi-finished item to its next operation, or to make sure partial packs are used before new ones are opened.

Because MES/MOM knows the order and its bill of materials, it can check each item when it's scanned:

- Is it in a good quality state?
- Is it on the bill of materials for this order?
- Is it within its use-by date, and has it aged for long enough?
- Is it the next pack in FIFO sequence?

Validation at the point of use error-proofs the process. The wrong material is stopped before it's used, rather than discovered afterwards.

### Levels of consumption

| Level | What's recorded | Typical use |
| --- | --- | --- |
| **Backflush** | Nothing on the shopfloor. ERP assumes the bill of materials quantity was used | Low-value materials that don't need tracing |
| **Lot traceability** | The lot consumed, and the quantity | Most raw materials and ingredients |
| **Serial traceability** | Each serial number consumed | High-value or regulated components |
| **Time-based traceability** | The time window in which material was used | Continuous processes such as silos and extrusion |

Traceability can be recorded against the production order, or against the individual inventory created. ERP usually works at order level. MES/MOM can record which lots and serials went into each unit or pack produced. That detail is essential in assembly, and in any recall.

## Where the line between ERP and MES sits

Where inventory lives is one of the most debated decisions in any project, and there's no single answer for every factory.

A common starting position is that ERP is the master of inventory, so every transaction should happen in ERP, including on the shopfloor. It helps to be precise about what "master" means. ERP should usually own inventory at an aggregated level: stock by material and warehouse, valued for the balance sheet. The shopfloor needs much finer detail: individual lots and containers, exact locations, quality status, and what was consumed into which order and when.

That detail is usually best captured in real time by operational systems such as MES/MOM or a WMS, which keep ERP updated with the totals it needs. Pushing every shopfloor transaction into ERP adds high volumes of transactions it wasn't designed for. More on the options in [WMS vs MES vs ERP: who owns inventory once it reaches the line?](/post/wms-vs-mes-inventory)

## Creating inventory

MES/MOM knows the order, the material, the lot and the quantity, so it can print a correct label the moment inventory is made. The trigger can come from the operator or automatically from the equipment.

Without MES, factories often pre-print labels. That leads to mislabelling and manual tidy-up afterwards. Printing at the point of creation, with the right template on the right printer, avoids all of it.

### Co-production

An ERP order is usually an instruction to make one material. Some processes make several at once:

- **Grading:** some output misses the specification but can be sold as a lower grade, common in battery production
- **By-products:** waste that can be sold or recycled, such as offcuts when metal is cut to size
- **Slitting:** a wide reel slit into daughter reels of different widths
- **Shared ovens:** different materials treated in the same oven cycle

More capable MES/MOM platforms handle these scenarios natively.

### Work in progress and rework

WIP is inventory with some operations complete and others outstanding. Tracking it in real time shows where every partly made product is, and can trigger the next step automatically.

Material that fails quality is scrapped, or, if it can be saved, sent for rework: repeating earlier operations or carrying out a manual repair. Recording rework properly is what makes [first pass yield](/post/first-pass-yield-vs-rolled-throughput-yield) measurable.

## State and location

Every piece of inventory has a location and a state, such as available, on hold, quarantined or consumed. Keeping both accurate in real time means people can find material quickly, and quality holds actually stop material moving. Stock levels can then be trusted without waiting for the next count.

## Traceability

A major reason for tracking inventory in detail is traceability: everything that went into a finished product, back to the supplier lots.

Genealogy is only the start. When the same system also records quality results at each stage, the machine, the operator and process parameters such as temperatures, all of it is linked to the inventory. A customer complaint can then be traced to the lots consumed and their supplier batches, with inspection results attached, in minutes rather than days. More in [Your traceability probably isn't as good as you think](/post/manufacturing-traceability).

## The benefits

- **Fewer errors.** Validation at the point of use stops the wrong material being consumed, and FIFO rules reduce waste from expired stock.
- **Better data in ERP.** Reporting actual consumption, rather than backflushing, keeps stock and costs accurate. ERP often issues material before it leaves the warehouse, and the sequence it assumes isn't always what happens on the line.
- **Less WIP.** Real-time visibility of work in progress and line-side stock helps keep both lower.
- **Detailed traceability.** Genealogy at inventory level, with quality and process data attached, supports complaints and recalls.
- **Correct labels.** Labels printed on demand with the right information remove a common source of mistakes.

## My view

Inventory in production belongs in MES/MOM wherever you have one. It's the system that knows the order and its bill of materials, so it's the one that can validate what's used and record what's made. Let ERP own the totals and the value, and let the shopfloor system own the detail.

This article is part of the [MES functionality in depth](/paths/mes-functionality) learning path.

How confident are you that the stock your system shows at the line is what's actually there?
