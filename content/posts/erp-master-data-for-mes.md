---
title: "Your ERP master data isn't ready for MES"
short: "Master data for MES"
description: "MES/MOM needs more detailed master data than ERP was set up with. Why routings built for costing aren't enough, and how to fix master data once."
published: 2026-05-28
category: advice
art: bridge
---

Your ERP and MES/MOM should share master data: materials, production orders, bills of materials, routings and more, depending on the scope of the MES.

Otherwise you're maintaining the same data in several places. Not a recipe for success.

But please don't assume your existing ERP master data is good enough.

## MES needs more detail

MES/MOM is a more detailed application for factory data. That's why you're investing in it: to get a granular, real-time view of the factory.

So guess what. The master data needs to be at a level that supports it.

Most ERP implementations had enough to worry about. Often the routing detail was set to what costing needed, and nothing more. That's not a criticism. It's what was needed at the time, based on the information available.

But MES/MOM needs to know things like:

- Which machines or lines each operation can actually run on
- Realistic cycle times and setup times, by product and machine
- Which materials are consumed at which operation, not just in the order overall
- Units of measure that convert correctly between operations
- Which quality checks apply at which step

If ERP has one generic operation called "Production", MES/MOM has nothing to work with.

## Fix it once, for everyone

A part of any MES/MOM project is getting the ERP master data right. That often means improving materials, BOMs and, most commonly, routings.

The principle is simple. The system of record for each piece of master data needs enough detail for every application that relies on it. Not just MES/MOM, but warehouse, maintenance and planning systems too.

Fix it at the source, once, and let it flow to everyone who needs it. Where a specialised application needs extra detail, add it there.

## Plan for it early

The most successful projects I've seen don't assume their data is MES-ready. They invest time to clean and standardise materials, BOMs and routings early, rather than trying to fix it later in the project.

If you're implementing or upgrading ERP, and you're looking ahead to MES/MOM, think about this now. Otherwise you'll do the master data work twice.

## Don't rush it

Master data isn't glamorous. Everyone wants to get to real-time OEE, automated traceability and SPC. But those all sit on top of the basics.

Rushing data preparation to get to the exciting functionality is one of the most common causes of delay and rework I see. Get the data right first. Everything else follows.

Where do you see the most confusion around master data between ERP and the shopfloor?
