---
title: "MES Functionality: Inventory Management"
slug: "mes-functionality-inventory-management"
legacyUrl: "https://www.mesmatters.com/post/mes-functionality-inventory-management"
description: "TerminologyAs a general concept, inventory is the physical material that exists in the factory, this could be: • Raw materials - received into the factory from suppliers. • Semi-finished materials - created as part of the manufacturing process, with their own unique material number. The materials are not sold to customers, but are consumed into subsequent manufacturing processes. • Finished goods - the final material which is ready to be shipped.Inventory can be tracked and managed at several di"
published: "2023-07-12T14:40:43.726Z"
updated: "2023-11-04T17:24:33.683Z"
author: "Matthew Barber"
categories: ["MES Education"]
heroImage: "/images/legacy/b75fc5_ad26781dd6234a9c85bdd1a51126c7f8-mv2.png"
wordCount: 2943
---

## Terminology

As a general concept, inventory is the physical material that exists in the factory, this could be:

- **Raw materials** - received into the factory from suppliers.
- **Semi-finished materials** - created as part of the manufacturing process, with their own unique material number. The materials are not sold to customers, but are consumed into subsequent manufacturing processes.
- **Finished goods** - the final material which is ready to be shipped.

Inventory can be tracked and managed at several different levels, examples of the different inventory terminology are defined below. These terms can vary by process, industry, and even customer, but the general principles are the same.

#### Inventory

Inventory is a uniquely labelled quantity of material in a location. The unique identifier is a number that represents this specific piece of inventory, it's typically printed onto a barcode label so that inventory transactions can be performed using a mobile handheld barcode scanner device. Inventory is moved around the factory, consumed into the manufacturing process, or created as an output of the manufacturing process.

Examples of inventory include:

- A pallet of cans.
- A reel of cable.
- A box of screws.
- A tote of meat.

#### Serial Items

Serial items are inventory with a quantity of 1. They are typically higher value items, or items which require detailed traceability, or items which need to be uniquely identified so they can be tracked and serviced after being sold to a customer. Examples include:

- A car.
- A printed circuit board.
- An electrical component.

Serial items are more common in discrete environments, it's common for serial items to be engraved with a unique barcode or identifier.


#### Lot

A lot is a unique identifier for a collection of inventory. When inventory is created on a production line, it is often grouped into lots for traceability purposes. The lot number follows an algorithm, here are some examples of when the lot number could change:

- Every day
- Every shift
- Every production order

For example, if 10 pallets of cans are all produced on the same production order, then they would all have the same lot number.

When inventory is shipped to a customer the lot number is provided, this indicates when inventory came from the same lot. When receiving inventory from a supplier, the lot number is tracked. It is common to do a quality check on some of the inventory from the supplier lot. If the quality check passes then it is assumed all inventory in the lot is good to use.

Sometimes the lot number is the most granular identifier of the inventory. For example, if 250kg of a material is received from a supplier, with a supplier lot number of "SL2304", this could consist of 10 bags, each containing 25kgs. If the bags don't have a unique label and identifier, then the only way to identify the traceability is at the lot level.

If more granular traceability is required then the 10 bags can go through a re-labelling processes to uniquely identify each bag with an individual label.

#### Batch

A batch is typically a quantity of material that was produced in a single vessel. This is more common in process industries. For example, a vat of cookie dough. At the beginning of the process, all of the ingredients are put into the vessel, these are then mixed to produce a batch of cookie dough. The batch has a unique identifier which is tracked into future processes. When the cookies are packaged, the batch number is recorded.

#### Handling Unit

A handling unit is a combination of inventory, and packaging materials that are labelled as a single transferable unit.

For example, a handling unit could consist of:

- 3 boxes of material A, each box has a quantity of 10.
- 2 boxes of material B, each box has a quantity of 2, and each item in the box is a serial items.
- Packaging materials.

Each piece of inventory on the handling unit has a unique identifier, and the handling unit itself also has a unique identifier and a label. Scanning the label transacts upon the handling unit. For example, if the handling unit is moved then all pieces of inventory on the handling unit are also moved.

#### Containers

Containers are physical assets in the factory which hold inventory.

Inventory can be loaded onto or off of a container, if the container moves, then the inventory also moves.

It can be important to track containers for a variety of reasons:

- Containers might need to be cleaned, maintained, or inspected after use.
- Containers might have RFID tags to automatically track their location in the factory.
- Containers allow inventory that can't use a physical label to be tracked, for example if the inventory goes through an oven, a label isn't a viable option.
- Some containers might only be valid for specific materials, or processes. Validating the container helps error-proof the process for the operator.

## Inventory on the shopfloor

Inventory is delivered by the Logistics team to the correct location on the shopfloor. This could be directly to the machine that will consume the material, or it could be to a "supermarket" in the production area.

#### Supermarkets

