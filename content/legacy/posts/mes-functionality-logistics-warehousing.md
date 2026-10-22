---
title: "MES Functionality: Warehouse Management"
slug: "mes-functionality-logistics-warehousing"
legacyUrl: "https://www.mesmatters.com/post/mes-functionality-logistics-warehousing"
description: "Inventory and logistics in warehousesTracking inventory movements in real-time allows manufacturers to optimise stock, reduce WIP (Work In Progress), and ensure that inventory is available when and where it is needed. Managing the flow of inventory in warehouses, between warehouses, and across the boundary into the production area is a crucial part of any inventory system. Logistics operations at a high level includes the following: • Receiving stock from suppliers and storing it in a warehouse."
published: "2023-07-13T14:46:22.884Z"
updated: "2026-10-17T09:00:00.000Z"
author: "Matthew Barber"
categories: ["MES Education"]
heroImage: "/images/legacy/b75fc5_dd7d8d21cc2b41deb5fe95aa20cd4580-mv2.png"
wordCount: 2386
---

## Inventory and logistics in warehouses
Tracking inventory movements in real-time allows manufacturers to optimise stock, reduce WIP (Work In Progress), and ensure that inventory is available when and where it is needed. Managing the flow of inventory in warehouses, between warehouses, and across the boundary into the production area is a core part of any inventory system.

Logistics operations at a high level includes the following:

- Receiving stock from suppliers and storing it in a warehouse.
- Managing inventory in warehouses.
- Moving stock to production when it is required, either manually or with automated replenishment rules.
- Returning unused stock back to a warehouse.
- Moving finished inventory to a warehouse for storage before shipping.
- Picking inventory from the warehouse and loading it onto a lorry for delivery.

Warehousing operations are performed by the Logistics team within the factory. It's common for the Logistics team to operate forklift trucks, and use handheld mobile barcode scanners to complete transactions.

## Warehouse Management
Warehouse management can be handled in one of three systems:

1. **ERP -** Enterprise Resource Planning
2. **WMS -** Warehouse Management System
3. **MES -** Manufacturing Execution System

Each of these approaches has positives and negatives, and it's important to consider what works best for your factory, I can not stress strongly enough that it is not a one-size-fits-all approach. You need to approach this modelling challenge with an open mind, and ensure anyone you take advice from understands the pros and cons of each solution. I come from a world of MES, but I often recommend ERP or WMS for warehousing depending on the customer situation. The best advisers I've worked with lay out the strengths of each option before they recommend one.

|  |  |  |
| --- | --- | --- |
| ​ | **Pros** | **Cons** |
| **ERP** | ERP is the master of inventory and responsible for stock levels.    ERP often has reasonable warehousing and logistics functionality baked in.    ERP is a fundamental system, you don't need to buy another system (providing you don't need an MES for production activities). | ERP screens are usually designed for office users rather than warehouse operatives.   ERP lacks advanced functionality provided by a dedicated WMS.   ERP needs to handover ownership of inventory to MES when it moves out of warehouse and into production (or when inventory is returned to a warehouse). If the applications aren't pre-integrated this could introduce complications and effort in interfacing.   ERP often manages inventory at a "Lot" level, which lacks granularity and detail. This may be important to you depending on your traceability requirements. |
| **WMS** | WMS has advanced warehousing functionality that could be beneficial for some manufacturers. WMS is particularly strong in distribution.   WMS is often more user-friendly than an ERP for operational users, geared up for mobile scanners.   Good for manufacturers with a complex supply chain, fast moving warehouses, and warehouse automation. | Consider whether your functionality can be covered with ERP, or an MES if you have/need one. A WMS is an extra cost, an extra system to train users on, and another set of interfaces to transfer data.   WMS can be overkill for many warehouses.   Some manufacturers need a WMS for their finished goods warehouses, but could consider a simpler, option in their goods in and other warehouses. |
| **MES** | When MES responsible for warehouses, it simplifies moving inventory across the boundaries between warehousing and production and means the logistics team only need to use one application (because MES is used in production).   MES is typically the most user-friendly application for operational users (followed by WMS, then ERP). Look for an MES that runs on handheld mobile scanners.   MES can be paired with Automated Storage and Retrieval Systems (ASRS) for automated warehouse management without needing to invest in a full-blown WMS. ASRS use AGV (Automated Guided Vehicle) robots to move inventory around warehouses. | MES is only an option when the manufacturer needs an MES for other operational functionality (such as production, or quality). It wouldn't make sense to consider an MES just to manage stock in the warehouses.   MES is typically only good for more general warehousing and logistics requirements, in general both ERP and WMS have more advanced functionality.   Some MES systems are narrow in scope and don't support warehousing and logistics functionality (focussing more on production activities). Limited systems like this are probably worth steering clear of during the selection process. |

