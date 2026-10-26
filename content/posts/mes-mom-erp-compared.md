---
title: "ERP, MES, MOM and the rest of the stack: what each one does"
short: "The manufacturing systems stack"
description: "ERP, MES, MOM, APS, WMS, QMS, LIMS, EAM, PLM, SCADA and IIoT side by side: what each one does, what data it owns, and whether you need it."
published: 2026-10-15
category: education
art: stack
guide: true
---

Every factory runs on more than one system. The confusion starts when the acronyms overlap and nobody agrees where one system's job ends and the next one's begins. Vendors stretching their definitions doesn't help.

This guide puts them side by side. If you only read one thing, read the first table. If you're deciding what to buy, the last two tables are the useful ones.

## The short version

**ERP** runs the business. **MES** runs production on the shopfloor. **MOM** runs the whole operation on the shopfloor, covering production, quality, inventory and maintenance on one set of data. Everything else is a specialist that adds depth in one area, connected to those three.

MES and MOM aren't competitors to ERP. They do a different job, at a much finer level of detail, for different people. I explain the difference between the two in [MES vs MOM](/post/mes-vs-mom).

## Side by side

| System | Main job | Time horizon | Main users | ISA-95 level |
| --- | --- | --- | --- | --- |
| **ERP** | Run the business: finance, orders, purchasing, planning, costing | Months to days | Finance, sales, planning, purchasing | 4 |
| **PLM** | Define the product: designs, specifications, engineering BOM, changes | The product's life | Engineering | 4 |
| **CPQ** | Configure and price products for a quote | The sales cycle | Sales, customers | 4 |
| **APS** | Sequence work against finite capacity | Days to hours | Planners and schedulers | 4, sometimes 3 |
| **MES** | Execute production orders and record what happened | Shifts to seconds | Operators, supervisors | 3 |
| **MOM** | Run production, quality, inventory and maintenance on one set of data | Shifts to seconds | Everyone in operations | 3 |
| **WMS** | Run the warehouse: putaway, picking, storage, automation | Hours to minutes | Warehouse and logistics | 3 |
| **QMS** | Enterprise quality: CAPA, complaints, audits, supplier quality | Weeks to months | Quality and compliance | 4, sometimes 3 |
| **LIMS** | Run the lab: samples, methods, results, certificates | Hours to days | Lab analysts, QA | 3 |
| **EAM / CMMS** | Manage assets and maintenance work | Months to hours | Maintenance and reliability | 3 and 4 |
| **SCADA** | Monitor and control equipment in real time | Seconds and below | Control room, process engineers | 2 |
| **IIoT / historian** | Connect equipment and store high-frequency data | Milliseconds to years | Engineers, data teams | 1 and 2, feeding 3 |

The levels refer to [ISA-95](/post/isa-95-explained), the standard for how business and shopfloor systems fit together. Level 4 is business planning, level 3 is manufacturing operations, and levels 0 to 2 are the machines and their control.

## MES vs ERP

This is the comparison I get asked about most.

ERP knows that 500 units of an order should be made this week, from which materials, at what cost. MES/MOM knows which operator ran the line at 2.14am, which lot went into machine 7, why the line stopped for 11 minutes, and whether the torque on station 4 was in tolerance.

| | ERP | MES/MOM |
| --- | --- | --- |
| **Question it answers** | What should we make, and what did it cost? | What's happening right now, and is it right? |
| **Level of detail** | Orders, transactions and summaries | Events, measurements, genealogy and test results |
| **Screens built for** | Office users | Operators at a terminal or tablet |
| **Production orders** | Creates and costs them | Executes them and reports actuals back |
| **Consumption** | Often backflushed from the BOM | Recorded as it happens, by lot |

The two work best together. MES/MOM sends ERP validated actuals instead of estimates, which improves costing, inventory and planning. And some ERPs designed with manufacturing in mind already cover more of the production side, which makes the gap smaller. More in [What is ERP](/post/what-is-erp) and [Implement MES to remove complexity from your ERP](/post/mes-simplifies-erp).

One firm rule: never wire ERP straight to the machines. That's what MES/MOM is for.

## MES vs MOM

MES is the production pillar. MOM is the whole operation.

