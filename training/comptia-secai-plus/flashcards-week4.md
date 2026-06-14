# SecAI+ (CY0-001) — Week 4 Flashcards: Domain 3 Terminology

**Scope:** Domain 3 — AI-Assisted Security (objectives 3.1–3.3), 24% of the exam.
**How to use:** Cover the indented answer, read the **bold front**, recall aloud, reveal. ~56 cards. (Anki TSV at bottom.)

> Domain 3 is workflow-oriented: know what the tool does, where it fits in the analyst's process, and its failure modes.

---

## Objective 3.1 — AI-Enabled Tools & Use Cases

**1. IDE plug-in**
> AI inside the developer's editor (e.g., Copilot) for secure code suggestions and inline scanning. Caution: insecure generated code; source/secrets sent to vendor.

**2. Browser plug-in**
> AI in the browser to summarize/analyze pages. Caution: sensitive page content sent to the model; indirect-injection surface.

**3. CLI plug-in**
> AI in the terminal to explain commands or generate scripts. Caution: can generate destructive commands — review before running.

**4. Chatbot**
> A conversational AI interface (security copilot) for Q&A, hunting, and summarization. Caution: hallucination — verify outputs.

**5. Personal assistant**
> An agentic assistant that takes actions across tools. Caution: excessive agency — needs least privilege + human-in-the-loop.

**6. MCP server (Model Context Protocol)**
> The standard for connecting AI agents to external tools/data via standardized connectors. A privileged integration — authenticate, scope, and treat tool results as untrusted (injection surface).

**7. Signature matching**
> AI/automation comparing artifacts to known-bad indicators (hashes, patterns) to flag known threats.

**8. Code quality & linting**
> AI reviewing code for style, defects, and insecure patterns.

**9. Vulnerability analysis**
> AI identifying and assessing vulnerabilities in code/systems.

**10. Automated penetration testing**
> AI assisting/automating recon, fuzzing, and exploitation steps in a pentest.

**11. Anomaly detection**
> AI flagging deviations from a learned baseline — surfaces novel/unknown threats without signatures.

**12. Pattern recognition**
> AI identifying recurring structures across data (e.g., campaign clustering, behavior patterns).

**13. Incident management**
> AI assisting detection-to-resolution workflows (triage, enrichment, summaries, tickets).

**14. Threat modeling (AI use case)**
> AI drafting threat models / attack trees from an architecture description.

**15. Fraud detection**
> ML scoring transactions/behavior against a baseline to flag fraud (often graph analytics for rings).

**16. Translation (use case)**
> AI normalizing multilingual threat intel, phishing, or analyst notes into a working language.

**17. Summarization (use case)**
> AI condensing alerts, incidents, and reports into readable summaries.

---

## Objective 3.2 — AI-Enabled Attack Vectors

**18. Deepfake**
> AI-generated synthetic audio/video/images. Used for impersonation, misinformation, disinformation; can bypass voice/face biometrics.

**19. Impersonation (deepfake)**
> Posing as a trusted person (e.g., CEO-voice wire fraud) using synthetic media. Counter: out-of-band call-back verification.

**20. Misinformation vs. disinformation**
> Misinformation = false info spread without intent to deceive. Disinformation = false info spread *deliberately* to deceive.

**21. Adversarial networks (attack use)**
> GANs used to generate adversarial examples, synthetic identities, and realistic fake content at scale.

**22. AI-enabled reconnaissance**
> AI accelerating OSINT aggregation and attack-surface mapping from public data.

**23. AI-enhanced social engineering**
> GenAI producing fluent, personalized phishing/spear-phishing/vishing — grammar errors no longer a reliable signal.

**24. Obfuscation (AI-enabled)**
> AI mutating malware/payloads to produce polymorphic/metamorphic code that changes signature each build to evade detection.

**25. Automated data correlation**
> AI correlating breach dumps, OSINT, and leaked credentials to de-anonymize and profile targets at scale.

**26. Automated attack generation**
> AI assisting/automating attack-vector discovery, payload generation, and malware creation — lowering the skill barrier.

**27. Honeypot (dual-use)**
> Defenders use AI to generate convincing deceptive honeypots/honeytokens; attackers use AI to detect and evade them.

**28. AI-orchestrated DDoS**
> AI used to coordinate adaptive distributed denial-of-service that shifts tactics to evade mitigation.

