---
title: "MES Functionality: Production Monitoring"
slug: "mes-functionality-production-monitoring"
legacyUrl: "https://www.mesmatters.com/post/mes-functionality-production-monitoring"
description: "Production MonitoringPerhaps the most fundamental functionality of an MES system is to manage and monitor production operations. Once the production schedule has been released to production, operators are able to start and monitor production runs on production lines. An MES system can manage this process through direct communication with the shopfloor equipment. As a result of managing the process, vast quantities of useful data about the process are collected as a by-product.A production order"
published: "2023-06-08T08:56:01.503Z"
updated: "2026-10-16T09:00:00.000Z"
author: "Matthew Barber"
categories: ["MES Education"]
heroImage: "/images/legacy/b75fc5_a534adcd2fce408680b1a87dc1a3d1ab-mv2.png"
wordCount: 2323
---

## Production Monitoring

Perhaps the most fundamental functionality of an MES system is to manage and monitor production operations.

Once the production schedule has been released to production, operators are able to start and monitor production runs on production lines. An MES system can manage this process through direct communication with the shopfloor equipment.As a result of managing the process, vast quantities of useful data about the process are collected as a by-product.

A production order is the primary context in any MES application. In a good MES system, all key information is tied back to the production order, not just production related information but also quality checks, inventory consumptions and creations, and other critical operational data.

With this in mind, it's important to choose an application that can grow and scale with your operational needs.

For many manufacturers, a production monitoring solution is their first foray into MES. There are many production monitoring, or OEE solutions on the market that are very good, and often cheaper than a full MES system. Just be careful when choosing an application though, because choosing a system without broader MES functionality available is likely to be more costly in the long run as your requirements grow.

As a manufacturing business, the chances are you are heading towards a future where a comprehensive MES is a must-have to be able to achieve operational excellence. Be wary of choosing a cheaper solution now as a stop-gap, only to have to replace it with a full MES in the long run. Recognise the direction you are heading as a business in order to stay competitive in the market, and make decisions with a long term view.

It's important to have a long-term plan when considering the convergence of IT (Information Technology) and OT (Operational Technology) across your manufacturing operations. Think about how your manufacturing operations could benefit from investments in industry 4.0, smart manufacturing, and process automation. What does that vision of the future look like for your organisation? Even if you are just taking small steps into this space to begin with, think about the long term, and make carefully considered decisions with the future in mind.

## Production Monitoring Functionality

#### Production Counts

Production counts are a critical metric for monitoring and optimising production operations in real-time. By tracking the quantity of material produced over time, manufacturers can identify trends and patterns in production output, enabling them to optimise production schedules and resource allocation. By comparing actual production counts against planned production counts, manufacturers can identify and address production inefficiencies, reduce waste, and improve overall productivity. Collecting production counts in real-time enables a current view of production and OEE.

Production can be counted differently depending on the manufacturing process, for example:

- Producing widgets: count each individual widget.
- Producing a batch of material: weigh the batch.
- Stamping out multiple pieces at the same time, or using a tool with multiple cavities: record the number of machine cycles, and let the MES multiple the cycle count by the number of pieces that can be produced each cycle.

More advanced MES systems can also record the same production in multiple units. For example when producing a reel of material it might be important to capture the length of the reel in metres, but also multiply this by the width of the reel to capture metres squared.

#### Scrap Counts

Scrap counts are a measure of the number of units produced that are defective or unusable, or a quantity of waste material.

Tracking scrap is important for identifying and addressing quality issues in the production process. MES systems provide real-time visibility into scrap, enabling manufacturers to identify quality issues as they arise and take corrective action to minimise waste and reduce costs. By analysing scrap counts over time, manufacturers can identify trends and patterns in quality issues, enabling them to take proactive measures to prevent future issues.

Some machines, such as vision systems, or in-line quality gauges can automatically record scrap. If the machine can determine the issue then the reason code should automatically be logged in MES. Sometimes the scrap is automatically recorded, but the operator has to explain the scrap to give the correct reason.

#### Rework Counts

If a defective piece is found, it may be salvageable, if this is the case then often the piece needs to go back through some prior operations in the routing, or needs to go to a specific rework operation to be worked on.

Rework is better than scrap, and is typically only relevant for discrete and assembly manufacturing processes, and usually for higher value items.

