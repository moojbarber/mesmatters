---
title: "OT cybersecurity for MES/MOM: what operations leaders need to know"
short: "OT cybersecurity"
description: "MES/MOM sits between IT and OT, which makes it a security boundary. The practical basics: zones, conduits, access, patching, cloud and recovery."
published: 2026-10-16
category: advice
art: gates
---

MES/MOM sits in an awkward place for security. It talks to ERP and the cloud on one side, and to PLCs, SCADA and machines on the other. That makes it both a bridge and a boundary.

Security used to be something IT handled and operations tolerated. That doesn't work any more. Ransomware has stopped production lines for days and weeks. When it happens, it's an operations problem, with an operations-sized bill.

I'm not a security specialist, and you'll need one. But here's what I think every operations and digital leader should understand.

## IT and OT are different

In IT, the priority is usually confidentiality: protect the data. In OT, the priority is availability and safety: keep the line running, and don't hurt anyone.

That changes how you do security. You can't patch a PLC on a Tuesday afternoon because a bulletin came out. You can't run an aggressive network scan that knocks over a 20-year-old controller. Some machines run operating systems that went out of support a decade ago, and they'll stay in service for another decade.

Security for MES/MOM has to respect that.

## Zones and conduits

The core idea in **IEC 62443**, the main OT security standard, is to group assets into **zones** with similar security needs, and control the **conduits** between them.

In practice, for a typical plant:

- **Enterprise zone.** ERP, email, office IT, cloud services.
- **Industrial DMZ.** A buffer between IT and OT. Nothing passes straight through; it stops here first.
- **Site operations zone.** MES/MOM, historians, the operations side of your data platform.
- **Control zones.** SCADA, PLCs and machines, often split by line or area.

MES/MOM usually lives in the site operations zone, with tightly controlled conduits up to ERP through the DMZ and down to the control zones. The rule of thumb: no direct connection from the enterprise network to a PLC, ever.

You'll often hear this described with the Purdue model levels. Same idea, different vocabulary.

## Where MES/MOM projects create risk

Every integration in this series is a conduit. Every one of them is a potential path in. A few that come up often:

- **Remote vendor access.** Support connections left permanently open "for convenience". Use controlled, logged, time-limited access instead.
- **Cloud connectivity.** Cloud MES or analytics needs data to leave the plant. Make connections outbound-only from OT where you can, through the DMZ, and never expose control systems to the internet. I discuss deployment choices in [Cloud, on-premises or hybrid](/post/cloud-vs-on-premises-mes).
- **Shared accounts.** "Line1 / Line1" on every shopfloor terminal. Individual logins matter for security and for your audit trail. Badge or quick sign-in makes it practical.
- **Flat networks.** Everything on one network because it was easier. One infected laptop then reaches every machine.

## Basics that matter more than tools

You can spend a fortune on OT security products. These basics matter more:

1. **Know what you have.** An asset inventory of everything on the OT network. You can't protect what you don't know exists.
2. **Control access.** Individual accounts, least privilege, and multi-factor authentication for remote and privileged access.
3. **Patch on a plan.** Not instantly, but deliberately. Test patches, schedule them in maintenance windows, and protect what can't be patched with segmentation.
4. **Back up, and test the restore.** Including MES/MOM configuration, recipes and PLC programs. Keep a copy offline.

## Plan for the bad day

Assume that one day something will get through. What then?

Can the plant run if MES/MOM is unavailable for 24 hours? For a week? What's the manual fallback for order execution, traceability and quality records? Who decides whether to disconnect from the enterprise network?

These are operations decisions, not just IT ones. Rehearse them, the same way you'd rehearse a fire drill.

## Regulation is catching up

In the EU, **NIS2** brings many manufacturers into scope for cybersecurity obligations, including incident reporting and management accountability. Other regions are moving the same way. If you sell into critical supply chains, your customers will increasingly ask how you secure your operations.

So, here's a question for your next leadership meeting: if ransomware hit the plant tonight, who makes the call to isolate the shopfloor, and do they know it's them?
