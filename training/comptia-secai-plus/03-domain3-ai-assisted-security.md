# Domain 3 — AI-Assisted Security

**Exam domain:** 3 of 4 | **Weight:** 24% (~14 questions)
**Study time:** 8–10 hours reading + 2 hours workflow design
**Week:** 4 (complete Domain 2 first — many threats referenced here are defined there)

> This domain covers AI as a practitioner's tool: using AI to detect threats, triage alerts, hunt threats, prioritize vulnerabilities, scan code, and automate response. The exam is workflow-oriented here — know not just what the tool does but where it fits in the analyst's process and what its failure modes are.

---

## Learning Objectives Checklist

- [ ] Explain how ML-based anomaly detection differs from signature-based detection and when to use each
- [ ] Describe UEBA: what it monitors, what models it uses, and what threats it surfaces
- [ ] Explain how AI reduces false positives in network and endpoint detection
- [ ] Map the AI-assisted SOC workflow: alert ingestion, enrichment, triage, response, feedback loop
- [ ] Distinguish SOAR from AI copilots and explain how they interact
- [ ] Describe AI's role in threat intelligence: correlation, pattern extraction, indicator enrichment
- [ ] Explain AI-assisted vulnerability prioritization beyond raw CVSS scores
- [ ] Describe AI applications in offensive security: AI-assisted recon, fuzzing, and exploit assistance
- [ ] Map AI integration points in a DevSecOps pipeline: SAST, DAST, SCA, IaC scanning, secrets detection, secure code generation
- [ ] Explain how AI detects phishing and fraud at scale
- [ ] Identify AI security **tool form factors** (IDE/browser/CLI plug-ins, chatbots, personal assistants, **MCP servers**) and name the 3.1 use cases (incl. translation, threat modeling, linting)
- [ ] Describe **AI-enabled attacks** (3.2): deepfakes, adversarial networks, obfuscation/polymorphic malware, automated data correlation, automated attack generation, honeypots, DDoS — and distinguish them from attacks *on* AI (Domain 2)
- [ ] Describe **AI automation scenarios** (3.3): low/no-code scripting, document synthesis, IR ticket mgmt, change-mgmt approvals, CI/CD hooks, unit/regression/model testing, automated deploy/rollback
- [ ] Articulate all major limitations and risks of defensive AI: hallucination, automation bias, adversarial evasion, bias, explainability, data privacy

---

## Section 1 — AI/ML for Threat Detection

### The Fundamental Problem AI Addresses

Traditional signature-based detection is reactive: it only catches threats whose exact signatures have been written. Zero-day attacks, polymorphic malware, and living-off-the-land techniques evade signatures by design. Volume also breaks human-scale detection: a mid-sized enterprise generates millions of events per day.

AI addresses both: it finds **patterns in large data volumes without pre-written rules** and can **detect anomalies** — deviations from established baseline behavior — that have no prior signature.

### Signature-Based vs. Anomaly-Based Detection

| Dimension | Signature-Based | Anomaly-Based (AI/ML) |
|---|---|---|
| Detection mechanism | Matches known patterns/IOCs | Detects deviation from learned baseline |
| Zero-day coverage | None (signature must pre-exist) | Can detect novel attacks if behavior deviates |
| False positive rate | Low (specific matches) | Can be high until baseline matures |
| False negative rate | High for unknowns | Lower for novel threats; depends on drift |
| Evasion method | Modify payload to avoid pattern | Stay within the learned "normal" range |
| Tuning required | Signature updates | Baseline calibration, threshold tuning |
| Best for | Known malware, CVE exploits, IOC matching | Insider threats, novel malware, lateral movement |

**Hybrid approach:** most mature SOCs layer both — signatures for speed and precision on known threats, AI/ML anomaly detection as a second layer for behavioral and novel threats.

### Anomaly Detection Methods

**Statistical anomaly detection:** Establishes a statistical baseline (mean, standard deviation) of normal behavior. Alerts when observed metrics exceed a threshold (e.g., more than 3 standard deviations above the baseline byte-out rate).

**ML-based anomaly detection:** Trains a model (isolation forest, autoencoder, one-class SVM) on normal data. At inference time, scores new data against the learned distribution. Isolation forest isolates anomalies by randomly partitioning feature space — anomalies require fewer partitions. Autoencoders reconstruct normal data well; anomalies have high reconstruction error.

**Deep learning anomaly detection:** Recurrent neural networks (RNNs) or transformer-based sequence models detect temporal anomalies in time-series data (e.g., an RNN that learns typical login sequences and flags unusual patterns).

### User and Entity Behavior Analytics (UEBA)

**UEBA** applies ML to logs from identity systems, HR systems, endpoints, and network infrastructure to build behavioral baselines for individual users, devices, and entities, then score deviations.

What UEBA monitors:
- Login times, locations, and frequency
- Data access volumes and patterns (which resources, at what hours)
- Privileged account usage
- File access and download volume
- Email forwarding rules and external sharing
- Application and process execution patterns

Threats UEBA surfaces:
- **Insider threats:** employees exfiltrating data before resignation
- **Compromised credentials:** attacker using a stolen account but behaving anomalously
- **Lateral movement:** an account accessing systems it never historically accessed
- **Privilege escalation:** sudden access to high-value resources

**Peer-group analysis:** UEBA compares users to their **peer groups** (same department, same role) rather than only to their own historical baseline. A finance user who suddenly behaves like a developer (accessing code repositories) is anomalous even if they have no personal history to compare against.

**Risk scoring:** UEBA produces a continuous risk score per entity rather than a binary alert. High scores trigger investigation. This reduces alert volume while maintaining coverage.

### AI in Network Detection (NDR / NTA)

**Network Detection and Response (NDR)** applies ML to network traffic metadata (flow records, PCAP headers, DNS, TLS metadata) to detect threats without decrypting payloads.

Key AI applications in NDR:
- **Encrypted traffic analysis:** classifying protocol, application, or threat category from TLS metadata (SNI, certificate, traffic timing patterns) without decrypting — protects privacy while maintaining visibility
- **C2 communication detection:** detecting command-and-control beaconing patterns (periodic connections at regular intervals, domain generation algorithm [DGA] domains, unusual byte ratios)
- **Data exfiltration detection:** detecting large outbound transfers, slow-and-low exfiltration, DNS tunneling (anomalously large DNS query payloads)
- **Lateral movement detection:** identifying unusual east-west traffic patterns (SMB to hosts the source has never communicated with, credential spray patterns)

### AI in Endpoint Detection (EDR / XDR)

**Endpoint Detection and Response (EDR)** collects telemetry from endpoints (process creation, file writes, registry changes, network connections) and applies ML to detect malicious activity.

