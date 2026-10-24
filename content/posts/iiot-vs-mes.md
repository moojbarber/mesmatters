---
title: "IIoT vs MES: why IIoT doesn't replace MES"
short: "IIoT vs MES"
description: "IIoT platforms sound cooler than MES. But connecting sensors is a small part of running a factory. Where IIoT fits, where MES/MOM fits, and why you need both."
published: 2026-06-09
category: education
art: signal
---

IIoT and MES are often compared, and some IIoT platforms are positioned as an alternative to MES. They do different jobs, and most factories that use both connect them. This article sets out what each one is, and how they fit together.

## IIoT is a concept, not a system

IIoT, the Industrial Internet of Things, is about connecting machines, sensors and devices so their data can be collected and used. When people say IIoT, they usually mean OPC UA, and increasingly MQTT.

It's a concept. Many systems help deliver it: IIoT platforms, historians, edge devices and MES/MOM itself.

In [ISA-95](/post/what-is-the-isa-95-model-and-where-does-mes-fit) terms, IIoT lives in the connectivity layer: Levels 1 and 2, the sensors and the control systems.

## MES/MOM is operational management

MES/MOM sits at Level 3. It takes that sensor data and puts it to work:

- It knows which order is running, so a count becomes progress against a plan.
- It knows the material and the lot, so data becomes traceability.
- It knows the quality plan, so a measurement triggers the right check at the right time.
- It knows the maintenance history, so a fault becomes a work request with context.
- It guides and validates what operators do, not just what machines do.

IIoT gives you data points. MES/MOM gives you operational management.

## Data collection is part of MES

Collecting data from devices, sensors and equipment is one of the core functions of MES/MOM. So an IIoT platform overlaps with one part of MES, the connectivity and data collection, rather than with the whole.

## How to make IIoT projects succeed

IIoT has real value. Successful projects tend to share a few traits:

- **They're connected to operations.** IoT data that feeds MES/MOM, or sits inside it, gains the context of the order and the lot.
- **They focus on data quality.** The right sensors, properly calibrated, with data validated before it's trusted.
- **They start small.** Bottleneck assets first, then scale across the site.
- **They take security seriously.** Connecting OT equipment to networks without proper cybersecurity is asking for trouble.

## How they work together

IIoT feeds data into MES/MOM, a historian or a data platform. MES/MOM turns it into managed operations and contextualised data. A data platform makes it available for analytics and AI.

## My view

Some companies market themselves as IIoT platforms when they don't have enough functionality to be a full MES. To be fair, it's great marketing: IIoT sounds much cooler than MES. But it creates real confusion for buyers.

The pattern I see is a manufacturer investing heavily in sensors and dashboards, then realising they still can't manage a production order or trace a lot. So they build those functions on top, or buy an MES/MOM and integrate the two, and do some of the work twice. It's not about how many devices you connect. If you need MES functionality, you need an MES.

How is your IIoT project going, and can it tell you which order was running when that sensor spiked?
