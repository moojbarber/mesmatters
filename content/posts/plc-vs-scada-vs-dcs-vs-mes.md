---
title: "PLC vs SCADA vs DCS vs MES: the automation stack explained"
short: "PLC vs SCADA vs DCS vs MES"
description: "PLCs control machines, SCADA supervises them, a DCS controls whole process plants, and MES/MOM manages the operation above them all. What each layer does, where they overlap, and how they connect."
published: 2026-10-24
category: education
art: stack
---

PLC, SCADA, DCS and MES all sit between the machine and the business, and all of them show data on a screen. So it's easy to see why they get confused, and why people ask which one they actually need.

The simplest way to separate them is by layer. Each one does a different job, at a different speed.

## PLC: controlling the machine

A **PLC** (programmable logic controller) is a rugged industrial computer that controls a machine or a section of a line. It reads sensors, runs its program in a continuous scan, often every few milliseconds, and drives motors and valves.

PLCs sit at ISA-95 levels 1 and 2, right next to the equipment. They're built to run for years without stopping, and they keep running whether or not anything above them is connected. Most machines you buy come with one.

## SCADA: supervising the equipment

**SCADA** (supervisory control and data acquisition) sits above the PLCs. It collects data from them and shows operators and engineers what the equipment is doing. It also raises alarms and lets people change setpoints. It's common in discrete plants, and across utilities spread over large areas.

SCADA sits at ISA-95 level 2. Its focus is the equipment, in real time.

## DCS: controlling a process plant

A **DCS** (distributed control system) does a similar job to PLCs and SCADA combined, but is designed as one integrated system for large, continuous or batch process plants. Control is distributed across controllers around the plant, with operator consoles in a central control room. It holds temperatures, pressures, flows and levels at their setpoints, continuously.

Many DCS platforms include a batch manager that runs recipes in line with the ISA-88 batch standard. A DCS spans ISA-95 levels 1 and 2, and it's the heart of most chemical and pharmaceutical plants.

The line between a DCS and a PLC-plus-SCADA system has blurred over the years. As a rough guide, a DCS is chosen for large, tightly integrated process control, and PLCs with SCADA for machines and lines.

## MES/MOM: managing the operation

**MES/MOM** sits above the control layer at ISA-95 level 3. It manages the operation rather than the equipment. It takes orders from ERP and guides operators through the work. It records what was made and what went into it, along with downtime and its reasons, quality results and the genealogy of every lot.

Its focus is the order, the material, the people and the evidence. Its time scale is minutes and shifts.

## Side by side

| | PLC | SCADA | DCS | MES/MOM |
| --- | --- | --- | --- | --- |
| **Main job** | Control a machine | Supervise equipment | Control a process plant | Manage the operation |
| **ISA-95 level** | Levels 1 and 2 | Level 2 | Levels 1 and 2 | Level 3 |
| **Time scale** | Milliseconds | Seconds | Milliseconds to seconds | Minutes to shifts |
| **Typical users** | Controls engineers | Control room operators, engineers | Control room operators, process engineers | Operators, supervisors, quality, planners |
| **Knows about** | Signals and logic | Equipment states and alarms | Process variables, recipes | Orders, materials, quality, downtime reasons |
| **Typical setting** | Every machine | Discrete plants, utilities | Large process plants | Every plant that wants to run on facts |

## Where they overlap

**Visibility.** SCADA, a DCS and MES/MOM can all show what a machine is doing. Often they read the same data from the same PLCs. Where SCADA is used mainly for visibility, MES/MOM can sometimes cover it. More in [SCADA vs MES: what each one does, and do you need both?](/post/scada-vs-mes)

**Recipes.** A DCS batch manager runs the control steps of a recipe. MES/MOM manages the order and material side: which lots are used, and the batch record. The boundary is the batch, and getting it right matters in regulated industries. More in [ISA-88 and ISA-95: how the two standards fit together](/post/isa-88-and-isa-95).

**Sending data down.** Some MES/MOM platforms send setpoints and recipes to the machine, as well as reading data up. That should always go through the control layer, which keeps responsibility for safe operation.

## Doesn't the control layer already do this?

It does some of it. But PLCs, SCADA and a DCS are designed to control equipment, not to manage orders, material status, quality release or genealogy across the plant.

Some sites stretch the control layer to do more through custom code. It can work, but it pushes business logic into systems that weren't designed for it, and every change then carries control-system risk and validation effort.

## How they connect

Data flows up from the control layer to MES/MOM, often through OPC UA or MQTT. MES/MOM adds the context of the order and the lot, then passes what the business needs to ERP. Instructions flow down the same path.

That's the ISA-95 model in practice. More in [ISA-95 explained](/post/what-is-the-isa-95-model-and-where-does-mes-fit) and [OPC UA vs MQTT](/post/opc-ua-vs-mqtt).

## Which do you need?

- **Every plant** has PLCs, because the machines come with them.
- **Large process plants** almost always run a DCS.
- **Discrete plants and utilities** often use SCADA to supervise their equipment.
- **Anyone who wants to manage orders, quality and traceability on facts** needs MES/MOM above the control layer.

If batch records are still assembled on paper, or downtime reasons still live on a whiteboard, it's the MES/MOM layer that's missing, not more control.

Which layer in your plant has the least reliable data today?