Key AI applications in EDR:
- **Process behavior classification:** ML models that score process behavior in real time — is powershell.exe spawned by Word normal? (No — this is a macro execution indicator)
- **Malware classification:** static and dynamic analysis at scale — file features (PE header structure, entropy, API call patterns) fed to a classifier
- **Ransomware early detection:** detecting file-encryption patterns (rapid sequential file writes, entropy increase in file content) before significant damage
- **Living-off-the-land (LotL) detection:** detecting misuse of legitimate system tools (certutil, mshta, wscript) that evade traditional AV

**XDR (Extended Detection and Response):** Correlates signals across endpoint, network, identity, email, and cloud telemetry in a unified ML-driven detection platform. Reduces alert fragmentation.

### AI and False Positive Reduction

Alert fatigue — the SOC being overwhelmed by false positives — is one of the most damaging operational problems in security. AI addresses it through:

- **Correlation:** grouping related alerts into a single incident rather than firing one alert per event
- **Confidence scoring:** attaching a probability or confidence score so analysts can prioritize high-confidence alerts
- **Suppression models:** learning which alert patterns are consistently false positives for the specific environment and suppressing future instances
- **Contextualization:** enriching alerts with asset criticality, recent threat intel, and user risk score so analysts can assess priority without manual lookup

> **Exam tip:** Alert fatigue and false positive reduction are exam favorites. Know that AI does not eliminate false positives — it reduces them. A poorly tuned AI detector can generate more false positives than it eliminates.

---

## Section 2 — AI in the Security Operations Center (SOC)

### The AI-Assisted SOC Workflow

```
Event Sources → SIEM Ingestion → AI Enrichment & Triage → Analyst Review → Response → Feedback
     |                |                   |                      |              |          |
 Endpoint,       Normalization,      Risk scoring,          Investigate,    SOAR or    Label
 Network,        Correlation,        Contextualization,     Validate,       Manual,    correct/
 Identity,       Deduplication       Summarization,         Escalate        Contain     incorrect
 Cloud                               Priority ranking                                (retraining)
```

### Alert Triage and Enrichment

AI performs the initial work that previously required an analyst for every alert:

**Automated enrichment:** querying threat intel feeds, IP reputation databases, WHOIS, VirusTotal, and internal asset inventories to add context to each alert before a human sees it.

**Risk-based prioritization:** ranking the alert queue by estimated severity, confidence, and asset criticality rather than time of arrival. A low-confidence alert against a non-critical printer ranks below a high-confidence alert against an identity provider.

**Alert summarization:** using an LLM to produce a natural-language summary of the raw technical event data, enabling a Tier 1 analyst to understand the alert without reading hundreds of log lines.

**Deduplication and correlation:** identifying that 200 alerts are actually one attacker performing credential stuffing — presenting one incident rather than 200 tickets.

### Generative AI Copilots in the SOC

LLM-based copilots (Microsoft Copilot for Security, Google Chronicle AI, Splunk AI Assistant, CrowdStrike Charlotte AI) assist analysts with:

- **Natural-language threat hunting:** "Show me all processes that spawned cmd.exe in the last 24 hours on finance workstations" — the copilot converts this to a query (KQL, SPL, SQL) without the analyst knowing the query language
- **Incident summarization:** auto-generating the timeline and summary for an incident ticket
- **Explanation of detections:** "Why did this alert fire?" translated from raw logic to plain English
- **Playbook recommendation:** suggesting the appropriate response playbook based on detection type
- **Report drafting:** generating draft executive summaries and post-incident reports

**Key limitation:** copilot outputs must be analyst-verified. Hallucination in a SOC context (a confident but wrong threat summary, a fabricated IOC) can cause an analyst to close a real incident or over-respond to a benign event.

### SOAR and AI-Driven Automation

**SOAR (Security Orchestration, Automation, and Response)** platforms (Splunk SOAR/Phantom, Palo Alto XSOAR, Microsoft Sentinel SOAR) automate response playbooks triggered by detection events.

AI enhances SOAR in several ways:

| SOAR Capability | How AI Enhances It |
|---|---|
| Playbook selection | AI recommends or auto-selects the appropriate playbook based on incident classification |
| Decision points | ML models make triage decisions (isolate host? block IP?) that previously required manual gates |
| Anomalous playbook behavior | AI monitors playbook execution and flags unexpected paths |
| Playbook generation | LLMs draft new playbooks from natural-language descriptions |
| Feedback loop | Analyst verdicts feed back into the ML model to improve future triage accuracy |

**Human-in-the-loop vs. fully automated response:** The exam distinguishes these. Fully automated response (block, isolate, quarantine without human approval) is appropriate for high-confidence, high-speed threats (ransomware detonation, active C2). Human-in-the-loop is appropriate for ambiguous alerts and irreversible actions. **Automation bias** — the danger of over-trusting automated decisions — is a core exam topic (see Section 7).

---

## Section 3 — AI for Threat Intelligence

### Threat Intelligence at Scale

Traditional threat intelligence is manually curated — analysts read reports, extract IOCs, and upload them. This process cannot keep pace with the volume of threat actor activity, open-source reporting, dark web chatter, and technical feeds.

AI applications in threat intelligence:

**Automated IOC extraction:** NLP models extract indicators (IPs, domains, hashes, CVEs, TTPs) from unstructured text — threat reports, blog posts, forum posts, security advisories — at machine speed.

**TTPs mapping:** NLP + classification models map extracted behaviors to MITRE ATT&CK techniques automatically, building structured threat profiles from unstructured reporting.

**Attribution clustering:** ML groups malware samples, infrastructure patterns, and TTPs into **threat actor clusters** without requiring prior knowledge of the actor. Overlapping infrastructure, similar code, and behavioral patterns cluster together.

**Dark web monitoring:** AI crawls and indexes dark web markets and forums, applying NLP to detect references to specific organizations, leaked credentials, or planned attacks.

**Predictive threat intel:** ML models trained on historical attack patterns and CVE exploitation data attempt to predict which vulnerabilities are most likely to be exploited next (connects to vuln management — Section 4).

**Correlation with internal telemetry:** matching external threat intel with internal logs to identify whether a known-malicious IOC has appeared in the environment — automated "have we seen this?" at scale.

### MITRE ATT&CK and AI

The MITRE ATT&CK framework is the structured vocabulary for threat behaviors. AI uses ATT&CK as:
- A **classification taxonomy** for alert-to-TTP mapping
- A **gap analysis tool** — which ATT&CK techniques does the organization have no detection for?
- A **red team planning framework** — AI-assisted adversary emulation (covered in Section 5)

---

## Section 4 — AI in Vulnerability Management

### The False Promise of Raw CVSS

