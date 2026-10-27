---
title: "OPC UA vs MQTT: which one, and when"
short: "OPC UA vs MQTT"
description: "OPC UA brings structured, secure machine data; MQTT moves data efficiently to many systems. How they compare, and how to pick the right one for each job."
published: 2026-07-15
category: education
art: network
---

OPC UA versus MQTT is a debate that comes up regularly. Both are widely used, and they're designed for different jobs. This article compares them, and shows where each one fits.

## OPC UA in one paragraph

OPC UA (Open Platform Communications Unified Architecture) is the industry standard for machine-to-system communication. It's vendor-neutral and platform-independent. Its big strength is the information model: a tag doesn't just carry a value, it carries meaning. This is a temperature, on this machine, in degrees Celsius. Security is built in. The classic pattern is client and server, where a system connects to a machine and reads what it needs, and the standard also defines a publish-subscribe mode.

## MQTT in one paragraph

MQTT is a lightweight messaging protocol. Devices and systems *publish* messages to a central broker, and anything interested *subscribes*. Nobody polls anybody. It's light and copes well with unreliable networks, which is why it's popular for IIoT and edge devices. On its own, MQTT doesn't say what a message means. Sparkplug B adds that, with a defined payload format and a way to track whether each device is online.

## Side by side

| | OPC UA | MQTT |
| --- | --- | --- |
| **What it is** | A full communication standard with an information model | A lightweight messaging protocol |
| **Main pattern** | Client/server, plus publish-subscribe | Publish-subscribe through a broker |
| **Data meaning** | Built in, through the information model | Not defined, unless you add Sparkplug B or your own conventions |
| **Security** | Built into the standard | Through TLS and the broker's authentication |
| **Footprint** | Heavier | Very light |
| **Best at** | Reading structured data from machines and PLCs | Moving lots of data to many consumers efficiently |
| **Native in** | Many modern PLCs and machines | Many IIoT devices, gateways and cloud platforms |

## Where each one fits

**OPC UA is usually the first hop.** Many machines and PLCs speak it natively, and gateways translate older protocols into it. If you want to read structured data from a machine with its meaning intact, OPC UA is the natural choice.

**MQTT can be the distribution layer.** Once data is collected, MQTT moves it efficiently to everyone who needs it: MES/MOM, a historian, a data platform, an analytics tool. Many systems subscribe without each one connecting to every machine.

Both can be used in the same factory. Pick the right one for each job, rather than assuming you need both.

## Where UNS comes in

A unified namespace is an architecture, usually built on an MQTT broker. It's a real-time view of whatever operational data connected applications have published to it, organised by the plant hierarchy: enterprise, site, area, line, machine.

It carries real risks. The sender gets no confirmation that the data arrived or was processed, so data can fail to reach the systems it's meant for without anyone noticing. It keeps no history, and without strict governance it quickly becomes a very big pile of tags with no context. Direct interfaces, which confirm each message, are often the safer choice. More in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

## And MES/MOM?

Connectivity moves data. MES/MOM gives it meaning.

A broker can tell you a machine changed state. MES/MOM knows which order was running, which material, which shift, and that the operator entered the reason as a jam. Where a UNS is used, MES/MOM can consume machine data from it and publish contextualised data to it. More in [Raw machine data is worthless](/post/contextualised-manufacturing-data).

## Questions to ask vendors

- Which protocols do your machines and PLCs support natively?
- Does the MES/MOM connect to OPC UA servers directly, subscribe to an MQTT broker, or both?
- Can it publish its own contextualised events to a broker?
- If you use MQTT, which payload convention: Sparkplug B or something custom?
- How is security handled at each hop?

## My view

I don't think it's a contest. They solve different problems. OPC UA brings meaning and security at the machine. MQTT moves data efficiently to many consumers. Both can sit in the same factory, so pick the one that fits each job.

Which camp are you in, and why?
