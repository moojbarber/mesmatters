---
title: "Build, stitch or configure: three ways to run your shopfloor systems"
short: "Build, stitch or configure"
description: "Building blocks you assemble yourself, best-of-breed applications stitched together, or a configurable platform. The honest advantages and drawbacks of each, and how to choose."
published: 2026-08-26
category: advice
art: gates
---

Every so often a manufacturer with a strong internal IT team asks me whether they should just build their own MES. Others ask whether they should buy the best tool for each job and connect them through a unified namespace. Others have already decided on a single platform and want to know how to choose one.

They're all asking the same underlying question: what kind of shopfloor systems do we want to run for the next ten years?

There are broadly three answers. Each one has real advantages and real drawbacks, and I've seen all three work. I've also seen all three go wrong.

I'll be upfront about my own position before I start. I work for a vendor of the third kind, so weigh my view accordingly. I've tried to describe each approach the way its best advocates would.

## 1. Build from building blocks

**What it is.** You assemble your own applications from components: low-code platforms, IIoT and data toolkits, databases, dashboards and your own code. The tools are flexible, but they're not a finished product. Your people design and build each application, then keep it running.

**Where it works well:**

- **It fits exactly.** Every screen and rule is built around how you work, with nothing you don't need.
- **Fast to start.** A narrow use case, such as a dashboard or a digital checklist, can be live in weeks.
- **Control.** You decide what gets built and when, with no vendor roadmap to wait for.
- **Low cost at first.** Licences for building-block tools are often modest, and the developers may already be on the payroll.

**What to watch:**

- **You own it forever.** Design, testing, documentation, security and upgrades are all yours, for the life of the system.
- **Key-person dependency.** Knowledge sits with the people who built it. When they move on, it goes with them.
- **Breadth arrives slowly.** Production, quality, inventory and maintenance each become a project. Connecting them properly is another.
- **You design the data model.** Context only exists if someone models it and keeps it consistent as the applications grow.

**A typical example:** a plant with a capable digital team builds downtime tracking and a few digital forms on a low-code platform in a couple of months. It's genuinely useful. Two years later it covers five use cases, depends on two people, and every new request joins a queue.

## 2. Stitch together best-of-breed applications

**What it is.** You buy the best specialist tool for each job and connect them. An OEE tool, a quality system, a CMMS, a connected worker app, a scheduling tool. Increasingly they're joined through a unified namespace (UNS), where each application publishes what it knows and subscribes to what it needs.

**Where it works well:**

- **Depth where it matters.** Each department gets a tool that is very good at its job.
- **Quick wins, one area at a time.** You can start where the pain is biggest without committing to everything at once.
- **Freedom to swap.** If one tool disappoints, you can replace it without replacing everything.
- **A UNS helps a lot.** Publishing to one structured place cuts point-to-point integrations and makes data far easier to find and reuse.

**What to watch:**

- **Every boundary is an interface.** Someone has to design it, monitor it and retest it whenever either side upgrades.
- **Context thins out between systems.** You pass a subset of data across each boundary. The quality system knows a sample failed, but not necessarily what the machine was doing at the time.
- **Data moves after the event.** Even a fast integration is one step behind a single system that records everything once.
- **Operators juggle applications.** Several logins and several screens, often for one task.
- **Someone has to own the architecture.** The UNS structure, the data model and the integrations are yours to design and govern.

**A typical example:** a site buys a strong OEE tool, a separate quality app and a connected worker tool, each chosen by a different team. Each works well on its own. The work, and most of the value, then sits in connecting them so that a failed check, the order that was running, the material lot and the operator's sign-off all line up.

## 3. Configure an out-of-the-box platform

**What it is.** You buy an MES/MOM platform that already covers production, quality, inventory, maintenance and more on one data model, and you configure it to your processes rather than coding it. You extend it at the edges where you genuinely need to.

**Where it works well:**

- **The data is connected and contextualised from the start.** A downtime event, a quality result, a material consumption and an operator's sign-off all belong to the same order, in the same system.
- **No integrations between shopfloor functions.** Production, quality, inventory and maintenance share one database, so nothing waits to be transferred.
- **The vendor builds and maintains it.** Upgrades, security, new capabilities and AI arrive through the roadmap, paid for across many customers.
- **Breadth is ready to switch on.** Start with one function and add the next without a new project to connect it.

**What to watch:**

- **Higher cost up front.** Licences and services show up on day one, even if the ten-year picture looks different.
- **You adapt some processes.** Configuration covers a lot, but not everything. Some of your ways of working will change to fit the product.
- **Depth varies by area.** In a niche function, a specialist tool may go deeper than the platform's module.
- **You depend on a vendor.** Their roadmap and commercial health matter, so choose carefully. See [How to choose an MES](/post/how-to-choose-an-mes).

**A typical example:** a manufacturer goes live with production and quality on one line, then switches on inventory and maintenance on the same platform the following year, without building an interface between them.

## Side by side

| | Build from blocks | Stitch best-of-breed | Configure a platform |
| --- | --- | --- | --- |
| **Fit on day one** | Exact | Strong in each area | Close, through configuration |
| **Cost on day one** | Lowest | Moderate, spread across tools | Highest |
| **Cost over ten years** | Grows with every feature and departure | Grows with every interface and upgrade | Most predictable |
| **Connected, contextualised data** | Only if you model it | Partly, across interfaces or a UNS | Built in |
| **Integrations to maintain** | Yours, between everything you build | One per boundary, or UNS governance | Mainly to ERP, PLM and equipment |
| **Upgrades and security** | All yours | Spread across several vendors | Mostly the vendor's |
| **Who you depend on** | A few internal people | Several vendors, plus your integrators | One vendor |

## Most factories end up with a mix

In practice very few factories are purely one type. A common and sensible pattern is a platform as the operational backbone, specialist systems where depth genuinely matters, a UNS or integration layer to connect it all to the wider business, and some building at the edges for the things that really are unique.

So the real question is which one you make the backbone.

## Where I land

Having seen all three over a lot of projects, I think a configurable platform gives the most value over time for most manufacturers. All the data is connected and in context from the moment it's captured. There are no integrations between shopfloor functions to build or maintain, and nothing waits to be transferred. And you're not building and maintaining it yourself for ten years. The vendor does that, across many customers.

That's a view, not a law. A strong digital team with a narrow scope can do very well building from blocks. A site with good specialist tools already in place, and the discipline to govern a UNS, can get a lot from stitching. What matters is choosing deliberately, with the ten-year cost in front of you.

## How to decide

- What will each option cost over ten years, including your own people, not just the first project?
- Who maintains it when the original team moves on?
- How much of the value depends on data from different functions lining up in real time?
- How many interfaces will you own, and who will monitor them?
- Is your process really unique, or does it just feel that way? See [Configure, don't customise](/post/configure-dont-customise).
- How will you add AI and new capabilities, and who will build them?

If you're already running a homegrown system, there's no shame in it. Many were built when the market had nothing suitable. I cover what changes when you replace one in [Replacing a homegrown MES](/post/replacing-a-homegrown-mes).

Which of the three is your backbone today, and is it the one you'd choose again?
