# Test Scenarios — Multi-channel Sentiment Analysis (crisis detection) (Skill #153)

## Overview

These scenarios validate the harness end-to-end: stage order, framework grounding, scoring with citations, gates, roadmap, and graceful degradation. Each scenario includes sample inputs, expected step-by-step processing, and validation criteria.

## Test Execution Template

For each scenario:
1. **Input**: User request
2. **Expected Stage Sequence**: Which stages execute in what order
3. **Expected Outputs**: What each stage produces
4. **Validation Criteria**: Pass/fail checkpoints
5. **Sample Output**: Full example response

---

## Scenario 1: Sentiment Scan

### User Input
```
"Analyze sentiment on our last product launch. We launched TechWidget X500
on June 1st and I'm concerned about the reaction on social media."
```

### Expected Stage Sequence

1. **sub-intake** → Gather brand, launch date, channels, baseline
2. **sub-framework-selector** → Select NLP + Net Sentiment + Channel Coverage frameworks
3. **Research** → Fetch latest sentiment analysis benchmarks
4. **sub-scoring-engine** → Score all 5 dimensions
5. **Challenge** → Verify assumptions about data representativeness
6. **sub-compliance-check** → Verify no PII, proper attribution
7. **sub-improvement-roadmap** → Prioritize quick wins for sentiment improvement
8. **Synthesize** → Assemble professional report

### Expected Outputs by Stage

#### sub-intake Output
```yaml
intake_summary:
  subject:
    brand: "TechWidget X500"
    industry: "Consumer Technology"
    primary_products: "TechWidget X500"
    target_audience: "Tech enthusiasts, early adopters"

  scope:
    timeframe:
      start: "2026-06-01"
      end: "2026-06-30"
    geographic: "Global"
    languages: "English, Spanish, Japanese"

  channels:
    social:
      - platform: "Twitter/X"
        has_data_access: true
        data_volume: "high"
      - platform: "Reddit"
        has_data_access: true
        data_volume: "medium"
    review:
      - platform: "Amazon"
        has_data_access: true
        data_volume: "high"
      - platform: "Google Play"
        has_data_access: true
        data_volume: "medium"

  goals:
    primary: "Assess post-launch sentiment health"
    secondary:
      - "Identify any crisis signals"
      - "Benchmark against pre-launch baseline"

  thresholds:
    sentiment_baseline: "72% net sentiment (pre-launch)"
    crisis_trigger: "2σ below baseline for 4+ hours"
    response_time: "Within 60 minutes of detection"
```

#### sub-framework-selector Output
```yaml
framework_selection:
  selected_frameworks:
    - framework: "NLP Sentiment Analysis (Transformer - BERT/RoBERTa)"
      citation: "Devlin et al., 2019, NAACL"
      rationale: "High accuracy required for launch sentiment assessment"
      application: "Polarity and emotion scoring across social media and reviews"

    - framework: "Net Sentiment Score"
      citation: "Industry standard; Gavra et al., 2020"
      rationale: "Quantified brand health metric for launch comparison"
      application: "(Positive - Negative) / Total mentions"

    - framework: "Channel Coverage & Aggregation"
      citation: "Industry best practices from Brandwatch, Sprout Social"
      rationale: "Multi-channel launch requires weighted aggregation"
      application: "Weight by audience size and platform relevance"

  excluded_frameworks:
    - framework: "SCCT"
      rationale: "No crisis identified yet; crisis detection not primary goal"
    - framework: "Image Repair Theory"
      rationale: "Response planning not requested"
```

