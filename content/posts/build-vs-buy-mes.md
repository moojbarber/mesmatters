---
title: "Code, build, stitch or configure: four ways to run your shopfloor systems"
short: "Code, build, stitch or configure"
description: "Four ways to run shopfloor systems: code from scratch, build from blocks, stitch best-of-breed tools, or configure a platform. The trade-offs of each."
published: 2026-08-26
category: advice
art: gates
---

Every so often a manufacturer with a strong internal IT team asks me whether they should just write their own MES. Some want to build applications on a low-code platform instead. Others ask whether they should buy the best tool for each job and connect them through a unified namespace. Others have already decided on a single platform and want to know how to choose one.

They're all asking the same underlying question: what kind of shopfloor systems do we want to run for the next ten years?

There are broadly four answers. I've seen every one of them work, and I've seen every one of them go wrong.

Online, this debate can get almost political, with very strong voices in every camp. It doesn't need to be confrontational. Different approaches suit different companies, and there are trade-offs whichever way you go.

I'll be upfront about my own position before I start. I work for a vendor of the fourth kind, so weigh my view accordingly. I've tried to describe each approach the way its best advocates would.

## 1. Code it from scratch

**What it is.** Your own developers write a bespoke system in a general-purpose language, on your own database and infrastructure. Every screen, rule, report and interface is your code. This is the classic homegrown MES, and plenty of factories still run one.

**Where it works well:**

- **Complete control.** It does exactly what you want, in exactly the way you want, and you own the intellectual property.
- **A genuinely niche process.** If you make something no product on the market can handle, code may be the only way to support it.
- **No licence fees.** The developers' time is the main cost, and that can look attractive when they're already on the payroll.
- **Deep knowledge in-house.** The people who wrote it understand your process and your system inside out.

It's usually a better fit for smaller companies with a narrow scope than for enterprises with many sites. Building from scratch is a bit like building a kit car. It can be rewarding, as long as you have the right expertise. But you miss out on years of innovation from people who've done it many times before.

**What to watch:**

- **The longest road to value.** A system of any real scale takes years to build well, including the parts every factory needs, such as genealogy and audit trails.
- **The gaps are easy to miss.** Homegrown systems often fall short on the things product teams spend years on: user experience, industry best practice and standard KPIs such as ISO 22400, performance at scale, and integrations.
- **You own everything, forever.** Security patches, operating system and database upgrades, documentation, testing and support all sit with you.
- **Key-person dependency is at its highest.** When the original developers leave, the knowledge often leaves with them.
- **It gets harder as you grow.** Add plants and the need to standardise, and custom code tends to multiply until the system is outgrown.

**A typical example:** a system written years ago by a small internal team, which still runs the plant and does its core job well. Few people understand how it works, change requests take months, and nobody wants to be the one who touches it. More on what changes when you replace one in [Replacing a homegrown MES](/post/replacing-a-homegrown-mes).

## 2. Build from building blocks

**What it is.** You assemble your own applications on a platform made for builders: low-code tools, IIoT and data toolkits, databases, dashboards, with some of your own code where needed. You're not starting from nothing, because the platform handles the plumbing. The tools are flexible, but they're not a finished product. Your people design and build each application, then keep it running.

**Where it works well:**

- **Much faster than coding.** Configuring something in a low-code environment is usually far quicker than building it from scratch.
- **It fits exactly.** Every screen and rule is built around how you work, with nothing you don't need.
- **It empowers your own people.** Engineers can make changes themselves without waiting for a vendor, which keeps the cost of change down.
- **Low cost at first.** Licences for building-block tools are often modest, and a narrow use case, such as a dashboard or a digital checklist, can be live in weeks.

You see this most in smaller companies with tech-savvy teams, and some of the platforms in this space are doing very well.

**What to watch:**

- **It relies heavily on internal skills.** Design, testing, documentation and support are yours, for the life of every application.
- **Apps can multiply.** It's easy to end up with a collection of apps solving narrow problems, rather than a joined-up operation.
- **You design the data model.** Context only exists if someone models it and keeps it consistent as the applications grow.
- **Key-person dependency.** Knowledge sits with the people who built each app. When they move on, it goes with them.

**A typical example:** a plant with a capable digital team builds downtime tracking and a few digital forms on a low-code platform in a couple of months. It's genuinely useful. Two years later it covers five use cases, depends on two people, and every new request joins a queue.

**Low-code and MES/MOM aren't either/or.** Most modern MES/MOM platforms include low-code tools of their own for screens and workflows. So the real difference is how much is already built for you before you start. Plenty of manufacturers combine the two: MES/MOM runs the core operation on one data model, and low-code fills gaps at the edges, such as a site-specific form or an improvement idea someone wants to try.

## 3. Stitch together best-of-breed applications

**What it is.** You buy the best specialist tool for each job and connect them. An OEE tool, a quality system, a CMMS, a connected worker app, a scheduling tool. Increasingly they're joined through a unified namespace (UNS), where each application publishes what it knows and subscribes to what it needs.

**Where it works well:**

- **Depth where it matters.** Each department gets a tool that is very good at its job.
- **Quick wins, one area at a time.** You can start where the pain is biggest without committing to everything at once.
- **Freedom to swap.** If one tool disappoints, you can replace it without replacing everything.
- **A UNS helps a lot.** Publishing to one structured place cuts point-to-point integrations and makes data far easier to find and reuse.

**What to watch:**