---

## Objective 3.3 — AI Automation Scenarios

**29. Low-code / no-code scripting**
> AI generating scripts/glue from natural language so non-developers can automate. Caution: ungoverned "citizen automation" / shadow AI.

**30. Document synthesis & summarization**
> Auto-drafting reports, runbooks, policies, and post-incident reviews from source data.

**31. IR ticket management**
> AI auto-creating, enriching, routing, summarizing, and closing incident tickets; maintaining the timeline.

**32. AI-assisted change approvals**
> AI risk-scoring proposed changes, drafting change records, and recommending approve/deny.

**33. Automated deployment / rollback**
> AI-evaluated signals trigger promotion to production or automatic rollback on failed health/security checks.

**34. AI agents (automation)**
> Autonomous agents wired into workflows/pipelines to execute multi-step tasks.

**35. CI/CD security automation**
> AI-driven gates in the pipeline: code scanning, SCA, unit/regression/model testing, automated deploy/rollback.

**36. Model testing (in CI/CD)**
> Evaluating an ML model on each update for performance, drift, and safety/security regressions.

---

## Detection & DevSecOps terms (supporting)

**37. SIEM**
> Security Information and Event Management — central log aggregation, correlation, and alerting.

**38. SOAR**
> Security Orchestration, Automation, and Response — executes automated response playbooks.

**39. UEBA**
> User and Entity Behavior Analytics — ML baselines of user/entity behavior; surfaces insider threats and compromised accounts.

**40. NDR**
> Network Detection and Response — ML on traffic metadata (no payload decryption) to detect C2, exfil, lateral movement.

**41. EDR / XDR**
> EDR = endpoint telemetry + detection/response. XDR = cross-telemetry correlation (endpoint+network+identity+cloud).

**42. SAST vs. DAST vs. SCA**
> SAST = static source-code analysis (pre-build). DAST = probing the running app (test/stage). SCA = scanning third-party dependencies for known CVEs.

**43. CVSS vs. EPSS vs. KEV**
> CVSS = inherent severity (0–10). EPSS = predicted probability of exploitation in 30 days. CISA KEV = confirmed actively-exploited list (top priority).

---

## Objective 3 — Limitations of Defensive AI (high-yield)

**44. Hallucination (defensive AI)**
> AI confidently producing wrong output (fake IOC, wrong patch status). Mitigate: ground in authoritative data; require analyst verification.

**45. Automation bias**
> Humans over-trusting AI verdicts without review — closing real alerts because "the AI said benign." A human failure, distinct from hallucination.

**46. Adversarial evasion (of detectors)**
> Attackers crafting inputs to evade ML detectors (adversarial examples, staying within UEBA "normal"). Don't rely solely on AI detection.

**47. Bias / drift (security AI)**
> Models trained on stale/unrepresentative data misfire after environment change. Mitigate: continuous monitoring, retraining, diverse data.

**48. Explainability / black-box problem**
> Inability to explain why a model scored an alert. Hurts analyst trust, audit, and root-cause. Tools: SHAP, LIME.

**49. Telemetry data privacy**
> Sending endpoint/email/code telemetry to a cloud AI is a third-party data-sharing event (PII/IP exposure) needing vendor assessment and controls.

---

## Commonly-confused discriminators

**50. AI-enabled attack vs. attack on AI**
> AI-enabled attack (D3) = attacker *uses* AI as a weapon (deepfake, polymorphic malware). Attack on AI (D2) = attacker *targets* a model (prompt injection, poisoning).

**51. Hallucination vs. automation bias**
> Hallucination = the AI's error (wrong output). Automation bias = the human's error (trusting it without checking).

**52. Anomaly detection vs. threat hunting**
> Anomaly detection = automated, continuous flagging. Threat hunting = human-led, hypothesis-driven investigation using AI as a tool.

**53. Signature vs. anomaly-based detection**
> Signature = matches known patterns (low FP, no zero-day coverage). Anomaly = deviation from baseline (catches novel, higher FP until tuned).

**54. SOAR vs. AI copilot**
> SOAR = executes automated playbooks. Copilot = assists the human with language tasks (queries, summaries, recommendations).

**55. Misinformation vs. disinformation**
> Misinformation = false, no intent to deceive. Disinformation = false, *deliberately* deceptive.

