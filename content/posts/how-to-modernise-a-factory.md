---
title: "How to modernise a factory, step by step"
short: "How to modernise a factory"
description: "A practical route from paper and spreadsheets to a connected, data-driven factory: what to do first, and how to know you're ready for the next step."
published: 2026-10-20
category: advice
art: ladder
guide: true
---

People ask me some version of the same question all the time. "We know we need to modernise. Where do we actually start?"

There's no single answer, because every factory starts from a different place. But there is an order that works, and most of the expensive mistakes I see come from doing the steps out of sequence. Buying software before mapping the process. Customising the software to match every old quirk.

So this is the route I'd follow, step by step, with a simple test for each one so you know when you're ready to move on.

## Step 1: Be honest about where you are today

Not where the last board presentation said you are. Where you actually are.

One way I look at it is time to truth. Take an example: when a line stops at 2am, how long until the right person knows, and do they know why? The stages run from "eventually" to "without asking". Most factories sit somewhere between eventually and after the fact, and often further back than they'd like to admit. Travellers on clipboards, and a morning meeting that starts with someone reading yesterday's numbers from a notebook. That's "eventually", and it's very common.

You can't plan a route if you're lying to yourself about the starting point. More in [Time to truth](/post/time-to-truth).

**Ready to move on when:** you can describe, with evidence, how data is captured today on each line, and you've agreed a realistic level with the people who run the shopfloor.

## Step 2: Map the process before you buy anything

Digitise a broken process and you get a faster broken process.

Start with the physical structure: enterprise, site, area, line, machine. Then map what really happens, warts and all, rather than what the manual says. I like a swimlane grid with departments across the top and manufacturing processes down the side. Every handoff and every gap becomes visible.

Do it with operators, quality technicians, maintenance engineers and logistics in the room, not just managers. You'll almost certainly find two sites, or two shifts, making the same product in different ways. Decide which way you're going to standardise on before you build it into software. More in [Process before technology](/post/manufacturing-process-mapping).

**Ready to move on when:** you have current-state maps for the site you'll start with, and you've agreed the target process for it.

## Step 3: Put a number on the problem

Leadership approves business impact, not features. So take the pain you found in step 2 and put money on it:

- What do scrap, rework and complaints cost a year?
- What's an hour of lost production on your bottleneck worth?
- How many hours a week go on manual data entry and chasing information?
- How much working capital is tied up in buffers you hold because you don't trust the data?

Then show how the risk will be managed: phased delivery, measures and points where leadership can decide whether to continue. In my experience, fear of overrun and failure is what really blocks most business cases. Address it directly. More in [How to build an MES business case leadership will sign](/post/mes-business-case).

**Ready to move on when:** you have a sponsor with the authority to allocate resources, and a first phase that's funded.

## Step 4: Build the team

The team you build matters as much as the software you choose.

You need an executive sponsor who'll clear the way, a project manager who's properly freed up, IT and operations working as one team, and the right external expertise where you don't have it in-house. Bring in super users from the shopfloor early. If you're a multi-site business, think now about who will own the global standard later, usually a centre of excellence blending IT and OT.

And plan for resistance. Every project meets it, because change is uncomfortable. Involve people in the design and explain why it makes their shift easier. Adoption deserves as much investment as implementation. See [Building the right team](/post/mes-implementation-team) and [Resistance to change is guaranteed](/post/manufacturing-change-management).

**Ready to move on when:** named people have time in their diaries for the project, with their day jobs backfilled where needed.

## Step 5: Fix the master data

This is the step everyone wants to skip.

ERP master data was usually set up for what costing needed. A routing with one generic operation called "Production" gives MES/MOM nothing to work with. You need to know which machines each operation runs on, realistic cycle and setup times, which material is consumed at which operation, and which quality checks apply at each step.

Get it right in ERP first, so every system benefits, then add any extra detail in the specialised applications where it's needed. More in [Your ERP master data isn't ready for MES](/post/erp-master-data-for-mes).

