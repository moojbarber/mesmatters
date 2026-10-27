---
title: "The smart factory tech stack, system by system"
short: "The smart factory tech stack"
description: "ERP, PLM, APS, MES/MOM, WMS, CMMS, LIMS, historians and data platforms. What each system does, where the boundaries sit, and how they fit together."
published: 2026-08-18
category: education
art: stack
---

Your IT landscape isn't, and shouldn't be, a single system. But it shouldn't be lots of systems stitched together either. You need to get the balance right.

A smart factory runs on several applications working together. The skill is knowing what each one is for, where the boundaries sit, and when you actually need it. Get that wrong and you either over-buy or stretch a system into a job it was never designed for.

Let's go through it layer by layer.

## The enterprise layer

**ERP (Enterprise Resource Planning)** runs the business. Finance, procurement, sales orders, costing, high-level planning and inventory valuation. It's where production orders are usually created, based on demand and stock. More in [What is ERP?](/post/what-is-erp)

**PLM (Product Lifecycle Management)** holds the product definition. Engineering designs, specifications, bills of materials, changes and their approvals. It's the source of truth for what a product *is*. More in [PLM, ERP and MES](/post/plm-erp-mes-digital-thread).

**APS (Advanced Planning and Scheduling)** produces detailed, constraint-based schedules when ERP's planning isn't enough. Useful where you have complex sequencing, shared resources or tight changeover constraints. More in [APS vs ERP scheduling](/post/aps-vs-mes-scheduling).

**EAM (Enterprise Asset Management)** manages physical assets across their whole life, including their costs, for asset-heavy businesses with advanced needs. ERP often covers the asset register, depreciation and capital spend already, so check what it does first. Day-to-day maintenance belongs in either a MOM platform or a standalone CMMS. A MOM platform is preferable, because it keeps production and maintenance on the same data. More in [CMMS vs EAM vs MES](/post/cmms-vs-eam-vs-mes).

## The operations layer

**MES/MOM** runs the factory. It receives orders from ERP, executes them on the shopfloor, enforces quality checks, tracks inventory and traceability, supports maintenance, guides operators and sends actuals back. I explain the distinction between MES and MOM in [MES vs MOM](/post/mes-vs-mom).

It sits at the heart of the stack, because it's the system that connects the business to the machines, and the departments to each other.

Alongside it, depending on how much depth you need:

- **WMS (Warehouse Management System)** for complex warehousing: optimised picking, storage strategies, automation, yard and dock management. It's the most advanced option for the most complex warehousing, particularly distribution centres. For simpler warehousing, ERP or the inventory capability of MOM can be enough, but it really depends on the situation. More in [WMS vs MES vs ERP](/post/wms-vs-mes-inventory).
- **LIMS (Laboratory Information Management System)** for lab testing, sample management and certificates, mainly in lab-heavy, regulated industries. Most manufacturers don't need one. More in [LIMS and MES](/post/lims-and-mes).
- **QMS (Quality Management System)** for enterprise quality processes: complaints, CAPA, audits, document control. A good MOM platform covers most of this alongside shopfloor checks and SPC, with serious non-conformances and CAPA escalated into ERP, which replaces the need for a separate QMS. More in [QMS vs LIMS vs MES](/post/qms-vs-lims-vs-mes).

## How they connect

The systems above can be integrated through ERP, directly to MOM, or a mix of both. In the middle sits MOM, covering production, quality, inventory and maintenance on one set of data. Pick a pattern, an application or a part of MOM to see what it does and what flows where.

::block integration-map

## The connectivity layer

Below the operations layer sit the machines, PLCs and sensors, and the connectivity that links them upwards: OPC UA and MQTT, sometimes a separate IIoT platform, and occasionally a unified namespace. MES/MOM often provides that connectivity itself. I explain those in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

The golden rule here: don't connect ERP directly to machines. ERP needs aggregated data at sensible intervals, such as confirmations, consumption and scrap, not raw machine signals. Turning one into the other is MES/MOM's job.

## The data layer

**Historians** store high-frequency time-series data: every temperature reading, every pressure, every second. They're needed where engineers want every reading; often MES/MOM already records the data that matters. More in [Historian vs MES](/post/historian-vs-mes).

**Data warehouses, lakes and platforms** bring data together from MES/MOM, ERP, historians and other sources for reporting, analytics and AI.

I go into those in [Historians, data lakes and data fabric](/post/manufacturing-data-platforms).

## How it fits together

Two ways of looking at it help.

**Vertically**, it's the [ISA-95](/post/isa-95-explained) stack. Orders, schedules and master data flow down from ERP. Actuals, consumption and quality results flow up from the shopfloor. Each layer works at the level of detail it needs.

**Horizontally**, it's the flow of a customer order through the factory: from product design in PLM, to the order in ERP, the schedule in APS, execution and quality in MES/MOM, storage in WMS, and shipment back through ERP.

## Questions to ask about each system

For every system in your landscape, ask:

- Is the functionality we already have enough for our requirements here?
- If not, do we need more depth in an existing system, or a dedicated application?
- Where exactly is the boundary, and what data crosses it, how often, at what level of detail?
- Who uses it, and how many applications will they need to open to do their job?

Don't skip that last question. Every boundary you add is an integration to build and maintain, and often another screen for an operator.

It's not a one-size-fits-all approach. It changes with your processes, your scale and your budget. But it pays to make long-term, deliberate decisions and pick applications that will grow with you.

Which system in your landscape is doing a job it was never designed for?
