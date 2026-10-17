---
title: "PLM, ERP and MES: where the digital thread actually runs"
short: "PLM, ERP and MES"
description: "How product data gets from PLM to the shopfloor. Why ERP usually sits in the middle, when a direct PLM to MES link makes sense, and how to choose."
published: 2026-10-16
category: education
art: pipeline
---

"Digital thread" is one of those phrases that sounds great on a slide. Product data flows from design to the shopfloor and back again, unbroken.

In practice, the thread has knots in it. And the biggest one is usually the handover between engineering and production.

Let's align on what each system does, and then look at how they connect. Because there's more than one right answer.

## What PLM owns

**PLM** (Product Lifecycle Management) is engineering's system. It holds the definition of what a product *is*:

- CAD models and drawings
- The engineering bill of materials (EBOM)
- Specifications and critical characteristics
- Engineering changes, their approvals and their revision history

It's the source of truth for design. It is not the source of truth for how or where you build it.

## What ERP owns

**ERP** owns the business side of making it. The manufacturing bill of materials (MBOM), routings, costing, purchasing, planning and the production order itself.

The EBOM and MBOM are rarely the same thing. Engineering structures a product by function. Manufacturing structures it by how it's built: sub-assemblies, phantom kits, consumables, packaging, the plant it's made in. That restructuring usually happens in ERP, or in a manufacturing process planning tool sitting alongside PLM. I explain that journey in [EBOM, MBOM, as-built: who owns the BOM at each stage](/post/ebom-mbom-as-built).

## What MES/MOM owns

**MES/MOM** owns execution. Which order is running, on which line, by which operator, with which material lot, and what happened. Counts, scrap, downtime, quality checks, genealogy.

MES/MOM doesn't need the whole product definition. It needs exactly the right slice of it, for the order that's running now.

## ERP usually sits in the middle

In most manufacturers I speak to, the product data reaches the shopfloor through ERP. PLM releases the EBOM to ERP. ERP builds the MBOM and routing, plans the work and releases production orders. Those orders, with their BOM and routing, go down to MES/MOM.

That's a good design. ERP is where costing, purchasing and planning happen, so it *has* to know about every BOM and every change. Routing everything through ERP gives you one controlled path and one place where the order is defined.

But it isn't the only option.

::block plm-erp-mes-options

## When a direct PLM to MES link makes sense

ERP does its job well: items, quantities, operations, cost and the order itself. Carrying a 400 MB 3D model, a 30-step illustrated work instruction or a list of 60 inspection characteristics with tolerances is a different job, and it's one PLM is already doing.

That's where some manufacturers add a direct link from PLM to MES/MOM, alongside the ERP path. ERP still sends the order, BOM and routing. PLM sends the engineering content the operator needs to build it right.

It tends to make sense when:

- **You build complex, highly engineered products.** Aerospace, defence, industrial equipment. Operators need the drawing, not just a part number.
- **Inspection plans come from engineering.** Critical characteristics defined in PLM become the in-process checks in MES/MOM.
- **Change frequency is high.** Where engineering changes land weekly, waiting for them to ripple through ERP adds lag.
- **Work instructions are authored in engineering.** If they live in PLM, it's simpler to publish them from there than to copy them.

If you make high-volume, stable products with simple instructions, the ERP-only route is often all you need. Don't build an integration you won't use.

## The hard part: changes and effectivity

Whichever option you choose, engineering changes are where the thread snaps.

An engineering change order (ECO) gets approved in PLM. Then what? Which orders does it affect? The ones already on the shopfloor? Only new ones? From serial number 1042? From a date? When the old stock of a component is used up?

That's **effectivity**, and it has to be agreed between engineering, planning and production *before* you design the integration. In my experience, most "MES shows the wrong revision" problems aren't technical. Nobody agreed who decides the cut-in point.

A few rules that help:

- **One system decides effectivity.** Usually ERP, because it knows the stock and the open orders.
- **MES/MOM executes against the revision on the order.** Not "the latest" revision in PLM.
- **Direct PLM content is revision-locked.** If PLM sends a work instruction directly, it must match the revision ERP put on the order.
- **Changes mid-order are explicit.** If a change has to hit an order already in progress, MES/MOM should force an acknowledgement at the operation, not quietly swap the drawing.

## Closing the loop back to engineering

The thread should run both ways. MES/MOM knows things engineering never sees: which characteristics drift, which operations generate the most scrap, which revision caused rework.

Some of that goes back through ERP as cost and yield. The rich detail, such as SPC data against a specific characteristic, is more useful sent straight back to the engineers who own the design. That's a third option worth considering once the downward flow is stable.

So, which path is right for you? Ask your operators what they look at when they build a product. If the answer is a part number and a quantity, ERP has you covered. If it's a drawing they had to print themselves, you may need that direct link.