A supermarket (sometimes referred to as a "Shopfloor-Warehouse") is a location on the shopfloor that is kept stocked by the logistics team with fast moving materials, and with materials planned to be used on upcoming production orders. Typically supermarkets have many locations, often one location per material. It is common for materials to be selected from a supermarket in FIFO (First-In-First-Out) sequence. Supermarkets are often loaded from the back, and picked from the front ensuring the materials are taken in correct order.

::block supermarket-flow

By moving inventory from a warehouse to a supermarket in the production area, the lead times for moving inventory to the consuming machine are reduced. Materials required at the machine are replenished from the supermarket, which is closer to production. This also reduces the quantity of materials stored in a line-side location, keeping the shopfloor clean and tidy.

#### Consuming Inventory

Once inventory is available at a line-side location, it is available to be consumed into the process.

Inventory can be pre-allocated to orders, ensuring only the specific planned material is used. For example:

- When inventory created on one operation as semi-finished material needs to be linked to the next specific operation.
- When partial packs of the desired material exist and should be finished before starting to consume new packs.

MES knows about inventory on the shopfloor and can validate it at the point of consumption, checking things like:

- It's in a good state.
- It's a material in the bill of materials for the order.
- It's not exceeded its use-by date.
- It's aged for long enough.
- It's the next pack in FIFO.
- ...

By validating the inventory when it is scanned, MES error-proofs and enforces the business process.

Consumption can be recorded at several levels of detail.

1. **Backflush** - for low value materials that don't need to be tracked, ERP assumes that the quantity defined in the bill of materials is the quantity consumed. The lot that the quantity came from isn't tracked. MES ignores backflushed material, as operators don't need to record anything, ERP handles it.
2. **Lot Traceability** - Inventory traceability is recorded at a lot level. The lot number is recorded, which defines the supplier batch.
3. **Serial Traceability** - The unique serial identifier is recorded in the traceability data.

Lots and serials can be tracked at two levels of granularity:

1. Production Order Level
2. Inventory Level

ERP typically gives traceability at a production order level (although some can work at a finer granularity), whereas a good MES is able to track against the inventory being created on the process for additional detail. This is especially important for processes like assembly, where the exact serials being used are crucial to track.

###### Silos

Some materials can be stored in silos at a line-side location. The silos are topped up with new inventory periodically, and the manufacturing process consumes material from the silo as required.

This is common in many processes, for example injection moulding machines often consume pellets from silos into the process.

###### Kitting

Sometimes multiple consumable materials are picked and collected together in advance of a production order being started. The collection of materials is often referred to as a kit, and can be stored in a container, or on a trolley. The trolley is then moved to the production line ready to be consumed against the planned production order.

This is common in processes such as making printed circuit boards. Reels of input materials (resistors, transistors, etc) are loaded onto a trolley, with each input material placed in the correct position. The trolley is then attached to the side of the machine, with the input materials available to be consumed. As the printed circuit board moves past, the machine automatically dispenses one or more items from each reel and solders it onto the circuit board.

## Key Functionality

#### Inventory Management

Tracking inventory movements in real-time allows manufacturers to optimise stock, reduce WIP (Work In Progress), and ensure that inventory is available when and where it is needed. Managing the flow of inventory in warehouses, between warehouses, and across the boundary into the production area is a crucial part of any inventory system.

Inventory in the production area should always be managed in an MES if you have one. MES has the context of the production order, the material being made, and the bill of materials. This allows MES to consume inventory into the process, create new inventory and print labels, track traceability at a detailed inventory level.

ERP is a mature market, and a lot of people know about ERP. MES is on a trajectory as a rapidly growing market, it's exciting, but it means true knowledge on how these systems play together is limited.

Sometimes this can lead to misunderstandings around where the ERP/MES boundaries can be drawn, even from experienced consultants.

You may hear people say things like "ERP is the master of Inventory, and should be responsible for all Inventory transactions, even on the shopfloor in ERP". I'd urge you to proceed with caution if you hear people say this, it probably means they are inexperienced with MES, remember MES is still a rapidly growing market, people are still learning, and best practices change quickly.

