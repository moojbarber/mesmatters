---
title: "MRP vs MES: how they differ, and where ERP fits"
short: "MRP vs MES"
description: "MRP works out what to make and buy, and when. MES/MOM runs and records the work on the shopfloor. How they differ, how data flows between them, and why most manufacturers need both."
published: 2026-10-23
category: education
art: gantt
---

MRP and MES sound similar, and both deal with production. So they're often confused, especially by people who've grown up with ERP.

They do very different jobs, on very different clocks.

## What MRP does

Material requirements planning (MRP) is the part of ERP that works out what you need to make and buy, and when. It takes demand, from sales orders and forecasts, and explodes it through your bills of materials. It nets off the stock you already have and what's on order, then uses lead times to suggest planned production orders and purchase orders.

MRP thinks in days and weeks. It mostly assumes infinite capacity, or uses rough-cut checks, which is why many manufacturers add an APS for detailed scheduling.

The output is a plan: make 2,000 of this by Friday, buy 500kg of that by Tuesday.

## What MES/MOM does

MES/MOM takes the orders the plan creates and runs them on the shopfloor. It dispatches work to lines and operators, guides people through the steps, captures what was actually made, scrapped and consumed, records downtime and quality results, and builds the genealogy of every lot.

MES/MOM thinks in seconds and minutes. Its output is the truth about what really happened, with the context attached.

## Side by side

| | MRP | MES/MOM |
| --- | --- | --- |
| **Question it answers** | What should we make and buy, and when? | How is it being made, right now, and what actually happened? |
| **Lives in** | ERP | A shopfloor system between ERP and the equipment |
| **Time horizon** | Days, weeks, months | Seconds, minutes, shifts |
| **Main inputs** | Demand, BOMs, stock, lead times | Orders, routings, machine signals, operator actions |
| **Main outputs** | Planned production and purchase orders | Confirmations, consumption, scrap, downtime, genealogy |
| **Users** | Planners, buyers | Operators, supervisors, quality, maintenance |
| **ISA-95 level** | Level 4 | Level 3 |

## How they work together

The loop is simple in principle. MRP plans the orders. ERP releases them to MES/MOM. MES/MOM runs them and sends back what actually happened: quantities, scrap, material consumed, time taken.

That feedback is what keeps the next MRP run honest. If stock levels, scrap and yields are accurate and timely, the plan is built on reality. If they're keyed in late and rounded, MRP plans from fiction, and planners end up overriding it with spreadsheets.

Master data matters just as much. MRP and MES/MOM both depend on the same BOMs, routings, units of measure and work centres being right. I cover that in [Your ERP master data isn't ready for MES](/post/erp-master-data-for-mes).

## Can MRP run the shopfloor on its own?

Some manufacturers book production straight into ERP at a terminal, typically every hour or at the end of the job or shift. It's a real step forward from paper, and ERP knows the order started and finished.

What it doesn't capture is what happened in between: the short stops, the reason for the scrap, which lot went into which product, whether the check was done. That isn't ERP's job, and it's exactly what MES/MOM is for. More in [MES vs ERP](/post/mes-vs-erp).

How accurate is the data your MRP plans from today?