#### sub-scoring-engine Output (Sample)
```yaml
scoring_results:
  overall:
    weighted_score: 78
    grade: B
    confidence: medium
    assessment: "Good sentiment analysis capability with room for improvement in early warning"

  dimensions:
    sentiment_accuracy_coverage:
      score: 88
      weight: 0.25
      weighted_contribution: 22
      evidence:
        - "BERT F1-score of 0.87 on similar datasets (Devlin et al., 2019)"
      improvement_potential: 2

    early_crisis_signal_detection:
      score: 65
      weight: 0.25
      weighted_contribution: 16.25
      evidence:
        - "No formal anomaly detection (Yang et al., 2020 benchmark: 4-6 hour lead time)"
      improvement_potential: 10

    channel_coverage_aggregation:
      score: 82
      weight: 0.15
      weighted_contribution: 12.3
      evidence:
        - "4 channels covered vs. 8+ recommended"
      improvement_potential: 3

    severity_escalation_scoring:
      score: 70
      weight: 0.20
      weighted_contribution: 14
      evidence:
        - "Sentiment-based severity only (Olteanu et al., 2019 recommends multi-factor)"
      improvement_potential: 8

    response_recommendation_quality:
      score: 75
      weight: 0.15
      weighted_contribution: 11.25
      evidence:
        - "Basic response timing; no framework matching (Coombs, 2007)"
      improvement_potential: 5
```

### Validation Criteria

- [ ] **Correct stage order**: intake → framework → research → scoring → challenge → compliance → roadmap → synthesize
- [ ] **Framework named**: At least one framework cited with full academic reference
- [ ] **Scores cited**: Every dimension score has at least one evidence citation
- [ ] **Roadmap prioritized**: Recommendations ranked by effort × impact
- [ ] **Limitations stated**: Confidence level and data limitations disclosed
- [ ] **Compliance passed**: No PII, proper attribution, GDPR considerations addressed
- [ ] **No real execution**: No actual API calls or model training performed

### Pass/Fail Conditions

**PASS**: All validation criteria met; outputs match expected format

**FAIL**: Any of:
- Stage order incorrect or skipped
- Frameworks not properly cited
- Scores without evidence citations
- Roadmap not prioritized
- Compliance check missing or failed
- Real model/API execution attempted

---

## Scenario 2: Crisis Alert

### User Input
```
"Is this complaint thread on Reddit a crisis? We're getting a lot of
negative comments about our app's latest update crashing."
```

### Expected Stage Sequence

1. **sub-intake** → Identify app, update, complaint thread details
2. **sub-framework-selector** → Select SCCT + Anomaly Detection + NLP
3. **Research** → Fetch SCCT guidance, crisis detection benchmarks
4. **sub-scoring-engine** → Score crisis detection and response dimensions
5. **Challenge** → Verify if truly a crisis or normal complaint volume
6. **sub-compliance-check** → Verify Reddit API compliance, no PII
7. **sub-improvement-roadmap** → Prioritize crisis response and stability fixes
8. **Synthesize** → Crisis alert report with SCCT-matched response

### Expected Outputs by Stage

#### sub-intake Output
```yaml
intake_summary:
  subject:
    brand: "[App Name]"
    industry: "Mobile Software"
    primary_products: "Mobile application"
    incident: "App crash issues after latest update"

  scope:
    timeframe:
      start: "[Update release date]"
      end: "ongoing"
    geographic: "Global"
    channels:
      - platform: "Reddit"
        has_data_access: true
        specific_thread: "[Reddit thread URL]"

  goals:
    primary: "Determine if this constitutes a crisis requiring formal response"
    secondary:
      - "Assess crisis severity"
      - "Recommend appropriate response strategy"

  thresholds:
    crisis_trigger: "Sustained negative sentiment > 2σ for 4+ hours"
    response_time: "Within 60 minutes of crisis confirmation"
```