- **Integration is the hard part.** Integrations between third-party systems are one of the hardest and most expensive parts of any project, and every one needs retesting whenever either side upgrades.
- **Context thins out between systems.** You can't pass all the context across every integration, so naturally you share a subset. The quality system knows a sample failed, but not necessarily what the machine was doing at the time.
- **A UNS shows what's happening now.** It's an organisational structure on top of a broker, so you still need applications around it to add meaning and keep the history. OEE is a good example: you can't aggregate an OEE figure, you have to go back to the raw data. It's a useful pattern, but not a silver bullet.
- **Operators juggle applications.** Switching screens and logging in and out, losing context at each step. When something goes wrong, which system do they check first? Putting one front end over several apps is possible, but it tends to become bespoke.
- **Someone has to own the architecture.** Designing and governing the UNS structure, the data model, the integrations and the security around them is down to you.

**A typical example:** a site buys a strong OEE tool, a separate quality app and a connected worker tool, each chosen by a different team. Each works well on its own. The work, and most of the value, then sits in connecting them so that a failed check, the order that was running, the material lot and the operator's sign-off all line up.

## 4. Configure an out-of-the-box platform

**What it is.** You buy an MES/MOM platform that already covers production, quality, inventory, maintenance and more on one data model, and you configure it to your processes rather than coding it. Most are modular, so you can start with one or two functions and switch on more as you go. You extend it at the edges where you genuinely need to.

**Where it works well:**

- **The data is connected and contextualised from the start.** A downtime event, a quality result, a material consumption and an operator's sign-off all belong to the same order, in the same system.
- **No integrations between shopfloor functions.** Production, quality, inventory and maintenance share one database, so nothing waits to be transferred. Operators get one login and one interface, and context stays intact as they move between tasks.
- **The vendor builds and maintains it.** Best practice from many factories, standard KPIs, upgrades, security and new capabilities such as AI all arrive through the roadmap, paid for across many customers.
- **Start small on the right path.** Begin with production or quality, then add inventory, logistics, maintenance, tooling or energy later without a new project to connect them.
- **You can still make it your own.** A good platform lets you build your own screens, reports and workflows with low-code tools, without going back to the vendor.

**What to watch:**

- **Higher cost up front.** Licences and services show up on day one. Judge it on total cost of ownership over the life of the system, not the first quote.
- **You adapt some processes.** You'll need to decide the mix: where you adapt to the system, and where the system adapts to you.
- **Not every platform is truly configurable.** Some are really toolkits that need a lot of coding to fit together. Check how much is configuration and how much is customisation.
- **Integrations still need work.** Configuration reduces customisation, but rarely removes it entirely, especially for equipment and third-party software.
- **You depend on a vendor.** Their roadmap and commercial health matter, so choose carefully. See [How to choose an MES](/post/how-to-choose-an-mes).

**A typical example:** a manufacturer goes live with production and quality on one line, then switches on inventory and maintenance on the same platform the following year, without building an interface between them.

## Side by side

| | Code from scratch | Build from blocks | Stitch best-of-breed | Configure a platform |
| --- | --- | --- | --- | --- |
| **Fit on day one** | Exact, once it's built | Exact | Strong in each area | Close, through configuration |
| **Time to first value** | Longest | Fast for narrow use cases | Fast in each area | Moderate, then fast to extend |
| **Cost on day one** | Low licences, high effort | Lowest | Moderate, spread across tools | Highest |
| **Cost over ten years** | Grows with every feature, fix and departure | Grows with every feature and departure | Grows with every interface and upgrade | Most predictable |
| **Connected, contextualised data** | Only if you design it | Only if you model it | Partly, across interfaces or a UNS | Built in |
| **Integrations to maintain** | All of them, written by you | Yours, between everything you build | One per boundary, or UNS governance | Mainly to ERP, PLM and equipment |
| **Upgrades and security** | All yours, down to the infrastructure | Mostly yours | Spread across several vendors | Mostly the vendor's |
| **Who you depend on** | A few developers | A few internal people | Several vendors, plus your integrators | One vendor |

## Most factories end up with a mix

In practice very few factories are purely one type. A common and sensible pattern is a platform as the operational backbone, with specialist systems where the requirements are genuinely advanced, such as a WMS for complex warehousing or an EAM for advanced maintenance. Add a UNS or integration layer to connect it all to the wider business, and some building or coding at the edges for the things that really are unique.

So the real question is which one you make the backbone.

## How to decide

- What will each option cost over ten years, including your own people, not just the first quote?
- Who maintains it when the original team moves on?
- How much of the value depends on data from different functions lining up in real time?
- How many interfaces will you own, and who will monitor them?
- Is your manufacturing process really unique, or is it the business processes around it? See [Configure, don't customise](/post/configure-dont-customise).
- How will you add AI and new capabilities, and who will build them?

## My view

Personally, I like being part of a connected ecosystem. It's a bit like owning all Apple products: everything works together, and it gets better over time.

Having seen all four over a lot of projects, I think a configurable platform gives the most value over time for most manufacturers. All the data is connected and in context from the moment it's captured. There are no integrations between shopfloor functions to build or maintain, and nothing waits to be transferred. And you're not building and maintaining it yourself for ten years. The vendor does that, across many customers.

That's a view, not a law. A truly niche process can justify writing your own code, and a smaller company with a strong digital team can do very well building from blocks. Building and configuring aren't really competing, because they suit different kinds of business. A site with good specialist tools already in place, and the discipline to govern a UNS, can get a lot from stitching.

Whichever you choose, start small, but start small on the right path, with the destination in mind.

If you're already running a homegrown system, there's no shame in it. Many were written when the market had nothing suitable, and they've served their factories well.

Which of the four is your backbone today, and is it the one you'd choose again?
