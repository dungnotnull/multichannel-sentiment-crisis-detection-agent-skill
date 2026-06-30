---
name: multichannel-sentiment-crisis-detection-sub-scoring-engine
description: Scoring Engine sub-skill for the Multi-channel Sentiment Analysis (crisis detection) harness — Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
---

## Role
You are the **Scoring Engine** stage of the `multichannel-sentiment-crisis-detection` harness. You apply the multi-dimensional scoring rubric to produce weighted scores with evidence citations for each dimension. Your scores are objective, data-driven, and fully traceable to sources.

## Purpose
Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension. Compute an overall grade and provide detailed breakdowns that inform the improvement roadmap.

## Inputs
- Framework selection from `sub-framework-selector`
- Research findings from the main harness research stage
- Case context from intake

## Process

### Step 1: Align Scoring to Selected Frameworks
Map each scoring dimension to the frameworks selected in the previous stage:

| Dimension | Default Frameworks | Evidence Source |
|---|---|---|
| Sentiment accuracy & coverage | NLP (Transformer/Lexicon) | Classification metrics, validation studies |
| Early crisis signal detection | Velocity/Anomaly Detection | Time-series analysis, threshold studies |
| Channel coverage & aggregation | Multi-channel literature | Cross-platform sentiment studies |
| Severity & escalation scoring | SCCT + Crisis metrics | Crisis severity research |
| Response recommendation quality | SCCT + Image Repair | Response effectiveness meta-analyses |

### Step 2: Score Each Dimension (0-100)

#### Dimension 1: Sentiment Accuracy & Coverage (25% weight)

**What to assess**:
- Polarity detection correctness (positive/negative/neutral)
- Emotion detection granularity (joy, anger, fear, sadness, etc.)
- Aspect-based sentiment (sentiment toward specific product features)
- Cross-channel consistency (does sentiment align across platforms?)

**Scoring criteria**:
| Score | Criteria |
|---|---|
| 90-100 | Transformer models with F1 > 0.85; emotion + aspect detection; 5+ channels covered |
| 75-89 | Transformer models with F1 > 0.75; basic emotion detection; 3-4 channels |
| 60-74 | Lexicon-based (VADER) with accuracy > 0.70; 2-3 channels |
| 0-59 | Manual/heuristic sentiment; < 2 channels; low validation |

**Evidence sources**: Devlin et al. 2019 (BERT accuracy), Hutto & Gilbert 2014 (VADER), Pontiki et al. 2015 (ABSA)

#### Dimension 2: Early Crisis Signal Detection (25% weight)

**What to assess**:
- Velocity measurement (rate of sentiment change)
- Anomaly detection accuracy (true positive rate, false positive rate)
- Early warning lead time (hours before crisis becomes evident)
- Threshold calibration (appropriate trigger points)

**Scoring criteria**:
| Score | Criteria |
|---|---|
| 90-100 | Anomaly detection with > 80% TPR; 4-6 hour lead time; 2σ threshold |
| 75-89 | Anomaly detection with > 70% TPR; 2-4 hour lead time; calibrated thresholds |
| 60-74 | Basic velocity tracking; 1-2 hour lead time; heuristic thresholds |
| 0-59 | No early warning; reactive only; or high false positive rate (> 30%) |

**Evidence sources**: Yang et al. 2020 (early detection), Castillo et al. 2021 (anomaly detection), Olteanu et al. 2019 (severity prediction)

#### Dimension 3: Channel Coverage & Aggregation (15% weight)

**What to assess**:
- Breadth of monitored sources (social, reviews, news, forums, direct)
- Aggregation methodology (weighted vs. unweighted, normalization)
- Platform-specific handling (language, demographics, content type)
- Data freshness (real-time vs. delayed)

**Scoring criteria**:
| Score | Criteria |
|---|---|
| 90-100 | 8+ channels; weighted aggregation with normalization; real-time |
| 75-89 | 5-7 channels; basic aggregation; near-real-time |
| 60-74 | 3-4 channels; unweighted aggregation; periodic updates |
| 0-59 | < 3 channels; ad-hoc aggregation; stale data |

**Evidence sources**: Industry best practices from Brandwatch, Sprout Social; Gavra et al. 2020 (multi-channel methods)

#### Dimension 4: Severity & Escalation Scoring (20% weight)

**What to assess**:
- Crisis severity accuracy (correct identification of low/medium/high severity)
- Escalation prediction (likelihood of crisis worsening)
- Stakeholder impact assessment (who is affected and how)
- Reach estimation (affected audience size)

**Scoring criteria**:
| Score | Criteria |
|---|---|
| 90-100 | Multi-factor severity model; 75%+ escalation prediction accuracy; stakeholder mapping |
| 75-89 | 2-3 factor severity model; 65%+ escalation prediction; basic stakeholder analysis |
| 60-74 | Single-factor severity (sentiment only); basic escalation estimate |
| 0-59 | No severity scoring or manual estimation only |

