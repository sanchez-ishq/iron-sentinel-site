# CompTIA SecAI+ (CY0-001) — Master Study Plan

**Candidate:** Owner, Iron Sentinel
**Exam:** CompTIA SecAI+ — exam code **CY0-001 V1**
**Format:** Deep, 6+ week curriculum (reading → drills → practice exams)
**Objectives source:** Anchored to the **official CompTIA SecAI+ CY0-001 V1 Exam Objectives, Document Version 2.0 (© 2025 CompTIA)** — the authoritative document. (Earlier drafts used a third-party reproduction; the kit has since been reconciled to the official objectives and acronym list.)

> CompTIA's objectives doc lists "number of questions" and "length of test" as **TBD**; the 60-question / 60-minute / 600-to-pass figures come from CompTIA's product page and may be finalized at launch. Treat them as planning estimates and confirm on your exam registration.

> **Official acronyms & lab list:** see `07-official-acronyms-and-lab.md` — every acronym CompTIA lists for this exam, plus the official hardware/software list. Know the acronyms cold.

---

## Exam facts (official)

- **Questions:** Max 60 (multiple-choice **and performance-based**)
- **Duration:** 60 minutes
- **Passing score:** 600 (scale 100–900)
- **Launched:** Feb 17, 2026 · ~3-year lifecycle
- **Recommended experience:** 3–4 yrs IT, 2+ yrs hands-on cybersecurity; Security+, CySA+, or PenTest+ helpful
- **Language:** English

> Note the tight clock: 60 questions in 60 minutes = **~1 min/question**, and some are
> performance-based (longer). Timed practice matters more than usual.

---

## Exam blueprint (official domain weighting)

| # | Domain | Weight | Module owner |
|---|--------|--------|--------------|
| 1 | Basic AI concepts related to cybersecurity | 17% | CTO |
| 2 | **Securing AI systems** | **40%** | CISO |
| 3 | AI-assisted security | 24% | CTO |
| 4 | AI governance, risk & compliance | 19% | CSO |

**Domain 2 is 40% of the exam** — nearly half. Budget your study time accordingly.
Domains 2 + 3 (securing AI + using AI defensively) together are 64%; this is a
hands-on, applied exam, not a memorization exam.

### Official objective map (CY0-001 V1, v2.0)

| Obj | Title | Module |
|---|---|---|
| 1.1 | Compare/contrast AI types & techniques | 01 |
| 1.2 | Importance of data security in relation to AI | 01 (§5A) |
| 1.3 | Security throughout the AI life cycle | 01 (§11) |
| 2.1 | Use AI threat-modeling resources | 02 (§A13) |
| 2.2 | Implement security controls for AI systems | 02 (§B1) |
| 2.3 | Implement access controls for AI systems | 02 (§B2, B5) |
| 2.4 | Implement data security controls | 02 (§B5A) |
| 2.5 | Implement monitoring & auditing | 02 (§B6) |
| 2.6 | Analyze attack evidence & compensating controls | 02 (§A1–A14) |
| 3.1 | Use AI-enabled tools for security tasks | 03 (§6A) |
| 3.2 | How AI enables/enhances attack vectors | 03 (§6B) |
| 3.3 | Use AI to automate security tasks | 03 (§6C) |
| 4.1 | Organizational governance structures for AI | 04 (§6A) |
| 4.2 | Risks associated with AI | 04 (§9.0) |
| 4.3 | Impact of compliance on AI | 04 (§7.6, §1–6) |

### Practice question bank (300+ questions)

In addition to the in-module questions, the kit includes weighted question banks
sized to the blueprint — see `qbank-domain1.md`…`qbank-domain4.md` and the
full-length `qbank-final-mock-60.md`. Target **85%+** on each bank before booking.

---

## 6-week schedule

### Week 1 — AI foundations for security (Domain 1, 17%)
- Read Module 01: AI/ML/GenAI fundamentals, model types, training vs inference, LLMs,
  embeddings/RAG, agents/tool-use, the AI attack surface vocabulary.
- Drill: flashcards on AI terminology (you must be fluent before Domain 2).
- Checkpoint: Domain 1 quiz (target 80%).

### Weeks 2–3 — Securing AI systems (Domain 2, 40% — two weeks)
- Read Module 02 in two passes:
  - Pass A: attacks ON AI (prompt injection direct/indirect, jailbreaks, data/model
    poisoning, model inversion/extraction/theft, evasion/adversarial examples,
    membership inference, insecure plugins/tools, AI supply chain).
  - Pass B: defenses & controls (input/output validation, guardrails, least-privilege
    agents, model/data governance, secure MLOps, runtime monitoring, red-teaming AI).
- Lab: run through a prompt-injection and a data-poisoning walkthrough.
- Checkpoint: two Domain 2 quizzes (this is 40% — over-study it). Target 85%.

### Week 4 — AI-assisted security (Domain 3, 24%)
- Read Module 03: AI for detection (anomaly/UEBA), SOC automation/SOAR enrichment,
  alert triage, AI in vuln management & threat intel, AI in DevSecOps pipelines,
  limitations/risks of AI tooling (hallucination, bias, over-trust).
- Lab: design an AI-assisted SOC workflow.
- Checkpoint: Domain 3 quiz (target 80%).

### Week 5 — AI governance, risk & compliance (Domain 4, 19%)
- Read Module 04: NIST AI RMF, EU AI Act, GDPR/privacy for AI, ISO/IEC 42001,
  AI risk assessment, model cards/data sheets, third-party/AI vendor risk,
  acceptable-use & AI policy, audit & evidence for AI.
- Checkpoint: Domain 4 quiz (target 80%).

### Week 6 — Integration & exam readiness
- Full-length, **timed** practice exam #1 (60 Q / 60 min). Review every miss.
- Targeted remediation on weakest domain (almost certainly inside Domain 2).
- Full-length timed practice exam #2 + at least one performance-based scenario.
- Target 85%+ before booking.

> Add a Week 7 buffer if any practice exam is below 80%, or if Domain 2 is below 85%.

---

## How to use this kit
1. Read the module for the week.
2. Do the end-of-module practice questions (in each module file).
3. Log scores in the progress tracker.
4. Re-test weak areas before advancing. Don't move past a week below 80% (85% for Domain 2).
5. In Week 6, always practice **timed** — the 1-min/question pace is the silent killer on this exam.

## Module files
- `01-domain1-ai-concepts-for-security.md` (CTO)
- `02-domain2-securing-ai-systems.md` (CISO) ← largest, 40%
- `03-domain3-ai-assisted-security.md` (CTO)
- `04-domain4-ai-governance-risk-compliance.md` (CSO)