CVSS (Common Vulnerability Scoring System) scores rate vulnerability severity on a 0–10 scale. The problem: there are hundreds of thousands of known CVEs. A CVSS-9.8 vulnerability in software the organization does not run is less urgent than a CVSS-6.5 vulnerability in an internet-facing, unpatched, actively-exploited application server.

AI-assisted vulnerability prioritization considers:

| Signal | What It Adds |
|---|---|
| CVSS base score | Inherent severity |
| EPSS score | Empirical probability that the CVE is exploited in the wild within 30 days |
| CISA KEV (Known Exploited Vulnerabilities) | Confirmed exploitation by threat actors — top priority signal |
| Asset criticality | Is the vulnerable asset internet-facing? Does it hold PII? Is it a DC? |
| Exploit availability | Is a working PoC or Metasploit module published? |
| Threat actor targeting | Do known APTs targeting this org use this vulnerability? |
| Compensating controls | Is the vulnerable service behind a WAF or network-isolated? |

**EPSS (Exploit Prediction Scoring System):** An ML model maintained by FIRST that predicts the probability of exploitation within 30 days using features including CVE metadata, public exploit availability, and historical exploitation patterns. EPSS + CVSS together dramatically sharpen prioritization.

AI in patch management:
- Predicts **patch regression risk** (will this patch break something?)
- Correlates vulnerability scans with CMDB data to identify affected hosts at scale
- Generates natural-language remediation guidance tied to the specific environment
- Prioritizes patch sequencing to maximize risk reduction per unit of downtime

### AI-Assisted Penetration Testing and Red Teaming

AI assists human testers in every phase of an engagement:

**Reconnaissance:** AI aggregates OSINT (open-source intelligence) from DNS, certificate transparency logs, LinkedIn, GitHub, Shodan, VirusTotal — tools like Maltego + AI plugins automate the correlation that previously took days. LLMs can summarize organizational attack surface from collected data.

**Vulnerability identification / fuzzing:** AI-guided fuzzing (AI-driven fuzzing tools like Google OSS-Fuzz with ML guidance) intelligently mutates inputs to maximize code coverage rather than random mutation, finding edge cases faster.

**Exploit assistance:** LLMs assist in writing proof-of-concept code, explaining vulnerability mechanics, and adapting known exploits to target-specific contexts. This accelerates testing but also lowers the barrier for less-skilled attackers (dual-use concern — Domain 2).

**Report generation:** LLMs draft findings narratives and executive summaries, dramatically reducing post-engagement reporting time.

> **Exam tip:** The exam tests whether AI-assisted offensive tools are a concern for defenders — they are. AI-generated spear-phishing, AI-assisted exploit development, and AI recon automation are threat-actor capabilities that defenders must anticipate.

---

## Section 5 — AI in DevSecOps Pipelines

### Shift-Left Security and AI

"Shift left" means finding and fixing security issues earlier in the development lifecycle, when they are cheaper to fix. AI accelerates shift-left by automating security analysis steps that previously required dedicated security engineers.

### AI Integration Points in the Pipeline

```
Code Write → Commit → Build → Test → Stage → Deploy → Monitor
    |           |        |       |       |        |        |
   AI IDE    Secrets   SAST   DAST   IaC   Container  Runtime
  Copilot   Detection  Scan   Scan  Scan    Scan    monitoring
```

### AI-Augmented SAST (Static Application Security Testing)

Traditional SAST: rule-based pattern matching for known vulnerable code patterns. Generates many false positives; misses novel vulnerability classes.

AI-augmented SAST:
- ML models trained on large vulnerability corpora (NVD, code commit histories, bug bounty findings) classify code paths as vulnerable or benign
- Reduces false positive rate vs. rule-only SAST
- Semantic understanding of code (context-aware analysis) — can detect SQL injection patterns even when the query is built across multiple functions
- Tools: GitHub Advanced Security (CodeQL + AI), Semgrep with AI, Snyk Code

**Key limitation:** AI SAST can still hallucinate — flag code as vulnerable when it is not, or miss vulnerabilities that require deep data-flow understanding.

### AI-Augmented DAST (Dynamic Application Security Testing)

Traditional DAST: automated web application scanning (crawl, probe, analyze responses). Prone to missing business-logic flaws.

AI-augmented DAST:
- ML-guided crawling to discover deeper application states that simple crawlers miss
- Intelligent fuzzing of API parameters to find injection points
- Anomaly detection on responses to identify unusual server behavior that may indicate a vulnerability
- AI-generated test cases based on API specifications (OpenAPI/Swagger) to achieve better coverage

### Comparison: AI-SAST vs AI-DAST

| Dimension | AI-SAST | AI-DAST |
|---|---|---|
| When it runs | Against source code (pre-build) | Against running application (post-deploy or in test env) |
| What it needs | Source code access | Running application with network access |
| What it finds | Code-level flaws, logic errors in source | Runtime flaws, auth bypasses, injection in live app |
| False positive risk | Higher (code may not be reachable) | Lower (observed in running state) |
| False negative risk | Misses runtime-only issues | May miss code paths not exercised |
| Phase | Development / commit | Test / staging |

### Secrets Detection

AI-enhanced secrets scanning detects **credentials, API keys, tokens, certificates** accidentally committed to source control or configuration files. Beyond regex patterns (which catch common key formats), ML models detect high-entropy strings and context-sensitive patterns that may be secrets even when they do not match known formats.

Tools: GitGuardian, Trufflehog, GitHub Secret Scanning (AI-enhanced), Semgrep Secrets.

Pipeline integration: secrets scanners run as a **pre-commit hook** (blocks commit if secrets detected) and as a **CI pipeline gate** (blocks pull request merge).

### IaC (Infrastructure as Code) Security Scanning

AI analyzes Terraform, CloudFormation, Kubernetes YAML, Ansible, Helm charts, and Bicep files for:
- Misconfiguration patterns (S3 bucket public access, security group 0.0.0.0/0, privilege escalation via IAM, unencrypted storage volumes)
- Drift from security baselines and CIS Benchmarks
- Dependency vulnerabilities in referenced container images

AI goes beyond rule matching by understanding **configuration relationships** — a public subnet plus a misconfigured routing table plus an overly permissive security group together create an exposure even if each individual rule is acceptable.

Tools: Checkov (with AI), Snyk IaC, Wiz, Bridgecrew.

### AI-Assisted Secure Code Generation and Review

LLM coding assistants (GitHub Copilot, Amazon CodeWhisperer / Q Developer, Google Gemini Code Assist) generate code from natural-language prompts. Security considerations:

**Risk of AI-generated insecure code:**
- LLMs trained on public code corpora inherit insecure coding patterns present in that data
- AI may generate SQL queries without parameterization, shell commands with unsanitized input, or cryptographic implementations with known weaknesses
- "Confidently wrong" code: the LLM produces plausible-looking code that has subtle security flaws