Even in the item can be reworked, this still has an impact on productivity and costs. A common metric used is First-Time-Through-Quality (FTTQ). If 100 pieces are produced and 3 need rework then the FTTQ figure is 97%. If one of those pieces needs further rework then the FTTQ figure is still 97%, second rework passes don't contribute to the FTTQ figure. Having said that, the OEE figure will be reduced, as more time was spent working on the same piece, and costs will increase further due to the additional work required.

#### Downtime

Downtime is a measure of the amount of time that production equipment is not in operation due to equipment failure, maintenance, lack of resources, or other factors. Downtime is a major contributor to lost productivity and increased costs. MES systems provide real-time visibility into downtime, enabling manufacturers to identify and address issues as they arise. By analysing downtime over time, manufacturers can identify trends and patterns in equipment failures, enabling them to take proactive measures to prevent future downtime.

Often it's the frequent short stops that have a bigger impact on performance than the longer stops. A long downtime is less likely to occur, for example a breakdown or a resourcing issue. These are impactful and should be addressed, but the real killer is short stops causing production to stop frequently for the same reason, because then the operator is constantly interrupted with minor downtime and has to spend time getting the machine running again. Identify any repeating short machine stop reasons to try and boost long term machine availability.

Without real-time automated data capture from the machine, these short stops can often go unnoticed. It's unlikely the operator will manually record stops of just a few seconds, or sometimes of just a few minutes. Collecting data automatically opens the door to immediate efficiency improvements that were often invisible to management before. As a result, you should expect your OEE to significantly decrease when you first implement an MES, because you will start to see the true figures for each production line.

#### Labour

Labour is a critical component of production operations, and labour costs represent a significant portion of overall production costs. MES systems provide real-time visibility into labour utilisation, enabling manufacturers to optimise resource allocation and reduce costs.

It's important to consider whether each user has their own account for the MES system, or whether a shared login is used. Individual accounts is preferable to be able to allocate resources more effectively, review performance, and limit functionality by user or qualifications. However you may get push back from some areas of the business, or from unions.

#### Overall Equipment Effectiveness (OEE)

OEE is a measure of the productivity of production equipment. OEE is calculated by multiplying availability, performance, and quality rates.

It's such an important topic that it has it's own [OEE blog post.](/post/what-is-oee-overall-equipment-effectiveness).

#### Executing Production Orders

Executing production orders is a critical aspect of production operations. MES systems provide real-time visibility into production orders, enabling manufacturers to monitor and optimise production schedules. By tracking the progress of production orders, manufacturers can identify potential bottlenecks or issues that may impact production output. MES systems also provide tools for managing and scheduling production orders, enabling manufacturers to optimise resource allocation and ensure on-time delivery.

For more information about production orders scheduling, see this article...HERE

## Prevent, don't just record

Some people think MES just records what happened. That's a limited view.

A good MES prevents problems. It validates actions in real time, catches deviations as they happen and enforces a standard way of handling exceptions. The wrong material can't be consumed. An order can't start without its first-off check. A stop can't be closed without a reason.

If your system isn't doing that, you're just documenting failures after the fact. Some manufacturers spend a lot on systems that do nothing more than create a digital paper trail.

Production monitoring is the production pillar of MES/MOM. On its own it's valuable. Connected to quality, inventory and maintenance on the same data, it's far more powerful, which is the point I make in [MES vs MOM](/post/mes-vs-mom).

## Automated vs Manual Data Collection

Most production information can be captured manually through operator interaction, or automatically by connecting directly to the shopfloor equipment.

Automated data collection is always preferable because it:

- Is captured in real-time, giving real-time visibility of the process and improving reactivity, and prevention measures.
- Is accurate, as there is no scope for the operator entering the data incorrectly, or missing seemingly insignificant data such a many recurring short machine stops for the same reason.
- Saves the operator time by collecting the data directly from the machine, without any operator input.

## Data Capture

The data captured is immensely valuable for continuous improvement activities.

MES data is captured at a much finer granularity than ERP, and sent back to ERP as aggregated data. This is excellent news for your ERP system, as the ERP shouldn't have lots of transactional data, it just needs the summarised information for costing and planning purposes.

Data captured by MES is a valuable source of input data for AI (Artificial Intelligence) and ML (Machine Learning) algorithms.

The industry standard for collecting data is OPC (Open Platform Communication). There are two flavours of OPC:

- OPC DA (Data Access): This is old technology now and not recommended for security purposes. It used DCOM for communication between servers.
- OPC UA (Unified Architecture): This is the new standard everyone should be adopting, it's inherently safer and uses certificates to authenticate.

