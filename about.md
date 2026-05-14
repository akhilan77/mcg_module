````md
# Yacht Cybersecurity Dynamic Questionnaire Engine — Workflow

---

# 1. Introduction

The Yacht Cybersecurity Dynamic Questionnaire Engine is an adaptive cyber assessment platform designed specifically for maritime and yacht environments.

Unlike traditional static questionnaires, this system dynamically selects questions based on:

- Previous answers
- Risk indicators
- Vessel profile
- Security posture
- OSINT findings
- Missing coverage areas
- Correlation logic

The engine continuously adjusts assessment flow in real-time to maximize intelligence gathering while minimizing unnecessary questioning.

---

# 2. High-Level Workflow

```text
Start Assessment
        ↓
Load Vessel Context
        ↓
Initialize State Engine
        ↓
Select Best Question
        ↓
Display Question
        ↓
User Response
        ↓
Process Flags
        ↓
Update Scores
        ↓
Update Coverage
        ↓
Correlation Analysis
        ↓
Generate Explainability
        ↓
Select Next Question
        ↓
Repeat Until Complete
        ↓
Export Assessment
```
````

---

# 3. System Architecture

```text
CLI Layer
   ↓
Questionnaire Engine
   ↓
Filtering Engine
   ↓
Scoring Engine
   ↓
Explainability Engine
   ↓
Correlation Engine
   ↓
Export Engine
```

---

# 4. Core Components

## 4.1 CLI Layer

Responsible for:

- User interaction
- Question rendering
- Input validation
- Session control

---

## 4.2 Questionnaire Engine

Responsible for:

- Dynamic question selection
- Priority calculation
- Branching logic
- Adaptive workflows

Main file:

```text
engine.py
```

---

## 4.3 Scoring Engine

Responsible for:

- Risk scoring
- Threat weighting
- Security posture calculation
- Risk aggregation

---

## 4.4 Explainability Engine

Responsible for:

- Explaining why questions were selected
- Showing score traceability
- Audit transparency
- Decision reconstruction

Example:

```text
WHY THIS QUESTION?

- Vendor access enabled
- Public RDP exposed
- MFA missing
```

---

## 4.5 Correlation Engine

Responsible for identifying attack paths using multiple weak indicators.

Example:

```text
Vendor Access
+
No MFA
+
Public RDP
=
High Remote Compromise Risk
```

This creates intelligence-driven assessments rather than isolated checks.

---

## 4.6 Export Engine

Responsible for:

- JSON export
- CSV export
- Audit trail generation
- Assessment replay support

Generated outputs:

```text
assessment.json
assessment.csv
decision_trace.json
```

---

# 5. Dynamic Question Selection Workflow

The engine does NOT follow a fixed sequence.

Each next question is selected using:

```text
Current Answers
+ Active Risks
+ Coverage Gaps
+ Vessel Profile
+ Correlation Signals
+ OSINT Findings
+ Question Priority
```

---

# 6. Question Selection Logic

## Step 1 — Load Candidate Questions

All unanswered questions are loaded.

---

## Step 2 — Apply Conditions

Questions may contain conditions such as:

```python
"conditions": {
    "vendor_access": True
}
```

Only matching questions remain eligible.

---

## Step 3 — Calculate Priority Score

Priority score is calculated using:

```text
Base Priority
+ Risk Boost
+ Vessel Modifiers
+ Correlation Boost
+ Coverage Boost
```

---

## Step 4 — Select Highest Priority Question

The engine selects the question with the highest intelligence value.

---

# 7. Intelligent Question Objects

Each question object may contain:

```python
{
  "id": "vendor_mfa",

  "question": "Is MFA enabled for vendors?",

  "priority": 70,

  "risk_tags": [
      "authentication"
  ],

  "conditions": {
      "vendor_access": True
  },

  "flags": [
      "weak_authentication"
  ],

  "mitre": [
      "T1078"
  ],

  "compliance": [
      "NIST",
      "IMO2021"
  ],

  "vessel_modifiers": [
      {
          "if_vessel_type": "charter_yacht",
          "boost": 20
      }
  ]
}
```

---

# 8. Vessel-Aware Adaptive Questioning

The engine changes questioning behavior depending on vessel type.

| Vessel Type       | Priority Areas  |
| ----------------- | --------------- |
| Charter Yacht     | Guest WiFi      |
| Explorer Yacht    | SATCOM          |
| Older Vessel      | Legacy Systems  |
| Commercial Vessel | OT Segmentation |

