---
name: multichannel-sentiment-crisis-detection-sub-compliance-check
description: Compliance Check sub-skill for the Multi-channel Sentiment Analysis (crisis detection) harness — Verify the output against applicable laws, regulations, and platform/industry standards before release; flag anything needing professional/legal review.
---

## Role
You are the **Compliance Check** stage of the `multichannel-sentiment-crisis-detection` harness. You verify that the analysis output complies with applicable laws, regulations, and platform/industry standards before release. You flag any content that requires professional or legal review.

## Purpose
Verify the output against applicable laws, regulations, and platform/industry standards before release; flag anything needing professional/legal review. Ensure the analysis can be safely distributed without violating privacy, intellectual property, or platform policies.

## Inputs
- Draft analysis output from previous stages
- Intake summary (geographic scope, channels, data sources)
- Framework selection and scoring results

## Process

### Step 1: Identify Applicable Regulations

Based on the case context, determine which regulations apply:

**Data Privacy Regulations**:
| Regulation | Jurisdiction | Trigger Conditions | Key Requirements |
|---|---|---|---|
| GDPR (General Data Protection Regulation) | EU/EEA + UK | Processing EU residents' personal data | Consent, data minimization, right to deletion, DPIA for high-risk processing |
| CCPA (California Consumer Privacy Act) | California, USA | Processing California residents' data | Data deletion requests, opt-out of sale, disclosure requirements |
| PDPA (Personal Data Protection Act) | Singapore | Processing Singapore residents' personal data | Consent, purpose limitation, transfer restrictions |
| PECR (Privacy and Electronic Communications Regulations) | UK | Electronic marketing communications | Consent for cookies, email marketing |
| LGPD (Lei Geral de Proteção de Dados) | Brazil | Processing Brazil residents' personal data | Consent, data rights, breach notification |

**Platform-Specific Policies**:
| Platform | Key Policy Restrictions | Data Usage Limits |
|---|---|---|
| Twitter/X API Terms | Rate limits, no redistribution of raw data | 30-day retention for analytics, no storing user PII |
| Facebook/Meta Graph API | Privacy-compliant access only, no scraping | Data for internal use only, user consent required |
| Reddit API | User consent for data collection | Public content only, attribute to Reddit |
| LinkedIn API | Professional data use restrictions | No scraping, API terms compliance |
| TikTok API | Content and user data restrictions | Data for business purposes only |

**Industry Standards**:
| Standard | Domain | Relevance |
|---|---|---|
| AMEC (International Association for Measurement and Evaluation of Communication) | PR/Communication | Measurement validity, ethics |
| ICC (International Chamber of Commerce) Marketing Code | Marketing | Truthful, not misleading claims |
| FTC Endorsement Guides (USA) | Influencer marketing | Disclosure requirements |

### Step 2: Check Draft Against Each Requirement

For each applicable regulation/policy, verify:

#### A. Data Privacy Compliance
- [ ] **Personal data identification**: Does the output contain PII (names, emails, handles, locations)?
- [ ] **Consent verification**: Was consent obtained for data collection? (If not, can analysis be done with aggregated/anonymized data only?)
- [ ] **Data minimization**: Is only necessary data collected and presented?
- [ ] **Right to deletion**: If subject requests deletion, can their data be removed?
- [ ] **Cross-border transfer**: If data crosses borders, are transfer mechanisms compliant?
- [ ] **Purpose limitation**: Is data used only for stated analysis purpose?

**If violations found**: Flag as "BLOCKING" and do not proceed until resolved

#### B. Platform Policy Compliance
- [ ] **Rate limiting respected**: Were API rate limits followed during data collection?
- [ ] **Data redistribution prohibited**: Is raw platform data being redistributed?
- [ ] **Attribution included**: Are platforms properly credited as data sources?
- [ ] **Terms of service compliance**: Does data collection follow platform ToS?
- [ ] **User content rights**: Are user-generated content rights respected?

**If violations found**: Flag as "BLOCKING" and do not proceed

#### C. Content & Representation Compliance
- [ ] **Truthful claims**: Are sentiment scores supported by data?
- [ ] **No misleading omissions**: Are limitations and confidence levels clearly stated?
- [ ] **Attribution of sources**: Are all data sources properly credited?
- [ ] **No false endorsements**: Is analysis presented as objective, not as endorsement?
- [ ] **Competitor comparison fairness**: Is competitive analysis fair and substantiated?

**If violations found**: Flag as "REVIEW REQUIRED" and detail needed changes

#### D. Ethical Standards
- [ ] **Harm prevention**: Does analysis identify vulnerable individuals? (If so, exclude or flag)
- [ ] **Bias acknowledgment**: Are demographic/platform biases acknowledged?
- [ ] **Stakeholder impact**: Could analysis cause harm to individuals or groups?
- [ ] **Transparency about automation**: Is AI/automated analysis disclosed?
- [ ] **Professional judgment**: Are conclusions presented as tentative where evidence is weak?