**Ready to move on when:** the materials, BOMs and routings for your first site are detailed enough to run the target process, and someone owns keeping them that way.

## Step 6: Choose a platform for the long term

Now you're ready to talk to vendors, with process maps and real requirements rather than a wish list.

A few principles I'd hold to:

- **Choose for where you're going**, not just today's problem. A cheap tool for one form, then another for the next, swaps paper silos for digital silos.
- **Look at breadth.** Production, quality, inventory and maintenance overlap constantly. One platform on one set of data avoids arguing about whose numbers are right.
- **Configure, don't customise.** Every customisation costs you again at every upgrade.
- **Check the vendor can keep investing.** You'll run this system for a decade or more, and it needs to keep improving in that time.

Use the [12 questions](/post/how-to-choose-an-mes) to structure the evaluation, and put the system in front of one of your operators before you sign.

**Ready to move on when:** you've seen the system run your process, in a demo built for your type of manufacturing, and your operators have used it.

## Step 7: Start with one site, with the end in mind

Commit to a whole site rather than a single production line. Within that site you can still phase what you switch on first. Often the best first move is removing the paper that hurts most: quality check sheets, downtime logs, work instructions or travellers.

Phasing doesn't mean narrow-minded. The end state should still be clear on day one, even if you only use part of the platform at first. That's the difference between a first phase that scales and one that becomes another silo. More in [Going paperless](/post/paperless-manufacturing).

**Ready to move on when:** the first site runs on the new system every shift, including nights and weekends, with no paper fallback.

## Step 8: Connect the machines

Automatic data capture is what turns MES/MOM from a place where people type things in into a real-time view of the factory.

Start with your bottleneck assets. Detect stops automatically and let operators add the reason while it's fresh. Most people are genuinely surprised when they first see their micro-stops. More on the connectivity options in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

And treat every new connection as a security decision. MES/MOM sits between IT and OT. Keep the enterprise network away from the PLCs.

**Ready to move on when:** downtime and output on the bottleneck come from the equipment, not from memory at the end of the shift.

## Step 9: Go live, then keep going

Go-live is the starting line. Plan hypercare with extra support on every shift, including nights, and super users who are visible and have time to help. Fix things quickly enough that people keep trusting the system.

Then measure what the business case promised, against the baseline you set before you started, and share the results. That evidence keeps leadership committed and funds the next phase. More in [Go-live is the starting line](/post/mes-go-live).

**Ready to move on when:** you can show the improvement you promised, in numbers leadership accepts.

## Step 10: Scale with a template

Once the first site works, turn what you built into a template: standard processes, master data rules, KPIs, screens and integrations. Roll it out site by site, allowing local differences only where there's a genuine reason. Later sites go much faster. See [Rolling out across sites](/post/mes-multi-site-rollout).

## The checklist

| Step | You're ready to move on when |
| --- | --- |
| 1. Know where you are | Data capture on each line is described with evidence, and everyone agrees the time to truth by area |
| 2. Map the process | Current-state maps exist for the first site and the target process is agreed |
| 3. Put a number on it | A sponsor is in place and the first phase is funded |
| 4. Build the team | Named people have the time, with day jobs backfilled |
| 5. Fix the master data | Materials, BOMs and routings can run the target process, and have an owner |
| 6. Choose the platform | You've seen it run your process, and operators have used it |
| 7. Start with one site | The first site runs on the system every shift with no paper fallback |
| 8. Connect the machines | Bottleneck downtime and output come from the equipment |
| 9. Go live and measure | The promised improvement shows up in numbers leadership accepts |
| 10. Scale | Later sites deploy from a template with only justified local differences |

## Where AI fits

You don't have to wait until the end for AI. Generative AI can help with procedures and plain-English questions early on, and once accurate, contextualised data is flowing from the shopfloor, predictive and optimising AI has something real to learn from. More in [AI will transform your factory, if you give it the right data](/post/ai-needs-shopfloor-data).

Which step is your factory on right now, and which one are you tempted to skip?
