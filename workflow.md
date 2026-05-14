# Dynamic Questionnaire Engine — Complete Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                      START ASSESSMENT                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                 LOAD INITIAL ASSESSMENT STATE                │
│--------------------------------------------------------------│
│ • answers = {}                                               │
│ • flags = []                                                 │
│ • scores = {}                                                │
│ • coverage = {}                                              │
│ • decision_trace = []                                        │
│ • vessel_context = {}                                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                    LOAD VESSEL CONTEXT                       │
│--------------------------------------------------------------│
│ • IMO Number                                                 │
│ • Vessel Type                                                │
│ • Connectivity Type                                          │
│ • Vendor Access                                              │
│ • Operational Context                                        │
│ • Existing Infrastructure                                    │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                      LOAD QUESTION BANK                      │
│--------------------------------------------------------------│
│ Each question contains:                                      │
│                                                              │
│ • Question Text                                              │
│ • Base Priority                                              │
│ • Conditions                                                 │
│ • Risk Tags                                                  │
│ • Coverage Tags                                              │
│ • Correlation Rules                                          │
│ • Vessel Modifiers                                           │
│ • Compliance Mapping                                         │
│ • MITRE Mapping                                              │
│ • Explainability Metadata                                    │
└──────────────────────────────────────────────────────────────┘
                              ↓
════════════════════════ MAIN ENGINE LOOP ══════════════════════
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                 FILTER ELIGIBLE QUESTIONS                    │
│--------------------------------------------------------------│
│ Remove questions that are:                                   │
│                                                              │
│ • Already answered                                           │
│ • Invalid by conditions                                      │
│ • Blocked by workflow logic                                  │
│ • Irrelevant to vessel type                                  │
│ • Below risk threshold                                       │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                CALCULATE QUESTION PRIORITIES                 │
│--------------------------------------------------------------│
│ Final Priority =                                             │
│                                                              │
│ Base Priority                                                │
│ + Active Risk Boost                                          │
│ + Coverage Gap Boost                                         │
│ + Vessel Modifier                                            │
│ + Correlation Boost                                          │
│ + Threat Intelligence Boost                                  │
│ + Explainability Weight                                      │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                SELECT BEST NEXT QUESTION                     │
│--------------------------------------------------------------│
│ Engine selects:                                              │
│                                                              │
│ • Highest intelligence value                                 │
│ • Highest risk relevance                                     │
│ • Highest missing coverage                                   │
│ • Strongest attack-path significance                         │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                     DISPLAY QUESTION                         │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                    RECEIVE USER ANSWER                       │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                     UPDATE STATE ENGINE                      │
│--------------------------------------------------------------│
│ • Store answer                                               │
│ • Mark question completed                                    │
│ • Update timestamps                                          │
│ • Update assessment history                                  │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                     PROCESS RISK FLAGS                       │
│--------------------------------------------------------------│
│ Example:                                                     │
│                                                              │
│ NO MFA                                                       │
│ → weak_authentication                                        │
│                                                              │
│ Public RDP                                                   │
│ → remote_exposure                                            │
│                                                              │
│ Legacy OT                                                    │
│ → legacy_system_risk                                         │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                    UPDATE RISK SCORES                        │
│--------------------------------------------------------------│
│ Risk categories updated dynamically:                         │
│                                                              │
│ • Authentication                                             │
│ • Remote Access                                              │
│ • Network Security                                           │
│ • Vendor Security                                            │
│ • OT Security                                                │
│ • Endpoint Protection                                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                    UPDATE COVERAGE ENGINE                    │
│--------------------------------------------------------------│
│ Engine tracks how much visibility exists for:                │
│                                                              │
│ • Authentication                                             │
│ • Infrastructure                                             │
│ • OT Systems                                                 │
│ • Remote Access                                              │
│ • Vendor Management                                          │
│ • Wireless Security                                          │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                    RUN CORRELATION ENGINE                    │
│--------------------------------------------------------------│
│ Engine correlates weak indicators into attack paths:         │
│                                                              │
│ Vendor Access                                                │
│ + No MFA                                                     │
│ + Public RDP                                                 │
│ = High Remote Compromise Risk                                │
│                                                              │
│ Weak WiFi                                                    │
│ + Shared Crew Devices                                        │
│ + Flat Network                                               │
│ = Lateral Movement Risk                                      │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                  GENERATE EXPLAINABILITY                     │
│--------------------------------------------------------------│
│ Engine records WHY decisions were made:                      │
│                                                              │
│ Example:                                                     │
│                                                              │
│ "VPN question selected because:"                             │
│ • remote exposure detected                                   │
│ • authentication weakness found                              │
│ • vendor access enabled                                      │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                  UPDATE DECISION TRACE                       │
│--------------------------------------------------------------│
│ Every decision is logged for:                                │
│                                                              │
│ • Replayability                                              │
│ • Auditability                                               │
│ • Debugging                                                  │
│ • Compliance Evidence                                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                 RECALCULATE SYSTEM PRIORITIES                │
│--------------------------------------------------------------│
│ New priorities are generated using:                          │
│                                                              │
│ • Latest answers                                             │
│ • Active risk flags                                          │
│ • Coverage gaps                                              │
│ • Correlation signals                                        │
│ • Vessel-aware modifiers                                     │
│ • Threat intelligence                                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│              ARE HIGH VALUE QUESTIONS REMAINING?             │
└──────────────────────────────────────────────────────────────┘
                    ↓ YES                     ↓ NO
                    ↓                         ↓
        ═══════════ LOOP ═══════════      ┌───────────────────┐
                    ↓                     │ ASSESSMENT ENDS   │
                    ↓                     └───────────────────┘
                    ↓                               ↓
         SELECT NEXT QUESTION                       ↓
                    ↓                               ↓
               REPEAT LOOP                          ↓
                                                    ↓
┌──────────────────────────────────────────────────────────────┐
│                     EXPORT RESULTS                           │
│--------------------------------------------------------------│
│ • assessment.json                                            │
│ • assessment.csv                                             │
│ • decision_trace.json                                        │
│ • risk_summary.json                                          │
│ • explainability_log.json                                    │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                        FINAL OUTPUT                          │
│--------------------------------------------------------------│
│ • Dynamic Risk Assessment                                    │
│ • Vessel Cybersecurity Posture                               │
│ • Attack Path Visibility                                     │
│ • Compliance Visibility                                      │
│ • Coverage Analysis                                          │
│ • Explainable Decision Trail                                 │
│ • Risk Correlation Insights                                  │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                             END                              │
└──────────────────────────────────────────────────────────────┘
```
