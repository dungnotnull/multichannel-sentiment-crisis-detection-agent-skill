# Example Crisis Detection Report

**Brand**: TechCorp Industries
**Analysis Period**: June 15-30, 2026
**Analysis Date**: 2026-06-30
**Report ID**: CR-2026-06-001

---

## Executive Summary

**Overall Grade: C (68/100)**

**CRISIS ALERT: CONFIRMED**

TechCorp Industries is experiencing an active crisis. Sentiment has dropped 3.2σ below baseline with sustained velocity for 8+ hours. The crisis is classified as a **preventable crisis with high responsibility attribution** per the Situational Crisis Communication Theory (SCCT) framework.

**Key Findings:**
- Sentiment dropped from 72% baseline to 41% current (31-point decline)
- Negative mentions increased 450% following product announcement
- Crisis severity: HIGH (78/100) with escalation probability of 67%
- Velocity exceeds crisis threshold (2σ) by 60%
- Recommended response: Rebuild strategy (corrective action + mortification)

**Immediate Action Required:** Formal response within 60 minutes using SCCT-matched framework.

---

## Context & Scope

### Analysis Scope
- **Brand**: TechCorp Industries (consumer technology sector)
- **Incident**: Product pricing announcement perceived as price gouging
- **Timeframe**: June 15-30, 2026 (2 weeks)
- **Geography**: Global, with primary impact in North America and Europe
- **Languages**: English, Spanish, French, German

### Channels Monitored
- **Social Media**: Twitter/X, Reddit, Facebook, LinkedIn
- **Review Platforms**: Amazon, Google Reviews, Trustpilot
- **News/Media**: TechCrunch, Wired, The Verge, Ars Technica
- **Forums**: Product-specific communities, r/technology

### Data Availability
- Total mentions analyzed: 8,432
- Pre-crisis baseline (June 1-14): 2,156 mentions
- Crisis period (June 15-30): 6,276 mentions (291% increase)
- Data sources: Public APIs and authorized data exports
- Compliance: GDPR-compliant, no PII in outputs

### Frameworks Applied
1. **Situational Crisis Communication Theory (SCCT)** - Coombs, 2007
2. **Image Repair Theory (Benoit)** - Benoit, 1995
3. **Velocity/Anomaly Detection** - Yang et al., 2020; Castillo et al., 2021
4. **NLP Sentiment Analysis (Transformer)** - Devlin et al., 2019 (BERT)

---

## Dimension Scores

| Dimension | Score | Weight | Contribution | Status |
|---|---|---|---|---|
| Sentiment Accuracy & Coverage | 82/100 | 25% | 20.5 | ✅ Good |
| Early Crisis Signal Detection | 55/100 | 25% | 13.75 | ⚠️ Poor |
| Channel Coverage & Aggregation | 75/100 | 15% | 11.25 | ⚠️ Fair |
| Severity & Escalation Scoring | 78/100 | 20% | 15.6 | ✅ Good |
| Response Recommendation Quality | 48/100 | 15% | 7.2 | ❌ Poor |
| **TOTAL** | **68/100** | **100%** | **68.3** | **C** |

### Dimension Breakdown

#### Sentiment Accuracy & Coverage (82/100)
**Strengths:**
- BERT-based sentiment classification with 87% F1-score
- 4 major social platforms covered
- Multi-language sentiment analysis (EN, ES, FR, DE)

**Weaknesses:**
- Limited emotion detection granularity
- No aspect-based sentiment for pricing specifically
- Review platforms covered but not integrated

**Evidence:**
- BERT F1-score of 0.87 on similar datasets (Devlin et al., 2019)
- Cross-platform sentiment consistency validated

**Improvement Potential:** +3 points with emotion detection and aspect-based analysis

#### Early Crisis Signal Detection (55/100)
**Strengths:**
- Basic velocity measurement in place
- 2σ threshold configured

**Weaknesses:**
- **No formal anomaly detection** (high false positive rate)
- Thresholds not calibrated to historical baseline
- Reactive rather than proactive (3-8 hour delay vs. 4-6 hour best practice)

**Evidence:**
- Current system provides < 4 hour lead time (Yang et al., 2020 benchmark: 4-6 hours)
- No statistical process control implementation

**Improvement Potential:** +20 points with formal anomaly detection

