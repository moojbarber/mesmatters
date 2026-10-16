---
title: "Getting started with MES: A complete overview to Manufacturing Execution Systems"
slug: "what-is-mes-and-why-is-it-important-in-manufacturing"
legacyUrl: "https://www.mesmatters.com/post/what-is-mes-and-why-is-it-important-in-manufacturing"
description: "IntroductionWelcome to MES Matters. You have landed on the first ever blog post which provides an overview of MES. I hope you find this and the rest of the blog enlightening and interesting. It's time to get stuck in.First things first, let's align on some terminology. The most popular term \"MES\" stands for Manufacturing Execution System, this is still most used and recognised. More recently, people have also started to use \"MOM\" (Manufacturing Operations Management). This new name tries to enca"
published: "2022-08-01T21:43:05.220Z"
updated: "2023-11-04T16:31:08.320Z"
author: "Matthew Barber"
categories: ["MES Education"]
heroImage: "/images/legacy/b75fc5_b6ae7d5b61b54c74a656aada893d08fe-mv2.jpg"
wordCount: 2229
---

## Introduction

Welcome to MES Matters. You have landed on the first ever blog post which provides an overview of MES. I hope you find this and the rest of the blog enlightening and interesting. It's time to get stuck in.

First things first, let's align on some terminology. The most popular term "MES" stands for Manufacturing Execution System, this is still most used and recognised.

More recently, people have also started to use "MOM" (Manufacturing Operations Management). This new name tries to encapsulate the growing scope of traditional MES, which was seen primarily as a production system. As the scope of MES grew to cover all manufacturing operations (inventory, quality, maintenance) some in the industry thought the name didn't accurately reflect the capabilities of the application.

MOM is a more accurate and descriptive name, but it's unfortunate that this divergence has evolved, because now there are two interchangeable terms, which introduces confusion.

Going forward, it's possible there will be a lot more emphasis on smart factory, and smart manufacturing, and perhaps the MES/MOM terms will eventually subside. Time will tell, but for now both MES and MOM are here to stay.

On this blog, I'll use the original MES term as it is still the most popular.

## Overview

MES applications manage all factory operations, including:

- [**Production Operations**](https://www.mesmatters.com/post/mes-functionality-production-monitoring)**:** manufacturing process on the shop floor.
- [**Quality Operations**](https://www.mesmatters.com/post/mes-functionality-quality-operations)**:** quality of the products being produced.
- [**Inventory Operations**](https://www.mesmatters.com/post/mes-functionality-inventory-logistics-overview)**:** inventory and traceability on the shop floor, and management of stock throughout the factory.
- **Maintenance Operations:** asset care of equipment in the factory.

MES is the foundation of Smart Manufacturing, Industry 4.0, and the Digital Factory.

#### Life Before MES

Before MES, manufacturing companies relied on a patchwork of disparate systems to manage different aspects of their manufacturing operations. In some cases these systems would have been software applications, but the processes could have been managed using paperwork and spreadsheets.

Using this approach results in siloed data with limited communication between departments, making it difficult to get a complete picture of what is happening on the shop floor. Ultimately this leads to a lack of visibility, poor data management, inefficient communication, and increased risk of errors.

Manufacturing departments have a degree of overlap in the data that is relevant to them. For example both Production and Maintenance are interested in machine downtime, but if there are two different systems trying to give the same data there could be a conflict. This approach hinders the ability to make data-driven decisions and respond in an agile way.

If connection between applications and systems is important, then integrations between those solutions need to be built to share the data. Integrating solutions is common place, but takes time, and incurs cost. Integrations should be carefully considered to ensure data is moved between systems with an appropriate frequency and granularity of data.

#### Life with MES

With the emergence of MES, these disparate operational systems can be replaced with a single, integrated platform that connects all aspects of manufacturing operations. A single platform for all operations management means:

- Operators, who are at the heart of the process have access to information they need from all departments.
- All users have access to a single-source of truth for all data.
- Powerful cross-departmental functionality can be realised.
- All operations users only need to be trained on one system.
- Integration between systems isn't required, which can sometimes be costly, fragile. and data transfer can be delayed.

## MES Functions

MES covers all manufacturing operations. The scope of each individual MES application will vary, but broadly speaking you can expect to see functionality such as:

#### Production Scheduling

The production plan is typically downloaded from ERP. For complex scheduling requirements an Advanced Planning and Scheduling (APS) application may also be required.

MES receives the production plan, allowing planners to further tweak the schedule (if required), then release orders to production to be executed on the shop floor. MES systems can take into account various factors, such as machine availability, labour capacity, availability of raw materials, and demand forecasts, to help production planners manage the schedule effectively.

When the plan is released to production, operators are able to follow the plan in MES without the need for paper print outs. If the planners need to make real-time adjustments to the schedule, changes are reflected immediately in production without the need for further print outs, or direct communication.

For more information, please see: [Production Scheduling](https://www.mesmatters.com/post/mes-basics-production-scheduling)

#### Production Monitoring

MES plays a crucial role in optimising manufacturing processes by providing real-time visibility and insights into key metrics such as production volumes, scrap counts, downtime, labour, and [OEE](https://www.mesmatters.com/post/what-is-oee-overall-equipment-effectiveness).

MES records key information about the manufacturing process to measure productivity and efficiency. Ideally production operation data is captured directly from plant equipment in real-time, but it can also be captured manually if the required signals aren't available.

MES systems allow manufacturers to gain a deep understanding of their production operations, make data-driven decisions, and take proactive measures to address issues that arise through continuous improvement activities. Manufacturers can reduce costs, increase productivity, and improve overall efficiency ([OEE](https://www.mesmatters.com/post/what-is-oee-overall-equipment-effectiveness)), helping manufacturers remain competitive and thrive in an increasingly complex and competitive marketplace.

For more information, please see: [Production Monitoring](https://www.mesmatters.com/post/mes-functionality-production-monitoring)

#### Quality Control

MES monitors and control the quality of products during the manufacturing process, using a range of techniques such as Statistical Process Control (SPC) and Six Sigma.

Identifying and correcting quality issues early in the process, means manufacturers can reduce the number of defective products, improve customer satisfaction, and avoid costly recalls.

MES has the context of the materials being produced on the line, and knows the quality control plan. With this information, a good MES system will prompt the operators to perform the correct inspections at the right time. Using a separate QMS (Quality Management System) means the context of the production order and material being produced is not available. This means the user needs to manually enter additional data every time an inspection is recorded, with MES this information is known automatically preventing the need to manually enter the data and saving time. MES is also able to ensure the correct specifications are always used.

Some quality checks are performed in-line by the operator, but other checks might require lab equipment, or to be sent off-site for further examination. Samples taken from the line are usually labelled for further testing elsewhere.

Measurements may be entered manually, but more advanced MES systems allow automated collection via metrology equipment such as scales and gauges. This could be through a direct connection from the MES to the equipment, or through a measurement file imported into MES. Automated files imported automatically by the MES reduce manual input from the operators, and to increase the accuracy of data.

For more information, please see: [Quality Operations](https://www.mesmatters.com/post/mes-functionality-quality-operations)

#### Inventory Management

Inventory refers to any moveable quantity of material. For example:

- A box of pieces
- A bag of powder
- A pallet of boxes
- etc

The inventory in the factory is referred to as "stock".

Inventory usually has a label with a unique identifier (barcode), specifying the material, quantity, and other key information about the inventory. MES ensures that the right materials are available at the right time. By tracking inventory levels in real-time and taking into account production schedules and demand forecasts, MES can help to reduce inventory costs.

MES tracks the consumption of materials into the manufacturing process, the creation of output materials, printing labels, and tracking Work In Progress (WIP). Most MES systems track traceability at a much finer granularity than ERP (be warned - many ERP specialists who have had limited exposure to MES will likely refute this point). People who really understand ERP, understand that ERP shouldn't be keeping a detailed record of shop floor transactions, and instead should be allowing MES to record this information, and send back key data to ERP. You can read more about this here: [MES removes complexity from ERP](https://www.mesmatters.com/post/implementing-mes-can-simplify-your-erp)

Logistical operations can also be managed in MES, moving Inventory around the factory, managing the state of inventory, putting inventory away into a warehouse, receiving deliveries into the factory, and picking and shipping outbound shipments. The decision of which system to use in the warehouse is a complex one, there isn't a one-size-fits-all approach that works here, think carefully about what works best for your organisation, or your customers.

For more information, please see: [Inventory & Logistics](https://www.mesmatters.com/post/mes-functionality-inventory-logistics-overview)

#### Maintenance Engineering

MES monitors and manages the maintenance of equipment and machines, ensuring that they are functioning properly and that downtime is minimised. MES should provide alerts when equipment needs maintenance, and schedule maintenance activities during periods of low production to minimise the impact on operations.

Asset care is increasingly becoming the responsibility of the operator, who are often expected to perform autonomous maintenance procedures such as safety checks and cleaning.

Through MES, Maintenance engineers and managers have access to real-time machine status and downtime information, as well as the production schedule.

## MES Benefits

MES is becoming increasingly important in modern manufacturing, it's easy to understand why when you consider some of the key benefits.

#### Digitalisation and Automation

MES is the foundation of Smart Manufacturing, which is currently a hot topic transforming the manufacturing industry. Digitalising the manufacturing process removes paperwork, improves communication, and reduces errors. Factory automation integrated with MES allows advanced processes and data capture, improving productivity and enforcing processes.

#### Improved Visibility

MES provides real-time visibility into all aspects of the manufacturing process, including equipment status, production progress, quality data, and more. This enables companies to make better-informed decisions and quickly identify and address issues as they arise.

MES can provide increased visibility and traceability throughout the manufacturing process, from raw materials to finished products. This can help to identify the source of quality issues or defects, as well as to track and trace products to document full traceability of finished goods.

#### Improved Efficiency and Productivity

MES can help manufacturers to improve their efficiency and productivity by providing real-time information about the manufacturing process. This can help to identify bottlenecks, reduce waste, and optimise the use of resources, resulting in increased output and profitability. MES supports continuous improvement initiatives, enabling data-driven decision making.

#### Better Quality Control

MES can help to improve the quality of products by monitoring and controlling the manufacturing process in real-time. This can help to identify and correct quality issues before they become a problem, ensuring that products meet the required specifications.

#### Compliance with Regulations

Some MES systems can help manufacturers to comply with regulations and standards, such as:

1. Food and Drug Administration (FDA 21CFR Part 11) regulations for pharmaceutical and medical devices.
2. International Organisation for Standardisation (ISO) standards for quality management.

By providing real-time data on the manufacturing process, MES helps manufacturers demonstrate compliance and avoid costly fines and penalties. Some MES solutions also generate Electronic Batch Records (EBRs).

#### Data Analytics

MES provides real-time data on all aspects of the manufacturing process, which can be used for analysis and optimisation. This can help companies identify opportunities for improvement and increase overall efficiency. A good MES system will have advanced built-in reporting and analytics, as well as being able to easily share data with other reporting tools, if required.

MES data is rich, accurate, and interesting data set, perfect for AI (Artificial Intelligence) and ML (Machine Learning). These advanced capabilities are driven by algorithms which are only as good as the data they are built on top of.

## Integration

MES is typically not used as a stand-alone application. The ISA-95 model is a global standard that defines where MES sits in the customer landscape in terms of IT (Information Technology) and OT (Operational Technology).

For more information, please see: [ISA-95](https://www.mesmatters.com/post/what-is-the-isa-95-model-and-where-does-mes-fit)

MES may need to integrate with other applications (ERP, PLM, WMS) as well as factory equipment (machines, metrology equipment).

It's important to consider the boundaries between MES and other systems carefully. Many factors will affect how and where to draw these touch points:

- The functionality in the "other" system.
- The functionality in the MES system.
- The physical manufacturing processes.
- The departmental processes.

## Summary

MES covers all manufacturing operations across the factory: Production, Quality, Inventory, and Maintenance. However, the scope of MES does vary by MES vendor.

By replacing old departmental, or home grown applications, MES provides a single application for factory operations.

As manufacturing continues to evolve, MES will play an increasingly important role in helping manufacturers to stay competitive and meet the demands of their customers.

MES is an incredibly exciting space right now. If you want to learn more, please take a look around the rest of the MES Matters blog.