**Secure code generation review workflow:**
1. Developer prompts the AI copilot
2. Generated code is immediately submitted to AI-augmented SAST
3. Security gate flags issues before the developer commits
4. Developer reviews flagged items — not a blind accept
5. Commit triggers secrets scanning and SCA (Software Composition Analysis) for dependency vulnerabilities

SCA (Software Composition Analysis) with AI: AI classifies third-party libraries, scores transitive dependency risk, and prioritizes which vulnerable dependency update is most urgent given the application's actual usage of the affected component.

---

## Section 6 — AI for Phishing and Fraud Detection

### AI-Powered Phishing Detection

Traditional phishing filters rely on URL blacklists and keyword rules. AI-based phishing detection:

**Email analysis features used by AI models:**
- Sender reputation and domain registration age
- Header analysis (SPF/DKIM/DMARC alignment)
- Linguistic pattern analysis: urgency language, impersonation signals, grammatical patterns characteristic of AI-generated phishing
- URL analysis: domain squatting detection, redirect chain analysis, lookalike domain scoring
- Attachment analysis: sandbox execution + ML malware classification
- Behavioral: does this email pattern match prior phishing campaigns targeting this organization?

**Image and brand impersonation detection:** Vision models detect when an email contains a logo or UI element that impersonates a trusted brand (Microsoft, DocuSign, bank logos), flagging it even when the URL and text are novel.

**The GenAI phishing problem:** LLMs produce highly fluent, personalized phishing emails that eliminate the grammar errors that traditional filters relied on. AI-generated spear phishing (using OSINT to personalize each email) is now accessible at scale. This is a threat actor capability that AI-based defenses must counter — but with a time lag. Defenders must not rely on grammar errors as an indicator.

### AI in Fraud Detection

Financial fraud detection was one of the first production uses of ML in security:

**Transaction anomaly detection:** ML models score each transaction against a behavioral baseline for the account (normal transaction amounts, merchants, geographies, timing). Outliers are held for step-up authentication or declined.

**Graph analytics for fraud rings:** Graph neural networks (GNNs) detect interconnected fraudulent accounts, synthetic identity fraud, and money mule networks by analyzing relationships between accounts, devices, and transactions.

**Account takeover (ATO) detection:** ML detects behavioral biometrics anomalies (typing rhythm, mouse movement, device fingerprint changes) that indicate a stolen credential being used by a new actor.

---

## Section 6A — AI Security Tooling: Form Factors and Use Cases (Objective 3.1)

Objective 3.1 expects you to recognize the *form factors* AI security tools take and the *use cases* they serve — not just the detection concepts above.

### Tool form factors (how AI reaches the practitioner)

| Form factor | What it is | Security use / caution |
|---|---|---|
| **IDE plug-ins** | AI inside the developer's editor (Copilot, Q Developer) | Secure code suggestions + inline scanning; caution: insecure generated code, source/secrets sent to vendor |
| **Browser plug-ins** | AI in the browser (summarize page, analyze content) | Quick research/triage; caution: page content (incl. sensitive) sent to the model; indirect-injection surface |
| **CLI plug-ins** | AI in the terminal (explain command, generate script) | Fast ops/IR scripting; caution: can generate destructive commands — review before run |
| **Chatbots** | Conversational AI interfaces (security copilots) | Q&A, hunting, summarization; caution: hallucination, must verify |
| **Personal assistants** | Agentic assistants that take actions across tools | Workflow automation; caution: excessive agency, needs least-privilege + HITL (Domain 2) |
| **MCP servers** | **Model Context Protocol** servers — standardized connectors that expose tools/data/resources to an AI model/agent | Let a copilot/agent securely call SIEM, ticketing, threat-intel, etc.; caution: an MCP server is a privileged integration — authenticate it, scope it, and treat tool results as untrusted (indirect-injection vector) |

> **Exam tip — MCP servers:** the **Model Context Protocol** is the current standard for connecting AI agents to external tools/data. Recognize MCP as an *integration/tooling* mechanism, and remember each MCP connection is an access-control and prompt-injection surface (ties to Domain 2 integration abuse).

### Use cases CompTIA names explicitly

Beyond detection/triage already covered: **signature matching**, **code quality / linting**, **vulnerability analysis**, **automated penetration testing**, **anomaly detection**, **pattern recognition**, **incident management**, **threat modeling** (AI drafting threat models / attack trees from an architecture), **fraud detection**, **translation** (normalizing multilingual threat intel, phishing, or analyst notes into a working language), and **summarization** (alerts, incidents, reports). If a scenario asks "which AI use case applies," match to this list.

---

## Section 6B — AI-Enabled Attacks (Objective 3.2)

The flip side of AI-assisted *defense* is AI-assisted *offense*. Objective 3.2 expects you to recognize how adversaries weaponize AI. (Attacks *on* AI models live in Domain 2; this is attackers *using* AI as a tool.)

- **Deepfakes:** synthetic AI-generated audio/video/images used for **impersonation** (CEO-voice wire-fraud, fake video calls), **misinformation/disinformation** (fabricated events), and bypassing voice/face biometrics. Defense: liveness detection, deepfake-detection models, call-back verification, out-of-band confirmation for high-value requests.
- **Adversarial (generative) networks:** GANs used to generate adversarial examples, synthetic identities, and realistic fake content at scale.
- **Reconnaissance:** AI-accelerated OSINT aggregation and attack-surface mapping (covered in Section 4).
- **Social engineering:** GenAI mass-producing fluent, personalized phishing/spear-phishing/vishing (Section 6) — grammar errors are no longer a reliable signal.
- **Obfuscation:** AI used to obfuscate/mutate malware and payloads, generate **polymorphic/metamorphic** malware that changes its signature each build, and rewrite code to evade signature and static detection.
- **Automated data correlation:** AI correlating breach dumps, OSINT, and leaked credentials to de-anonymize targets and build victim profiles at scale.
- **Automated attack generation:** AI assisting (or automating) **vulnerability discovery**, **payload generation**, and **malware creation** — lowering the skill barrier and increasing attack speed/volume.
- **Honeypots:** dual-use — defenders use AI to generate convincing **deceptive honeypots/honeytokens** that engage and profile attackers; attackers use AI to *detect and evade* honeypots. Know both directions.
- **DDoS:** AI used to orchestrate adaptive, distributed denial-of-service (intelligently shifting tactics to evade mitigation) and to optimize botnet behavior.

> **Exam tip:** distinguish **AI-enabled attacks (3.2)** — attacker *uses* AI as a weapon (deepfake, polymorphic malware, automated exploit gen) — from **attacks on AI (Domain 2)** — attacker *targets* a model (prompt injection, poisoning, extraction). The verb tells you the domain.

