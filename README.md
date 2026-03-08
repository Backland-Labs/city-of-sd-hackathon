# Claude Community x City of SD Impact Lab

> **Disclaimer:** All data and resources linked below are subject to their respective terms of access and terms of service. Participants are responsible for reviewing and complying with applicable usage policies, licensing terms, API rate limits, and data use restrictions before accessing or incorporating any data into their projects.

### Discord: https://discord.gg/vzMDyb48

# Submission Deadline: 5pm

---

## 1. Open Data Portal

| Resource | Link | Notes |
|----------|------|-------|
| City of San Diego Open Data Portal | [data.sandiego.gov](https://data.sandiego.gov/) | Hundreds of machine-readable datasets. CSV, JSON, API access. |
| Open Data — All Datasets | [data.sandiego.gov/datasets](https://data.sandiego.gov/datasets/) | Browse/filter all available datasets. |
| Open Data — Getting Started | [data.sandiego.gov/get-started](https://data.sandiego.gov/get-started/) | Documentation and usage guides. |
| Open Source Projects | [data.sandiego.gov/open-source](https://data.sandiego.gov/open-source/) | City-maintained open source code on GitHub. |
| Government Publications (Library) | [sandiego.gov/public-library/govpub](https://www.sandiego.gov/public-library/govpub) | Historical and current government publications. |

### Hackathon Tips — Open Data
- Datasets cover topics including permits, code enforcement, police calls, traffic, budgets, and more.

---

## 2. Municipal Code

| Resource | Link | Notes |
|----------|------|-------|
| Municipal Code (Official) | [sandiego.gov/city-clerk/officialdocs/municipal-code](https://www.sandiego.gov/city-clerk/officialdocs/municipal-code) | Full code organized by chapter, article, division, section. HTML browsable. |
| Municipal Code (American Legal) | [codelibrary.amlegal.com](https://codelibrary.amlegal.com/codes/san_diego/latest/sandiego_regs/0-0-0-71708) | Searchable, cross-referenced. Good for programmatic text extraction. |
| Codes & Regulations (Dev Services) | [sandiego.gov/development-services/codes-regulations](https://www.sandiego.gov/development-services/codes-regulations) | Local amendments to California Building Standards Code (Title 24). 2025 CBC effective Jan 1, 2026; local amendments expected March–April 2026. |

### Hackathon Tips — Municipal Code
- The Municipal Code is HTML-structured with predictable chapter/section IDs.

---

## 3. Council Transcripts & Meeting Records

| Resource | Link | Notes |
|----------|------|-------|
| Council Meeting Documents (Agendas, Minutes, Results) | [sandiego.gov/city-clerk/city-council-docket-agenda](https://www.sandiego.gov/city-clerk/city-council-docket-agenda) | Official dockets, agendas, minutes, and result summaries. |
| Council Archived Videos (Granicus) | [sandiego.granicus.com](https://sandiego.granicus.com/ViewPublisher.php?view_id=3) | Video archives posted within 24–48 hours. Not an official record. |
| Committee Webcasts | [sandiego.granicus.com (view 31)](https://sandiego.granicus.com/ViewPublisher.php?view_id=31) | Additional webcasts for committee meetings. |
| Citywide Agendas & Minutes | [sandiego.gov/citywide-agendas-minutes](https://www.sandiego.gov/citywide-agendas-minutes) | Broader collection including all committee meetings. |
| Official City Documents | [sandiego.gov/city-clerk/official-city-documents](https://www.sandiego.gov/city-clerk/official-city-documents) | Charter, resolutions, ordinances, and council actions. |
| Digital Archives | [sandiego.gov/digitalarchives](https://www.sandiego.gov/digitalarchives) | Historical documents, photos, images, audio files. |
| Public Records Requests (NextRequest) | [sandiego.nextrequest.com](https://sandiego.nextrequest.com/) | 40,000+ searchable public records requests. |

### Hackathon Tips — Council Data
- Granicus video archives can be used with speech-to-text tools (e.g., Whisper) to generate searchable transcripts.
- The NextRequest portal is a goldmine for FOIA-style data if you need specific documents.

---

## 4. Permitting Codes & Guidelines

| Resource | Link | Notes |
|----------|------|-------|
| Building Permit Overview | [sandiego.gov/.../building-permit](https://www.sandiego.gov/development-services/permits/building-permit) | Requirements, exempt projects, permit types, how to apply. |
| Permits, Approvals & Inspections | [sandiego.gov/.../permits-inspections](https://www.sandiego.gov/development-services/permits-inspections) | Full hub for all permit and inspection processes. |
| Permits and Approvals | [sandiego.gov/.../permits](https://www.sandiego.gov/development-services/permits) | Overview of all available permit types. |
| Permits FAQs | [sandiego.gov/.../permits/faqs](https://www.sandiego.gov/development-services/permits/faqs) | Common questions about the permitting process. |
| San Diego Building Codes (UpCodes) | [up.codes/codes/san-diego](https://up.codes/codes/san-diego) | Third-party searchable building codes. Includes 2022 CBC viewer. |
| San Diego Building Code 2022 Viewer | [up.codes/viewer/san-diego/ca-building-code-2022](https://up.codes/viewer/san-diego/ca-building-code-2022) | Full-text viewer for Vol 1 & 2 of the 2022 California Building Code as adopted by San Diego. |

### Hackathon Tips — Permitting
- UpCodes has the most developer-friendly interface for code lookups.
- Building permit data may also appear in the Open Data Portal (see above).

## Submission Guidelines

Projects are submitted via MCP server. Add the submission server to Claude Code by running:

```bash
claude mcp add impact-lab-submissions --transport http https://mcp-submissions.casper-studios.workers.dev/mcp
```

For other MCP clients (e.g. Claude Desktop), add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "submissions": {
      "url": "https://mcp-submissions.casper-studios.workers.dev/mcp"
    }
  }
}
```

Once added, you can submit your project directly through your MCP client using the tools provided by the `impact-lab-submissions` MCP server.

**Note:** Only your most recent submission will be reviewed. You can resubmit as many times as you like, but each new submission replaces the previous one.

### Required in Your Repo's README

Every project repo must include a README with the following:

- **Team name**
- **Team members**
- **Problem statement** -- what civic problem are you solving?
- **What it does** -- a short paragraph describing the application
- **Data sources used** -- which city datasets or resources your project uses
- **Architecture / approach** -- How did you use Claude to build it? How is Claude used inside the app?
- **Links** -- URL to the live application, if deployed
- **Demo video** -- a 60-second walkthrough of the application. Optional if your app is deployed and accessible via a public link; **required** if it is not.

---

## Rules

- **No early starts.** Your first commit must be after 10:30 AM on 3/7. Projects with evidence of development before that time will be disqualified.
- **Original work only.** Third-party libraries and frameworks are fine, but the core project must be built during the hackathon. No pre-existing projects.
- **One submission per team.** Each team submits one project via the MCP submission server.
- **Use city data responsibly.** Use public APIs and open data. Do not scrape or abuse city systems.
- **Code must be in a public GitHub repo.** Judges need to be able to review your code. You're free to make the repo private after the hackathon closes.

---

## Judging Criteria

Each project will be scored across four categories on a **1-5 scale** (1 = minimal, 5 = exceptional), for a **maximum of 20 points**.

---

### 1. Civic Impact (1-5)

Does this solve a real problem for San Diego residents, city staff, or the community?

Judges should ask: **Would someone actually use this?**

| Score | Description |
|-------|-------------|
| 5 | Addresses a clear, pressing civic need with a compelling use case |
| 4 | Solves a real problem with a well-defined audience |
| 3 | Useful concept, but the target user or problem could be sharper |
| 2 | Loosely connected to a civic use case |
| 1 | No clear civic relevance |

> **Bonus consideration:** Solutions that enable broader access -- such as MCP servers, CLIs, or agentic tools that others can build on -- should be rewarded.

---

### 2. Use of City Data (1-5)

How effectively does the project leverage San Diego's open data, municipal code, council records, or other city resources?

| Score | Description |
|-------|-------------|
| 5 | Deeply integrates multiple city data sources in a meaningful way |
| 4 | Strong use of at least one city data source with clear value |
| 3 | Uses city data, but doesn't go beyond surface-level access |
| 2 | Minimal or superficial use of city data |
| 1 | No meaningful use of city data |

> **Bonus consideration:** Projects that creatively combine datasets (e.g., joining permit data with zoning codes, enriching 311 data with budget info) should be rewarded.

---

### 3. Technical Execution (1-5)

Does it work? Is the demo functional and reasonably polished for a hackathon timeframe?

| Score | Description |
|-------|-------------|
| 5 | Fully functional, polished, and well-scoped for the time available |
| 4 | Working demo with minor rough edges |
| 3 | Core functionality works but notable gaps or bugs |
| 2 | Partially working; significant issues during demo |
| 1 | Non-functional or unable to demo |

> A focused, working MVP beats an ambitious idea that crashes during the demo. Judges should reward smart scoping.

---

### 4. Presentation & Story (1-5)

Did the team clearly communicate what they built, why it matters, and who it's for?

| Score | Description |
|-------|-------------|
| 5 | Compelling narrative, clear demo, and strong delivery |
| 4 | Well-structured presentation with a clear problem/solution arc |
| 3 | Adequate presentation but missing clarity on problem, audience, or impact |
| 2 | Disorganized or hard to follow |
| 1 | No clear communication of the project's purpose |

> A strong demo tells a story: here's the problem, here's how we solve it, here's what it looks like in action.

---

### Scoring Summary

| Category | Max Score |
|----------|-----------|
| Civic Impact | 5 |
| Use of City Data | 5 |
| Technical Execution | 5 |
| Presentation & Story | 5 |
| **Total** | **20** |

---

## Submissions

| ID | Team Name | GitHub | Problem Statement |
|----|-----------|--------|-------------------|
| 3 | AquaWatch SD | [GudipatiPallavi/AquaWatch](https://github.com/GudipatiPallavi/AquaWatch) | San Diego publishes water quality monitoring data — but it is effectively invisible to the public. The City's effluent dataset contains 9,431 chemical readings across 14 analytes spanning a decade. |
| 4 | ParkPilotSD | [avinash-gudipati/ParkPilotSD](https://github.com/avinash-gudipati/ParkPilotSD.git) | Finding available parking in San Diego is a frustrating, time-consuming experience — drivers circle blocks, miss hidden spots, and often overpay at unfamiliar lots. There is no unified, real-time solution that helps users discover, compare, and navigate to parking options efficiently. ParkPilot SD addresses this by providing a smart parking assistant that helps San Diego drivers quickly locate nearby parking spots, view availability and pricing, and navigate to their chosen destination — reducing urban congestion and the stress of parking. |
| 5 | ZoneCheck SD | [reegs/2026-03-07_san_diego_impact_hackathon](https://github.com/reegs/2026-03-07_san_diego_impact_hackathon) | Residents, small business owners, and developers in San Diego constantly face the question "Can I do [X] at [Y address]?" — whether that's opening a coffee shop, building an ADU, or converting a property. Answering it today requires navigating the city's GIS map, cross-referencing the 1,000+ page Land Development Code, and decoding cryptic permission codes. This information is public but practically locked behind bureaucratic complexity. ZoneCheck SD is a web app that lets anyone type a San Diego address and a proposed use and instantly see whether it's allowed, needs a permit, or isn't permitted — with plain-English explanations, color-coded results, and links to the relevant municipal code sections. It covers 353 use categories across 116 zone codes, with all zoning rules bundled as static JSON for sub-second lookups and zero hosting cost. |
| 6 | Team Foxtrot | [Reston2024/sdmc-compliance](https://github.com/Reston2024/sdmc-compliance) | San Diego processes tens of thousands of building permits each year. Each permit must be verified against the San Diego Municipal Code (SDMC) — a dense, evolving body of rules governing structural loads, zoning setbacks, electrical systems, solar installations, and more. Today that verification is largely manual: inspectors cross-reference paper or PDF code sections, decisions are recorded in siloed systems, and there is no cryptographic audit trail proving what was checked, when, and by whom. The result: compliance gaps, contested permit decisions, slow appeals, and no machine-readable record a future auditor can trust without re-doing the entire review. The SDMC Compliance Platform solves this by giving inspectors and applicants a structured submission workflow, evaluating every permit against live OPA policy rules (Rego), and writing a SHA-256 hash-chained evidence record to an immutable PostgreSQL ledger — creating a tamper-evident audit trail from first submission to final sign-off, compliant with NIST SP 800-53 and 21 CFR Part 11. |
| 7 | Team PermitSniper | [ZeldashC/claude-hackla](https://github.com/ZeldashC/claude-hackla) | Local B2B businesses and contractors in San Diego (HVAC, Plumbing, Electrical, etc.) struggle to identify high-intent customers. Raw city data is currently trapped in massive, unstructured CSV files that are difficult for small businesses to parse, leading to missed economic opportunities and inefficient sales cycles. PermitSniper transforms this raw permit data into actionable sales leads using AI enrichment via the Claude API. |
| 8 | PocketStack | [tonymathen/claude-impact-hackathon/](https://github.com/tonymathen/claude-impact-hackathon/) | San Diego discharges 175 million gallons of treated sewage into the Pacific daily, but 24 years of city monitoring data sits in disconnected CSVs inaccessible to residents. Pipe to Pacific is an interactive dashboard with a Claude-powered AI analyst that tracks the wastewater lifecycle from treatment plant to ocean contamination, proving with data that the poorest communities (Imperial Beach $52K, San Ysidro $38K) face the highest bacteria levels while affluent La Jolla ($138K) has near-zero contamination. Features: agentic tool-use AI, anomaly detection, equity overlay joining city data with Census income, live NOAA/NWS/NDBC ocean conditions, 24-year time slider, guided narrative tour, and an MCP server exposing all data. |
| 9 | Team Ctrl+P | [bookchiq/block-report](https://github.com/bookchiq/block-report) | San Diego residents, community organizers, and council staff lack a quick, digestible way to access hyperlocal civic data — 311 service requests, nearby public resources, and language demographics — for their specific neighborhood. Block Report aggregates scattered city open data and Census datasets into a single civic profile per neighborhood, then uses Claude to generate printable, multilingual community briefs ready for sharing via QR codes on printed flyers. |
| 11 | Hong Van Pham | [hvtpham/sd-budget-voice](https://github.com/hvtpham/sd-budget-voice) | San Diego faces a $120M FY2027 budget deficit, but the mayor's official budget survey asks residents for opinions without providing actual dollar amounts, year-over-year comparisons, revenue options, or any mechanism to connect input to decision-makers. SD Budget Voice is the survey the city should have built: an interactive civic tool that gives residents real budget numbers, lets them make real tradeoffs across departments and revenue options, and delivers aggregate community priorities directly to all nine council members and the mayor's office. It also generates personalized AI-drafted letters (Claude Haiku, streaming) from each resident's specific slider choices and top priorities, so residents can take direct action beyond the survey itself. |
| 12 | Bruno Granatowicz | [bgrana75/MyBlockSD](https://github.com/bgrana75/MyBlockSD) | San Diego publishes open data across dozens of CSV files and portals but no single tool lets a resident see everything for their block. My Block SD ingests 11 city data sources into one backend with a polished web dashboard at myblocksd.xyz and an MCP server at api.myblocksd.xyz/mcp with 10 tools for any AI agent. Features include interactive map, live SDPD dispatch, drill-down detail modals, and AI chat powered by Claude. |
| 13 | Peter Medina | [peterjohannmedina/streetbot-sd](https://github.com/peterjohannmedina/streetbot-sd) | San Diego maintains over 37,000 street repair records but has no machine-to-machine interface for AI agents to query or report against this data. StreetBot creates a dual-interface gateway — a human-friendly dashboard with neighborhood-labeled district views, light/dark mode, and a repair reporting form, alongside a structured bot API for agentic AI systems to query repairs, search streets, and submit repair tickets programmatically via web_fetch. It establishes the pattern for how cities can offer bot-ready interfaces for agentic AI alongside traditional web portals, with edge deployment potential on embedded devices like the AAEON Boxer Nano for autonomous infrastructure monitoring and automated ticket generation at the compute edge. |
| 14 | PocketStack | [tonymathen/claude-impact-hackathon](https://github.com/tonymathen/claude-impact-hackathon) | San Diego discharges 175 million gallons of treated sewage into the Pacific Ocean every day through deep-water outfalls. The city has collected 24 years of ocean monitoring data across 157 stations - nearly a million readings tracking bacteria, sediment contamination, and fish tissue contaminants. But this data sits in disconnected CSV files on the city's open data portal, inaccessible to residents, journalists, surfers, and policymakers who need to understand: Is the ocean safe? Is it getting better? And who bears the burden of contamination? The data reveals a stark environmental justice story: the poorest communities (Imperial Beach at $52K median income, San Ysidro at $38K) face the highest bacteria levels and exceedance rates, while affluent areas like La Jolla ($138K) enjoy near-zero contamination. No existing tool connects water quality data to demographics to make this inequity visible. Pipe to Pacific is an interactive dashboard that tracks the lifecycle of San Diego's wastewater - from treatment plants to ocean outfall to measurable contamination, with a Claude-powered AI analyst using tool-calling to query the data on demand. |
| 15 | Spire Labs | [orpheuscode/sd-environmental-intelligence](https://github.com/orpheuscode/sd-environmental-intelligence) | San Diego's environmental data is locked in 11 separate government databases. Residents don't know if their beach is safe. City ops teams lack synthesized intelligence. Elected officials can't track if their resolutions are working. Three Claude AI agents synthesize real-time air, water, ocean, and regulatory data for any SD address — resident health report, city ops briefing, and regulatory accountability scorecard. Team members: Quintin and Claude. Demo video: https://youtu.be/nHjXmAty3No |
| 16 | Model Citizens | [CalvinFronda/claude-sd-hackaton](https://github.com/CalvinFronda/claude-sd-hackaton) | Every week, hundreds of San Diego residents take time out of their lives to speak at City Council meetings. They show up. They wait their turn. They say their piece in two minutes or less. And then the minutes get filed away. City council meetings are public — but effectively invisible. |
| 17 | OpenSD.app | [SimonBaars/city-of-sd-hackathon](https://github.com/SimonBaars/city-of-sd-hackathon) | San Diego publishes hundreds of open datasets — council votes, 311 complaints, budgets, permits, police calls, street conditions, and more — but they're scattered across CSVs, GeoJSON files, and disconnected portals. A resident who wants to know "which council district has the worst potholes?" would need to download files, write SQL, and cross-reference multiple sources. Nobody does that. OpenSD makes all of this data instantly queryable through conversation. It's an AI-powered civic data explorer (live at https://opensd.app) that lets anyone query, visualize, and cross-reference 270+ City of San Diego datasets through natural language. |
| 18 | city clerk claude | [ako89/advocacy_bot](https://github.com/ako89/advocacy_bot) | City council agendas are dense, hard to follow, and published with little fanfare — making it easy for residents to miss issues they care about. Our Discord bot scrapes the San Diego City Council agenda portal and notifies community members when topics matching their interests appear. With the addition of semantic matching (sentence-transformers + ONNX), watches go beyond exact keyword hits: a watch for "affordable housing" now surfaces items like "low-income rental assistance program" that would otherwise be missed. The goal is to lower the barrier to civic engagement by bringing relevant government activity directly to the communities already organizing on Discord. |
| 19 | 2G2G - 2 girls 2 guys | [kenaung/CityNavigator_SDCloudImpact_030726](https://github.com/kenaung/CityNavigator_SDCloudImpact_030726) | San Diego residents face fragmented, hard-to-navigate city services across language barriers. City Navigator provides an AI-powered multilingual self-service system for permit guidance, 311 issue reporting, and budget transparency — accessible in 5 languages (English, Spanish, Filipino, Arabic, Korean) via a conversational interface. It also exposes all city services as a Civic MCP Server with 10 tools and 5 resources, enabling other AI agents to programmatically access San Diego city services including live budget data. |
| 21 | o2mediaco | [o2mediaco/Claude-Community-x-City-of-SD-Impact-Lab](https://github.com/o2mediaco/Claude-Community-x-City-of-SD-Impact-Lab) | San Diego issues thousands of business tax certificates every year, but the raw data sits as CSV files on the city open data portal with no way to explore trends visually. Residents, policymakers, and entrepreneurs cannot easily see which industries are growing, where new businesses are opening, or how policy changes affect business creation. SD Business Growth Explorer transforms this data into an interactive AI-powered dashboard with category trends, geographic heatmaps, event timelines, and a Claude-powered natural language query interface. |
| 22 | TenantSafe SD | [palakg28/tenantsafeSD](https://github.com/palakg28/tenantsafeSD) | Renting in San Diego is one of the most consequential financial decisions a person can make — yet tenants routinely sign leases without knowing a property's history. Open code violations, unresolved 311 complaints, and recurring maintenance failures are all documented in public city datasets, but they are buried in data portals that most renters never access and wouldn't know how to interpret. The result: tenants move into properties with known problems, are blindsided by habitability issues, and lack the context to negotiate repairs, withhold rent appropriately, or simply walk away from a bad deal. TenantSafe SD closes that information gap by making public city data legible, actionable, and accessible to any renter in under 60 seconds. |
| 23 | ClockedCode | [a-chahal/openshop](https://github.com/a-chahal/openshop) | Starting a small business in San Diego means navigating a maze of zoning codes, permit requirements, competitive dynamics, and neighborhood conditions — information scattered across dozens of city portals, dense legal documents, and government databases that were never designed for regular people. A single oversight (signing a lease on a wrongly-zoned property, missing a conditional use permit, opening in an oversaturated market) can cost months of time and thousands of dollars before the doors even open. OpenShop is an AI-powered site assessment tool that takes a natural-language query and runs parallel real-time assessments against 17+ City of San Diego datasets — ArcGIS zoning maps, SDPD NIBRS crime data, NAICS-coded business registrations, parking meter transactions, building permits, transit stops, 311 requests, and more — to deliver an instant, data-backed go/no-go verdict for any business type at any San Diego address in under 10 seconds. |
| 24 | SD Smart Park Team | [rariss/sd-smart-park](https://github.com/rariss/sd-smart-park) | Finding parking in San Diego is frustrating and time-consuming. SD Smart Park predicts parking meter availability using historical City of San Diego meter transaction data combined with Claude AI recommendations, helping drivers find the best nearby spots based on real occupancy patterns, citation risk, and real-time context like events or time of day. |
| 26 | My Tax Dollars | [neonetizen/tax-dollars](https://github.com/neonetizen/tax-dollars) | San Diego collects property taxes from hundreds of thousands of homeowners every year, but residents have almost no intuitive way to understand what they're actually funding. Budget documents are dense, portals are hard to navigate, and aggregate statistics obscure how money is allocated. The result: taxpayers pay without any meaningful sense of what they got in return. My Tax Dollars reframes the question. Instead of "here is the city budget," it asks: "you paid X dollars — here is your receipt." |
| 28 | Hole Patrol | [jwilber/city-of-sd-hackathon](https://github.com/jwilber/city-of-sd-hackathon) | San Diego residents report hundreds of thousands of quality-of-life issues each year through the city's Get It Done program -- illegal dumping, potholes, graffiti, encampments, parking violations, and more. But there's no easy way to explore this data spatially, filter across categories, or understand trends over time. City staff, journalists, and engaged residents lack a fast, interactive tool to drill down into neighborhood-level patterns and ask questions like: "What are the most common issues in Mid-City? How has encampment reporting changed since 2020? Which neighborhoods have the lowest closure rates?" We built a browser-based interactive dashboard that visualizes nearly 1 million Get It Done 311 service requests across San Diego (2016-present) using DuckDB-WASM, Mosaic crossfiltering, and deck.gl -- entirely client-side with no backend. Team members: Kitu Komya, Madi Bianes. |
| 29 | Team Ctrl+P | [bookchiq/block-report](https://github.com/bookchiq/block-report) | San Diego residents, community organizers, and council staff lack a quick, digestible way to access hyperlocal civic data — 311 service requests, nearby public resources, and language demographics — for their specific neighborhood. This information is scattered across multiple city portals and Census datasets, making it hard to get a clear picture of what's happening on your block and what resources are available. |
| 30 | AIVengers | [rdsingh/claude-impact-hackathon](https://github.com/rdsingh/claude-impact-hackathon) | How do you measure quality of life (QoL) issues in a neighborhood and track it over time? |
| 31 | San Diego Real Estate Development Assistant | [BrandonGarate177/SanDiego_x_Claude](https://github.com/BrandonGarate177/SanDiego_x_Claude) | Real estate developers in San Diego must navigate a fragmented landscape of zoning codes, land use regulations, municipal ordinances, and parcel data spread across multiple city agencies. Finding answers to basic development questions — setbacks, permitted uses, density limits — requires hours of manual research. This tool consolidates that information into a single conversational interface backed by authoritative city data, using a RAG pipeline that classifies developer intent, resolves locations to Community Planning Areas, retrieves relevant municipal code excerpts from a vector store, cross-references zoning overlays and land use GIS data, and returns grounded, cited answers. |
| 32 | Nomads | [quinnzeda/ImpactSanDiego](https://github.com/quinnzeda/ImpactSanDiego) | San Diego's building permit process is opaque and complex. Residents and developers waste hours navigating 45+ permit types, exemptions, municipal code sections, and required forms across multiple disconnected city websites. There's no single tool that answers: "I want to do X to my property - what permits do I need?" |
| 33 | Claude Coders | [bansal1600/ripa-data](https://github.com/bansal1600/ripa-data) | By better understanding police activities, California law enforcement are required to collect and publish officer reports of every stop, pedestrian, traffic, or other means. |