#### Channel Coverage & Aggregation (75/100)
**Strengths:**
- 4 major channels covered (social platforms)
- Near-real-time data collection (15-minute latency)

**Weaknesses:**
- Review platforms not fully integrated
- No weighted aggregation (all channels treated equally)
- Forums and news media coverage limited

**Evidence:**
- 4 channels vs. 8+ recommended (Brandwatch best practice)
- Unweighted aggregation reduces accuracy (Gavra et al., 2020)

**Improvement Potential:** +5 points with weighted aggregation and expanded coverage

#### Severity & Escalation Scoring (78/100)
**Strengths:**
- Multi-factor severity model (sentiment + velocity + reach)
- SCCT crisis classification applied correctly
- Escalation probability calculated (67%)

**Weaknesses:**
- Stakeholder impact assessment incomplete
- No historical severity validation

**Evidence:**
- SCCT crisis classification: Preventable crisis (Coombs, 2007)
- Multi-factor model aligns with Olteanu et al., 2019

**Improvement Potential:** +7 points with stakeholder impact assessment

#### Response Recommendation Quality (48/100)
**Strengths:**
- Response timing guidance provided
- Basic acknowledgment template available

**Weaknesses:**
- **Response NOT matched to SCCT framework** (critical gap)
- No Image Repair strategy selection
- Generic recommendations only

**Evidence:**
- Framework-matched responses have 72% effectiveness (Coombs & Holladay, 2018)
- Current approach: Generic best practices only

**Improvement Potential:** +22 points with SCCT and Image Repair integration

---

## Findings & Risks

### Strongest Areas

1. **Sentiment Analysis Accuracy** (82/100)
   - BERT models provide state-of-the-art accuracy
   - Consistent methodology across platforms
   - Multi-language capability

2. **Severity Assessment** (78/100)
   - Multi-factor scoring provides nuanced severity measurement
   - SCCT crisis classification is accurate
   - Escalation prediction helps with resource allocation

### Weakest Areas

1. **Response Strategy Alignment** (48/100) - **CRITICAL**
   - Response recommendations not matched to crisis type
   - No Image Repair framework application
   - Missing 24 percentage points vs. best practice

2. **Early Warning System** (55/100) - **HIGH PRIORITY**
   - No formal anomaly detection
   - Crisis detected 3-8 hours late vs. best practice
   - Reactive rather than proactive posture

### Crisis Timeline

| Time (UTC) | Event | Sentiment | Velocity | Status |
|---|---|---|---|---|
| Jun 15, 09:00 | Pricing announcement posted | 68% | Normal | 🟢 |
| Jun 15, 14:00 | First negative reactions | 62% | +1.2σ | 🟡 |
| Jun 15, 18:00 | TechCrunch coverage | 54% | +1.8σ | 🟡 |
| Jun 16, 08:00 | Reddit discussion spikes | 48% | +2.4σ | 🔴 |
| Jun 16, 12:00 | Crisis threshold crossed | 41% | +3.2σ | 🔴 |
| Jun 16, 16:00 | Current status | 41% | +3.2σ sustained | 🔴 |

### Risk Assessment

**HIGH RISK FACTORS:**
- **Reputational Damage**: Crisis severity 78/100 with high stakeholder impact
- **Escalation Probability**: 67% likelihood of worsening without proper response
- **Competitive Vulnerability**: Competitors may capitalize on crisis (SOV down 8 points)

**MEDIUM RISK FACTORS:**
- **Media Amplification**: Tech media coverage increasing negative sentiment velocity
- **Customer Churn**: Negative sentiment correlates with 12% increase in cancellation inquiries

**MITIGATING FACTORS:**
- **Brand Equity**: Strong pre-crisis sentiment (72% baseline) provides resilience
- **Response Window**: Still within optimal response window (golden hour + 3 hours)

---

## Improvement Roadmap

### Prioritized Recommendations (Effort × Impact)

#### Priority 1: Implement SCCT-Matched Response (DO FIRST)
- **Dimension**: Response Recommendation Quality
- **Current Score**: 48/100 → Target: 75/100 (+27 points)
- **Framework**: SCCT (Coombs, 2007); Image Repair (Benoit, 1995)
- **Description**: For preventable crises with high responsibility, SCCT prescribes "Rebuild" strategy (corrective action + mortification). Implement formal response framework.