#### sub-framework-selector Output
```yaml
framework_selection:
  selected_frameworks:
    - framework: "Situational Crisis Communication Theory (SCCT)"
      citation: "Coombs, W.T., 2007, Corporate Reputation Review"
      rationale: "Crisis identification and response matching required"
      application: "Classify crisis type (victim/accidental/preventable) and recommend response"

    - framework: "Velocity/Anomaly Detection"
      citation: "Yang et al., 2020, IEEE Access; Castillo et al., 2021, ACM TWEB"
      rationale: "Determine if complaint volume exceeds normal thresholds"
      application: "Time-series analysis with 2σ threshold"

    - framework: "NLP Sentiment Analysis (Transformer)"
      citation: "Devlin et al., 2019, NAACL"
      rationale: "Sentiment severity assessment for crisis triage"
      application: "Polarity and emotion scoring for severity determination"

  excluded_frameworks:
    - framework: "Image Repair Theory"
      rationale: "Will be applied in roadmap stage after SCCT classification"
```

#### sub-scoring-engine Output (Sample)
```yaml
scoring_results:
  overall:
    weighted_score: 68
    grade: C
    confidence: high
    assessment: "Moderate crisis detection with gaps in early warning"

  dimensions:
    early_crisis_signal_detection:
      score: 78
      weight: 0.25
      weighted_contribution: 19.5
      assessment: "Complaint velocity 3.2σ above baseline; crisis confirmed"
      evidence:
        - "Velocity exceeds 2σ threshold (Yang et al., 2020)"
        - "Sustained for 6+ hours (exceeds 4-hour crisis threshold)"

    severity_escalation_scoring:
      score: 72
      weight: 0.20
      weighted_contribution: 14.4
      assessment: "Moderate severity; preventable crisis (software failure)"
      evidence:
        - "SCCT classification: Preventable crisis (Coombs, 2007)"
        - "Sentiment depth: Strong negative emotion in 65% of posts"

    response_recommendation_quality:
      score: 82
      weight: 0.15
      weighted_contribution: 12.3
      assessment: "SCCT-matched response recommended"
      evidence:
        - "Rebuild strategy for preventable crises (Coombs, 2007)"
        - "72% effectiveness when response matches crisis type (Coombs & Holladay, 2018)"
```

### Validation Criteria

- [ ] **Crisis classification**: SCCT framework applied correctly (victim/accidental/preventable)
- [ ] **Velocity measurement**: Anomaly detection with σ threshold
- [ ] **Response strategy matched**: Response aligns with SCCT guidance
- [ ] **Reddit compliance**: API terms acknowledged, no PII
- [ ] **Severity assessment**: Multi-factor severity scoring (not just sentiment)
- [ ] **Urgency communicated**: Clear statement of crisis status and timeline

### Pass/Fail Conditions

**PASS**: All validation criteria met; crisis properly classified with appropriate response

**FAIL**: Any of:
- SCCT not applied or misapplied
- Crisis status ambiguous or contradictory
- Response doesn't match crisis type
- Compliance issues with Reddit data
- No severity assessment

---

## Scenario 3: Response Plan

### User Input
```
"Draft a response to the backlash about our environmental policy.
Environmental groups are criticizing our new sustainability report."
```

### Expected Stage Sequence

1. **sub-intake** → Understand policy, criticism specifics, stakeholders
2. **sub-framework-selector** → Select SCCT + Image Repair Theory
3. **Research** → Fetch best practices for environmental crisis communication
4. **sub-scoring-engine** → Score response quality framework alignment
5. **Challenge** → Verify if criticism is justified or perception issue
6. **sub-compliance-check** → Verify claims are substantiated, no greenwashing
7. **sub-improvement-roadmap** → Recommend both response and policy improvements
8. **Synthesize** → Response plan with Image Repair strategy

### Expected Outputs by Stage

#### sub-intake Output
```yaml
intake_summary:
  subject:
    brand: "[Company Name]"
    incident: "Backlash against environmental sustainability report"
    critics: "Environmental groups, activists, concerned customers"

  scope:
    timeframe:
      start: "[Report release date]"
      end: "ongoing"
    channels:
      - "Twitter/X"
      - "News/Media coverage"
      - "Press statements"

  goals:
    primary: "Draft theory-backed response to environmental criticism"
    secondary:
      - "Assess if criticism is justified"
      - "Recommend policy improvements if needed"

  stakeholders:
    recipients: "PR team, executives, legal"
    compliance_requirements: "FTC guidelines for environmental claims, substantiation requirements"
```

