---
title: "Connecting MES/MOM to everything else: integration patterns that last"
short: "Integration patterns"
description: "Point-to-point, middleware, event-driven or UNS. How to connect MES/MOM with ERP, PLM, WMS and QMS, and choose a pattern that survives upgrades."
published: 2026-10-01
category: advice
art: network
---

Ask anyone who has run an MES project where the time went, and integration will be near the top of the list. Not because it's technically complicated, but because getting the right people to decide what data actually needs to be moved, and how it needs to be mapped, is time consuming. And then you have to maintain it forever, through upgrades on both sides.

This article pulls together the patterns behind the rest of this series: [PLM](/post/plm-erp-mes-digital-thread), [CPQ](/post/cpq-to-shopfloor), [WMS](/post/wms-vs-mes-inventory), [APS](/post/aps-vs-mes-scheduling), [QMS](/post/qms-and-mes-quality), [EAM](/post/eam-cmms-and-mes) and [LIMS](/post/lims-and-mes).

## Start with ISA-95, not with technology

ISA-95 gives you a common language for what flows between business systems (level 4) and manufacturing operations (level 3). I explain the model in [What is ISA-95, and where does MES fit?](/post/isa-95-explained)

::block isa95-stack

The useful part isn't the diagram. It's the discipline. For every integration, agree:

- **What object is moving?** An order, a material lot, a quality result, a downtime event.
- **Which system owns it?** One owner. Everyone else holds a copy.
- **What triggers the move?** An event, a schedule, a request.
- **How fresh does it need to be?** Seconds, minutes or overnight changes the design entirely.
- **Does the sending system need confirmation?** Does it need to know the receiving system processed the data successfully, or hit an error? For most transactions it does, and that rules some patterns out.

Get those answers for every flow before anyone mentions an API.

## ERP is usually the hub

In most manufacturers, ERP sits between MES/MOM and the other business systems. Product data comes from PLM *via* ERP. Orders come from ERP. Inventory, cost and quality status go back to ERP. That's a sound design. ERP has to know about all of it anyway.

There are exceptions. Throughout this series I've described cases where a direct link alongside ERP makes sense: engineering drawings from PLM, high-frequency replenishment with a WMS, rich non-conformance data into a QMS, where one is used, in-process lab results from LIMS. The rule I'd suggest:

> **Business transactions go through ERP. Execution detail can go direct when speed or richness demands it.**

A direct link is an addition to the ERP path, not a bypass of it.

## The four patterns

**Point-to-point.** System A calls system B directly. Easy to understand, and often the safest option: the sending system gets a response from the receiving system, so it knows each message arrived and was accepted. As the number of systems grows, so does the number of links to maintain when either side changes.

**Middleware or integration platform.** An integration layer (an ESB, or a cloud iPaaS) sits in the middle. Each system connects once. Mapping, routing, retries and monitoring live in one place, in exchange for another layer to run and maintain.

**Event-driven.** Systems publish events ("order released", "lot on hold", "machine stopped") and anyone interested subscribes. Producers don't need to know who's listening, which decouples the systems and suits near real-time flows. The flip side is that the publisher doesn't know whether anyone received or processed what it sent.

**Unified namespace (UNS).** An event-driven pattern applied to the plant: a single, structured hierarchy (usually on MQTT) where systems publish their current state and others can subscribe. It has real limitations for business data. The sender gets no confirmation that the data arrived or was processed, there's no history by default, and it needs strong governance of the hierarchy, plus a broker to run and secure. I explain the basics, and the alternatives, in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

These aren't mutually exclusive. A common mix: direct links for transactional flows between MES/MOM and ERP, where a confirmed response matters most, with an integration platform or a UNS where many systems need the same data.

## Transactions vs telemetry

One distinction that saves a lot of pain:

| | Transactions | Telemetry |
| --- | --- | --- |
| Examples | Order release, goods issue, production confirmation, quality status | Machine states, temperatures, counts, alarms |
| Must arrive | Exactly once, in order, acknowledged | Latest value matters most |
| Typical pattern | Integration platform, APIs, guaranteed messaging | UNS, MQTT, OPC UA |
| If lost | Stock or cost is wrong | A gap in a trend |

Be wary of anyone who wants to push ERP transactions through the same "fire and forget" path as sensor data. Losing a temperature reading is annoying. Losing a goods issue means your stock is wrong until the next count.

## Design for the upgrade

The integration you build today will outlive at least two upgrades of every system it touches. A few habits that help:

- **Use standard, supported APIs.** Avoid writing directly to another system's database. It will work until the day it doesn't.
- **Keep mapping logic out of both endpoints.** Put it in the integration layer, where it can be changed without touching either system. It's [configure, don't customise](/post/configure-dont-customise) applied to integration.
- **Monitor and alert.** A failed message should page someone, not wait to be found at month end.
- **Make it replayable.** When something fails, you need to resend from the point of failure without creating duplicates.

How many of your current integrations would survive an ERP upgrade without anyone touching them?