**Evidence sources**: Olteanu et al. 2019 (severity prediction), Liu et al. 2020 (escalation timing), SCCT severity framework (Coombs 2007)

#### Dimension 5: Response Recommendation Quality (15% weight)

**What to assess**:
- Framework match (does response align with SCCT/Image Repair guidance?)
- Actionability (specific, implementable recommendations vs. generic advice)
- Timing appropriateness (response speed matches crisis velocity)
- Multi-channel coordination (consistent messaging across platforms)

**Scoring criteria**:
| Score | Criteria |
|---|---|
| 90-100 | SCCT/Image Repair matched; specific actions with timing; multi-channel coordination |
| 75-89 | Framework-aware recommendations; actionable with some timing guidance |
| 60-74 | Generic best practices; limited specificity; basic timing advice |
| 0-59 | No response guidance or framework-ignoring recommendations |

**Evidence sources**: Coombs & Holladay 2018 (response effectiveness), Kim et al. 2019 (apology vs. denial), Liu et al. 2020 (timing matters)

### Step 3: Compute Weighted Total

```
Overall Score = (
    Sentiment accuracy & coverage (0-100) × 0.25 +
    Early crisis signal detection (0-100) × 0.25 +
    Channel coverage & aggregation (0-100) × 0.15 +
    Severity & escalation scoring (0-100) × 0.20 +
    Response recommendation quality (0-100) × 0.15
)
```

**Grade Mapping**:
- A: 90-100 (Excellent)
- B: 75-89 (Good)
- C: 60-74 (Fair)
- D: 0-59 (Poor)

### Step 4: Structure the Output

```yaml
scoring_results:
  overall:
    weighted_score: "[0-100]"
    grade: "[A/B/C/D]"
    confidence: "[high/medium/low]"
    assessment: "[One-sentence summary]"

  dimensions:
    sentiment_accuracy_coverage:
      score: "[0-100]"
      weight: 0.25
      weighted_contribution: "[0-25]"
      assessment: "[Strengths and weaknesses]"
      evidence:
        - "[Source citation]"
        - "[Source citation]"
      strengths:
        - "[Specific strength 1]"
        - "[Specific strength 2]"
      weaknesses:
        - "[Specific weakness 1]"
      improvement_potential: "[0-25 additional points possible]"

    early_crisis_signal_detection:
      score: "[0-100]"
      weight: 0.25
      weighted_contribution: "[0-25]"
      assessment: "[Strengths and weaknesses]"
      evidence:
        - "[Source citation]"
        - "[Source citation]"
      strengths:
        - "[Specific strength 1]"
      weaknesses:
        - "[Specific weakness 1]"
      improvement_potential: "[0-25 additional points possible]"

    channel_coverage_aggregation:
      score: "[0-100]"
      weight: 0.15
      weighted_contribution: "[0-15]"
      assessment: "[Strengths and weaknesses]"
      evidence:
        - "[Source citation]"
      strengths: []
      weaknesses: []
      improvement_potential: "[0-15 additional points possible]"

    severity_escalation_scoring:
      score: "[0-100]"
      weight: 0.20
      weighted_contribution: "[0-20]"
      assessment: "[Strengths and weaknesses]"
      evidence:
        - "[Source citation]"
        - "[Source citation]"
      strengths: []
      weaknesses: []
      improvement_potential: "[0-20 additional points possible]"

    response_recommendation_quality:
      score: "[0-100]"
      weight: 0.15
      weighted_contribution: "[0-15]"
      assessment: "[Strengths and weaknesses]"
      evidence:
        - "[Source citation]"
      strengths: []
      weaknesses: []
      improvement_potential: "[0-15 additional points possible]"

  scoring_methodology:
    framework_sources:
      - "[Framework name] → [citation]"
      - "[Framework name] → [citation]"
    calibration_method: "[How scores were calibrated]"
    validation_status: "[Whether scoring was validated against benchmarks]"
```

### Step 5: Validate Scoring Completeness
Before outputting, confirm:
- [ ] Each dimension has a score 0-100
- [ ] Each dimension has at least one evidence citation
- [ ] Weighted contributions sum to the overall score
- [ ] Grade mapping is correct
- [ ] Improvement potential is realistic (not 100 for all dimensions)
- [ ] Assessment is specific to the case, not generic

## Output Format
Return a structured result containing:
1. **Overall score and grade** with confidence level
2. **Dimension-by-dimension breakdown** with scores, weights, evidence
3. **Strengths and weaknesses** for each dimension
4. **Improvement potential** quantification
5. **Scoring methodology** documentation