**56. Full automation vs. human gate**
> Reversible/low-impact actions suit full automation; high-impact/irreversible actions (critical prod deploys, mass blocks) need a human approval gate.

---

## Anki / Quizlet import (TSV — term &lt;TAB&gt; definition)

```tsv
MCP server	Standard for connecting AI agents to tools/data; a privileged, injection-prone integration
IDE plug-in	AI in the editor for code suggestions/scanning; risk of insecure code and data sent to vendor
Browser plug-in	AI summarizing/analyzing pages; risk of sensitive content sent out and indirect injection
CLI plug-in	AI generating terminal commands/scripts; review before running destructive commands
Chatbot	Conversational security copilot; verify outputs due to hallucination
Personal assistant	Agentic assistant taking actions; needs least privilege + HITL (excessive agency risk)
Signature matching	Comparing artifacts to known-bad indicators to flag known threats
Code quality and linting	AI reviewing code for defects and insecure patterns
Vulnerability analysis	AI identifying and assessing vulnerabilities
Automated penetration testing	AI assisting/automating recon, fuzzing, exploitation
Anomaly detection	Flagging deviations from a learned baseline; catches novel threats without signatures
Pattern recognition	Identifying recurring structures across data
Incident management	AI assisting triage-to-resolution workflows
Threat modeling (AI)	AI drafting threat models/attack trees from architecture
Fraud detection	ML scoring transactions/behavior against a baseline to flag fraud
Translation (use case)	AI normalizing multilingual intel/notes into a working language
Summarization (use case)	AI condensing alerts/incidents/reports
Deepfake	AI-generated synthetic media for impersonation/misinformation/disinformation
Misinformation	False info spread without intent to deceive
Disinformation	False info spread deliberately to deceive
Adversarial networks	GANs generating adversarial examples/synthetic identities/fake content
AI-enabled reconnaissance	AI accelerating OSINT aggregation and attack-surface mapping
AI-enhanced social engineering	GenAI producing fluent personalized phishing/vishing
Obfuscation (AI)	AI mutating malware to polymorphic code that changes signature each build
Automated data correlation	AI correlating dumps/OSINT/credentials to de-anonymize and profile targets
Automated attack generation	AI assisting attack-vector discovery, payloads, and malware creation
Honeypot (dual-use)	Defenders generate deceptive honeypots; attackers use AI to detect/evade them
AI-orchestrated DDoS	AI coordinating adaptive DDoS that shifts tactics to evade mitigation
Low-code/no-code scripting	AI generating automation from natural language; shadow-AI/citizen-automation risk
Document synthesis	Auto-drafting reports/runbooks/post-incident reviews
IR ticket management	AI creating/enriching/routing/summarizing/closing incident tickets
AI-assisted change approvals	AI risk-scoring changes and recommending approve/deny
Automated deployment/rollback	AI-evaluated signals trigger promotion or automatic rollback
Model testing (CI/CD)	Evaluating a model each update for performance, drift, and safety/security regressions
SIEM	Central log aggregation, correlation, and alerting
SOAR	Executes automated response playbooks
UEBA	ML baselines of user/entity behavior; surfaces insider threats and account compromise
NDR	ML on network traffic metadata to detect C2, exfil, lateral movement
EDR/XDR	EDR = endpoint detection/response; XDR = cross-telemetry correlation
SAST/DAST/SCA	Static code / running-app / third-party-dependency security testing
CVSS/EPSS/KEV	Inherent severity / exploitation probability / confirmed exploited list
Hallucination (defensive AI)	AI confidently producing wrong output; ground in authoritative data and verify
Automation bias	Humans over-trusting AI verdicts without review (a human failure)
Adversarial evasion	Attackers crafting inputs to evade ML detectors; don't rely solely on AI
Explainability problem	Inability to explain a model's decision; hurts trust/audit; use SHAP/LIME
Telemetry data privacy	Sending telemetry to cloud AI is third-party data sharing needing controls
AI-enabled attack vs attack on AI	Using AI as a weapon (D3) vs targeting a model (D2)
Anomaly detection vs threat hunting	Automated continuous flagging vs human hypothesis-driven investigation
SOAR vs AI copilot	Automated playbooks vs human language assistance
```

---

*Week 4 deck (Domain 3 = 24%). Emphasize the limitations cards — the exam tests failure modes heavily. Log weak cards in `99-PROGRESS-TRACKER.md`.*
