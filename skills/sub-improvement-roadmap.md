---
name: multichannel-sentiment-crisis-detection-sub-improvement-roadmap
description: Improvement Roadmap sub-skill for the Multi-channel Sentiment Analysis (crisis detection) harness — Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
---

## Role
You are the **Improvement Roadmap** stage of the `multichannel-sentiment-crisis-detection` harness. You generate a prioritized, effort/impact-ranked set of recommendations that are directly traceable to the scored findings from the previous stage. Your roadmap is actionable, realistic, and grounded in the frameworks and evidence already established.

## Purpose
Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings. Transform diagnostic scores into an actionable improvement plan that stakeholders can implement systematically.

## Inputs
- Scoring results from `sub-scoring-engine`
- Framework selection from `sub-framework-selector`
- Case context from intake
- Compliance check results (if any constraints affect recommendations)

## Process

### Step 1: Map Low Scores to Improvement Areas

For each dimension with a score below the target threshold (typically < 80), identify specific improvement opportunities:

| Dimension Score | Interpretation | Priority Level |
|---|---|---|
| 0-59 | Critical gap; immediate action needed | HIGH |
| 60-74 | Significant gap; plan within 1-2 quarters | MEDIUM |
| 75-89 | Minor gap; optimize when possible | LOW |
| 90-100 | Excellent; maintain current practices | NONE |

### Step 2: Generate Specific Recommendations

For each improvement area, create specific, actionable recommendations using the SMART framework:
- **Specific**: Clear action item
- **Measurable**: Can verify completion
- **Achievable**: Realistic given resources
- **Relevant**: Directly addresses the scored gap
- **Time-bound**: Has a clear timeline

**Recommendation Template**:
```
Title: [Action-oriented recommendation]

Dimension Addressed: [Which scoring dimension]
Source Finding: [Specific weakness from scoring results]
Framework Basis: [Which framework/research supports this recommendation]

Description: [2-3 sentences explaining what to do and why]

Implementation Steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Resources Required: [What's needed: budget, tools, personnel, time]

Estimated Effort: [HIGH/MEDIUM/LOW] with rationale
Expected Impact: [HIGH/MEDIUM/LOW] with quantified improvement potential

Timeline: [Specific duration or milestone]

Dependencies: [What must happen first]
Risks: [What could go wrong and how to mitigate]

Success Metrics: [How to measure completion and effectiveness]
Traceability: [Direct link to scoring dimension and specific finding]
```

### Step 3: Prioritize by Effort × Impact

Use the **Effort/Impact Matrix** to prioritize:

```
HIGH IMPACT    │  (1) Do First      │  (2) Schedule Next
               │  [High Impact      │  [High Impact
               │   Low Effort]      │   High Effort]
───────────────┼────────────────────┼────────────────────
MEDIUM/LOW     │  (3) Backlog       │  (4) Avoid/Defer
IMPACT         │  [Low Impact       │  [Low Impact
               │   Low Effort]      │   High Effort]
               │────────────────────┼────────────────────
               │ LOW EFFORT         │ HIGH EFFORT
```

**Quadrant Definitions**:
- **Do First (Q1)**: Maximum quick wins; implement immediately
- **Schedule Next (Q2)**: High value but requires planning; schedule for next quarter
- **Backlog (Q3)**: Low-value quick wins; do when resources allow
- **Avoid/Defer (Q4)**: Low-value, high-effort; not worth pursuing currently

### Step 4: Structure the Roadmap Output

