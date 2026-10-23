---
title: "SCADA vs MES: what each one does, and do you need both?"
short: "SCADA vs MES"
description: "SCADA and MES often read the same PLCs. When you need both, when MES/MOM can do the job on its own, and how to decide."
published: 2026-06-23
category: education
art: signal
---

I had a great discussion recently: do you need both SCADA and MES?

My answer: maybe. But not always.

## What each one does

**SCADA** (supervisory control and data acquisition) is for real-time control and monitoring of equipment. Process engineers and control room operators use it to see what the plant is doing and adjust it: setpoints, alarms, valve states, tank levels.

**MES/MOM** is for managing operations: which order is running, what's been produced, what was scrapped and why, whether quality checks were done, what material was used, what maintenance is due. I explain the full scope in [What is MES/MOM?](/post/what-is-mes-and-why-is-it-important-in-manufacturing)

So far, clearly different. But there's overlap.

## Where they overlap

MES/MOM also gives real-time visibility of the shopfloor through PLC connections. Some MES systems offer advanced two-way communication with equipment: sending setpoints and recipes down to the machine, not just reading data up. Some show things like fill levels in tanks and silos.

And often, SCADA and MES are reading the same data from the same PLCs anyway.

## When MES/MOM can do the job on its own

In many discrete and lighter process environments, where SCADA is mainly used for visibility rather than tight process control, MES/MOM can often cover what's needed.

The benefits of rationalising:

- **One system for operators.** A simpler user experience, with production context alongside machine status.
- **A simpler application landscape.** Fewer systems to integrate, maintain and secure.
- **Lower cost.** Fewer licences, less infrastructure, less support.
- **Faster troubleshooting.** When a machine alarms, the order, the material and the operator are right there.

## When you need both

In heavier process industries, SCADA usually stays. Think continuous chemical processes, utilities, complex batch control or anything with safety-critical control loops. There, SCADA and the control layer are doing real-time control that MES/MOM isn't designed for.

In that case, get the boundary clear. SCADA controls the process. MES/MOM manages the operation, receiving the data it needs from the control layer and sending down orders, recipes and parameters where appropriate.

## How to decide

Ask:

- Is SCADA here mainly for **control**, or mainly for **visibility**?
- Are operators using both systems to do their jobs? If so, what are they getting from each?
- Are the two systems reading the same signals from the same PLCs?
- Could MES/MOM provide the visibility operators need, with production context added?

If SCADA is mostly a visibility layer, and operators are switching between two screens to see the same machine, it's worth exploring whether one system will do.

I'm sure plenty of people will disagree with parts of this. So, in your factory, is SCADA doing control, visibility, or both?