---

## Section 6C — AI Automation Scenarios (Objective 3.3)

Objective 3.3 covers AI/agents *automating* security and delivery workflows end-to-end.

- **Low-code / no-code scripting:** AI generates scripts, queries, and integration glue from natural language, letting non-developers automate tasks (caution: ungoverned "citizen automation" / shadow AI).
- **Document synthesis:** auto-drafting reports, runbooks, policies, executive summaries, and post-incident reviews from source data.
- **IR ticket management:** auto-creating, enriching, summarizing, routing, and closing incident tickets; maintaining the incident timeline.
- **Change-management approvals & deployment/rollback:** AI assists change workflows — risk-scoring proposed changes, drafting change records, recommending approval/denial, and triggering **automated deployment and rollback** when health checks or security gates fail.
- **AI agents and CI/CD hooks:** agents wired into pipeline hooks to run security gates, open PRs/fixes, and gate promotion automatically.
- **Code scanning & SCA:** automated SAST/DAST/secrets/SCA gates in the pipeline (Section 5).
- **Unit / regression / model testing:** AI generates and runs unit and regression tests, and — for ML systems — **model testing** (evaluation, drift, safety/security regression) on each update.
- **Automated deploy/rollback:** promotion to production and automatic rollback driven by AI-evaluated signals, with the governance caution that high-impact automated actions still need guardrails and HITL for irreversible steps.

> **Exam tip:** automation scenarios reward the same judgment as Domain 2's HITL discussion — full automation suits high-confidence/reversible actions; **change approvals, production deploys, and rollbacks of critical systems warrant a human gate**. Watch for over-automation as the wrong answer's trap.

---

## Section 7 — Limitations and Risks of Defensive AI

This section is high-yield for the exam. The exam will present scenarios where the question is not "what can AI do" but "what can go wrong."

### Hallucination

LLMs generate plausible but factually incorrect output with apparent confidence. In a security context:

- An AI SOC copilot summarizes an alert and states "this IP is a known Lazarus Group C2 server" when no such intel exists
- An AI vulnerability scanner claims a specific CVE is unpatched on a host when the host was patched three days ago
- A threat hunting query auto-generated by an LLM is syntactically valid but logically incorrect — hunting for the wrong thing

**Mitigation:** Grounding AI outputs in authoritative data sources (threat intel feeds, CMDBs, scan results — not the LLM's parametric memory), implementing analyst review of all AI-generated findings before action, and measuring hallucination rate in model evaluations.

### Automation Bias (Over-Trust)

**Automation bias** is the human tendency to over-rely on automated system outputs and under-apply critical judgment. In a SOC context: an analyst accepts an AI triage verdict without reviewing the evidence because "the system said it was benign."

This is the **silent killer of AI-assisted SOC effectiveness.** The alert that matters most is the one where the AI is wrong and the analyst trusts it.

**Manifestations:**
- Closing alerts as benign because the AI scored them low-risk without verifying
- Blocking resources without verifying because the AI scored them malicious
- Approving AI-generated incident reports without checking the underlying evidence

**Mitigation:** Design workflows that require analysts to make explicit decisions supported by (not replaced by) AI recommendations. Log and review instances where humans override AI. Measure analyst agreement rates — if analysts agree with AI 99% of the time, investigate whether they are actually reviewing or rubber-stamping.

### Adversarial Evasion of AI Detectors

ML-based detectors have their own attack surface. Attackers who know a defender uses ML detection can craft inputs that evade it (covered in depth in Domain 2):

- **Adversarial examples:** slightly perturbing malware to change the model's classification from malicious to benign, without changing the malware's functionality
- **Model extraction + evasion:** extracting the defender's detection model by querying it, building a surrogate, and then using the surrogate to craft samples that evade the original
- **Staying in baseline:** conducting malicious activity at rates and patterns that remain within the UEBA model's learned normal range, never triggering anomaly scores

Security implication: AI detectors should not be the sole control layer. Defense-in-depth with non-ML controls (network segmentation, MFA, EDR + signatures) prevents an adversary from evading all layers simultaneously.

### Bias in Security AI

ML models inherit biases from their training data. In security:

- A malware classifier trained primarily on Windows PE malware will have poor performance on Linux ELF binaries or macOS Mach-O binaries
- A UEBA model trained on a pre-COVID office-hours baseline will flag legitimate remote work patterns as anomalous
- An anomaly detector trained on only one organization's traffic will have high false positives when that organization changes its environment (cloud migration, merger)

**Bias types relevant to security AI:**
- **Selection bias:** training data does not represent the deployment environment
- **Temporal bias:** model trained on old data encounters a changed threat landscape
- **Label bias:** historical analyst verdicts used as training labels embed the errors and prejudices of prior analysts
- **Imbalance bias:** security datasets are highly imbalanced (far more benign events than attacks), causing models to be biased toward the majority class

### Explainability and the Black Box Problem

Many high-performing ML models (deep neural networks, ensemble methods like gradient boosting) are not interpretable. An analyst cannot look inside and understand why the model scored a specific alert as high-risk.

Security implications:
- **Analyst trust:** analysts are less likely to trust (and more likely to ignore) verdicts they cannot understand
- **Audit and compliance:** regulators and auditors may require explanation of automated security decisions
- **Root cause analysis:** when the AI is wrong, lack of explainability makes it hard to diagnose and fix
- **Adversarial robustness:** opaque models are harder to audit for adversarial vulnerabilities

**Explainability techniques:** SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) provide post-hoc explanations that highlight which features drove a specific prediction. These are approximations, not ground truth, but improve analyst trust and debugging.

### Data Privacy of Security Telemetry

AI-powered security tools typically require sending telemetry to cloud-based ML inference engines. This creates tension:

**What gets sent:** network packet metadata, endpoint process trees, user activity logs, email content, file contents, code snippets.

**Privacy risks:**
- Telemetry may contain PII (employee names, email contents, health data) sent to a third-party AI vendor
- Code sent to AI code scanning may include proprietary algorithms, credentials, or trade secrets
- AI training on customer telemetry can cause one customer's data to surface in another customer's AI responses (cross-tenant leakage)

**Mitigations:** data residency controls, telemetry anonymization before sending, contractual data processing agreements with AI vendors, on-premises or private cloud inference for sensitive workloads, reviewing vendor data retention and training data policies.

> **Exam tip:** The data privacy of telemetry section is tested at the intersection of Domain 3 and Domain 4. Know that sending endpoint telemetry to a cloud AI product is a third-party data sharing event requiring vendor assessment and privacy controls.

### Summary Table: AI Security Tool Limitations