## Key Functionality

#### Receiving Goods In

Inbound deliveries arrive at the goods in warehouse, for example:

- Raw material delivery from suppliers.
- Internal stock transfers from other plants.
- Customer returns.

Inbound deliveries are orchestrated by ERP. If MES is responsible for the goods in warehouse then ERP shares information about upcoming inbound deliveries with MES via an interface. The logistics team then receive the inventory using MES, and MES confirms back to ERP that the delivery has been received.

MES manages the stock in the warehouse, and can perform inspections on the incoming material.

If WMS handles this process then there needs to be an interface between ERP and WMS.

If ERP handles this process then there needs to be a set of interfaces further down the process to hand inventory over to MES in production, from the ERP warehouse.

It's common to re-label inventory as it arrives in the factory to give it a standard label, and to use the correct material number (rather than the item code provided by the supplier). Re-labelling at goods-in enables more granular tracking of inventory, as sometimes multiple packs of inventory are delivered from the supplier with the same lot code, but no unique identification. Re-labelling allows a unique barcode to be printed for each individual pack which is best practice, and has enormous traceability benefits. It also makes it simpler to move inventory around the factory, and into production.

###### ASN

Depending on the industry, an Advanced Shipment Notice (ASN) may be provided by the supplier, with information about the exact inventory on the delivery. This process is handled by ERP, and again the information about the expected inventory can be shared with MES.

#### Replenishment to Production Lines
Production needs to have enough material to execute the planned production orders. If material is unavailable, the production line stops, affecting the OEE of the production line.

It's possible to manage replenishment manually, often a simple system like pushing an empty container forward to show it needs replacing is used. As the Logistics team move around the factory they spot these empty containers, pick them up, and replace them. This might work well in a smaller factory, where they same materials are always required, but for more complex operations this isn't a workable solution.

Automated replenishment solves this issue by tracking stock at specific locations, and deciding when to move more material based on pre-defined algorithms, some examples include:

- **Re-Order point replenishment**: When the quantity of a material at a specific location is reduced to below the re-order point, a replenishment request is automatically raised to deliver more inventory.
- **Kanban replenishment**: As soon as inventory is removed from a location, a replenishment request is automatically raised to deliver more inventory.
- **Demand based replenishment**: Look ahead at the production order schedule and automatically raise a replenishment request to deliver the next set of materials required for the upcoming demand.

Replenishment to production lines is a key component of inventory operations. MES systems provide tools for managing inventory replenishment to production lines, ensuring that materials and components are available when and where they are needed. By tracking consumption of materials in real-time, MES systems can trigger automated replenishment processes, ensuring that production lines are never starved of the necessary materials to keep running.

#### Put Away
At the end of production, MES creates and labels new inventory. This inventory needs to be handed back to ERP or WMS, depending on which systems is managing the finished goods warehouse. A put-away transaction is the first movement out of the production environment into a warehouse. If MES doesn't own the warehouse, then it is at this point that MES is no longer able to transaction the inventory.

Before putting away the inventory, it may be packed into larger packages referred to as "Handling Units". A handling unit contains multiple pieces of inventory, packaging materials, and could optionally be linked to a physical container. Handling units are a way of packaging together inventory so they can be moved at the same time in a single transaction. The put away transaction could be performed on the handling unit by scanning the handling unit master label. This prevents the logistics team from putting away each pack on the handling unit individually.

###### Guided Put Away
Some applications can perform "guided-put-aways", where the systems recommends to the logistics operator where to put the inventory in the warehouse based on available space and other rules such as whether this material is a high-mover, or already allocated to a customer delivery.

###### Automated Guided Vehicles
AGVs are robots which automatically move inventory around the factory. It is becoming increasingly common for AGV's to handle put away transactions, as well as replenishment.

###### Automated Storage and Retrieval Systems
ASRS applications are dedicated warehouse systems which treat the warehouse as an automated "black box". Inventory is handed over to an ASRS, which puts the inventory away in the warehouse. Later a request is made to retrieve inventory and the ASRS determines which inventory to collect and brings it back out of the warehouse.

ASRS requires the use of AGVs, or uses automated racking systems.

The benefit of using an ASRS is that it can often make use of warehouse space much more efficiently, and of course it reduces the need for logistics operators, and can improve safety.

#### Warehouse Management
When inventory is in the warehouse it is stored in a physical location. It's possible to perform a number of common transactions on inventory.

###### Split
If you have a pallet with 100 pieces on it, you could split this into a pallet of 30 and another pallet of 70. Scenarios include splitting packs to quantities ordered by customers, or splitting inventory into smaller quantities to move to the shopfloor for consumption.

###### Sort
Sorting is a little bit like a split, but the purpose is to separate out quarantined or scrapped pieces. In the example above, the pallet of 70 could be good quantity, and the pallet of 30 could be scrapped.

