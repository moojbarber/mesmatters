---
title: "OPC UA, MQTT and UNS in plain English"
short: "OPC UA, MQTT and UNS"
description: "The shopfloor connectivity layer without the rabbit hole. What OPC UA, MQTT and a unified namespace are, how they relate to MES/MOM, and what to ask vendors."
published: 2026-07-07
category: education
art: network
---

Without a connection to the equipment, MES/MOM is just another application where people type things in. The real value comes from automatic, real-time data exchange with the machines.

That's the connectivity layer. And it's surrounded by acronyms and strong opinions. I won't go down every rabbit hole, but you need enough to have a sensible conversation.

## OPC UA

OPC stands for Open Platform Communications. OPC UA (Unified Architecture) is the modern version and the industry standard for machine-to-system communication.

What makes it useful:

- It's platform-independent and vendor-neutral, so equipment from different manufacturers can be read in a consistent way.
- It doesn't just carry values. It carries structure and meaning: this tag is a temperature, on this machine, in these units. And it has security built in.

If there's one connectivity standard to know, it's this one. Many machines and PLCs support it directly, and gateways can translate older protocols into it.

## MQTT

MQTT is a lightweight messaging protocol. Instead of a system asking each machine for data, devices *publish* messages to a central broker, and any system that's interested *subscribes* to them.

It's simple, efficient and works well over unreliable networks, which is why it's popular for IIoT and edge devices. On its own, MQTT doesn't define what the data means. Extensions such as Sparkplug add that structure.

OPC UA and MQTT aren't really competitors. They're often used together.

## Unified namespace (UNS)

A unified namespace is an architectural idea rather than a product. All operational data is published to one central, structured place, usually an MQTT broker, organised by the plant hierarchy: enterprise, site, area, line, machine.

Systems publish what they know and subscribe to what they need, instead of every system integrating point-to-point with every other.

Done well, it reduces point-to-point integrations and makes data easier to find and reuse. It needs a clear structure and someone to govern it, so the context travels with the data rather than a long list of tags.

## Where MES/MOM fits

Connectivity moves data. MES/MOM gives it meaning.

A UNS can tell you a machine's state changed. MES/MOM knows which order was running, which material, which shift, and that the operator just entered the reason as a jam. That contextualised data is often exactly what other systems want to subscribe to.

So in a UNS architecture, MES/MOM is both a consumer of machine data and one of the most valuable publishers of contextualised operational data. More on why that context matters in [Raw machine data is worthless](/post/contextualised-manufacturing-data).

## A few practical rules

- **Don't connect ERP directly to machines.** ERP needs aggregated data at sensible intervals, not thousands of signals a second.
- **Start with what you'll use.** Connect bottleneck assets and the signals you need for counts, states and key parameters first.
- **Agree a naming standard early.** Asset hierarchies and tag names are dull, and they decide whether the data is usable later.
- **Treat OT security as part of the design.** Not an afterthought once everything's connected.

## What to ask vendors

- Which protocols do you support natively: OPC UA, MQTT, others?
- Can you consume and publish to a unified namespace?
- How do you handle older equipment without modern interfaces?
- How are connections configured: by your team through configuration, or through custom development?

How connected is your shopfloor today, and how much of that data has context?