| Limitation | Description | Mitigation |
|---|---|---|
| Hallucination | Confident, incorrect AI output | Ground in authoritative data; require analyst verification |
| Automation bias | Humans over-trust AI verdicts without review | Design workflows requiring explicit human decision; audit override rates |
| Adversarial evasion | Attackers craft inputs to evade ML detectors | Defense-in-depth; do not rely solely on AI detection |
| Bias / drift | Model trained on stale or unrepresentative data | Continuous monitoring; retrain on current data; diverse training sets |
| Black box / explainability | Cannot explain why AI made a decision | SHAP/LIME explanations; prefer explainable models for high-stakes decisions |
| Data privacy | Security telemetry contains PII and IP sent to AI vendors | Data minimization; vendor DPA review; on-prem inference where appropriate |
| False positive / negative | AI produces incorrect classifications | Tune thresholds; feedback loops; dual-layer detection (signature + AI) |

---

## Section 8 — Commonly Confused Concepts — Exam Tips

**SOAR vs. AI copilot:** SOAR executes automated playbooks (orchestration + automation). An AI copilot assists the human analyst with language tasks (query writing, summarization, recommendations). They often co-exist in the same platform but do different things.

**NDR vs. EDR vs. XDR:** NDR = network traffic analysis. EDR = endpoint telemetry + detection/response. XDR = cross-telemetry correlation (endpoint + network + identity + cloud). AI is present in all three, but each has different visibility and different blind spots.

**SAST vs. DAST vs. SCA:** SAST analyzes source code (static, before it runs). DAST probes a running application (dynamic, at runtime). SCA analyzes third-party open-source dependencies for known vulnerabilities. All three are AI-augmented and should be stages in a CI/CD pipeline, not just point-in-time scans.

**CVSS vs. EPSS:** CVSS rates inherent severity (0–10, doesn't change much). EPSS predicts exploitation probability within 30 days (0–1.0, changes as exploitation data accumulates). High CVSS + high EPSS + asset criticality = fix immediately. High CVSS + low EPSS + internal-only system = deprioritize.

**Anomaly detection vs. threat hunting:** Anomaly detection is automated and continuous — the AI flags deviations. Threat hunting is human-led, hypothesis-driven investigation using AI as a tool to search the data. They are complementary. The AI surfaces the anomalies; the hunter investigates them.

**Automation bias vs. hallucination:** Hallucination is an AI error (the model generates wrong output). Automation bias is a human error (the analyst trusts the wrong output without checking). Both result in the wrong security decision — but the root cause is different.

**Adversarial evasion vs. data poisoning:** Evasion happens at inference time — craft an input to fool the running model. Poisoning happens at training time — corrupt the training data so the model learns the wrong thing permanently. Evasion is opportunistic and reversible (one session). Poisoning is strategic and persistent (affects all future inferences).

---

## Practice Questions — Domain 3

**Instructions:** Select the single best answer unless instructed otherwise. Time limit: ~1 minute per question.

---

**Q1.** A SOC analyst is evaluating two intrusion detection approaches. System A fires an alert for every network packet that matches a rule in its signature database. System B builds a baseline of normal traffic patterns over 30 days and alerts when observed traffic deviates significantly from that baseline. Which statement BEST contrasts these systems?

A) System A requires more compute; System B is rule-based
B) System A catches zero-day attacks better; System B catches known malware better
C) System A has lower false positives for known threats; System B can detect novel attack patterns
D) System A uses supervised learning; System B uses unsupervised learning

---

**Q2.** A company deploys a UEBA platform that flags a finance manager for downloading an unusually large volume of HR data at 11:30 PM on a Friday. The following Monday, the manager submits a resignation letter. Which threat type did the UEBA most likely detect?

A) External adversary using a credential-stuffing attack
B) Insider threat — data exfiltration prior to departure
C) Ransomware reconnaissance phase
D) An advanced persistent threat establishing lateral movement

---

**Q3.** An AI SOC copilot automatically triages incoming alerts and labels 85% of them as "benign, close" without analyst review. Analysts accept the verdicts and close the tickets. Two weeks later, the organization discovers an ongoing intrusion that generated 47 alerts, all labeled benign by the AI. Which failure mode BEST explains what happened?

A) Hallucination — the AI generated incorrect threat intel about the attacker
B) Automation bias — analysts accepted AI verdicts without independent verification
C) Adversarial evasion — the attacker crafted inputs to avoid network detection
D) Bias — the AI model was trained on biased threat data

---

**Q4.** Which vulnerability prioritization approach would produce the MOST operationally useful ranking for a mid-size organization with a three-person patch team?

A) Sort all vulnerabilities by CVSS base score descending and patch the top 20 each week
B) Patch only CISA KEV entries, regardless of CVSS score
C) Combine CVSS, EPSS score, CISA KEV status, asset criticality, and existing compensating controls
D) Use a random sample of high-severity CVEs to avoid systematic blind spots

---

**Q5.** A developer uses an AI coding assistant (LLM copilot) to generate a database query function. The generated code does not use parameterized queries. The code passes the automated unit tests and is merged. Which control would have been MOST effective at catching this before merge?

A) Runtime anomaly detection on database queries in production
B) AI-augmented SAST integrated into the CI pipeline as a merge gate
C) Network intrusion detection system scanning SQL traffic
D) Training the developer on secure coding principles

---

**Q6.** A threat intelligence team wants to automatically extract MITRE ATT&CK technique IDs from hundreds of daily threat reports, blog posts, and vendor advisories. Which AI capability is MOST applicable?

A) Diffusion model generating synthetic threat reports for training purposes
B) Reinforcement learning agent exploring the MITRE ATT&CK matrix
C) NLP classification model mapping extracted behaviors to ATT&CK technique taxonomy
D) Vector database storing historical IOCs for nearest-neighbor search

---

**Q7.** An attacker knows that a target organization's email security gateway uses an ML model trained to detect phishing based on linguistic patterns, urgency language, and grammatical errors. The attacker uses a GPT-4-class LLM to generate highly fluent, personalized phishing emails. What is the MOST accurate characterization of this technique?

A) Model extraction — the attacker is stealing the email gateway's model
B) Adversarial ML — the attacker is crafting inputs to evade an ML-based detector
C) Prompt injection — the attacker is injecting instructions into the email gateway's LLM
D) Data poisoning — the attacker is corrupting the email gateway's training data

---

**Q8.** A security engineer is asked to explain why the AI-based malware detection system cannot explain why it classified a sample as malicious. The engineer responds that the model is a deep neural network and its decision-making process is not directly interpretable. Which term describes this challenge?

A) Automation bias
B) Model drift
C) The black box / explainability problem
D) Adversarial robustness

---

**Q9.** An organization sends full endpoint process telemetry, including command-line arguments, to a cloud-based AI-powered EDR platform. A security risk review flags this practice. What is the PRIMARY privacy concern?