Sorting can be done as a warehouse transaction, or it can be modelled as a manufacturing operation, where a sorting job is scheduled to take multiple pallets that need to be sorted. If the sorting process takes time then it is preferable to record as a production operation, as the cost of the sort can be recorded and sent back to ERP. For example, the labour time it took to perform the sort.

A sorting operations might consume 5 quarantined pallets, then output 2.7 good pallets, and 2.3 scrap pallets.

###### Merge
If you have multiple partial pallets, merging them together creates a single pallet. Merging may be required when partial pallets exist but customers have ordered full pallets. Or after a sorting process where the good output from multiple sorted pallets are merged back together.

###### Reclassify
Inventory can be reviewed and classified as a different material. This is usually required when the quality or grading of the created material doesn't match the intended material. This is common in processes such as battery production, where the manufacturer attempts to make a grade A battery, but may actually make a lower grade. This lower grade can still be sold, but at a lower price point, so the material number is changed to represent the lower grade item code.

#### Shipping and Picking Customer Orders
Inventory in the warehouse is available to be picked by the logistics team to be loaded on deliveries. These could be:

- Customer Shipments
- Stock Transfers to other plants.

Outbound deliveries are orchestrated by ERP. If MES is responsible for the finished goods warehouse then ERP shares information about upcoming outbound deliveries with MES via an interface. The logistics team then pick the inventory using MES, load the truck, and MES confirms back to ERP that the delivery has been shipped.

By systematising the picking process, manufacturers can reduce the risk of errors and ensure that the correct items are picked and shipped to customers on time.

#### **Stock** Transfer

MES systems also provide tools for managing inventory transfers between warehouses, managing consignment inventory, and managing inventory counts and audits. By providing real-time visibility into inventory levels and movements.

## ERP, WMS or MES/MOM: make an informed choice

There's no single right answer for where warehouse management and replenishment should live. What matters is making the decision deliberately, based on how your warehouse and your lines actually work.

**ERP** is often the right home when the warehouse is simple: a few aisles of racking, straightforward picking, and replenishment on a daily or shift rhythm. You avoid another system and another integration, and stock stays in the system that values it. It gets harder when you need high-frequency line-side replenishment, or more detail than ERP holds about each lot and location.

**A dedicated WMS** earns its place when the warehouse is complex in its own right: high volumes, optimised pick paths, multiple storage zones (temperature-controlled, hazardous, high-value), automation such as AS/RS or conveyors, or a distribution operation alongside manufacturing. Many ERP suites include a WMS module, so it doesn't have to mean another vendor. The trade-off is another boundary to manage, and the risk of line-side logistics drifting away from production.

**MES/MOM** makes sense when most of the movement is driven by production: supermarkets feeding the lines, kitting and kanban, just-in-time replenishment triggered by actual consumption, and finished goods taken off the line. Keeping those flows with production means operators and logistics see the same picture. It's not the tool for running a large distribution warehouse.

Plenty of manufacturers combine them: ERP or a WMS for the main warehouse, and MES/MOM from the supermarket to the line. I go through the boundaries and integration options in [WMS, MES and ERP: who owns inventory once it reaches the line?](/post/wms-vs-mes-inventory)

## Benefits

Using MES to manage warehouse functions enables a number of benefits when combined with other MES functions.

MES has a more detailed view of traceability than ERP. If MES also has visibility of inventory received from suppliers then it can also bring this information into the traceability report, including any inbound quality checks that were performed. This supports investigation into customer complaints or recalls.

Providing you don't require complex warehousing transactions provided by a WMS, using an MES instead can reduce the application landscape by avoiding the need for a third party Warehouse Management System. Preventing the need for additional cost, support, infrastructure, interfacing, training, and maintenance.

Managing all inventory and logistics in a single system improves visibility across the board, and simplifies transactions between warehousing and production, as inventory data doesn't need to be interfaced at the point of handover. With all operations people using the same application, communication is greatly improved, and everyone has visibility of real-time accurate information.

If material shortages exist, but MES knows about upcoming deliveries, this information can be provided to planners in a single system.

Use the act of consuming Inventory to trigger ERP transactions such as stock movements, supplier actions, and Vendor Managed Inventory actions, if ERP is managing the warehouses.

## Summary

MES systems enable manufacturers to optimise inventory operations and make data-driven decisions that improve efficiency, reduce costs, and increase customer satisfaction. MES systems can be used in conjunction with other systems such as ERP and WMS, depending on the requirements of the factory. If you don't have complex warehousing requirements then using MES to manage your warehouses then MES could be a good solution for you.

It's always important to remember that there are many ways to implement solutions, so it's important to get tailored advice for your situation.

This article is part of the [MES functionality series](/post/mes-functionality-inventory-logistics-overview).