#### sub-framework-selector Output
```yaml
framework_selection:
  selected_frameworks:
    - framework: "Image Repair Theory (Benoit)"
      citation: "Benoit, W.L., 1995"
      rationale: "Response strategy selection required"
      application: "Select from denial, evasion, reduction, corrective action, mortification"

    - framework: "Situational Crisis Communication Theory (SCCT)"
      citation: "Coombs, W.T., 2007"
      rationale: "Crisis type classification informs response"
      application: "Classify as preventable crisis with high responsibility"

    - framework: "FTC Endorsement Guides / Green Guides"
      citation: "FTC Environmental Marketing Guidelines"
      rationale: "Compliance check for environmental claims"
      application: "Verify all claims are substantiated"

  excluded_frameworks:
    - framework: "Anomaly Detection"
      rationale: "Crisis already identified; focus on response"
```

#### sub-scoring-engine Output (Sample)
```yaml
scoring_results:
  overall:
    weighted_score: 74
    grade: C
    confidence: medium
    assessment: "Moderate response capability; needs framework alignment"

  dimensions:
    response_recommendation_quality:
      score: 68
      weight: 0.15
      assessment: "Current approach not matched to crisis type"
      evidence:
        - "Preventable crisis requires Rebuild strategy (Coombs, 2007)"
        - "Corrective action + mortification most effective (Kim et al., 2019)"

    severity_escalation_scoring:
      score: 78
      weight: 0.20
      assessment: "High severity due to reputation risk and stakeholder impact"
      evidence:
        - "Reputational crises have high escalation risk (Olteanu et al., 2019)"
        - "Environmental concerns have high stakeholder impact"
```

#### Response Template Output
```markdown
## Recommended Response Strategy

**Framework**: Image Repair Theory (Benoit, 1995)
**SCCT Classification**: Preventable crisis, high responsibility attribution
**Recommended Strategy**: Corrective Action + Mortification

### Response Elements

1. **Acknowledge and Apologize** (Mortification)
   - "We hear the concerns about our sustainability report..."
   - "We apologize that our reporting did not meet expectations..."

2. **Take Responsibility** (Corrective Action)
   - "We commit to the following immediate actions..."
   - [Specific actions with timelines]

3. **Provide Evidence** (Reduction)
   - "Here is our full environmental impact data..."
   - "Third-party verification sources..."

4. **Commit to Improvement** (Rebuild)
   - "We are implementing the following changes..."
   - [Timeline and metrics]

### Compliance Notes

- All claims must be substantiated with data
- Avoid vague terms like "eco-friendly" without specific meaning
- Consider legal review before publication
- Disclose any limitations in environmental commitments
```

### Validation Criteria

- [ ] **Framework applied**: Image Repair theory correctly applied
- [ ] **Strategy matched**: Response aligns with preventable crisis classification
- [ ] **Claims substantiated**: Environmental claims have evidence
- [ ] **Legal review flagged**: Compliance check identifies legal review need
- [ ] **Stakeholder considered**: Response addresses environmental groups specifically
- [ ] **Actionable**: Response includes specific commitments and timelines

### Pass/Fail Conditions

**PASS**: All validation criteria met; response is theory-backed and compliant

**FAIL**: Any of:
- Image Repair theory not applied
- Response doesn't match crisis type
- Unsubstantiated environmental claims
- No compliance/legal review flagged
- Generic response without specific commitments

---

## Scenario 4: Competitor Scan

### User Input
```
"Compare our sentiment vs. CompetitorX this quarter. We're both in
the SaaS project management space and want to see who's winning."
```

### Expected Stage Sequence