A) The AI platform might produce hallucinated threat verdicts
B) Command-line arguments may contain credentials, PII, or proprietary data sent to a third-party AI vendor
C) The high volume of telemetry may cause denial of service to the endpoint
D) Process telemetry is inaccurate and will cause the AI to produce false positives

---

**Q10.** Which of the following BEST describes the EPSS score for a CVE?

A) The CVSS environmental score adjusted for the organization's specific configuration
B) The predicted probability that a CVE will be exploited in the wild within the next 30 days
C) The number of publicly available proof-of-concept exploits for a given CVE
D) The vendor's recommended priority level for patching a specific vulnerability

---

**Q11.** A SOAR platform automatically blocks an IP address identified as malicious by an AI threat intelligence feed. The blocked IP turns out to be a legitimate CDN exit node, disrupting service for thousands of users. Which principle was violated?

A) Confidentiality — threat intelligence data should not be shared with the SOAR platform
B) The principle of least privilege — the SOAR should not have had firewall write access
C) Human-in-the-loop — irreversible, high-impact automated actions should require human approval
D) Defense in depth — multiple detection layers should have been used

---

**Q12.** An AI-powered network detection platform is deployed. For the first three months, false positive rates are high, but by month four they stabilize at an acceptable level. What is the MOST likely explanation for the initial high false positive period?

A) The model was hallucinating threat intelligence during the first three months
B) The platform needed time to build a behavioral baseline of normal network activity
C) The model was overfitting to the test environment data before generalizing
D) The vendor was retraining the model with new malware signatures each month

---

**Q13 (Performance-Based Scenario).** You are the lead security architect for a mid-size financial services firm. The CISO has approved deployment of an AI-powered SOC platform. You must design the triage workflow.

Review the following proposed workflow:

1. All security alerts from SIEM, EDR, NDR, and identity feeds ingress to the AI platform.
2. The AI platform enriches each alert with threat intel and asset data.
3. The AI platform assigns a risk score and triage verdict (Close / Investigate / Escalate).
4. All "Close" verdicts are automatically closed with no analyst review.
5. "Investigate" and "Escalate" verdicts go to the analyst queue.
6. Analyst verdicts on investigated alerts are logged but not fed back to the AI.

Identify the TWO most significant design flaws in this workflow and select the remediation pair that addresses both.

A) Flaw 1: Step 4 — auto-closing alerts without analyst review enables automation bias. Flaw 2: Step 6 — not feeding analyst verdicts back to the model prevents continuous improvement and drift detection.
B) Flaw 1: Step 2 — enrichment with external threat intel introduces prompt injection risk. Flaw 2: Step 3 — risk scoring should use CVSS only, not AI risk scores.
C) Flaw 1: Step 1 — ingesting EDR data alongside SIEM data causes alert duplication. Flaw 2: Step 5 — analysts should never review AI-escalated alerts without a second AI opinion.
D) Flaw 1: Step 3 — AI verdicts are more accurate than human triage and should not have a human review gate. Flaw 2: Step 6 — analyst override logs should be deleted to avoid contaminating the training data.

---

**Q14.** Which statement BEST characterizes the difference between AI-augmented SAST and AI-augmented DAST in a DevSecOps pipeline?

A) SAST requires a running application; DAST analyzes source code before compilation
B) SAST analyzes static source code in the development phase; DAST probes the running application in test or staging
C) Both analyze source code but DAST uses a different programming language model
D) DAST cannot be AI-augmented because it requires deterministic test results

---

**Q15.** A red team operator uses an AI assistant to analyze a target organization's job postings and LinkedIn profiles, automatically correlate the data to identify technology stack, cloud provider, and likely active projects, and produce a prioritized attack surface map. Which phase of the kill chain does this represent, and what is the MOST significant defensive implication?

A) Exploitation; organizations should patch all vulnerabilities before posting job listings
B) Reconnaissance; organizations should minimize sensitive operational detail in public job postings and employee profiles
C) Command and control; organizations should block all AI tools at the network perimeter
D) Lateral movement; organizations should restrict internal network segmentation

---

**Q16.** A security team wants their AI copilot to query the SIEM, open tickets in the ITSM tool, and pull threat intel — through a standardized connector interface rather than custom code for each. Which technology provides this, and what is the PRIMARY security consideration?

A) A diffusion model; watermarking its outputs
B) An MCP (Model Context Protocol) server; it is a privileged integration that must be authenticated, least-privilege scoped, and treated as an indirect-injection surface
C) A vector database; encrypting embeddings at rest
D) A SOAR playbook; disabling human-in-the-loop

---

**Q17.** A finance employee receives a video call from someone who looks and sounds exactly like the CFO, urgently directing a wire transfer. The "CFO" is AI-generated. Which AI-enabled attack is this, and which control MOST directly counters it?

A) Prompt injection; output filtering
B) Deepfake impersonation; out-of-band call-back verification for high-value financial requests
C) Model inversion; differential privacy
D) Data poisoning; dataset hashing

---

**Q18.** Malware authors use an LLM to automatically rewrite a payload's code on every build so its signature constantly changes while its behavior stays the same. Which AI-enabled attack category does this represent?

A) Reconnaissance
B) Membership inference
C) Obfuscation / polymorphic malware generation
D) Honeypot evasion

---

**Q19.** A platform team wires an AI agent into their CI/CD pipeline so that when a deployment's post-release health and security checks fail, the system automatically rolls back. For which type of action should this automation MOST likely retain a human approval gate?

A) Generating unit tests
B) Summarizing the deploy log
C) Promoting a high-impact change to a critical production system
D) Linting the source code

---

**Q20.** Which pairing correctly separates an AI-enabled attack (Domain 3, objective 3.2) from an attack on an AI system (Domain 2)?

A) Deepfake voice fraud = attack on AI; prompt injection = AI-enabled attack
B) Polymorphic malware generation = AI-enabled attack; training-data poisoning = attack on AI
C) Both are identical and belong to the same objective
D) Automated payload generation = attack on AI; model extraction = AI-enabled attack

---

## Answer Key — Domain 3

**Q1 — C** Signature-based (System A) has low false positives for known threats because it matches specific patterns. Anomaly-based (System B) can detect novel attacks by flagging deviations from baseline — it does not need a prior signature. Option D is incorrect: System A is rule-based, not necessarily supervised ML.

**Q2 — B** Large-volume data download at unusual hours, followed by imminent departure, is the classic insider threat exfiltration pattern. UEBA behavioral analytics is specifically designed to surface this.

**Q3 — B** The AI made errors (possibly evasion or drift), but the critical failure was that analysts accepted the verdicts without review. This is automation bias — humans delegating their judgment to an automated system without oversight.