```yaml
improvement_roadmap:
  summary:
    total_recommendations: "[Number]"
    high_priority: "[Number]"
    medium_priority: "[Number]"
    low_priority: "[Number]"
    overall_improvement_potential: "[Points achievable if all implemented]"
    quick_wins_available: true/false

  prioritized_recommendations:
    - priority: 1
      quadrant: "DO_FIRST"
      title: "[Recommendation title]"
      dimension_addressed: "[Dimension name]"
      source_finding: "[Specific scoring weakness]"
      framework_basis: "[Framework + citation]"
      description: "[2-3 sentence explanation]"
      implementation_steps:
        - "[Step 1]"
        - "[Step 2]"
        - "[Step 3]"
      resources_required:
        - "[Resource 1]"
        - "[Resource 2]"
      estimated_effort: HIGH/MEDIUM/LOW
      effort_justification: "[Why this effort level]"
      expected_impact: HIGH/MEDIUM/LOW
      impact_quantification: "[Expected score improvement: X points]"
      timeline: "[Duration or milestone]"
      dependencies: "[What must happen first]"
      risks:
        - "[Risk 1]: [Mitigation]"
      success_metrics:
        - "[Metric 1]"
        - "[Metric 2]"
      traceability:
        dimension: "[Dimension name]"
        current_score: "[Current score]"
        target_score: "[Expected score after implementation]"

    - priority: 2
      quadrant: "SCHEDULE_NEXT"
      [Same structure as above]

    - priority: 3
      quadrant: "BACKLOG"
      [Same structure as above]

  effort_impact_matrix:
    high_impact_low_effort: "[Count] recommendations"
    high_impact_high_effort: "[Count] recommendations"
    low_impact_low_effort: "[Count] recommendations"
    low_impact_high_effort: "[Count] recommendations"

  implementation_phasing:
    phase_1_immediate_0_3_months:
      recommendations: "[Priority numbers]"
      quick_wins: "[Count]"
      expected_improvement: "[Score points]"

    phase_2_short_term_3_6_months:
      recommendations: "[Priority numbers]"
      expected_improvement: "[Score points]"

    phase_3_medium_term_6_12_months:
      recommendations: "[Priority numbers]"
      expected_improvement: "[Score points]"

    phase_4_long_term_12_plus_months:
      recommendations: "[Priority numbers]"
      expected_improvement: "[Score points]"

  dependency_graph:
    - recommendation: "[Recommendation title]"
      depends_on: "[Prerequisite recommendation]"
      reason: "[Why it's a dependency]"

  resource_summary:
    budget_required: "[Estimated total budget]"
    personnel_required: "[Roles and FTE estimates]"
    tools_platforms: "[New tools or platforms needed]"
    external_support: "[Consultants, vendors, or training needed]"

  risk_assessment:
    implementation_risks:
      - risk: "[Risk description]"
        likelihood: HIGH/MEDIUM/LOW
        impact: HIGH/MEDIUM/LOW
        mitigation: "[Mitigation strategy]"

    not_doing_risks:
      - risk: "[Risk if recommendation NOT implemented]"
        consequence: "[What happens if skipped]"

  tracking_mechanism:
    review_cadence: "[How often to check progress]"
    owner_assignment: "[Who owns each recommendation]"
    success_dashboard: "[How to track completion]"
    kpis_to_monitor: "[Key performance indicators]"
```

### Step 5: Validate Roadmap Quality

Before outputting, confirm:
- [ ] Each recommendation traces to a specific scoring dimension
- [ ] Effort and impact estimates are realistic (not optimistic)
- [ ] Prioritization follows the effort/impact matrix logic
- [ ] Timeline accounts for dependencies
- [ ] Resources required are clearly specified
- [ ] Success metrics are measurable
- [ ] Quick wins are identified for early momentum

## Output Format
Return a structured result containing:
1. **Prioritized recommendations** with full details
2. **Effort/impact matrix** classification
3. **Implementation phasing** (immediate, short-term, medium-term, long-term)
4. **Dependency graph** showing recommendation relationships
5. **Resource summary** (budget, personnel, tools)
6. **Risk assessment** (implementation and not-doing risks)
7. **Tracking mechanism** (how to monitor progress)

## Quality Gate
Before passing to synthesis, verify:
- [ ] All recommendations trace to specific scoring findings
- [ ] Prioritization is consistent with effort/impact assessment
- [ ] Framework basis is cited for each recommendation
- [ ] Implementation steps are actionable (not vague)
- [ ] Resources and timelines are realistic
- [ ] Success metrics are measurable
- [ ] Quick wins are highlighted for stakeholder buy-in

## Example Output

**Case**: Social media crisis after product launch (Overall score: 72/C)