1. **sub-intake** → Identify both companies, timeframe, channels for comparison
2. **sub-framework-selector** → Select Net Sentiment + SOV + Competitive benchmarking
3. **Research** → Fetch competitive analysis best practices
4. **sub-scoring-engine** → Score competitive intelligence capability
5. **Challenge** → Verify data comparability (same channels, same timeframe)
6. **sub-compliance-check** → Verify fair comparison, no misleading claims
7. **sub-improvement-roadmap** → Recommend improvements based on competitive gaps
8. **Synthesize** → Competitive intelligence report

### Expected Outputs by Stage

#### sub-intake Output
```yaml
intake_summary:
  subject:
    brand: "[Your Company]"
    competitor: "CompetitorX"
    industry: "SaaS project management"

  scope:
    timeframe:
      start: "2026-04-01"
      end: "2026-06-30"
    channels:
      - "Twitter/X"
      - "G2 reviews"
      - "Capterra reviews"
      - "Reddit (r/SaaS, r/projectmanagement)"

  goals:
    primary: "Competitive sentiment comparison"
    secondary:
      - "Identify competitive advantages/disadvantages"
      - "Benchmark channel performance"

  thresholds:
    baseline: "Historical net sentiment for both brands"
    statistical_significance: "Minimum sample size: 100 mentions per brand per channel"
```

#### sub-framework-selector Output
```yaml
framework_selection:
  selected_frameworks:
    - framework: "Net Sentiment Score"
      citation: "Industry standard; Gavra et al., 2020"
      rationale: "Direct comparability metric"
      application: "(Pos - Neg) / Total for each brand"

    - framework: "Share-of-Voice (SOV)"
      citation: "Industry standard; Gavra et al., 2020"
      rationale: "Market presence metric"
      application: "Brand mentions / Total category mentions"

    - framework: "Competitive Intelligence Framework"
      citation: "Industry best practices from Brandwatch, Sprout Social"
      rationale: "Structured competitive comparison methodology"
      application: "Gap analysis across channels and sentiment dimensions"

  excluded_frameworks:
    - framework: "SCCT"
      rationale: "No crisis context; competitive benchmarking focus"
```

#### sub-scoring-engine Output (Sample)
```yaml
scoring_results:
  overall:
    weighted_score: 82
    grade: B
    confidence: high
    assessment: "Strong competitive intelligence capability"

  competitive_metrics:
    net_sentiment:
      your_brand: 74%
      competitor: 81%
      delta: -7 percentage points
      statistical_significance: "Yes (p < 0.05, n = 1,247 mentions)"

    share_of_voice:
      your_brand: 22%
      competitor: 31%
      delta: -9 percentage points
      interpretation: "Competitor has 41% larger share of category conversation"

    channel_breakdown:
      twitter:
        your_brand: "72% sentiment, 18% SOV"
        competitor: "78% sentiment, 28% SOV"
        winner: "competitor"
      g2_reviews:
        your_brand: "4.2/5 stars, 156 reviews"
        competitor: "4.5/5 stars, 312 reviews"
        winner: "competitor (volume and rating)"

  dimension_scores:
    channel_coverage_aggregation:
      score: 85
      assessment: "Strong multi-channel competitive tracking"

    sentiment_accuracy_coverage:
      score: 80
      assessment: "Consistent methodology across brands"
```

### Validation Criteria

- [ ] **Comparable metrics**: Same methodology applied to both brands
- [ ] **Statistical significance**: Sample sizes adequate for comparison
- [ ] **Channel parity**: Same channels analyzed for both brands
- [ ] **No bias**: Neutral presentation without favoring either brand
- [ ] **Data sourcing**: Public or consented data only
- [ ] **Clear winner**: Unambiguous interpretation of who is "winning"

### Pass/Fail Conditions

**PASS**: All validation criteria met; fair, substantiated competitive comparison

**FAIL**: Any of:
- Different methodologies for each brand
- Insufficient sample sizes
- Channel selection bias
- Misleading presentation of results
- Unsubstantiated competitive claims