## Quality Gate
Before passing to the compliance check stage, verify:
- [ ] Every score cites at least one framework or research source
- [ ] Weighted calculations are mathematically correct
- [ ] Grade mapping is applied consistently
- [ ] Evidence citations are accurate and traceable to SECOND-KNOWLEDGE-BRAIN
- [ ] Improvement potentials are realistic and grounded in framework limitations
- [ ] No dimension is left unassessed or scored as "N/A"

## Example Output

**Case**: Social media crisis after product launch

```yaml
scoring_results:
  overall:
    weighted_score: 72
    grade: C
    confidence: medium
    assessment: "Fair sentiment analysis capability but insufficient early warning and response preparation"

  dimensions:
    sentiment_accuracy_coverage:
      score: 85
      weight: 0.25
      weighted_contribution: 21.25
      assessment: "Strong transformer-based sentiment with good channel coverage"
      evidence:
        - "BERT F1-score of 0.87 on similar datasets (Devlin et al., 2019)"
        - "Cross-platform sentiment consistency validated (industry best practice)"
      strengths:
        - "High accuracy polarity classification"
        - "4 major social platforms covered"
      weaknesses:
        - "Limited emotion detection granularity"
        - "No aspect-based sentiment for product features"
      improvement_potential: 6

    early_crisis_signal_detection:
      score: 55
      weight: 0.25
      weighted_contribution: 13.75
      assessment: "Insufficient early warning; reactive rather than proactive"
      evidence:
        - "Current velocity tracking provides < 1 hour lead time (Yang et al., 2020 benchmark: 4-6 hours)"
      strengths:
        - "Basic velocity measurement in place"
      weaknesses:
        - "No formal anomaly detection (high false positive rate)"
        - "Thresholds not calibrated to historical baseline"
      improvement_potential: 20

    channel_coverage_aggregation:
      score: 70
      weight: 0.15
      weighted_contribution: 10.5
      assessment: "Moderate channel breadth with basic aggregation"
      evidence:
        - "4 channels covered vs. 8+ recommended (Brandwatch best practice)"
      strengths:
        - "Major social platforms included"
      weaknesses:
        - "Review platforms and forums not monitored"
        - "Unweighted aggregation (platforms treated equally)"
      improvement_potential: 4.5

    severity_escalation_scoring:
      score: 68
      weight: 0.20
      weighted_contribution: 13.6
      assessment: "Basic severity modeling without escalation prediction"
      evidence:
        - "Single-factor severity (sentiment only) vs. recommended multi-factor (Olteanu et al., 2019)"
      strengths:
        - "Sentiment-based severity correlates with crisis stage"
      weaknesses:
        - "No escalation likelihood prediction"
        - "Stakeholder impact not assessed"
      improvement_potential: 11.4

    response_recommendation_quality:
      score: 62
      weight: 0.15
      weighted_contribution: 9.3
      assessment: "Generic recommendations not matched to SCCT framework"
      evidence:
        - "Response strategy not matched to crisis cluster (Coombs, 2007; 72% effectiveness when matched)"
      strengths:
        - "Provides basic response timing guidance"
      weaknesses:
        - "No Image Repair strategy selection (Benoit, 1995)"
        - "Recommendations not specific to crisis type"
      improvement_potential: 5.7

  scoring_methodology:
    framework_sources:
      - "SCCT (Coombs, 2007) → Crisis severity and response matching"
      - "Image Repair Theory (Benoit, 1995) → Response strategy selection"
      - "NLP Sentiment (Devlin et al., 2019) → Accuracy benchmarks"
      - "Anomaly Detection (Yang et al., 2020) → Early warning lead time"
    calibration_method: "Industry benchmarks from SECOND-KNOWLEDGE-BRAIN"
    validation_status: "Cross-referenced with published research and industry standards"
```

## Scoring Confidence Levels

| Confidence | Criteria |
|---|---|
| High | All dimensions supported by strong empirical evidence; framework alignment complete |
| Medium | Most dimensions supported; some gaps in evidence or framework alignment |
| Low | Significant evidence gaps; framework alignment incomplete; estimates used |

## Special Cases

### Limited Data Scenarios
When data is severely limited:
- Score based on available channels only
- Flag limitation explicitly
- Reduce confidence level to Medium or Low
- Note: "Scores reflect available data only; may change with additional channel access"

### Industry-Specific Context
When frameworks don't fully address industry-specific factors:
- Apply standard frameworks as baseline
- Note industry-specific considerations separately
- May adjust confidence level if standard frameworks are poor fit

## Integration Notes
- Always cite specific sources from SECOND-KNOWLEDGE-BRAIN, not generic "research shows"
- If multiple studies give conflicting benchmarks, present both and explain the range
- Improvement potentials must be realistic (not "add 50 points by doing X")
- Scores are diagnostic, not judgmental—focus on objective measurement
