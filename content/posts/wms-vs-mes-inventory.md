---
title: "WMS, MES and ERP: who owns inventory once it reaches the line?"
short: "WMS vs MES inventory"
description: "ERP, WMS and MES/MOM all track stock. Where the boundaries sit for warehouse, line-side and WIP inventory, and the integration options that work."
published: 2026-10-16
category: education
art: bins
---

Three systems can all claim to know where your stock is. ERP, the warehouse management system (WMS) and MES/MOM. In a lot of factories, all three are a bit right and a bit wrong at the same time.

The fix isn't picking one winner. It's agreeing where each one's responsibility starts and stops.

## What each one is for

**ERP** owns inventory as a business asset. Quantities by item and site, valuation, purchasing, receipts, shipments, and the stock that planning relies on. It's the financial truth.

**WMS** owns inventory in the warehouse. Exact bin locations, putaway strategies, pick paths, wave planning, cycle counts, dock and yard, and any automation such as conveyors or AS/RS. It's the physical truth *inside the warehouse walls*.

**MES/MOM** owns inventory on the shopfloor. Line-side stock, kits, work in progress (WIP), what was consumed by which order, and which lot went into which product. It's the truth *at the point of use*.

I covered the shopfloor side in [MES functionality: logistics and warehousing](/post/mes-functionality-logistics-warehousing). This article is about the boundaries.

## Do you even need a WMS?

Not always. Plenty of manufacturers run their warehouse perfectly well on ERP's inventory and warehouse functions, with MES/MOM handling the shopfloor. If your warehouse is a few aisles of racking with simple picking, ERP plus MES/MOM is usually enough.

A dedicated WMS earns its place when you have:

- High volumes and complex pick strategies
- Warehouse automation to control
- Multiple storage zones with different rules: temperature, hazardous, high-value
- A distribution operation alongside manufacturing

Most ERP suites include a capable WMS module, so "WMS" doesn't necessarily mean another vendor. It means deeper warehouse functionality, wherever it comes from.

## The boundary that matters: the line

The messy part is the handover between warehouse and production. Let's walk through it.

**Replenishment.** The line needs material. Who asks for it? Ideally MES/MOM, because it knows what's running, what's next and what's left line-side. It raises a replenishment request based on real consumption or kanban signals, rather than ERP pushing kits days in advance.

**Delivery.** The warehouse picks and moves the material. WMS (or ERP) manages that task and records that stock left the warehouse.

**Receipt line-side.** MES/MOM takes ownership. From here, it tracks the lot at the line, in a [supermarket](/post/mes-functionality-inventory-management) or at the machine.

**Consumption.** MES/MOM records what was actually used, by order and by lot. That flows back to ERP for stock and cost.

**Output.** Finished goods are declared in MES/MOM, labelled, and handed back to the warehouse for putaway.

::block supermarket-flow

## Integration options

Here's where you have choices. Two common patterns:

| | Through ERP | ERP plus direct WMS link |
| --- | --- | --- |
| Replenishment requests | MES/MOM → ERP → WMS | MES/MOM → WMS directly |
| Material moved | WMS → ERP → MES/MOM | WMS → MES/MOM directly, ERP updated in parallel |
| Consumption and output | MES/MOM → ERP | MES/MOM → ERP |
| Best for | Lower volumes, slower replenishment cycles | High-frequency, just-in-time replenishment |

The ERP route is simpler and keeps one hub. The direct route reduces latency. If you're replenishing a line every 20 minutes, a round trip through ERP can be the difference between a delivery arriving on time and an idle line.

Whichever you pick, ERP stays the financial owner of the stock. A direct link is about speed of execution, not a second set of books.

## Where it goes wrong

- **Backflushing hides reality.** ERP deducts standard quantities when output is declared. Scrap, overuse and substitutions disappear. Record actual consumption in MES/MOM where it matters.
- **Line-side stock is a black hole.** Material leaves the warehouse and "vanishes" until the next stock count. Give it a location in MES/MOM.
- **Two systems manage the same bins.** If WMS and MES/MOM both think they own the supermarket, they'll both be wrong. Draw the line on a map, literally.
- **Quality status doesn't travel.** A lot put on hold by quality must be blocked in every system that could move or consume it. More on that in [QMS and MES](/post/qms-and-mes-quality).

## A simple test

Pick a component and ask three people where all of it is right now: the warehouse manager, the line supervisor and the finance controller. Do the answers add up to the same number?