---

## Scenario 5: Degraded Mode

### User Input
```
"Analyze this offline sentiment sample. We have exported Twitter data
from last month but no API access right now."
```

### Expected Stage Sequence

1. **sub-intake** → Confirm offline data, timeframe, limitations
2. **sub-framework-selector** → Select appropriate frameworks for offline analysis
3. **Research** → Graceful degradation to SECOND-KNOWLEDGE-BRAIN
4. **sub-scoring-engine** → Score based on provided data only
5. **Challenge** → Verify if offline sample is representative
6. **sub-compliance-check** → Verify data provenance and usage rights
7. **sub-improvement-roadmap** → Recommendations for future data collection
8. **Synthesize** → Report with explicit limitations

### Expected Outputs by Stage

#### sub-intake Output
```yaml
intake_summary:
  subject:
    brand: "[Brand Name]"
    data_source: "Offline export (CSV)"
    data_provenance: "Official Twitter API export (historical)"

  scope:
    timeframe:
      start: "[Export start date]"
      end: "[Export end date]"
      note: "Limited to exported timeframe only"

  data_availability:
    live_access: false
    offline_data: true
    data_format: "CSV with tweet_id, text, timestamp, metrics"
    data_volume: "[Number] records"

  limitations:
    - "No live sentiment - analysis period only"
    - "May not reflect current sentiment"
    - "Validation against live data recommended when available"

  goals:
    primary: "Analyze offline sentiment sample"
    secondary: "Identify any patterns requiring immediate attention"
```

#### sub-framework-selector Output
```yaml
framework_selection:
  selected_frameworks:
    - framework: "NLP Sentiment Analysis (Lexicon - VADER)"
      citation: "Hutto & Gilbert, 2014, AAAI"
      rationale: "Fast, rule-based sentiment suitable for offline batch processing"
      application: "Polarity scoring on exported tweet text"

    - framework: "SECOND-KNOWLEDGE-BRAIN Benchmarks"
      citation: "Internal knowledge base"
      rationale: "Graceful degradation when live research unavailable"
      application: "Use established benchmarks for comparison"

    - framework: "Basic Statistical Analysis"
      citation: "Industry standard for descriptive analytics"
      rationale: "Appropriate for offline sample analysis"
      application: "Descriptive statistics, trend identification"

  excluded_frameworks:
    - framework: "Live Anomaly Detection"
      rationale: "Cannot detect anomalies on static historical data"
    - framework: "Real-time Velocity Tracking"
      rationale: "No live data stream available"
```

#### Degraded Mode Warning Output
```yaml
degraded_mode:
  active: true
  reason: "Live data and research unavailable"
  limitations:
    - "Analysis based on historical sample only"
    - "May not reflect current sentiment"
    - "Recommendations based on sample period, not real-time conditions"
    - "Validation with live data strongly recommended when available"
  confidence_level: "medium"
  recommendation: "Re-run analysis with live data when API access restored"
```

#### sub-scoring-engine Output (Sample)
```yaml
scoring_results:
  overall:
    weighted_score: 70
    grade: C
    confidence: medium
    note: "Score based on offline sample only; may change with live data"

  data_summary:
    period_analyzed: "[Date range]"
    total_mentions: "[Number]"
    net_sentiment: "[Percentage]"
    sentiment_distribution:
      positive: "[Percentage]"
      neutral: "[Percentage]"
      negative: "[Percentage]"

  limitations_explicit:
    - "Static historical sample - no velocity measurement possible"
    - "No real-time anomaly detection"
    - "Current sentiment may differ from analysis period"
    - "Recommendations conditional on live data validation"

  dimension_scores:
    sentiment_accuracy_coverage:
      score: 75
      note: "VADER lexicon applied (no transformer models available offline)"

    early_crisis_signal_detection:
      score: 50
      note: "Cannot assess - no live velocity data available"

    channel_coverage_aggregation:
      score: 80
      note: "Twitter only (offline export limited to single channel)"
```

