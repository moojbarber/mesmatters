---
title: "DCS vs MES: controlling the process vs managing the operation"
short: "DCS vs MES"
description: "A DCS controls continuous and batch processes in real time. MES/MOM manages orders, materials, quality and records around them. How they differ in process plants, and where batch control and electronic batch records fit."
published: 2026-10-23
category: education
art: tanks
---

In process industries, the distributed control system (DCS) is often the most important system on site. It's been there for decades, the control engineers know it inside out, and it keeps the plant safe and running.

So when someone proposes an MES, the first question is usually: "Doesn't the DCS already do that?"

It does some of it. But they're built for different jobs.

## What a DCS does

A DCS controls the process. It reads sensors and drives valves, pumps, heaters and agitators, holding temperatures, pressures, flows and levels at their setpoints, continuously and in real time. Control is distributed across controllers around the plant, with operator consoles in the control room.

Many DCS platforms include a batch manager, which runs recipes in line with the ISA-88 batch standard: charge this, heat to that, hold, then transfer.

The DCS sits at ISA-95 levels 1 and 2. Its focus is the equipment and the process, second by second.

## What MES/MOM does

MES/MOM manages the operation around the process. It takes orders from ERP, decides which batch runs where, checks that the right materials are available and released, weighs and dispenses, records exactly which lots went into which batch, manages samples and quality results, and produces the batch record.

It sits at ISA-95 level 3. Its focus is the order, the materials, the people and the evidence.

## Side by side

| | DCS | MES/MOM |
| --- | --- | --- |
| **Main job** | Control the process safely and precisely | Manage orders, materials, quality and records |
| **Time scale** | Milliseconds to seconds | Minutes, shifts, batches |
| **ISA-95 level** | Levels 1 and 2 | Level 3 |
| **Users** | Control room operators, control engineers | Operators, supervisors, quality, planners, warehouse |
| **Recipes** | Executes the control steps | Manages the master recipe, order and material side |
| **Materials** | Charges what it's told to | Checks status, weighs, dispenses, records genealogy |
| **Records** | Process data and alarms | Batch record, deviations, quality results |

## Where they meet

The boundary is the batch. MES/MOM releases a batch order with the right recipe and confirmed materials. The DCS executes the control steps. Process data and events flow back to MES/MOM, which ties them to the order and the lots used.

In regulated industries, this is where an electronic batch record earns its keep. Instead of assembling paper and printouts after the fact, the record builds itself as the batch runs, with deviations captured at the time, so review by exception becomes possible. More in [MES/MOM in regulated industries](/post/mes-in-regulated-industries).

## Doesn't the batch manager cover it?

For the control steps, yes. But a DCS batch manager typically doesn't manage material status and genealogy across the warehouse, coordinate sampling and lab results, handle orders and scheduling from ERP, or give the wider plant one place to work.

Some plants stretch the DCS to do more of this through custom code. It can work, but it pushes business logic into a control system that wasn't designed for it, and every change then carries control-system risk and validation effort.

## Which do you need?

If you run a process plant, you almost certainly need a DCS, or a PLC and SCADA combination doing the same job. The question is whether you also need the layer above it. If batch records are still assembled on paper and materials are tracked in spreadsheets, the answer is probably yes.

I cover the related SCADA question in [SCADA vs MES](/post/scada-vs-mes), and the batch standard in [ISA-95 vs ISA-88](/post/isa-95-vs-isa-88).

How much of your batch record is still assembled by hand after the batch has finished?