You can read more about the decision making process around boundaries in [this article](https://www.mesmatters.com/post/mes-functionality-logistics-warehousing).

#### Creating Inventory

MES manages the manufacturing process, so it knows all the information required to print a label, for example:

- The production order
- The lot number
- The material
- The quantity

Operators can either manually print a label for the created inventory, or the signal to print a ticket can be picked up automatically from the equipment.

When factories don't have MES they often pre-print labels. This is bad practice, and can lead to mis-labelling, incorrect information on labels, and manual tidy-up actions to rectify data. It's much safer to print labels at the point the inventory is created, with the correct information.

#### Co-Production

A production order from ERP is typically an instruction to make a quantity of a single material.

However, some more complex processes are able to create multiple materials at the same time, examples of this include:

- **Grading**: The process is trying to make a material of a certain quality, some of the pieces created don't reach the specifications for the planned material, but can still be sold as a different material number for a lower value. This can be common in processes like making batteries.
- **By-Product**: The process is making a specific material, but there is waste from the process that can be sold or recycled back into the process. This is common when metal is being cut to size, the waste can often be recycled.
- **Slitting**: A reel of material is being made, and at the end of the process it is being slit into multiple reels of varying widths. For example, a 180cm reel is being slit into 4 daughter reels: 30cm, 40cm, 45cm, 65cm.
- **Ovens**: The oven is performing a recipe "32 hour oven cycle at 600 degrees", but multiple different materials can be treated in the oven at the same time.

Advanced MES systems can handle these co-production scenarios.

#### Creating Work in Progress (WIP)

WIP (Work in Progress) is inventory that exists on the factory floor, it has had some of the operations performed, but still has outstanding operations. MES systems provide tools for managing the creation of WIP inventory, enabling manufacturers to track the progress of unfinished products and ensure that they are completed on time. By tracking WIP inventory in real-time, MES systems can trigger automated processes to ensure that products move smoothly through the production process.

#### Rework

If inventory is not good enough quality then it is scrapped. However, if it is salvageable it could go through a rework process. The rework process involves repeating some prior operations, or alternatively a manual repair operation can be performed.

#### Printing Labels

Labels are crucial for tracking inventory through the factory, labels uniquely identify the inventory, and specify key information such as the material, and quantity. Labels are also used in some processes to track state, although to avoid re-printing labels this is sometimes marked on the label with a pen or sticker.

MES systems provide tools for printing inventory labels, enabling manufacturers to identify and track inventory items throughout the warehouse and production process. By automating the label printing process, manufacturers can reduce the risk of human error and ensure that inventory items are accurately identified and tracked.

#### Managing the State and Location of Inventory

Managing the state and location of inventory is critical for ensuring accurate inventory levels and minimizing the risk of errors. MES systems track the state and location of inventory items, enabling manufacturers to quickly locate inventory and ensure that they are in the correct state for use. By tracking inventory movements in real-time, manufacturers can optimise inventory levels and reduce the risk of stockouts.

#### Traceability

One of the primary reasons for tracking inventory is to get detailed traceability information. Traceability data tracks everything that went into a finished product, all the way through to the raw materials from suppliers. Using an MES allows additional related information to also be added to the traceability information. For example:

- If the MES also captures quality inspections against the raw material, the semi-finished material, or the finished goods then this information is available in the traceability report.
- If the production process captures parameters like pressures, temperatures, speeds these can be tracked back to the inventory and visible in the traceability report.

Of course, this isn't true for all MES systems, but in general MES is able to capture information at a much more detailed level of granularity than ERP, and if the MES manages all factory operations (rather than using different systems in different departments) then you can get synergistic benefits from the breadth and scope of data captured.

If complaints are raised by a customer, this will be tracked back to the inventory consumed into the process, validating quality check results, and the supplier batch information for raw materials.

## Benefits

Using MES to manage inventory functions enables a number of benefits when combined with other MES functions.

MES has a more detailed view of traceability than ERP, as it often tracks inventory at a more granular level of detail. This is helpful for supporting investigation into customer complaints or recalls, allowing full bi-directional traceability.

Using an MES can reduce work in progress (WIP) stock, through accurate Inventory management, resulting in potential cost savings.

Using MES for production, inventory, and quality allows all results to be tracked at an inventory and production level. The quality of Inventory can be tested and verified, identifying issues early, reducing customer complaints.

MES can eliminate errors by preventing invalid consumption based on various validation rules. These rules also help reduce waste by prioritising the oldest materials to be consumed first, for example using FIFO.

The accuracy of ERP data can be improved by reporting back the actual quantities used, as an alternative to back-flushing. ERP often issues material to an order before it leaves the warehouse, whereas in reality by the time material arrives at the production line this information may be out of date, or perhaps the sequence ERP assumes isn't what really happens on the shopfloor. MES eliminates this ambiguity by recording and validating exactly what is consumed.

MES bring improved efficiency and reduces waste by printing labels on demand. There is no need to print labels in advance, this minimises mislabelling by avoiding the need to pre-print labels or use a separate application or Excel spreadsheet where incorrect selections can be made. Print the correct label, with the correct information, on the correct template, to the correct printer, every time.

## Summary

In conclusion, MES plays a critical role in managing and optimising inventory operations on the shopfloor. By providing real-time visibility into inventory levels and movements, MES enables manufacturers to make data-driven decisions that improve efficiency, reduce costs, and increase customer satisfaction. Key inventory processes such as warehouse management, replenishment to production lines, consumption of materials, creating WIP, creating inventory, printing labels, managing the state and location of inventory, receiving goods in, shipping, and picking customer orders are all important components of an MES system's inventory operations. By implementing an MES system for inventory operations, manufacturers can improve inventory accuracy, reduce costs, and increase customer satisfaction.