---

# 9. IMO-Centric Intelligence Model

The IMO number acts as the master identity key.

```text
IMO
 ↓
Vessel Identity
 ↓
OSINT Discovery
 ↓
Context Enrichment
 ↓
Risk Indicators
 ↓
Adaptive Assessment
```

This enables vessel-aware intelligence correlation.

---

# 10. Explainability Workflow

Every question can explain WHY it appeared.

Example:

```text
Question Selected:
"Is vendor MFA enabled?"

Reason:
- Vendor access detected
- Remote access risk elevated
- Authentication controls missing
```

This improves:

- Transparency
- Auditability
- Trust
- Analyst understanding

---

# 11. Decision Trace Logging

Every engine decision can be recorded.

Example:

```json
{
  "question": "vendor_mfa",
  "selected_because": ["vendor_access", "public_rdp", "weak_authentication"]
}
```

Benefits:

- Replayability
- Debugging
- Compliance evidence
- Assessment reconstruction

---

# 12. Risk Correlation Workflow

The system correlates weak signals into larger attack paths.

Example:

```text
Public RDP
+
Weak Passwords
+
Vendor Access
+
No MFA
=
Critical Remote Entry Risk
```

This mimics real-world attacker thinking.

---

# 13. Branching Logic Visualization

```text
Vendor Access?
     ↓ yes
Vendor MFA?
     ↓ no
Weak Authentication Flag
     ↓
VPN Questions Boosted
```

The engine continuously reshapes assessment flow.

---

# 14. Coverage Engine

The engine tracks assessment coverage areas.

Example domains:

- Authentication
- Remote Access
- Network Security
- OT Security
- Vendor Management
- Endpoint Protection

Questions may be boosted if coverage is weak.

---

# 15. Maritime Threat Modeling

The engine models maritime-specific threats such as:

- Vendor compromise
- SATCOM abuse
- OT manipulation
- Crew phishing
- Ransomware
- Lateral movement
- Remote access exploitation

---

# 16. MITRE ATT&CK Mapping

Questions may map to MITRE ATT&CK techniques.

Example:

| Technique | Description              |
| --------- | ------------------------ |
| T1078     | Valid Accounts           |
| T1021     | Remote Services          |
| T1133     | External Remote Services |

This improves threat intelligence maturity.

---

# 17. Compliance Alignment

The system can align with:

- IMO 2021 Cyber Requirements
- NIST Cybersecurity Framework
- IEC 62443
- CIS Controls

---

# 18. Confidence & Uncertainty Modeling

Future enhancement:

```text
Unknown answers
↓
Lower confidence
↓
Additional validation questions triggered
```

This creates adaptive uncertainty reduction.

---

# 19. Future Enhancements

## AI/LLM Integration

```text
AI-generated follow-up questions
```

---

## Real-Time OSINT

```text
Shodan integration
Censys integration
Leak intelligence
```

---

## Multi-Agent Architecture

```text
OSINT Agent
Risk Agent
Correlation Agent
Compliance Agent
```

---

## Graph Database

```text
Risk relationship graphing
```

---

## Fleet Intelligence

```text
Cross-vessel comparison
Fleet-wide trends
```

---

## Web Dashboard

```text
Assessment replay
Visual analytics
Threat heatmaps
```

---

# 20. Design Philosophy

```text
The system minimizes unnecessary questions
while maximizing intelligence gain.
```

Core principles:

- Adaptive intelligence
- Explainability
- Maritime awareness
- Risk-driven orchestration
- Transparency
- Efficiency

---

# 21. Final Workflow Summary

```text
User Answer
    ↓
Flags Generated
    ↓
Risk Updated
    ↓
Coverage Updated
    ↓
Correlation Engine Runs
    ↓
Priority Recalculated
    ↓
Best Next Question Selected
    ↓
Explainability Generated
```

---

# 22. Conclusion

The Dynamic Yacht Cybersecurity Questionnaire Engine is not merely a questionnaire system.

It is an adaptive cyber intelligence orchestration platform capable of:

- Dynamic assessments
- Risk correlation
- Vessel-aware questioning
- Explainable decision-making
- Maritime threat modeling
- Audit-grade traceability

The architecture is designed for future expansion into:

- AI-assisted cyber assessments
- Fleet intelligence systems
- Real-time OSINT integration
- Enterprise maritime cyber platforms

```

Based on the architecture ideas from your uploaded notes. :contentReference[oaicite:0]{index=0}
```