**Implementation Steps:**
1. Classify crisis as preventable (high responsibility attribution)
2. Select Rebuild strategy per SCCT
3. Apply Image Repair: Corrective Action + Mortification
4. Draft response with:
   - Direct acknowledgment and apology
   - Acceptance of responsibility
   - Specific corrective actions with timelines
   - Commitment to prevention

**Resources Required:**
- Crisis communication consultant: 0.5 FTE, 2 weeks
- PR team for response drafting: 0.5 FTE, 1 week

**Timeline**: IMMEDIATE (within 4 hours)

**Success Metrics:**
- Response aligns with SCCT Rebuild strategy (100% compliance)
- Response issued within optimal window (4 hours of crisis confirmation)

---

#### Priority 2: Deploy Formal Anomaly Detection (DO FIRST)
- **Dimension**: Early Crisis Signal Detection
- **Current Score**: 55/100 → Target: 75/100 (+20 points)
- **Framework**: Velocity/Anomaly Detection (Yang et al., 2020; Castillo et al., 2021)
- **Description**: Deploy Isolation Forest or One-Class SVM on sentiment velocity data to identify spikes 2σ above historical baseline, enabling 4-6 hour early warning.

**Implementation Steps:**
1. Export last 90 days of sentiment timestamp data
2. Train Isolation Forest model on historical baseline
3. Set alert threshold at 2σ with 4-hour sustained requirement
4. Configure automated alerts to PR team on-call rotation
5. Calibrate thresholds to minimize false positives

**Resources Required:**
- Data scientist: 0.5 FTE, 2 weeks
- Anomaly detection library: scikit-learn (open-source)
- Alert integration: existing monitoring tools

**Timeline**: 2-3 weeks

**Success Metrics:**
- Model achieves >75% true positive rate
- Alerts provide 4+ hour warning before evident crisis
- False positive rate <25%

---

#### Priority 3: Expand Channel Coverage (SCHEDULE NEXT)
- **Dimension**: Channel Coverage & Aggregation
- **Current Score**: 75/100 → Target: 82/100 (+7 points)
- **Framework**: Multi-channel best practices (Brandwatch, Sprout Social)
- **Description**: Add review platforms (Yelp, Google Reviews) and forums (Reddit, industry forums) to monitoring scope. Implement weighted aggregation by channel relevance.

**Implementation Steps:**
1. Identify top 5 review/forums for tech industry
2. Set up data collection via APIs or compliant web scraping
3. Implement channel weighting (social: 40%, reviews: 30%, news: 20%, forums: 10%)
4. Update aggregation pipeline

**Resources Required:**
- Developer: 1 FTE, 4 weeks
- API access costs: $500-1,000/month

**Timeline**: 4-6 weeks

**Success Metrics:**
- 8+ channels actively monitored
- Weighted aggregation improves detection sensitivity by 15%

---

### Implementation Phasing

**Phase 1 (Immediate - 0-72 hours):**
- Priority 1: SCCT-matched response (CRITICAL)
- Expected improvement: +27 points (Response Quality)

**Phase 2 (Short-term - 2-4 weeks):**
- Priority 2: Anomaly detection deployment
- Expected improvement: +20 points (Early Warning)

**Phase 3 (Medium-term - 1-2 months):**
- Priority 3: Channel coverage expansion
- Expected improvement: +7 points (Channel Coverage)
- Priority 4: Weighted aggregation implementation
- Expected improvement: +3 points (Channel Coverage)

**Expected Final Score**: 95/100 (A) - 27-point improvement from baseline

---

## Limitations & Certainty

### Data Limitations
- **Offline analysis**: Based on data collected up to 2026-06-30 16:00 UTC; current sentiment may differ
- **Platform access**: Some forums have restricted API access; may miss niche discussions
- **Language coverage**: Primary analysis in English; other languages may have reduced accuracy

### Analysis Limitations
- **Historical baseline**: 2-week baseline may not fully represent "normal" sentiment
- **Competitive context**: Limited competitive benchmarking data available
- **Stakeholder mapping**: High-level stakeholder analysis; detailed mapping not performed

### Framework Limitations
- **SCCT applicability**: Framework assumes preventable crisis classification; if facts differ, recommended response may not be optimal
- **Severity prediction**: Escalation probability based on historical patterns; current crisis may deviate

### Certainty Assessment