### Validation Criteria

- [ ] **Limitations explicit**: Degraded mode clearly stated
- [ ] **No false precision**: Confidence level reduced appropriately
- [ ] **Static data acknowledged**: Clarify that current sentiment may differ
- [ ] **Appropriate frameworks**: Only frameworks suitable for offline data used
- [ ] **Validation recommended**: Explicit recommendation to validate with live data
- [ ] **No misleading claims**: No statements about "current" or "real-time" sentiment

### Pass/Fail Conditions

**PASS**: All validation criteria met; appropriate degraded mode operation

**FAIL**: Any of:
- Degraded mode not acknowledged
- Current/live claims made from static data
- Confidence level not reduced
- No recommendation to validate with live data
- Frameworks requiring live data applied inappropriately

---

## Regression Test Notes

### Adding Real User Runs as Regression Cases

When real users run the skill, add notable cases here:

```markdown
### Regression Case: [Brief Description]

**Date**: [YYYY-MM-DD]
**User Input**: "[Actual user request]"
**Expected Output**: [What should have happened]
**Actual Output**: [What actually happened]
**Status**: [PASS/FAIL]
**Notes**: [Any discrepancies or lessons learned]
```

### Continuous Validation

**Weekly** (via automated test or manual check):
- [ ] All 5 scenarios still pass
- [ ] No stage order changes
- [ ] Framework citations still accurate
- [ ] Compliance checks still pass

**After any code changes**:
- [ ] Run affected scenarios
- [ ] Verify no regression in outputs
- [ ] Update expected outputs if functionality intentionally changed

### knowledge_updater.py Validation

**Weekly** (after cron execution):
- [ ] Script executed without errors
- [ ] New entries appended (if any)
- [ ] Deduplication working (check for duplicate hashes)
- [ ] Markdown formatting correct
- [ ] Log file shows successful execution

**Dry-run test**:
```bash
python tools/knowledge_updater.py --dry-run
```

Expected output:
- Total entries fetched: [number]
- After deduplication: [number]
- [DRY RUN] Would append [number] entries

---

## Test Data Repository

For consistent testing, the following sample data can be used:

### Sample Sentiment Data (CSV format for Scenario 5)
```csv
tweet_id,text,timestamp,likes,retweets,reply_count
123456789,"Great experience with @Brand! Highly recommend.",2026-06-15T10:30:00Z,45,12,3
123456790,"Disappointed with the new update. #brandfail",2026-06-15T11:45:00Z,23,8,15
123456791,"@Brand support team helped me quickly. Thanks!",2026-06-15T12:00:00Z,67,5,2
```

### Sample Crisis Thread (Reddit format for Scenario 2)
```markdown
Title: Brand's latest update is completely broken
Author: u/user123
Date: 2026-06-20

Content:
"I updated to the latest version and the app crashes every time I open it.
Is anyone else experiencing this? This is unacceptable for a paid product."

Comments:
- "Same here, can't use the app at all now"
- "Customer support isn't responding"
- "Downgrading for now"
```

---

## Summary Table

| Scenario | Key Frameworks | Primary Validation | Critical Success Factor |
|---|---|---|---|
| 1. Sentiment Scan | NLP + Net Sentiment | Multi-channel aggregation | Accurate baseline comparison |
| 2. Crisis Alert | SCCT + Anomaly Detection | Crisis classification | Correct crisis type identification |
| 3. Response Plan | Image Repair + SCCT | Response strategy match | Framework-aligned response |
| 4. Competitor Scan | SOV + Net Sentiment | Fair comparison | Comparable methodologies |
| 5. Degraded Mode | Lexicon + Static analysis | Explicit limitations | No misleading claims from static data |

---

**Version**: 1.0.0
**Last Updated**: 2026-06-30
**Skill**: Multi-channel Sentiment Analysis (crisis detection) #153
