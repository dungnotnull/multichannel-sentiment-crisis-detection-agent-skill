# CLAUDE.md — Multi-channel Sentiment Analysis (crisis detection) (Skill #153)

**Slug:** `multichannel-sentiment-crisis-detection`  •  **Cluster:** `marketing-content-branding`  •  **Source idea:** 153  •  **Phase:** Built (v1)

## Tagline
Analyzes multi-channel customer sentiment to detect emerging PR crises early and recommend evidence-based response strategies.

## Problem This Skill Solves
Brands detect reputational crises too late because sentiment is scattered across channels with no early-warning scoring. This skill aggregates multi-channel sentiment, detects crisis signals, scores severity, and recommends a response grounded in crisis-communication theory.

## Harness Flow Summary
1. **Intake** (`sub-intake`) — gather structured inputs, scope, goals.

2. **Framework selection** (`sub-framework-selector`) — choose named world-renowned framework(s).
3. **Research** (WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN) — gather highest-tier evidence.
4. **Scoring** (`sub-scoring-engine`) — multi-dimensional weighted scores with citations.
5. **Challenge** — devil's-advocate review of assumptions and weak evidence.
7. **Compliance check** (`sub-compliance-check`) — verify against laws/standards.
**Roadmap** (`sub-improvement-roadmap`) — prioritized effort/impact recommendations.
**Synthesize** — assemble the professional deliverable; pass Quality Gates.

## Gates
- **Compliance gate:** `sub-compliance-check` MUST run before final output (regulated content).

## Sub-skills
- `skills/sub-intake.md` — Intake & Context Gathering: Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- `skills/sub-framework-selector.md` — Evaluation Framework Selector: Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- `skills/sub-scoring-engine.md` — Scoring Engine: Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- `skills/sub-compliance-check.md` — Compliance Check: Verify the output against applicable laws, regulations, and platform/industry standards before release; flag anything needing professional/legal review.
- `skills/sub-improvement-roadmap.md` — Improvement Roadmap: Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.

## Tools Required
- `WebSearch`, `WebFetch` — live evidence and standards updates
- `Read`, `Write` — load knowledge base, emit deliverables
- `Bash` — run `tools/knowledge_updater.py`
- Skill tool — invoke sub-skills in sequence

## Knowledge Sources
- ArXiv: cs.CL, cs.SI
- Authoritative domain sources:
  - https://www.brandwatch.com
  - https://sproutsocial.com/insights
  - https://instituteforpr.org
  - https://www.talkwalker.com
- Crawl queries: sentiment analysis NLP social media; crisis communication SCCT theory; social listening early crisis detection; brand reputation crisis case study

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that grows `SECOND-KNOWLEDGE-BRAIN.md` (weekly cron recommended).

## Active Development Tasks
- [x] Scaffold full deliverable set
- [x] Define 5 sub-skills
- [ ] Expand SECOND-KNOWLEDGE-BRAIN with first live crawl
- [ ] Add regression cases from real user runs

## Related Root Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving knowledge base
