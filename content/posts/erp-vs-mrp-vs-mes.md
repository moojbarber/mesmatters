---
title: "ERP vs MRP vs MES: what each one does, and how they fit together"
short: "ERP vs MRP vs MES"
description: "ERP runs the business, MRP plans what to make and buy, and MES/MOM runs it on the shopfloor. What each does, and how the three fit together."
published: 2026-10-23
category: education
art: gantt
---

ERP, MRP and MES get muddled all the time. They all deal with production, and two of them often come from the same vendor.

The quickest way to separate them is by the question each one answers.

## What ERP does

**ERP** (Enterprise Resource Planning) runs the business side of a manufacturer on one set of data: finance, sales orders, purchasing, inventory value, costing and, in most suites, HR. It's the system of record for money, customers, suppliers and stock value.

ERP thinks in days to months, and at the level of orders and totals.

## What MRP does

**MRP** (Material Requirements Planning) works out what to make and buy, and when. It takes demand from sales orders and forecasts, explodes it through your bills of materials, nets off stock and open orders, then uses lead times to suggest planned production and purchase orders.

In most companies MRP is a module inside ERP rather than a separate system. Standalone MRP software also exists, usually for smaller manufacturers who don't need a full ERP suite yet. MRP II extended the idea to capacity and other resources, and is where much of modern ERP came from.

MRP mostly assumes infinite capacity, which is why many manufacturers add an APS for detailed scheduling. More in [APS vs ERP scheduling](/post/aps-vs-mes-scheduling).

## What MES/MOM does

**MES/MOM** runs the work on the shopfloor. It dispatches the orders the plan creates to lines and operators, and guides people through each step. It records what was actually made and what went into it, along with downtime, scrap, quality results and the genealogy of every lot.

MES/MOM thinks in seconds and minutes. Its output is the truth about what actually happened, with the context attached.

## Side by side

| | ERP | MRP | MES/MOM |
| --- | --- | --- | --- |
| **Question it answers** | How is the business doing? | What should we make and buy, and when? | What is happening on the floor, and what actually happened? |
| **Usually lives in** | Its own suite | Inside ERP, sometimes standalone | A shopfloor system between ERP and the equipment |
| **Time horizon** | Days to months | Days to weeks | Seconds to shifts |
| **Main outputs** | Financials, orders, stock value, costs | Planned production and purchase orders | Confirmations, consumption, scrap, downtime, genealogy |
| **Users** | Finance, sales, purchasing, planning | Planners and buyers | Operators, supervisors, quality, maintenance |
| **ISA-95 level** | Level 4 | Level 4 | Level 3 |

## MRP vs ERP

If you're a small manufacturer choosing between standalone MRP software and an ERP, the difference is breadth. MRP covers planning and materials. ERP adds finance, sales, purchasing, costing and much more on the same data. Many companies start with MRP and move to ERP as they grow.

Either way, neither one is designed to run the shopfloor in real time.

## How the three work together

The loop is simple in principle. MRP plans the orders. ERP releases them to MES/MOM. MES/MOM runs them and sends back what actually happened: quantities, scrap, material consumed, time taken.

That feedback is what keeps the next MRP run honest. If stock levels and yields are accurate and timely, the plan is built on reality. If they're keyed in late and rounded, MRP plans from fiction, and planners end up overriding it with spreadsheets.

Master data matters just as much. All three depend on the same BOMs, routings, units of measure and work centres being right. More in [Your ERP master data isn't ready for MES](/post/erp-master-data-for-mes).

## Can ERP or MRP run the shopfloor on their own?

Some manufacturers book production straight into ERP at a terminal, typically every hour or at the end of the job or shift. It's a real step forward from paper, and ERP knows the order started and finished.

What it doesn't capture is what happened in between: the short stops, the reason for the scrap, which lot went into which product, whether the check was done. That isn't ERP's job, and it's exactly what MES/MOM is for. More in [MES vs ERP](/post/mes-vs-erp).

How accurate is the data your MRP plans from today?