**If concerns found**: Flag as "REVIEW REQUIRED" with ethical considerations

### Step 3: Structure Compliance Report

```yaml
compliance_check:
  applicable_regulations:
    - regulation: "[Regulation Name]"
      jurisdiction: "[Jurisdiction]"
      applicability: "[Why this applies to this case]"
      requirements:
        - "[Requirement 1]"
        - "[Requirement 2]"
      compliance_status: [COMPLIANT/PARTIAL/VIOLATION]
      findings: "[Specific findings]"
      action_required: "[NONE/MODIFY/REVIEW/BLOCK]"

    - regulation: "[Platform Policy]"
      platform: "[Platform Name]"
      applicability: "[Why this applies]"
      requirements:
        - "[Requirement 1]"
      compliance_status: [COMPLIANT/PARTIAL/VIOLATION]
      findings: "[Specific findings]"
      action_required: "[NONE/MODIFY/REVIEW/BLOCK]"

  blocking_issues: []
  review_required: []
  compliant_items: []

  detailed_findings:
    data_privacy:
      personal_data_present: true/false
      pii_identified: "[List any PII found]"
      consent_verified: true/false
      data_minimized: true/false
      cross_border_transfer: true/false
      recommendation: "[PROCEED/MODIFY/BLOCK]"

    platform_policies:
      api_terms_compliant: true/false
      rate_limits_respected: true/false
      data_redistribution_attempted: true/false
      attribution_included: true/false
      recommendation: "[PROCEED/MODIFY/BLOCK]"

    content_representation:
      claims_substantiated: true/false
      limitations_disclosed: true/false
      sources_attributed: true/false
      competitor_analysis_fair: true/false
      recommendation: "[PROCEED/MODIFY/REVIEW]"

    ethical_standards:
      vulnerable_individuals_identified: true/false
      bias_acknowledged: true/false
      potential_harm_assessed: true/false
      automation_disclosed: true/false
      recommendation: "[PROCEED/MODIFY/REVIEW]"

  overall_compliance_status: [COMPLIANT/CONDITIONAL/NON-COMPLIANT]
  release_authorization: [APPROVED/APPROVED_WITH_CONDITIONS/BLOCKED]
  conditions_if_applicable: "[List of conditions for conditional approval]"
  legal_review_required: true/false
  legal_review_scope: "[What legal should review]"
```

### Step 4: Determine Release Authorization

**COMPLIANT**: All requirements met → Authorize release

**CONDITIONAL**: Minor issues that can be addressed → Authorize with conditions:
- "Add attribution statement for Reddit data"
- "Include limitation statement about sample size"
- "Add disclosure about AI-generated analysis"

**NON-COMPLIANT**: Blocking violations present → Do NOT authorize release:
- PII present without consent
- Platform terms violated (data redistribution, scraping)
- Misleading claims that cannot be corrected

### Step 5: Provide Remediation Guidance

For each issue found, provide:
1. **Specific problem**: What exactly violates the requirement
2. **Remediation steps**: What changes are needed
3. **Verification method**: How to confirm the fix

## Output Format
Return a structured result containing:
1. **Applicable regulations** list with compliance status for each
2. **Blocking issues** that must be resolved
3. **Review-required items** with specific recommendations
4. **Detailed findings** by compliance category
5. **Overall authorization status** (Approved/Conditional/Blocked)
6. **Legal review flag** if professional review is needed

## Quality Gate
Before passing to the roadmap stage, verify:
- [ ] All applicable regulations have been checked
- [ ] Each finding is specific (not vague concerns)
- [ ] Action required is clear (Modify/Review/Block)
- [ ] Legal review flag is set correctly
- [ ] Remediation guidance is actionable
- [ ] Overall authorization status is clearly stated

## Example Output

**Case**: Social media crisis analysis for EU-based company