```yaml
improvement_roadmap:
  summary:
    total_recommendations: 7
    high_priority: 3
    medium_priority: 3
    low_priority: 1
    overall_improvement_potential: 28
    quick_wins_available: true

  prioritized_recommendations:
    - priority: 1
      quadrant: "DO_FIRST"
      title: "Implement formal anomaly detection for early warning"
      dimension_addressed: "Early crisis signal detection"
      source_finding: "No formal anomaly detection; reactive vs. proactive (Score: 55/100)"
      framework_basis: "Velocity/Anomaly Detection (Yang et al., 2020; Castillo et al., 2021)"
      description: "Deploy statistical anomaly detection (Isolation Forest or One-Class SVM) on sentiment velocity data to identify spikes 2σ above historical baseline. This enables 4-6 hour early warning vs. current <1 hour lead time."
      implementation_steps:
        - "Export last 90 days of sentiment timestamp data"
        - "Train Isolation Forest model on historical baseline"
        - "Set alert threshold at 2σ with 4-hour lookback"
        - "Configure automated alerts to PR team"
      resources_required:
        - "Data scientist for model training (0.5 FTE, 2 weeks)"
        - "Anomaly detection library (scikit-learn or PyCaret, open-source)"
        - "Alert integration with existing monitoring tools"
      estimated_effort: LOW
      effort_justification: "Uses existing data; libraries are open-source; integration is straightforward"
      expected_impact: HIGH
      impact_quantification: "20-point improvement in Early crisis signal detection (55 → 75)"
      timeline: "2-3 weeks"
      dependencies: "None"
      risks:
        - "False positives may trigger unnecessary alerts: Mitigate with 4-hour sustained threshold"
      success_metrics:
        - "Model achieves >70% true positive rate in validation"
        - "Alert provides 4+ hour warning before sentiment spikes are evident to stakeholders"
      traceability:
        dimension: "Early crisis signal detection"
        current_score: 55
        target_score: 75

    - priority: 2
      quadrant: "DO_FIRST"
      title: "Add emotion detection and aspect-based sentiment"
      dimension_addressed: "Sentiment accuracy & coverage"
      source_finding: "Limited emotion detection; no aspect-based sentiment (Score: 85/100, improvement potential: 6)"
      framework_basis: "NLP Sentiment Analysis (Transformer) - ABSA (Pontiki et al., 2015)"
      description: "Extend current BERT-based sentiment to include emotion classification (joy, anger, fear, sadness) and aspect-based sentiment for product features. This improves granularity for crisis severity assessment."
      implementation_steps:
        - "Fine-tune BERT model on emotion-labeled dataset (e.g., CARER or GoEmotions)"
        - "Implement aspect-based sentiment using ABSA pipeline"
        - "Validate model on product-specific sentiment data"
        - "Update reporting to show emotion and aspect breakdowns"
      resources_required:
        - "ML engineer for model fine-tuning (1 FTE, 4 weeks)"
        - "Labeled emotion dataset (public or annotated)"
        - "Compute resources for model training"
      estimated_effort: MEDIUM
      effort_justification: "Requires model fine-tuning and data annotation effort"
      expected_impact: MEDIUM
      impact_quantification: "6-point improvement in Sentiment accuracy (85 → 91)"
      timeline: "4-6 weeks"
      dependencies: "None"
      risks:
        - "Model accuracy on domain-specific language may be lower: Mitigate with domain adaptation"
      success_metrics:
        - "Emotion classification F1-score > 0.80"
        - "Aspect-based sentiment accurately identifies product features in 80%+ of cases"
      traceability:
        dimension: "Sentiment accuracy & coverage"
        current_score: 85
        target_score: 91

    - priority: 3
      quadrant: "DO_FIRST"
      title: "Integrate SCCT framework for response matching"
      dimension_addressed: "Response recommendation quality"
      source_finding: "Response not matched to crisis cluster (Score: 62/100)"
      framework_basis: "SCCT (Coombs, 2007); Response effectiveness (Coombs & Holladay, 2018)"
      description: "Implement SCCT framework to classify crisis type (victim/accidental/preventable) and match to appropriate response strategy. This increases response effectiveness from generic to framework-aligned (72% effectiveness when matched)."
      implementation_steps:
        - "Create SCCT classification matrix for crisis types"
        - "Train classifier to identify crisis cluster from sentiment patterns"
        - "Map response strategies to crisis clusters per SCCT"
        - "Integrate into crisis alert system with recommended responses"
      resources_required:
        - "Crisis communication consultant for framework alignment (0.2 FTE, 2 weeks)"
        - "Developer for integration (0.5 FTE, 3 weeks)"
      estimated_effort: LOW
      effort_justification: "Framework is documented; implementation is rule-based"
      expected_impact: HIGH
      impact_quantification: "15-point improvement in Response quality (62 → 77)"
      timeline: "3-4 weeks"
      dependencies: "Recommendation #1 (anomaly detection) for trigger context"
      risks:
        - "Framework may not fit all crisis types: Mitigate with manual override for edge cases"
      success_metrics:
        - "Crisis classification accuracy >80% in validation"
        - "Response recommendations align with SCCT guidance in 90%+ of cases"
      traceability:
        dimension: "Response recommendation quality"
        current_score: 62
        target_score: 77

    - priority: 4
      quadrant: "SCHEDULE_NEXT"
      title: "Implement multi-factor severity scoring"
      dimension_addressed: "Severity & escalation scoring"
      source_finding: "Single-factor severity (sentiment only); no escalation prediction (Score: 68/100)"
      framework_basis: "Severity prediction (Olteanu et al., 2019); Escalation modeling"
      description: "Expand severity scoring from sentiment-only to multi-factor model including reach, stakeholder impact, sentiment depth, and escalation probability. This improves crisis triage and resource allocation."
      implementation_steps:
        - "Define severity factor weights (sentiment, reach, stakeholder, escalation)"
        - "Implement escalation prediction model (LSTM or statistical)"
        - "Create severity dashboard with multi-factor visualization"
        - "Validate severity scores against historical crisis outcomes"
      resources_required:
        - "Data scientist (1 FTE, 6 weeks)"
        - "Stakeholder mapping exercise with PR team"
      estimated_effort: HIGH
      effort_justification: "Requires model development, stakeholder input, and validation"
      expected_impact: HIGH
      impact_quantification: "11-point improvement in Severity scoring (68 → 79)"
      timeline: "2-3 months"
      dependencies: "Recommendation #2 (emotion/aspect sentiment) for depth scoring"
      risks:
        - "Stakeholder input may be subjective: Mitigate with weighted consensus approach"
      success_metrics:
        - "Severity model predicts escalation direction with >65% accuracy"
        - "Severity scores correlate with actual crisis outcomes (r > 0.7)"
      traceability:
        dimension: "Severity & escalation scoring"
        current_score: 68
        target_score: 79

    - priority: 5
      quadrant: "SCHEDULE_NEXT"
      title: "Expand channel coverage to review platforms and forums"
      dimension_addressed: "Channel coverage & aggregation"
      source_finding: "4 channels vs. 8+ recommended; unweighted aggregation (Score: 70/100)"
      framework_basis: "Multi-channel best practices (Brandwatch, Sprout Social)"
      description: "Add review platforms (Yelp, Google Reviews, App Store) and forums (Reddit, Discord, industry forums) to monitoring scope. Implement weighted aggregation by channel relevance and audience size."
      implementation_steps:
        - "Identify top 5 review/forums for brand's industry"
        - "Set up data collection (APIs or web scraping compliant with terms)"
        - "Implement channel weighting based on audience size and relevance"
        - "Update aggregation pipeline to include weighted channels"
      resources_required:
        - "Developer for API integrations (1 FTE, 4 weeks)"
        - "API access costs (estimate: $500-2000/month depending on platforms)"
      estimated_effort: MEDIUM
      effort_justification: "API integration and compliance setup required"
      expected_impact: MEDIUM
      impact_quantification: "4.5-point improvement in Channel coverage (70 → 74.5)"
      timeline: "6-8 weeks"
      dependencies: "None"
      risks:
        - "Some forums may have restrictive APIs: Mitigate with public-only scraping where allowed"
      success_metrics:
        - "8+ channels actively monitored"
        - "Weighted aggregation improves crisis detection sensitivity by 15%"
      traceability:
        dimension: "Channel coverage & aggregation"
        current_score: 70
        target_score: 74.5

    - priority: 6
      quadrant: "BACKLOG"
      title: "Add real-time monitoring capability"
      dimension_addressed: "Channel coverage & aggregation"
      source_finding: "Near-real-time (5-15 min delay) vs. true real-time"
      framework_basis: "Industry standard for crisis monitoring (Brandwatch, Talkwalker)"
      description: "Reduce data processing latency from 5-15 minutes to <1 minute for true real-time crisis detection. Important for fast-moving crises on social media."
      implementation_steps:
        - "Optimize data pipeline for streaming vs. batch processing"
        - "Implement incremental sentiment scoring"
        - "Deploy auto-scaling infrastructure for spike handling"
      resources_required:
        - "Infrastructure engineer (0.5 FTE, 4 weeks)"
        - "Cloud infrastructure costs (increase: $200-500/month)"
      estimated_effort: MEDIUM
      effort_justification: "Pipeline architecture changes required"
      expected_impact: LOW
      impact_quantification: "2-3 point improvement in Channel coverage; marginal for other dimensions"
      timeline: "2-3 months"
      dependencies: "Recommendation #5 (expanded channel coverage)"
      risks:
        - "Cost increase for streaming infrastructure: ROI depends on crisis frequency"
      success_metrics:
        - "End-to-end latency < 1 minute from post to score"
        - "System handles 10x traffic spikes without degradation"
      traceability:
        dimension: "Channel coverage & aggregation"
        current_score: 70
        target_score: 73

    - priority: 7
      quadrant: "SCHEDULE_NEXT"
      title: "Develop Image Repair strategy playbooks"
      dimension_addressed: "Response recommendation quality"
      source_finding: "No Image Repair strategy selection (Score: 62/100)"
      framework_basis: "Image Repair Theory (Benoit, 1995); Strategy effectiveness (Kim et al., 2019)"
      description: "Create detailed response playbooks for each Image Repair strategy (denial, reduction, corrective action, mortification) with templates and decision trees. Enables rapid, theory-aligned response in crisis situations."
      implementation_steps:
        - "Document Image Repair strategies with decision criteria"
        - "Create response templates for each strategy"
        - "Build decision tree for strategy selection"
        - "Train PR team on playbook usage"
      resources_required:
        - "Crisis communication consultant (0.5 FTE, 4 weeks)"
        - "PR team training (2 days)"
      estimated_effort: MEDIUM
      effort_justification: "Requires documentation and training; no technical implementation"
      expected_impact: MEDIUM
      impact_quantification: "5-point improvement in Response quality (when combined with SCCT)"
      timeline: "4-6 weeks"
      dependencies: "Recommendation #3 (SCCT integration) for crisis classification"
      risks:
        - "Templates may feel generic: Mitigate with brand voice customization"
      success_metrics:
        - "Playbook used in 90%+ of crisis responses within 6 months"
        - "Response time reduced by 50% with playbook usage"
      traceability:
        dimension: "Response recommendation quality"
        current_score: 62
        target_score: 67 (with SCCT: 82)

  effort_impact_matrix:
    high_impact_low_effort: 3
    high_impact_high_effort: 1
    low_impact_low_effort: 1
    low_impact_high_effort: 0

  implementation_phasing:
    phase_1_immediate_0_3_months:
      recommendations: [1, 2, 3]
      quick_wins: 3
      expected_improvement: 41
      description: "Implement quick wins for immediate impact: anomaly detection, emotion detection, SCCT framework"

    phase_2_short_term_3_6_months:
      recommendations: [5, 7]
      expected_improvement: 9.5
      description: "Expand capabilities with channel coverage and Image Repair playbooks"

    phase_3_medium_term_6_12_months:
      recommendations: [4, 6]
      expected_improvement: 13
      description: "Complete advanced features: multi-factor severity, real-time monitoring"

    phase_4_long_term_12_plus_months:
      recommendations: []
      expected_improvement: 0
      description: "Maintain and optimize; no long-term items in current roadmap"

  dependency_graph:
    - recommendation: "SCCT framework integration"
      depends_on: "Anomaly detection for early warning"
      reason: "SCCT benefits from early warning context for appropriate response timing"

    - recommendation: "Multi-factor severity scoring"
      depends_on: "Emotion and aspect-based sentiment"
      reason: "Severity model uses sentiment depth from emotion detection"

    - recommendation: "Image Repair playbooks"
      depends_on: "SCCT framework integration"
      reason: "Playbooks build on SCCT crisis classification"

  resource_summary:
    budget_required: "$15,000-25,000 one-time + $500-2,500/month ongoing"
    budget_breakdown:
      - "Personnel (data scientists, developers, consultants): $15,000-20,000"
      - "API access costs: $500-2,000/month"
      - "Infrastructure (real-time scaling): $200-500/month increase"
    personnel_required:
      - "Data scientist: 1.5 FTE for 8-12 weeks"
      - "ML engineer: 1 FTE for 4-6 weeks"
      - "Developer: 1 FTE for 6-10 weeks"
      - "Crisis communication consultant: 0.7 FTE for 6-10 weeks"
    tools_platforms:
      - "scikit-learn or PyCaret (open-source)"
      - "Review platform APIs (Yelp, Google, App Store)"
      - "Cloud infrastructure for real-time processing"
    external_support:
      - "Crisis communication consultant for SCCT and Image Repair alignment"
      - "Potential training on advanced sentiment analysis techniques"

  risk_assessment:
    implementation_risks:
      - risk: "Model accuracy on domain-specific language may be lower than benchmarks"
        likelihood: MEDIUM
        impact: MEDIUM
        mitigation: "Domain adaptation with fine-tuning on brand-specific data"

      - risk: "False positives from anomaly detection may cause alert fatigue"
        likelihood: MEDIUM
        impact: MEDIUM
        mitigation: "Require 4-hour sustained threshold before alerting"

      - risk: "Stakeholder input for severity scoring may be subjective"
        likelihood: HIGH
        impact: LOW
        mitigation: "Use weighted consensus approach with multiple stakeholders"

    not_doing_risks:
      - risk: "No early warning system continues to mean reactive crisis response"
        consequence: "4-6 hour delay in crisis detection; potential for crisis to escalate before response"

      - risk: "Response not matched to crisis type per SCCT"
        consequence: "28% reduction in response effectiveness (Coombs & Holladay, 2018)"

      - risk: "Limited channel coverage misses emerging crises on untapped platforms"
        consequence: "Bl spots in monitoring; crisis may emerge on unmonitored channels"

  tracking_mechanism:
    review_cadence: "Bi-weekly roadmap review during implementation; monthly thereafter"
    owner_assignment:
      - "Recommendations 1-2: Data Science Lead"
      - "Recommendation 3: Crisis Communication Lead"
      - "Recommendations 4-6: Engineering Lead (with PR team input)"
    success_dashboard:
      - "Track overall score progression by dimension"
      - "Monitor recommendation completion status"
      - "Alert when recommendations fall behind timeline"
    kpis_to_monitor:
      - "Overall score improvement trajectory (target: 72 → 90 in 12 months)"
      - "Time-to-detect for crisis signals (target: <4 hours before evident)"
      - "Response alignment with SCCT (target: 90%+ compliance)"
      - "Channel coverage count (target: 8+ channels)"
```

## Integration Notes
- Every recommendation must trace directly to a scoring weakness—no generic "best practices"
- Prioritize quick wins (Q1) for stakeholder buy-in and early momentum
- Be realistic about timelines—over-promising damages credibility
- Include "not doing" risks to show the cost of inaction
- Update roadmap as conditions change (new data, new crises, resource shifts)

## Roadmap Maintenance
- Review quarterly with stakeholders
- Re-score dimensions after major implementations
- Add new recommendations based on evolving needs
- Deprioritize items that become obsolete
- Track actual vs. expected impact to improve estimation
