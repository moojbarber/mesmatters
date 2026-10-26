---
title: "The ISA-95 model explained, and where MES fits"
short: "ISA-95 explained"
description: "The ISA-95 levels in plain English: what lives at each layer, and how MES/MOM connects ERP above it with the automation below it."
published: 2023-05-10
updated: 2026-10-25
category: education
art: stack
start: 2
---

ISA-95, also known as ANSI/ISA-95 or IEC 62264, is the international standard for integrating business systems with manufacturing operations. It gives manufacturers and software vendors a shared model of how a factory's systems fit together, and what information they exchange.

This article explains the levels, and how data moves between them.

## Where the standard came from

ISA-95 is developed by the International Society of Automation (ISA), a non-profit standards body for industrial automation. Work began in the mid-1990s under ISA's SP95 committee, and Part 1 was published in 2000. The standard has since grown to eight parts, and the core parts are adopted internationally as IEC 62264 ([ISA](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard)).

Its main focus is the boundary between level 3 and level 4: the activities of manufacturing operations, and what ERP and MES/MOM exchange.

## The five levels

The model has five levels, often drawn as a pyramid:

- **Level 0:** the physical production process, meaning the machines and equipment on the shopfloor.
- **Level 1:** sensing and manipulating the process, through sensors and actuators, working in milliseconds.
- **Level 2:** monitoring and control, through systems such as PLCs and SCADA, controlling and supervising the process in seconds.
- **Level 3:** manufacturing operations management, through MES/MOM, working in minutes and shifts.
- **Level 4:** business planning and logistics, through ERP, working in weeks and months.

For most MES/MOM discussions, levels 0 to 2 can be treated together as the control layer that MES/MOM connects to for real-time data.

::block isa95-stack

## How the levels talk to each other

**ERP to MES/MOM.** ERP sends the production order schedule and shared master data, such as bills of materials and routings. MES/MOM then manages execution on the shopfloor.

**MES/MOM to ERP.** MES/MOM reports back what ERP needs: quantities produced and materials consumed. It usually sends a summary rather than every detail, because MES/MOM is better suited to storing and analysing the detailed operational data.

**MES/MOM and the control layer.** MES/MOM reads data from PLCs and other control systems, typically through OPC UA or MQTT. Some MES/MOM platforms also send instructions down, such as starting an order or sending machine setpoints, so operators don't have to enter them by hand. That's usually done by writing to tags through an OPC server, with a handshake that reads the values back and confirms they match what was sent before the machine runs.

The control layer itself is covered in [PLC vs SCADA vs DCS vs MES](/post/plc-vs-scada-vs-dcs-vs-mes), and the protocols in [OPC UA vs MQTT](/post/opc-ua-vs-mqtt).

## A closer look at each layer

**Levels 0 and 1.** The machines, and the sensors that read counts and process values such as temperatures.

**Level 2.** The control systems that run the equipment. PLCs are rugged industrial computers that read sensors and run logic, often programmed in ladder logic, one of the IEC 61131-3 languages. Process plants usually use a DCS, and many sites supervise equipment through SCADA.

**Level 3.** The systems that manage operations. Where there's no MES/MOM, a collection of other applications often fills the space, such as a quality management system (QMS) or a computerised maintenance management system (CMMS). A capable MOM covers what a QMS or CMMS would; narrower MES products often work alongside them. It's worth checking the breadth of any platform when buying, so it can grow with you. More in [QMS vs LIMS vs MES](/post/qms-vs-lims-vs-mes) and [CMMS vs EAM vs MES](/post/cmms-vs-eam-vs-mes).

**Level 4.** The business systems: ERP for finance and planning, alongside supply chain management (SCM) and customer relationship management (CRM) systems. More in [ERP vs MRP vs MES](/post/erp-vs-mrp-vs-mes).

## The four areas of manufacturing operations

At level 3, ISA-95 defines four areas of manufacturing operations management: production, quality, inventory and maintenance. That's the scope of MOM, explained in [MES vs MOM](/post/mes-vs-mom) and [What is MES/MOM?](/post/what-is-mes)

## Vertical and horizontal

Two perspectives help make sense of how systems fit together.

**Vertical** is the ISA-95 stack itself. Data flows up from equipment, through the control layer, into MES/MOM and on to ERP. Instructions flow down. A temperature reading becomes a process parameter in MES/MOM, and eventually part of a monthly report.

**Horizontal** is the flow of work across departments: a customer order moving from design and planning through production and quality to warehousing and shipping. Each step may touch a different system.

## Where IIoT and the unified namespace sit

IIoT lives in the connectivity layer, at levels 1 and 2. It's how data gets from equipment into the systems above. A unified namespace is an architecture for publishing that data, and the contextualised data from MES/MOM, in one structured place. Neither replaces level 3. More in [IIoT vs MES](/post/iiot-vs-mes) and [What is a unified namespace?](/post/unified-namespace-uns)

## Why ISA-95 matters

**A shared language.** ISA-95 gives IT and operations people common terms for the same things, which reduces misunderstanding in projects.

**A framework for data exchange.** It defines what information passes between ERP and MES/MOM, which makes integration more predictable and reduces manual re-keying. Practical patterns are in [Connecting MES/MOM to everything else](/post/isa95-integration-patterns).

Batch process plants usually use ISA-88 alongside it, covered in [ISA-88 and ISA-95](/post/isa-88-and-isa-95).

## My view

ISA-95 is more than 25 years old and still the best map I know of how a factory's systems should fit together. Most integration problems I see come from ignoring its boundaries, such as wiring ERP straight to the machines, rather than from the standard itself.

Where does your factory blur the line between level 3 and level 4?
