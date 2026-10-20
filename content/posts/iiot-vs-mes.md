---
title: "Why IIoT doesn't replace MES"
short: "IIoT vs MES"
description: "IIoT platforms sound cooler than MES. But connecting sensors is a small part of running a factory. Where IIoT fits, where MES/MOM fits, and why you need both."
published: 2026-10-16
category: education
art: signal
---

Some companies market themselves as IIoT platforms when they don't have enough functionality to be a full MES.

To be fair, it's great marketing. IIoT sounds much cooler than MES. Kudos.

But it creates real confusion for buyers, so let's untangle it.

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

## Collecting machine data is table stakes for MES

An MES isn't really an MES unless it can collect shopfloor data from devices, sensors and equipment. That's the basics.

So when an IIoT platform positions itself against MES, it's comparing one small part of MES to the whole thing.

## The pattern I see

A manufacturer invests heavily in an IIoT platform. Hundreds of sensors connected. Beautiful dashboards of real-time machine data.

Then they realise they still can't manage a production order, enforce a quality inspection, trace a lot of material or schedule maintenance. Because that was never what IIoT was for.

So they either build those functions on top, which is effectively building a homegrown MES, or they buy an MES/MOM and integrate the two. Either way, they've done some of the work twice.

## How to make IIoT projects succeed

IIoT absolutely has value. The projects that deliver it share a few traits:

- **They're connected to operations.** IoT inside MES/MOM, or feeding it, delivers far more than a standalone platform, because the data gets context.
- **They focus on data quality.** The right sensors, properly calibrated, with data validated before it's trusted.
- **They start small.** Bottleneck assets first, then scale across the site.
- **They take security seriously.** Connecting OT equipment to networks without proper cybersecurity is asking for trouble.

It's not about how many devices you connect. It's about how effectively you use the data to improve operations. And MES/MOM is what adds the context that makes the numbers meaningful.

## Complementary, not competing

IIoT and MES/MOM work together. IIoT feeds data into MES/MOM, a historian or a data platform. MES/MOM turns it into managed operations and contextualised data. A data platform makes it available for analytics and AI.

Don't let buzzwords confuse the architecture. If you need MES functionality, you need an MES.

How is your IIoT project going, and can it tell you which order was running when that sensor spiked?
