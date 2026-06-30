# PROJECT-detail.md — Multi-channel Sentiment Analysis (crisis detection) (Skill #153)

## Executive Summary
Analyzes multi-channel customer sentiment to detect emerging PR crises early and recommend evidence-based response strategies. This skill is a full Claude harness in the **marketing-content-branding** cluster. It runs a research-first, framework-grounded workflow that scores the subject against named world-renowned methodologies and returns a prioritized improvement roadmap, while continuously updating its knowledge base.

## Problem Statement
Brands detect reputational crises too late because sentiment is scattered across channels with no early-warning scoring. This skill aggregates multi-channel sentiment, detects crisis signals, scores severity, and recommends a response grounded in crisis-communication theory.

## Target Users & Use Cases
Practitioners, reviewers, and decision-makers who need an expert-grade, evidence-based assessment in this domain. Trigger examples:
1. **Sentiment scan** — User: "Analyze sentiment on our last launch" -> Skill aggregates channels, scores net sentiment, flags risks.
2. **Crisis alert** — User: "Is this complaint thread a crisis?" -> Skill scores velocity/severity, recommends SCCT response.
3. **Response plan** — User: "Draft a response to backlash" -> Skill applies Image Repair, scores fit, checks data privacy.
4. **Competitor scan** — User: "Compare our sentiment vs rival" -> Skill computes share-of-voice, net sentiment delta.
5. **Degraded mode** — User: "Analyze offline sample" -> Falls back to brain models, flags live data unavailable.

## Harness Architecture
```
/multichannel-sentiment-crisis-detection (main.md)
   ├── sub-intake .................... Intake & Context Gathering
   ├── sub-framework-selector ........ Evaluation Framework Selector
   ├── sub-scoring-engine ............ Scoring Engine
   ├── sub-compliance-check .......... Compliance Check
   ├── sub-improvement-roadmap ....... Improvement Roadmap
   ├── [research] WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN
   ├── [challenge] devil's-advocate assumption review
   └── synthesize ................... professional deliverable + quality gates
```

## Full Sub-Skill Catalog
### sub-intake — Intake & Context Gathering
- **Purpose:** Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-framework-selector — Evaluation Framework Selector
- **Purpose:** Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-scoring-engine — Scoring Engine
- **Purpose:** Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-compliance-check — Compliance Check
- **Purpose:** Verify the output against applicable laws, regulations, and platform/industry standards before release; flag anything needing professional/legal review.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-improvement-roadmap — Improvement Roadmap
- **Purpose:** Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.

## Evaluation Frameworks (World-Renowned, Citable)
| Framework / Standard | Role in this skill |
|---|---|
| NLP sentiment analysis (lexicon + transformer) | Polarity, emotion, aspect-based sentiment. |
| Situational Crisis Communication Theory (SCCT) | Matches response to crisis type/responsibility. |
| Image Repair Theory (Benoit) | Repair strategies: denial, reduction, corrective action. |
| Net Sentiment Score & share-of-voice | Quantified brand health signals. |
| Velocity/anomaly detection | Spike detection for early crisis warning. |

## Scoring Model
| Dimension | Weight | What is assessed |
|---|---|---|
| Sentiment accuracy & coverage | 25% | polarity/emotion correctness across channels |
| Early crisis signal detection | 25% | velocity/anomaly spotting before escalation |
| Channel coverage & aggregation | 15% | breadth of monitored sources |
| Severity & escalation scoring | 20% | reach, sentiment depth, stakeholder risk |
| Response recommendation quality | 15% | SCCT-matched, actionable, timely |
Each dimension is scored 0-100 with cited evidence; the weighted total yields an overall grade (A: 90+, B: 75-89, C: 60-74, D: <60).

## Skill File Format Specification
- Frontmatter: `name`, `description`.
- Required sections: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates.

## E2E Execution Flow
1. Parse user request; if inputs are insufficient, `sub-intake` asks targeted questions.

3. `sub-framework-selector` picks framework(s) and justifies the choice.
4. Research stage gathers highest-tier evidence (see evidence hierarchy); degrade gracefully to SECOND-KNOWLEDGE-BRAIN if offline.
5. `sub-scoring-engine` scores each dimension with citations.
6. Challenge stage stress-tests conclusions.
7. `sub-compliance-check` verifies output against applicable laws/standards.
8. `sub-improvement-roadmap` produces ranked actions.
9. Synthesize deliverable; run Quality Gates; present.

**Error handling:** missing inputs -> ask; conflicting evidence -> present both and grade certainty; tool failure -> fallback + explicit limitation notice.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: https://www.brandwatch.com, https://sproutsocial.com/insights, https://instituteforpr.org, https://www.talkwalker.com
- ArXiv categories: cs.CL, cs.SI
- Crawl queries: sentiment analysis NLP social media; crisis communication SCCT theory; social listening early crisis detection; brand reputation crisis case study
- Append format: dated entries with Title, Authors, Year, Venue, DOI/URL, key finding, relevance.

## Supporting Tools Spec
`tools/knowledge_updater.py`: inputs = source list + queries; outputs = appended SECOND-KNOWLEDGE-BRAIN entries; schedule = weekly cron; dedup by URL/DOI hash.

## Quality Gates (must all pass before final output)
- Compliance check passed against applicable laws/standards before release.
- Every score cites at least one source or the chosen framework.
- Challenge stage completed; key assumptions tested.
- Roadmap items are prioritized by effort and impact and traceable to findings.
- Limitations and evidence certainty are stated explicitly.

## Test Scenarios
1. **Sentiment scan** — User: "Analyze sentiment on our last launch" -> Skill aggregates channels, scores net sentiment, flags risks.
2. **Crisis alert** — User: "Is this complaint thread a crisis?" -> Skill scores velocity/severity, recommends SCCT response.
3. **Response plan** — User: "Draft a response to backlash" -> Skill applies Image Repair, scores fit, checks data privacy.
4. **Competitor scan** — User: "Compare our sentiment vs rival" -> Skill computes share-of-voice, net sentiment delta.
5. **Degraded mode** — User: "Analyze offline sample" -> Falls back to brain models, flags live data unavailable.

## Key Design Decisions
1. Framework-grounded scoring (no ad-hoc criteria).
2. Research-first with graceful degradation to the local knowledge brain.
3. Mandatory challenge stage to counter confirmation bias.
4. compliance check standard quality gates enforced before delivery.
5. Self-improving knowledge base via weekly crawl.