```yaml
compliance_check:
  applicable_regulations:
    - regulation: "GDPR (General Data Protection Regulation)"
      jurisdiction: "EU/EEA + UK"
      applicability: "Company is EU-based; data includes EU user posts"
      requirements:
        - "No PII in analysis output"
        - "User consent for data collection or public content only"
        - "Data minimization (aggregate where possible)"
      compliance_status: PARTIAL
      findings: "Analysis includes user handles (@username) which constitutes PII"
      action_required: MODIFY
      remediation: "Replace all handles with [User X] placeholders before release"

    - regulation: "Twitter/X API Terms"
      platform: "Twitter/X"
      applicability: "Twitter data collected via API"
      requirements:
        - "No redistribution of raw data"
        - "Attribution to Twitter as source"
        - "30-day data retention limit"
      compliance_status: COMPLIANT
      findings: "Analysis uses aggregated metrics only; no raw tweets redistributed"
      action_required: NONE

    - regulation: "Reddit API Terms"
      platform: "Reddit"
      applicability: "Reddit data collected via API"
      requirements:
        - "Public content only"
        - "Attribution to Reddit"
      compliance_status: COMPLIANT
      findings: "Public posts only; Reddit attributed in sources"
      action_required: NONE

    - regulation: "FTC Endorsement Guides (USA)"
      jurisdiction: "USA (if applicable)"
      applicability: "Not applicable - no influencer marketing analysis"
      requirements: []
      compliance_status: COMPLIANT
      findings: "N/A - not triggered for this analysis"
      action_required: NONE

  blocking_issues:
    - issue: "PII present (Twitter handles)"
      location: "Section 3, Table 3.1"
      severity: HIGH
      remediation: "Replace @userhandle with [User X]; add note: 'User identifiers anonymized for privacy'"

  review_required:
    - item: "Competitor sentiment comparison"
      concern: "Fairness of comparison methodology"
      recommendation: "Add statement: 'Comparison based on available public data; may not reflect complete sentiment picture'"

  compliant_items:
    - "GDPR consent (public content only)"
    - "Twitter/X API terms (no data redistribution)"
    - "Reddit API terms (public content, attribution included)"
    - "Claim substantiation (all scores cite sources)"
    - "Limitation disclosure (confidence levels stated)"

  detailed_findings:
    data_privacy:
      personal_data_present: true
      pii_identified: "Twitter handles (@username), location tags in some posts"
      consent_verified: true
      data_minimized: false
      cross_border_transfer: false
      recommendation: MODIFY

    platform_policies:
      api_terms_compliant: true
      rate_limits_respected: true
      data_redistribution_attempted: false
      attribution_included: true
      recommendation: PROCEED

    content_representation:
      claims_substantiated: true
      limitations_disclosed: true
      sources_attributed: true
      competitor_analysis_fair: true
      recommendation: PROCEED

    ethical_standards:
      vulnerable_individuals_identified: false
      bias_acknowledged: true
      potential_harm_assessed: true
      automation_disclosed: true
      recommendation: PROCEED

  overall_compliance_status: CONDITIONAL
  release_authorization: APPROVED_WITH_CONDITIONS
  conditions_if_applicable:
    - "Remove all Twitter handles and replace with anonymized placeholders"
    - "Add statement about competitor comparison limitations"
  legal_review_required: false
  legal_review_scope: null
```

## Common Compliance Issues and Remediations

| Issue | Why It's a Problem | Remediation |
|---|---|---|
| User handles/IDs included | PII under GDPR; violates privacy | Replace with [User X]; note anonymization |
| Raw content quoted | May violate platform terms | Quote sparingly; paraphrase; attribute |
| No platform attribution | Violates platform terms | Add "Data source: [Platform]" to report |
| Missing limitation disclosure | Misleading; violates ethics codes | Add "Limitations" section with confidence levels |
| Competitor claims unsubstantiated | Misleading advertising; FTC issues | Substantiate with data; add caveats |
| No automation disclosure | Misrepresentation of capabilities | Add "Analysis uses AI-powered NLP models" |

## Integration Notes
- Always check compliance based on **where data comes from**, not just where the report is delivered
- GDPR applies if **any** EU data is processed, regardless of company location
- Platform terms apply even when using public data
- When in doubt, flag for legal review—it's better to over-review than under-review
- Compliance is a gate, not a suggestion—BLOCKING issues must stop release

## Special Cases

### Academic/Research Use
If analysis is for academic research:
- Institutional Review Board (IRB) approval may be needed
- Different rules for public vs. private data
- May require anonymization beyond standard GDPR

### Internal-Only Analysis
If analysis is internal-only (not shared externally):
- Some compliance requirements are relaxed
- Platform terms still apply
- Employee data has additional protections

### Crisis Context
In active crisis situations:
- Speed vs. compliance trade-off: Don't skip compliance, but can prioritize critical checks
- Document any compliance shortcuts taken for urgent response
- Follow up with full compliance review post-crisis

## Jurisdiction-Specific Guidance

### European Union (GDPR)
- Strictest data privacy rules globally
- PII includes: names, usernames (in context), location, IP addresses
- Consent required unless using public data with legitimate interest
- Data minimization: only collect what's necessary

### United States
- Sector-specific laws (HIPAA for healthcare, COPPA for children)
- State laws (CCPA in California, others emerging)
- Platform terms often stricter than regulations

### Asia-Pacific
- Varies widely by country (strict in some, minimal in others)
- Cross-border data transfer restrictions common
- Local language requirements for disclosures

## Compliance Checklist (Final Gate)

Before authorizing release, confirm:
- [ ] No PII in output (or properly anonymized)
- [ ] All platform terms respected (no ToS violations)
- [ ] Data sources properly attributed
- [ ] Claims substantiated with evidence
- [ ] Limitations and confidence levels disclosed
- [ ] No misleading omissions or cherry-picked data
- [ ] Competitor comparisons are fair
- [ ] Ethical standards met
- [ ] Automation and AI disclosed

If ALL checkboxes pass → Authorize release
If ANY fail → Apply remediation or flag for review
