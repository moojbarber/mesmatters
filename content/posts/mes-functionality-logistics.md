---
title: "MES functionality: warehouse management and logistics"
short: "Warehouse and logistics"
description: "Goods-in, replenishment, putaway, warehouse moves and shipping: how material flows through a factory, and whether ERP, a WMS or MES/MOM should run it."
published: 2023-07-13
updated: 2026-10-25
category: education
art: flow
series: functionality
order: 5
---

Production can only run if the right material is at the line when it's needed. Getting it there, and getting finished goods back out, is the job of the logistics team, usually working with forklifts and handheld barcode scanners.

This article covers the main warehouse and logistics processes, and the choice of which system should run them. What happens to material once it's at the line is covered in [MES functionality: inventory management](/post/mes-functionality-inventory).

## The logistics flow

At a high level, logistics in a factory covers:

- Receiving stock from suppliers and storing it
- Managing stock while it's in the warehouse
- Moving material to production when it's needed, and returning what isn't used
- Putting finished goods away, then loading them for delivery

## Which system runs the warehouse?

Warehouse management can sit in ERP, a dedicated warehouse management system (WMS) or MES/MOM. Each has strengths, and the right answer depends on how your warehouse and your lines work.

| | Strengths | Watch out for |
| --- | --- | --- |
| **ERP** | Already the master of stock and its value, and often includes reasonable warehousing functions. No extra system to buy | Screens are usually designed for office users. Less depth than a WMS. Needs a clear handover to MES/MOM when material enters production. Often tracks only at lot level |
| **WMS** | Deep warehousing functions, strong in distribution and designed for mobile scanners. Suits complex supply chains and warehouse automation | Another system to license and integrate. Can be more than many warehouses need |
| **MES/MOM** | One application for logistics and production, so no handover at the line, and usually the friendliest for operational users. Can work with automated storage without a full WMS | Only sensible if you need MES/MOM for production anyway. Covers general warehousing rather than advanced distribution, and some narrower MES products don't cover logistics at all |

Many manufacturers combine them, for example ERP or a WMS for the main warehouse and MES/MOM from the supermarket to the line. The boundaries and integration options are covered in [WMS vs MES vs ERP: who owns inventory once it reaches the line?](/post/wms-vs-mes-inventory)

## Receiving goods in

Inbound deliveries range from supplier raw materials to customer returns, and ERP orchestrates them. Whichever system runs the goods-in warehouse receives the expected deliveries from ERP and confirms receipt back to it.

Suppliers in some industries send an advance shipping notice (ASN) listing the exact inventory on the delivery, which can be shared with the receiving system.

Material is often relabelled at goods-in with the factory's own label and material number. Suppliers sometimes deliver several packs under one lot code with no unique identifier, and a label for each pack makes every one individually traceable from then on. Incoming inspections can also be triggered at this point.

## Replenishment to the line

If material runs out, the line stops and OEE suffers. Replenishment can be manual, for example pushing an empty container forward as a signal. That works in a small factory with a stable set of materials, but struggles as complexity grows.

Automated replenishment tracks stock at each location and raises requests by rule:

| Method | How it works | Suits |
| --- | --- | --- |
| **Reorder point** | A request is raised when stock falls below a set level | Steady consumption |
| **Kanban** | A request is raised as soon as a container is emptied | Repetitive production |
| **Demand-based** | Requests are raised from the upcoming production schedule | High mix, changing schedules |
| **Manual call-off** | The operator or supervisor requests material | Occasional or unusual items |

Replenishment driven by actual consumption keeps lines supplied without piling stock beside them.

## Putaway

At the end of production, finished inventory is labelled and moved into a warehouse. If MES/MOM doesn't own that warehouse, putaway is the point where ownership passes back to ERP or the WMS.

**Handling units.** Inventory is often packed first into handling units, so a whole pallet can be put away with one scan.

**Guided putaway.** Some systems recommend a location based on available space and rules such as fast movers or stock already allocated to a delivery.

**AGVs.** Automated guided vehicles increasingly carry out putaway and replenishment moves.

**Automated storage and retrieval (AS/RS).** The warehouse is treated as a black box: inventory is handed over, then stored and retrieved automatically. It uses space efficiently and reduces forklift traffic, which helps safety.

## Moves within the warehouse

Common warehouse transactions include:

- **Split:** dividing a pallet, for example to match a customer order or send a smaller quantity to the line
- **Sort:** separating good from quarantined or scrap pieces. If sorting takes real time, it's often better modelled as an operation, so the labour cost can be recorded
- **Merge:** combining partial pallets into a full one
- **Reclassify:** changing the material number when the output turns out to be a different grade, common in battery production

## Picking and shipping

Outbound deliveries, whether customer shipments or transfers to other plants, are orchestrated by ERP. The system running the finished goods warehouse receives the delivery details from ERP, and confirms shipment once picking and loading are done. Scanning each pick against the order reduces the risk of sending the wrong item.

## Choosing where each flow lives

**ERP** often suits a simple warehouse: a few aisles of racking and straightforward picking, with replenishment on a daily or shift rhythm. It gets harder with high-frequency line-side replenishment, or when you need more detail about each lot and location than ERP holds.

**A WMS** earns its place when the warehouse is complex in its own right: high volumes, optimised pick paths, multiple storage zones, automation such as AS/RS, or a distribution operation alongside manufacturing. Many ERP suites include a WMS module, so it doesn't have to mean another vendor. The trade-off is another boundary to manage.

**MES/MOM** suits flows driven by production: supermarkets feeding the lines, kitting and kanban, just-in-time replenishment triggered by actual consumption, and finished goods taken off the line. It isn't designed to run a large distribution warehouse.

## The benefits of one system from goods-in to the line

Where MES/MOM does run logistics, there are some specific advantages:

- **Traceability back to receipt.** Inbound inspections and supplier lots appear in the same genealogy as production.
- **No handover interfaces.** Material moves from warehouse to production without being passed between systems.
- **One picture for everyone.** Logistics and production see the same stock, and planners can see expected deliveries when shortages loom.
- **A smaller application landscape.** Where advanced warehousing isn't needed, there's one system fewer to support and integrate.

## My view

I come from a world of MES, but I often recommend ERP or a WMS for warehousing, depending on the situation. There's no one-size-fits-all answer. What matters is making the decision deliberately, with advice from someone who'll lay out the strengths of each option before recommending one.

This article is part of the [MES functionality series](/post/mes-functionality-guide).

Where does ownership of material change hands in your factory, and does everyone agree where that line is?
