---
title: "MES vs ERP: what each one does, and why most manufacturers need both"
short: "MES vs ERP"
description: "ERP runs the business; MES/MOM runs the shopfloor. What each one does, where they overlap, and how they work together in most manufacturers."
published: 2026-06-03
category: education
art: bridge
---

"We've got an ERP. Why would we need an MES?"

It's one of the most common questions in manufacturing software, usually from people who know ERP well and are meeting MES for the first time. The answer starts with what ERP does well.

## What ERP does

ERP runs the business side of a manufacturer on one set of data. Finance, sales orders, purchasing, planning through MRP, inventory valuation and costing. When it's implemented well, leadership sees margin by product and customer, and sales can promise dates based on real stock and lead times.

In manufacturing, ERP is where production is *planned and accounted for*. It creates the production order, holds the bill of materials and routing behind it, and books the result. More in [What is ERP, and why every manufacturer needs a good one](/post/what-is-erp).

## What MES does

MES, and its broader form MOM, runs the shopfloor. It takes the order from ERP and executes it: which line, which operator, which material lot, what was produced and scrapped, and why the machine stopped. MOM extends that across quality, inventory and maintenance on the same data.

It works at the point of work, in real time, with screens designed for operators rather than office users. More in [What is MES/MOM?](/post/what-is-mes)

## Side by side

| | ERP | MES/MOM |
| --- | --- | --- |
| **Main job** | Run the business | Run the operation on the shopfloor |
| **Time horizon** | Months, weeks and days | Shifts, minutes and seconds |
| **Main users** | Finance, sales, planning, purchasing | Operators, supervisors, quality, maintenance, logistics |
| **Production orders** | Creates, plans and costs them | Executes them and reports actuals |
| **Material consumption** | Often backflushed from the BOM | Recorded as it happens, by lot |
| **Data** | Transactions and summaries | Events, measurements, genealogy and test results |
| **Connection to machines** | None, and there shouldn't be | Direct, through PLCs, OPC UA or a connectivity layer |
| **Typical question** | What should we make, and what did it cost? | What's happening right now, and is it right? |
| **ISA-95 level** | 4 | 3 |

## Where they overlap

The overlap is real, and it's where most of the confusion comes from.

**Production orders.** Both systems hold them. ERP owns the order as a business object; MES/MOM owns what happened while it ran.

**Inventory.** ERP owns stock as a financial asset. MES/MOM owns line-side stock, work in progress and what each order consumed.

**Shopfloor reporting.** Many ERPs can record operation completions and quantities, and some ERPs designed with manufacturing in mind cover detailed routings and shopfloor reporting well. That makes the gap to MES/MOM smaller.

What MES/MOM adds is a different layer of data: finer detail, captured in real time at the point of work, with every event tied to its order, batch, machine and operator.

## Can ERP do the job of an MES?

For a small, simple operation, ERP's shopfloor reporting may be enough. Plenty of manufacturers start there.

It stops being enough when you need any of these:

- Real-time data straight from the machines, including short stops
- Lot-level traceability with quality results and process parameters attached
- In-process quality checks and SPC triggered by what's running
- Guided work instructions and error-proofing for operators
- Maintenance working from the same downtime data as production

Standard ISA-95 practice is also not to connect ERP directly to the machines. MES/MOM, or a connectivity layer, sits between them.

## How they work together

The usual pattern:

1. ERP releases a production order, with its BOM and routing, to MES/MOM.
2. MES/MOM dispatches it on the shopfloor and captures what happens as it runs.
3. MES/MOM sends back actuals: quantities produced, material consumed by lot, scrap and labour.
4. ERP uses those actuals for costing, inventory and the next round of planning.

ERP data gets *better* when MES/MOM is in place, because it receives validated actuals instead of estimates. More in [Implement MES to remove complexity from your ERP](/post/mes-simplifies-erp).

Master data is the bit people underestimate. MES/MOM needs more detail than most ERP routings were set up with, so get it right in ERP first, then add any extra detail in MES/MOM where it's needed. See [Your ERP master data isn't ready for MES](/post/erp-master-data-for-mes).

## Deciding where the line sits

A few questions settle most of it:

- Who uses this function: people in the office, or people on the shopfloor?
- How fresh does the data need to be: overnight, or right now?
- Does it need context from the machine, the lot or the operator?
- Does it need more detail than the business needs for costing and planning?

The more answers point to the shopfloor, the more it belongs in MES/MOM.

## My view

You'd never use an MES to do the job of an ERP. So why use an ERP to do the job of an MES? The best-run manufacturers I see don't treat this as ERP versus MES. They treat ERP as the backbone and add MES/MOM where the operation needs the detail.

Where does the line sit in your business today, and is it where you'd draw it if you started again?
