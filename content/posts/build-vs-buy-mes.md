---
title: "Build vs buy MES: the real cost of a homegrown system"
short: "Build vs buy MES"
description: "Building your own MES can look cheaper and more flexible. What it really costs over ten years, when building parts of it makes sense, and how to make the decision."
published: 2026-08-26
category: advice
art: gates
---

Every so often a manufacturer with a strong internal IT team asks me whether they should just build their own MES. They know their processes. They have good developers. Why pay a vendor?

I have a strong opinion on this, so let me be upfront. I think it's irresponsible to suggest that building a full MES/MOM platform from scratch is better or less risky than buying one. But the question deserves a proper answer, not just an opinion.

## Why building looks attractive

The case for building usually goes like this:

- **It fits exactly.** Built around your processes, with no features you don't need.
- **No licence fees.** The developers are already on the payroll.
- **Control.** No vendor roadmap to wait for, no vendor to depend on.
- **Speed at the start.** A database, some screens and a couple of machine connections can be up in weeks.

All of that is true on day one. The problem is day 1,000.

## What happens over time

Homegrown systems almost always start small and work well for a while. Then requirements grow. Quality needs connecting to production, inventory to quality, maintenance to downtime, tooling to all of them. Each addition is another project for the same small team.

Then the risks start to show:

- **Key-person dependency.** The person who built it becomes the single point of failure. Eventually they leave, and the knowledge goes with them.
- **No upgrade path.** Operating systems and databases move on. Somebody has to keep the system compatible, on top of adding features.
- **Security.** A system that sits between IT and OT needs to be maintained to a high standard, for its whole life.
- **No roadmap.** AI, cloud, modern connectivity and mobile all have to be built in-house, competing with everything else on the team's list.
- **Hidden cost.** The developers' time is real money. It just doesn't show up as a licence line.

I cover what happens when companies finally replace these systems in [Replacing a homegrown MES](/post/replacing-a-homegrown-mes).

## Side by side

| | Build | Buy |
| --- | --- | --- |
| **Fit on day one** | Exact | Close, through configuration |
| **Cost on day one** | Lower, mostly internal time | Higher, licence and services |
| **Cost over ten years** | Grows with every feature, upgrade and departure | More predictable, shared across many customers |
| **Breadth** | Only what you've built | Production, quality, inventory, maintenance and more, ready to switch on |
| **Upgrades and security** | Entirely your responsibility | Shared with the vendor |
| **AI and new technology** | You build it | Part of the vendor's roadmap |
| **Dependency** | On a few internal people | On a vendor, with a contract and support |

## When building does make sense

I'm not saying never write code. Building makes sense for:

- **Extensions on a bought platform.** Low-code tools and supported extension points let you add genuinely unique logic without forking the product. See [Configure, don't customise](/post/configure-dont-customise).
- **Integrations** with niche equipment or in-house systems.
- **Analytics and reports** on top of the platform's data.
- **A truly unique process** that no product covers, kept small and well documented.

The pattern that works is buy the platform, build at the edges.

## How to decide

- What will this cost over ten years, including the people, not just over the first project?
- Who maintains it when the original developers move on?
- How will it keep up with security patches and platform changes?
- How will you add AI and new capabilities, and who will build them?
- Is your process really unique, or does it just feel that way? Most manufacturing processes aren't.

If you're already running a homegrown system, there's no shame in it. Many were built when the market had nothing suitable. The question is whether it's still the right foundation for the next ten years.

Have you built your own, and would you do it again?