Other standards also exit, but are far less common, for example:

- MQTT: A publish and subscribe message queuing service, typically for IoT (Industry of Things) data collection.
- MT Connect: Used in some manufacturing facilities to capture data from equipment, most commonly used in the automotive industry.

## Shopfloor Control

Further connection to machines is also possible in more advanced production processes. For example, MES is able to control the production process by connecting with the shopfloor equipment. When the operator starts to execute a production run in MES, the instructions on how the machines should behave to execute that job can automatically be sent to the equipment. This ensures the machines have the correct parameters set, and running the right program.

So MES can read data from machines, but also send instructions back to control the production process.

## Benefits of Production Monitoring as part of a broader MES solution.

Some of the primary reasons for investing in a production monitoring solution which is part of a broader MES application are:

1. **Digitising the manufacturing process:** Remove paperwork from the shopfloor, and allow real-time communication of the schedule to production. Business processes can be enforced through workflows, ensuring everyone is behaving in a consistent way, and exceptions are always escalated and managed correctly.
2. **Real-Time Visibility and Insights across all operations:** Implementing a Production Monitoring OEE solution provides real-time visibility into the performance of machines, production lines, and overall manufacturing operations. It enables manufacturers to track critical metrics, such as availability, performance, and quality, allowing for timely intervention and decision-making. Access to accurate and up-to-date insights empowers businesses to identify bottlenecks, optimise production processes, and improve overall operational efficiency.
3. **Enhanced Productivity:** By monitoring OEE, manufacturers gain valuable insights into the utilisation of their equipment and identify opportunities to maximise productivity. The solution helps uncover potential causes of downtime, such as equipment breakdowns, changeovers, or maintenance issues, allowing proactive measures to be taken. By minimising unplanned downtime and optimising production cycles, businesses can achieve higher throughput, reduce lead times, and increase overall productivity.
4. I**mproved Quality and Reduced Waste:** Production Monitoring OEE solutions enable businesses to monitor the quality of output in real-time. By capturing data on defects, rejections, or deviations from quality standards, manufacturers can identify root causes and implement corrective actions promptly. This leads to a reduction in product defects, waste, and rework, ultimately improving product quality and customer satisfaction. This is further supported when using an MES system that also covers quality operations as the production data and quality data are closely coupled.
5. **Performance Benchmarking and Continuous Improvement:** A robust Production Monitoring OEE solution provides the ability to benchmark performance across different machines, shifts, or production lines. By comparing OEE metrics, businesses can identify best practices, areas for improvement, and set performance targets. This data-driven approach fosters a culture of continuous improvement, enabling businesses to optimise processes, enhance equipment effectiveness, and strive for operational excellence.
6. **Resource Optimisation:** Effective resource management is critical for manufacturing businesses. Production Monitoring OEE solutions help identify opportunities for better utilisation of resources, including labour, materials, and energy. By analysing OEE data, manufacturers can make informed decisions regarding resource allocation, shift scheduling, and equipment maintenance, ensuring optimal use of available resources and minimising waste.
7. **Cost Reduction and Return on Investment (ROI):** Investing in a Production Monitoring OEE solution can deliver significant cost savings in various ways. By reducing downtime, improving productivity, and optimising resources, businesses can achieve operational efficiencies that directly translate into cost savings. Additionally, the data-driven insights provided by the solution enable better decision-making, minimising risks, and optimising inventory levels. Ultimately, these factors contribute to a positive ROI and long-term financial benefits for the business, especially when coupled with broader MES functionality at the same time, or in future.

## Conclusion

MES production operations play a crucial role in optimising manufacturing processes by providing real-time visibility and insights into key metrics such as production counts, scrap counts, downtime, labour, OEE, and executing production orders. With the help of MES systems, manufacturers can gain a deep understanding of their production operations, make data-driven decisions, and take proactive measures to address issues that arise. By leveraging MES systems, manufacturers can reduce costs, increase productivity, and improve overall efficiency. Ultimately, integrating MES systems into production operations can help manufacturers remain competitive and thrive in an increasingly complex and competitive marketplace.

This article is part of the [MES functionality series](/post/mes-functionality-inventory-logistics-overview). Related: [What is OEE?](/post/what-is-oee-overall-equipment-effectiveness) and [Manufacturing KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee).
