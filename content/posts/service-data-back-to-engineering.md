---
title: "Closing the loop: service data back to the shopfloor and engineering"
short: "Service data loop"
description: "When a product fails in the field, the answer is often in the as-built record. How service, ERP, MES/MOM and PLM connect to turn failures into fixes."
published: 2026-09-24
category: thought-leadership
art: orbits
---

Most talk about the digital thread runs one way: from design, through planning, to the shopfloor. But the thread should keep going after the product ships. Out to the customer, and back again.

Because when a product fails in the field, the most useful question is: what was different about the ones that failed?

And the answer is very often sitting in your MES/MOM.

## The systems at the far end of the thread

After shipment, product data spreads across a few places:

- **Field service management (FSM)** handles service visits, technicians, parts used and the fault found.
- **ERP** usually holds the installed base, warranty, service orders, returns and the cost of all of it. Many ERP suites include the service module.
- **PLM** owns engineering change requests: the formal route to fix the design.
- **QMS**, or the quality capability of MOM, owns complaints and CAPA.

And **MES/MOM** holds the [as-built record](/post/ebom-mbom-as-built): which component lots and serials went into each unit, which operator built it, which machine, the measurements recorded, any rework or deviations.

## The typical failure investigation

A customer reports a failure. Service replaces a component. A few weeks later, another. Then five more.

Someone in quality pulls the serial numbers. Then the hard part starts. Which component lot was in each of those units? Which supplier? Were they all built on the same line, the same week? Was there a deviation or rework on any of them? What were the torque values?

If MES/MOM has a proper as-built record, those answers take minutes. If it doesn't, they take weeks of digging through paper travellers. Or they're never found at all, and the fix becomes "replace the component on every unit", the most expensive answer available.

## How the loop connects

The serial number is the key that joins everything. A connected loop works like this:

1. **Service records the failure** against the unit's serial number, with the failed part and the fault.
2. **ERP links it** to the installed base, warranty and order history. Service orders and returns are business transactions, and they belong in ERP.
3. **The as-built record answers what's common.** Component lots, suppliers, build dates, machines, operators, process data. That's MES/MOM's contribution.
4. **The fix goes to the right owner.** A design weakness becomes an engineering change request in PLM. A process issue becomes a CAPA and a change on the shopfloor. A supplier issue goes to supplier quality.
5. **Containment uses the same data.** Which other units, in the field or in stock, share the suspect lot? Recall those, not everything.

## Integration options

Again, there's more than one way to wire it.

**Through ERP.** Service data lives in ERP. Genealogy from MES/MOM is posted to ERP as serial and lot relationships. Investigations run from ERP. Simple, and it works well if ERP holds the serial-level genealogy you need.

**ERP plus a genealogy query into MES/MOM.** ERP and service hold the case. When an investigation needs depth (process values, measurements, rework history), the team queries MES/MOM directly, or through a [data platform](/post/manufacturing-data-platforms) that combines both. ERP doesn't need to store every torque value. It needs to know where to look.

**Direct feedback to engineering.** Field failure trends and the matching build data go straight to the engineering team's PLM environment, alongside the formal change request. Engineers see not just "it failed" but "it failed on units where this characteristic ran near its upper limit".

Most manufacturers I speak to start with the first and grow into the second. The third is where real design improvement happens.

## Make it a habit, not a crisis

This loop shouldn't only run during a recall. Field data, linked to build data, can tell you every month:

- Which suppliers' lots correlate with early failures
- Which process parameters predict warranty claims
- Whether a design change actually fixed the problem
- What a quality escape really cost, from scrap to service visit

That last one is powerful when you're building an [MES business case](/post/mes-business-case). The cost of poor quality isn't the scrap bin. It's the technician's van outside a customer's site.

So, pick your most expensive warranty issue from last year. Could you link every failed unit back to how it was built, in an afternoon?