If a vendor tells you their MES covers everything, ask which of the four ISA-95 areas it actually handles, and how deeply. Production, quality, inventory and maintenance overlap constantly. The operator does a bit of all four, often in the same ten minutes. One platform means the downtime production sees is the downtime maintenance sees, and quality checks are triggered by what's actually running.

## Who owns which data

Most integration arguments I see come down to ownership. Agree this table early and a lot of them disappear.

| Data | Usually owned by | Notes |
| --- | --- | --- |
| Product design and engineering BOM | PLM | The source of truth for what a product *is* |
| Manufacturing BOM and routing | ERP | Restructured from the engineering BOM for how it's built. See [EBOM, MBOM, as-built](/post/ebom-mbom-as-built) |
| Production orders | ERP creates, MES/MOM executes | The order BOM is a copy taken when the order is released |
| Detailed sequence on the day | APS or MES/MOM | ERP's plan mostly assumes infinite capacity. See [ERP, APS and MES scheduling](/post/aps-vs-mes-scheduling) |
| Inventory as a financial asset | ERP | Quantities, valuation, receipts and shipments |
| Inventory inside the warehouse | WMS, or ERP if you don't have one | Bins, picks, cycle counts and automation. See [WMS, MES and ERP](/post/wms-vs-mes-inventory) |
| Line-side stock, WIP and consumption | MES/MOM | The truth at the point of use |
| As-built record and genealogy | MES/MOM | Nobody else is there when it happens |
| In-process quality results and SPC | MES/MOM | Triggered by what's running |
| CAPA, complaints and audits | QMS | Fed by shopfloor non-conformances. See [QMS and MES](/post/qms-and-mes-quality) |
| Lab results | LIMS | Flow back to MES/MOM against the batch. See [LIMS and MES](/post/lims-and-mes) |
| Downtime, run hours and counters | MES/MOM | Shared with maintenance |
| Maintenance work orders and asset history | MES/MOM, or an EAM for asset-heavy operations | See [EAM, CMMS and MES](/post/eam-cmms-and-mes) |
| High-frequency machine signals | Historian | MES/MOM keeps the events, not every reading |

One owner per object. Everyone else holds a copy.

## Do you need it?

Not every factory needs every system. The skill is adding depth where the operation genuinely needs it, and not stretching a system into a job it was never designed for.

| System | You probably need it when | You can probably do without it when |
| --- | --- | --- |
| **MES/MOM** | You're running on paper, spreadsheets or a set of disconnected point solutions, and you want real-time, trustworthy shopfloor data | Honestly, very few manufacturers beyond the smallest |
| **APS** | Sequence-dependent changeovers, shared tools, a bottleneck that drives everything, or hundreds of orders a day competing for resources | A handful of lines with stable products and simple changeovers |
| **WMS** | High volumes, warehouse automation, several storage zones with different rules, or distribution alongside manufacturing | Simpler warehousing, where ERP and the inventory and logistics capability of MOM are enough |
| **QMS** | Your MES doesn't cover CAPA, complaints and supplier quality | Your MOM platform covers the quality system as well as in-process checks |
| **LIMS** | A lab running samples, methods and certificates, common in process and regulated industries | Line-side checks such as weight or pH are enough |
| **EAM / CMMS** | Asset-heavy operations with advanced maintenance, spares and lifecycle cost needs | Maintenance needs are well covered by MES/MOM on the same downtime data |
| **SCADA** | Real control of continuous or safety-critical processes | It's mainly used for visibility that MES/MOM could provide. See [Do you need both SCADA and MES?](/post/scada-vs-mes) |
| **CPQ** | Configured or engineer-to-order products with complex rules | Standard products from a catalogue |

Many ERP suites include APS, WMS, EAM or service modules, so needing the capability doesn't always mean another vendor.

## How they connect

Business transactions usually go through ERP. Execution detail can go direct when speed or richness demands it, such as rich non-conformance data into a QMS, or drawings from PLM to the operator. Have a play with the patterns below.

::block integration-map

I go through the options in [Connecting MES/MOM to everything else](/post/isa95-integration-patterns), and system by system in [The smart factory tech stack](/post/smart-factory-tech-stack).

Which of these boundaries causes the most arguments in your business?
