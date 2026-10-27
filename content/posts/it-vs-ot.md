---
title: "IT vs OT: why the two worlds think differently, and where MES/MOM sits"
short: "IT vs OT"
description: "IT protects data; OT keeps machines running safely. Why the two worlds think differently, where MES/MOM sits, and how to make convergence work."
published: 2026-06-24
category: education
art: bridge
---

Put an IT manager and a controls engineer in the same room and ask them to plan a software update. You'll quickly see why IT/OT convergence is talked about so much and achieved so rarely.

Neither side is wrong. They're optimising for different things.

## Let's align on some terminology

**IT (information technology)** is the world of business systems: ERP, email, office applications, data centres and the cloud. It manages information.

**OT (operational technology)** is the hardware and software that monitors and controls physical equipment: PLCs, SCADA, DCS, sensors, drives and the machines themselves. It manages physical processes.

In [ISA-95](/post/isa-95-explained) terms, OT lives at levels 0 to 2 and IT at level 4. Level 3, manufacturing operations, sits between them. That's where MES/MOM lives.

## Side by side

| | IT | OT |
| --- | --- | --- |
| **First priority** | Confidentiality and integrity of data | Availability and safety |
| **Cost of an outage** | Lost productivity, disrupted business processes | Stopped production, scrap, possible safety risk |
| **Typical lifecycle** | Years | Decades |
| **Patching** | Regular, often automatic | Planned around production, sometimes impossible |
| **Timing** | Seconds are usually fine | Milliseconds can matter |
| **Typical owner** | CIO and IT team | Engineering, controls and operations |
| **Change control** | Release cycles | Production windows and validation |

## Why they think differently

**The cost of getting it wrong.** If an office server reboots unexpectedly, people grumble. If a controller reboots mid-batch, you might scrap the batch or damage the equipment. OT engineers are cautious for good reason.

**Age.** Some controllers on a shopfloor run operating systems that went out of support a decade ago, and they'll stay in service for another decade because the machine they control still works perfectly. IT's instinct to upgrade everything on a schedule doesn't fit.

**Timing.** Most IT systems are happy with a response in a second or two. A control loop may need an answer in milliseconds, every time.

**Security.** In IT, you scan networks and patch quickly. In OT, an aggressive network scan can knock over a 20-year-old controller, and a patch may need the line stopped and the process revalidated.

## Why convergence matters now

Smart manufacturing needs data to flow from the machines up to the business, and plans to flow back down. AI and cloud platforms both need shopfloor data to leave the plant safely, with its context intact. None of that works if IT and OT run as separate kingdoms.

Convergence doesn't mean IT takes over OT, or the reverse. It means an agreed architecture, and people on both sides who understand each other's constraints.

## Where MES/MOM fits

MES/MOM is the most IT-like thing on the shopfloor and the most OT-like thing in the IT landscape. It talks to ERP and the cloud on one side and to PLCs and SCADA on the other. That makes it both a bridge and a security boundary.

It's also why ownership of MES/MOM can get political. Some businesses give it to IT, some to operations, and some share it.

## Making it work

- **Agree the architecture together.** IT and operations teams both need to be involved as key stakeholders, and aligned on what connects to what and where the data goes.
- **Use standard connectivity.** OPC UA and MQTT rather than custom interfaces. See [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).
- **Never connect the enterprise network straight to a PLC.** Go through MES/MOM, with controlled connections between the two networks.
- **Put people from both sides on the project team** from the start, not just at sign-off.

## My view

MES/MOM needs both. IT should own the application, infrastructure, integrations and security. OT and operations should own the processes, master data standards, screens and KPIs. In multi-site businesses that blend usually becomes a centre of excellence. More in [Rolling out across sites](/post/mes-multi-site-rollout).

Who owns MES/MOM in your business today: IT, OT, or both?
