# Claude Community x City of SD Hackathon

# City of San Diego — Municipal Resources

> **Hackathon Quick Reference** — All links verified Feb 25, 2026. Includes open data endpoints, API access, and machine-readable sources where available.

---

## 1. Municipal Code

| Resource | Link | Notes |
|----------|------|-------|
| Municipal Code (Official) | [sandiego.gov/city-clerk/officialdocs/municipal-code](https://www.sandiego.gov/city-clerk/officialdocs/municipal-code) | Full code organized by chapter, article, division, section. HTML browsable. |
| Municipal Code (American Legal) | [codelibrary.amlegal.com](https://codelibrary.amlegal.com/codes/san_diego/latest/sandiego_regs/0-0-0-71708) | Searchable, cross-referenced. Good for programmatic text extraction. |
| Codes & Regulations (Dev Services) | [sandiego.gov/development-services/codes-regulations](https://www.sandiego.gov/development-services/codes-regulations) | Local amendments to California Building Standards Code (Title 24). 2025 CBC effective Jan 1, 2026; local amendments expected March–April 2026. |

### Hackathon Tips — Municipal Code
- The American Legal Publishing version is easier to scrape/parse than the official site.
- The Municipal Code is HTML-structured with predictable chapter/section IDs.
- No official API exists; consider scraping or using cached copies.

---

## 2. Council Transcripts & Meeting Records

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
- Official verbatim transcripts are not published online — contact City Clerk at **(619) 533-4000** or email **cityclerk@sandiego.gov** for requests.
- The NextRequest portal is a goldmine for FOIA-style data if you need specific documents.

---

## 3. Permitting Codes & Guidelines

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
- Building permit data may also appear in the Open Data Portal (see below).
- For permit status lookups, the city uses the **OpenDSD** system at [opendsd.sandiego.gov](https://opendsd.sandiego.gov).

---

## 4. Open Data & API Access (Bonus for Hackathon)

| Resource | Link | Notes |
|----------|------|-------|
| City of San Diego Open Data Portal | [data.sandiego.gov](https://data.sandiego.gov/) | Hundreds of machine-readable datasets. CSV, JSON, API access. |
| Open Data — All Datasets | [data.sandiego.gov/datasets](https://data.sandiego.gov/datasets/) | Browse/filter all available datasets. |
| Open Data — Getting Started | [data.sandiego.gov/get-started](https://data.sandiego.gov/get-started/) | API documentation and usage guides. |
| Open Source Projects | [data.sandiego.gov/open-source](https://data.sandiego.gov/open-source/) | City-maintained open source code on GitHub. |
| Government Publications (Library) | [sandiego.gov/public-library/govpub](https://www.sandiego.gov/public-library/govpub) | Historical and current government publications. |

### Hackathon Tips — Open Data
- The Open Data Portal supports **Socrata/SODA API** — you can query datasets programmatically with filters, pagination, and JSON responses.
- Start at the "Get Started" page for API keys and endpoint documentation.
- Datasets cover topics including permits, code enforcement, police calls, traffic, budgets, and more.

---

## Quick Contact

| Contact | Details |
|---------|---------|
| City Clerk (transcripts, municipal code) | **(619) 533-4000** · cityclerk@sandiego.gov |
| Development Services (permits, codes) | [sandiego.gov/development-services](https://www.sandiego.gov/development-services) |
| Open Data Portal | [data.sandiego.gov](https://data.sandiego.gov) |

---

*Last verified: February 25, 2026*