**Q4 — C** Combining CVSS, EPSS, CISA KEV status, asset criticality, and compensating controls is the context-rich prioritization approach that reflects actual risk. CVSS alone (A) ignores exploitation likelihood and asset context. KEV only (B) misses many high-risk vulnerabilities. Random sampling (D) is not risk-based.

**Q5 — B** AI-augmented SAST in the CI pipeline as a merge gate would analyze the code for insecure patterns (missing parameterization) before the code is merged. Runtime detection (A) catches the attack after deployment, not the vulnerability. Network IDS (C) detects exploitation, not the flaw. Training (D) is important but would not have caught this specific instance before merge.

**Q6 — C** Extracting behaviors from unstructured text and mapping them to ATT&CK is an NLP classification / information extraction task. Diffusion models generate images/content, not structured threat intelligence. RL is not the right paradigm here. Vector databases store and retrieve embeddings but do not perform the extraction/mapping.

**Q7 — B** The attacker is crafting inputs specifically to evade a deployed ML detector — this is adversarial ML / evasion attack at inference time. Model extraction would involve querying the system to steal its model. Prompt injection requires the target system to be LLM-based with injectable instructions.

**Q8 — C** The inability to explain a deep neural network's decision-making is the black box / explainability problem. Automation bias (A) is about humans over-trusting AI. Model drift (B) is about changing performance over time. Adversarial robustness (D) is about resistance to adversarial inputs.

**Q9 — B** Command-line arguments frequently contain credentials (passwords passed as arguments), PII (patient names in scripts), or proprietary business data. Sending this to a third-party cloud AI platform is a data privacy risk requiring vendor assessment and contractual controls.

**Q10 — B** EPSS (Exploit Prediction Scoring System) is an ML model that outputs the probability of exploitation in the wild within 30 days. It is separate from CVSS (which is severity, not exploitation likelihood) and separate from PoC count (though PoC availability is one of its features).

**Q11 — C** Auto-blocking at scale based on an AI verdict without human review is the failure. When the action is high-impact and difficult to reverse (blocking a CDN affects thousands of users), a human-in-the-loop gate is required before execution. Least privilege (B) is about access scope, not the approval workflow for specific actions.

**Q12 — B** NDR and UEBA platforms require a baselining period (typically 30–90 days) to learn normal behavior before their anomaly detection stabilizes. High initial false positives are expected and do not indicate a bug — they indicate the model is still calibrating its normal baseline.

**Q13 — A** Flaw 1 (Step 4): auto-closing with no review is automation bias — the attacker can craft behavior that scores as low risk, and no human ever sees it. Flaw 2 (Step 6): analyst verdicts are the ground truth signal for model improvement; not feeding them back means the model cannot learn from its mistakes and will drift. Options B, C, and D describe incorrect or invented problems.

**Q14 — B** SAST analyzes source code in the development phase — it requires source access and runs before the application is deployed. DAST probes a running application (in test or staging), finding issues that only manifest at runtime. The definitions in A are reversed. C and D are incorrect.

**Q15 — B** AI-accelerated aggregation of job postings and LinkedIn profiles is an AI-assisted reconnaissance technique. The defensive implication is limiting sensitive operational detail in public postings (technology stack specifics, project names, internal tooling) because AI now makes correlating and exploiting OSINT dramatically faster than it was when these controls were originally designed.

**Q16 — B** An **MCP (Model Context Protocol) server** is the standardized connector exposing tools/data to an AI agent. Because it grants the agent privileged reach into systems, it must be authenticated, least-privilege scoped, and treated as an indirect-prompt-injection surface.

**Q17 — B** A synthetic look/sound-alike executive is a **deepfake impersonation** attack; the direct counter is out-of-band verification (call-back on a known number) for high-value requests. The other controls address attacks on models, not deepfakes.

**Q18 — C** Continuously rewriting code so the signature changes while behavior stays constant is AI-driven **obfuscation / polymorphic malware** generation, defeating signature-based detection.

**Q19 — C** Reversible/low-impact steps (tests, summaries, linting) suit full automation; **promoting a high-impact change to a critical production system** is where a human approval gate belongs — over-automating it is the trap.

**Q20 — B** Attacker *using* AI as a weapon (polymorphic malware generation) is an **AI-enabled attack (3.2)**; attacker *targeting* a model (training-data poisoning) is an **attack on AI (Domain 2)**. The other pairings are reversed or wrong.

---

## Domain 3 Glossary of Acronyms

| Acronym | Expansion |
|---|---|
| ATO | Account Takeover |
| ATT&CK | Adversarial Tactics, Techniques, and Common Knowledge (MITRE framework) |
| AV | Antivirus |
| C2 / C&C | Command and Control |
| CDN | Content Delivery Network |
| CI/CD | Continuous Integration / Continuous Deployment |
| CMDB | Configuration Management Database |
| CVE | Common Vulnerabilities and Exposures |
| CVSS | Common Vulnerability Scoring System |
| DAST | Dynamic Application Security Testing |
| DGA | Domain Generation Algorithm |
| DPA | Data Processing Agreement |
| EDR | Endpoint Detection and Response |
| EPSS | Exploit Prediction Scoring System |
| FIRST | Forum of Incident Response and Security Teams (maintains EPSS) |
| GNN | Graph Neural Network |
| IaC | Infrastructure as Code |
| IOC | Indicator of Compromise |
| KEV | Known Exploited Vulnerabilities (CISA catalog) |
| KQL | Kusto Query Language (Microsoft Sentinel) |
| LotL | Living off the Land |
| MCP | Model Context Protocol (standard for connecting AI agents to tools/data) |
| NDR | Network Detection and Response |
| NLP | Natural Language Processing |
| NTA | Network Traffic Analysis |
| OSINT | Open-Source Intelligence |
| PCAP | Packet Capture |
| PII | Personally Identifiable Information |
| PoC | Proof of Concept |
| RAG | Retrieval-Augmented Generation |
| RLHF | Reinforcement Learning from Human Feedback |
| SAST | Static Application Security Testing |
| SCA | Software Composition Analysis |
| SIEM | Security Information and Event Management |
| SHAP | SHapley Additive exPlanations |
| SMB | Server Message Block |
| SOAR | Security Orchestration, Automation, and Response |
| SOC | Security Operations Center |
| SPF | Sender Policy Framework |
| TLS | Transport Layer Security |
| TTP | Tactics, Techniques, and Procedures |
| UEBA | User and Entity Behavior Analytics |
| WAF | Web Application Firewall |
| XDR | Extended Detection and Response |

---

*End of Domain 3 — proceed to Domain 4 (04-domain4-ai-governance-risk-compliance.md). Return to this module before the full practice exam to review the limitations section.*
