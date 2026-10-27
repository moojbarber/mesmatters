---
title: "WMS vs MES vs ERP: who owns inventory once it reaches the line?"
short: "WMS vs MES inventory"
description: "ERP, WMS and MES/MOM all track stock. Where the boundaries sit for warehouse, line-side and WIP inventory, and how material is handed over between them."
published: 2026-09-08
category: education
art: bins
---

Three systems can all claim to know where your stock is. ERP, the warehouse management system (WMS) and MES/MOM. In a lot of factories, all three are a bit right and a bit wrong at the same time.

The fix is agreeing where each one's responsibility starts and stops, rather than picking one winner.

## What each one is for

**ERP** owns inventory as a business asset. Quantities by item and site, valuation, purchasing, receipts, shipments, and the stock that planning relies on. It's the financial truth.

**WMS** owns inventory in the warehouse. Exact bin locations, putaway strategies, pick paths, wave planning, cycle counts, dock and yard, and any automation such as conveyors or AS/RS. It's the physical truth *inside the warehouse walls*.

**MES/MOM** owns inventory on the shopfloor. Line-side stock, kits, work in progress (WIP), what was consumed by which order, and which lot went into which product. It's the truth *at the point of use*.

I covered the shopfloor side in [MES functionality: logistics and warehousing](/post/mes-functionality-logistics). This article is about the boundaries.

## Which option fits your warehouse?

There are several options for warehousing. For the most complex requirements, particularly distribution centres, a WMS is the most advanced option and adds the most value. It makes the most sense when you have:

- High volumes and complex pick strategies
- Warehouse automation to control
- Multiple storage zones with different rules: temperature, hazardous, high-value
- A distribution operation alongside manufacturing

For simpler warehousing, ERP combined with the inventory and logistics capability of a MOM platform can be enough, with MOM running material from receipt to the line.

## The boundary that matters: the line

The messy part is the handover between warehouse and production. Let's walk through it.

**Replenishment.** The line needs material. Who asks for it? There are two good options. MES/MOM can raise the request, because it knows what's running, what's next and what's left line-side, so replenishment follows real consumption or kanban signals. Or ERP or a WMS can plan it from upcoming orders, picking and staging material ahead of time, which keeps warehouse work planned and suits stable schedules.

**Delivery.** The warehouse picks and moves the material. WMS (or ERP) manages that task and records that stock left the warehouse.

**Receipt line-side.** MES/MOM takes ownership. From here, it tracks the lot at the line, in a [supermarket](/post/mes-functionality-inventory) or at the machine.

**Consumption.** MES/MOM records what was actually used, by order and by lot. That flows back to ERP for stock and cost.

**Output.** Finished goods are created and labelled in MES/MOM, then put away in the warehouse and handed over to ERP or WMS.

::block supermarket-flow

## Where it goes wrong

- **Backflushing hides reality.** ERP deducts standard quantities when output is declared. Scrap, overuse and substitutions disappear. Record actual consumption in MES/MOM where it matters.
- **Line-side stock is a black hole.** Material leaves the warehouse and "vanishes" until the next stock count. Give it a location in MES/MOM.
- **Two systems manage the same bins.** If WMS and MES/MOM both think they own the supermarket, they'll both be wrong. It needs clear ownership and handover in both directions.
- **Quality status doesn't travel.** A lot put on hold by quality must be blocked in every system that could move or consume it. More on that in [QMS and MES](/post/qms-and-mes-quality).

## A simple test

Pick a component and ask three people where all of it is right now: the warehouse manager, the line supervisor and the finance controller. Do the answers match?