**Overall Certainty**: **MEDIUM-HIGH**

**High Certainty Areas:**
- Crisis classification (preventable, high responsibility): 90% certainty
- Sentiment accuracy: 87% F1-score validated
- Velocity measurement: Direct calculation from data

**Medium Certainty Areas:**
- Severity score: 78% certainty (historical validation limited)
- Escalation probability: 67% certainty (based on statistical models)
- Stakeholder impact: 60% certainty (qualitative assessment)

**Low Certainty Areas:**
- Long-term brand impact: 40% certainty (depends on response effectiveness)
- Competitive exploitation risk: 50% certainty (limited competitive intelligence)

**What Could Change Conclusions:**
- New information about product pricing rationale (could change crisis classification)
- Competitor response (could affect escalation probability)
- Customer sentiment post-response (could affect long-term impact assessment)

---

## Sources

### Academic Papers

1. Coombs, W.T. (2007). "Protecting Organization Reputations During a Crisis: The Development and Application of Situational Crisis Communication Theory." *Corporate Reputation Review*, 10(3), 163-176. DOI: 10.1057/palgrave.crr.1550049

2. Benoit, W.L. (1995). *Accounts, Excuses, and Apologies: Image Repair Theory*. Albany, NY: State University of New York Press.

3. Devlin, J., Chang, M.W., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *Proceedings of NAACL-HLT*, 4171-4186. DOI: 10.18653/v1/N19-1423

4. Yang, K., Ananiadou, S., & Siddharthan, R. (2020). "Early Detection of Public Health Crises from Social Media: A Case Study on COVID-19." *IEEE Access*, 8, 165423-165434. DOI: 10.1109/ACCESS.2020.3017434

5. Castillo, C., Mendoza, M., & Poblete, B. (2021). "Predicting Information Credibility in Time-Sensitive Social Media." *ACM Transactions on the Web*, 15(3), Article 14. DOI: 10.1145/3472308

6. Coombs, W.T., & Holladay, S.J. (2018). "The Function of Communication in Crisis Response: A Systematic Review of the Crisis Communication Literature." *Management Communication Quarterly*, 32(4), 508-543. DOI: 10.1177/0893318918777427

7. Olteanu, A., Castillo, C., Diaz, F., & Kiciman, E. (2019). "Social Data: Biases, Methodological Pitfalls, and Ethical Boundaries." *Proceedings of the International AAAI Conference on Web and Social Media*, 13(1), 545-548. DOI: 10.1609/icwsm.v13i01.3250

### Industry Sources

8. Brandwatch. (2026). "Social Listening Best Practices for Crisis Detection." Retrieved from https://www.brandwatch.com

9. Sprout Social. (2026). "Multi-Channel Sentiment Analysis: A Framework." Retrieved from https://sproutsocial.com/insights

10. Institute for Public Relations. (2026). "Crisis Communication Measurement Guidelines." Retrieved from https://instituteforpr.org

### Standards and Frameworks

11. AMEC (International Association for Measurement and Evaluation of Communication). (2025). *Valid Measurement Framework*. 3rd Edition.

12. ICC (International Chamber of Commerce). (2024). *The ICC Marketing Code*. 8th Edition.

---

## Next Steps (Immediate)

### Within 1 Hour
- [ ] Convene crisis response team
- [ ] Validate SCCT classification (preventable crisis)
- [ ] Begin drafting SCCT-matched response (Rebuild strategy)

### Within 4 Hours
- [ ] Issue formal response (corrective action + mortification)
- [ ] Monitor response sentiment impact
- [ ] Prepare follow-up statements

### Within 24 Hours
- [ ] Implement Isolation Forest anomaly detection
- [ ] Calibrate thresholds to reduce false positives
- [ ] Establish automated alert system

### Within 1 Week
- [ ] Review response effectiveness metrics
- [ ] Update crisis response playbook
- [ ] Begin channel coverage expansion planning

---

**Report Generated**: 2026-06-30 16:15:32 UTC
**Analysis Duration**: 45 minutes
**Compliance Status**: ✅ Passed (GDPR-compliant, no PII, platform terms respected)
**Next Review**: 2026-07-01 or upon significant sentiment change

---

*This report was generated by Skill #153: Multi-channel Sentiment Analysis (Crisis Detection)*
*Framework-grounded analysis with full evidence citations and quality gates*
