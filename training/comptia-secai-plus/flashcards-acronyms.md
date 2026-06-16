# SecAI+ (CY0-001) — Acronym Flashcards: The Official List

**Scope:** Every acronym on the **official CompTIA SecAI+ CY0-001 V1 acronym list** (Objectives doc v2.0). CompTIA states candidates need a **working knowledge of all of these** — you must be able to *expand* each one and *place* it in the right domain.
**How to use:** Cover the indented answer, read the **bold acronym front**, say the expansion *and* where it shows up on the exam, then reveal. Mark misses and re-drill. ~62 cards. (Anki-importable TSV at the bottom.)
**See also:** `07-official-acronyms-and-lab.md` — the same 62 acronyms as a lookup table, plus the official hardware/software lab list.

> This deck cuts across all four domains — drill it in parallel with the weekly decks, not as a separate week. The AI-specific ones (**ATLAS, MCP, MDLC, RMF, MLOps, GAN, SLM, RAG, SOAR, SCA**) are the ones candidates miss; get those automatic first.

---

## Core AI / ML concepts (Domain 1)

**1. AI**
> Artificial Intelligence — the umbrella field. Everything else nests under it.

**2. ML**
> Machine Learning — systems that learn patterns from data instead of hand-coded rules. A subset of AI (Domain 1, obj 1.1).

**3. NLP**
> Natural Language Processing — AI for understanding/generating human language; encompasses LLMs and SLMs (1.1).

**4. LLM**
> Large Language Model — transformer trained at scale to predict the next token. Primary target of prompt injection/jailbreaks (1.1).

**5. SLM**
> Small Language Model — compact model for edge/on-prem/low-cost use; keeps data off third-party APIs (1.1). High-yield.

**6. GAN**
> Generative Adversarial Network — generator vs. discriminator in competition; powers deepfakes and synthetic data (1.1, and attack use in 3.2).

**7. RAG**
> Retrieval-Augmented Generation — augmenting an LLM at inference time with retrieved documents; extends knowledge without retraining (1.2). High-yield.

**8. MDLC**
> Model Development Life Cycle — the end-to-end AI/model lifecycle (use case → data → train → evaluate → deploy → monitor → retire). Security across it = obj 1.3. **High-yield — easy to confuse with SDLC.**

---

## AI threat-modeling & attack surface (Domain 2)

**9. OWASP**
> Open Worldwide Application Security Project — publishes the **LLM Top 10** and the separate **ML Security Top 10** threat-modeling resources (2.1).

**10. ATLAS**
> Adversarial Threat Landscape for Artificial Intelligence Systems — MITRE's ATT&CK-style catalog of adversary techniques against AI (AML.Txxxx) (2.1). High-yield.

**11. MIT**
> Massachusetts Institute of Technology — namesake of the **MIT AI Risk Repository**, a curated catalog of documented AI risks (2.1).

**12. CVE**
> Common Vulnerabilities and Exposures — the public vuln-ID program; a **CVE AI Working Group** extends it to AI/ML flaws (2.1).

**13. CWE**
> Common Weakness Enumeration — taxonomy of software weakness *types* (the class behind CVEs); used in DevSecOps code review.

**14. DoS**
> Denial of Service — exhausting a system's resources; **Model DoS** (token flooding, sponge inputs) is a Domain 2 attack (2.6).

**15. DDoS**
> Distributed Denial of Service — DoS from many sources; AI can orchestrate adaptive DDoS (AI-enabled attack, 3.2).

**16. PII**
> Personally Identifiable Information — drives data-security controls, redaction/masking, and privacy compliance (2.4, 4.3).

---

## Access, identity & network controls (obj 2.3)

**17. IAM**
> Identity and Access Management — the discipline/systems governing who can access what; underpins AI access controls (2.3).

**18. IdP**
> Identity Provider — the service that authenticates users and issues identity assertions (e.g., for SSO).

**19. OAuth**
> Open Authorization — delegated-authorization standard (scoped access tokens) — relevant to scoping agent/API access.

**20. LDAP**
> Lightweight Directory Access Protocol — protocol for querying directory services (users/groups) in access control.

**21. MFA**
> Multifactor Authentication — requiring two+ independent factors; a baseline access control.

**22. NACL**
> Network Access Control List — allow/deny rules on network traffic; part of network/API access controls.

**23. API**
> Application Programming Interface — the call surface to a model/tool; agent and API access controls live here (2.3).

**24. VPC**
> Virtual Private Cloud — isolated cloud network; supports private/in-region model deployment (data sovereignty, 4.3).

**25. IDS**
> Intrusion Detection System — monitors for malicious activity/policy violations; classic detection control.

---

## Encryption & transport (obj 2.4)

**26. TLS**
> Transport Layer Security — encrypts data **in transit** to/from training, vector stores, and endpoints (2.4).

**27. HTTPS**
> Hypertext Transfer Protocol Secure — HTTP over TLS; encryption in transit for web/API traffic.

**28. SSH**
> Secure Shell — encrypted remote-access protocol; used for lab/server access.

---

## Security operations & AI-assisted detection (Domain 3)

**29. SOC**
> Security Operations Center — the team/function running detection and response; the workspace AI-assisted security augments (3.x).

**30. SIEM**
> Security Information and Event Management — central log aggregation, correlation, and alerting (3.1).

**31. SOAR**
> Security Orchestration, Automation, and Response — executes automated response playbooks (3.3). High-yield.

**32. EDR**
> Endpoint Detection and Response — endpoint telemetry + detection/response; AI-assisted detection (3.1).

**33. MSSP**
> Managed Security Service Provider — outsourced security operations/monitoring (service-delivery context).

---

## DevSecOps, pipeline & automation (obj 3.3)

**34. CI/CD**
> Continuous Integration / Continuous Deployment — the automated build-test-deploy pipeline where AI security gates live (3.3).

**35. SDLC**
> Software Development Life Cycle — the app-development lifecycle DevSecOps secures. (Contrast **MDLC** = the *model* lifecycle.)

**36. DAST**
> Dynamic Application Security Testing — probing the **running** app for flaws (test/stage stage of CI/CD). Pairs with static analysis and SCA below.

**37. SCA**
> Software Composition Analysis — scanning third-party/open-source dependencies for known CVEs in the pipeline (3.3). High-yield.

**38. IaC**
> Infrastructure as Code — provisioning infra via code; scanned for misconfig in the pipeline.

**39. ETL**
> Extract, Transform, Load — the data-pipeline pattern that feeds training/inference data stores.

**40. CDN**
> Content Delivery Network — distributed edge cache; cited as an **over-blocking pitfall** when AI auto-response blocks shared infrastructure.

---

## IT service management & change (Domain 3/ops)

**41. ITSM**
> Information Technology Service Management — the practice of delivering IT as services; context for AI-assisted IR ticket management (3.3).

**42. ITIL**
> Information Technology Infrastructure Library — the best-practice framework for ITSM (change/incident/problem management).

**43. CRM**
> Customer Relationship Management — a common business system AI agents integrate with (tool/integration surface).

---

## Compute & infrastructure

**44. CPU**
> Central Processing Unit — general-purpose compute.

**45. GPU**
> Graphics Processing Unit — parallel compute that accelerates model training and inference.

**46. LAN**
> Local Area Network — local network segment; appears in lab/network scenarios.

**47. SQL**
> Structured Query Language — database query language; the classic **insecure-output-handling** sink (model output → SQL injection) (2.6).

---

## Governance, risk & compliance (Domain 4)

**48. GRC**
> Governance, Risk, and Compliance — the whole of Domain 4.

**49. NIST**
> National Institute of Standards and Technology — author of the **NIST AI RMF** (4.3).

**50. RMF**
> Risk Management Framework — in this exam, the **NIST AI RMF**: voluntary, four functions (Govern/Map/Measure/Manage) (4.3). High-yield.

**51. ISO**
> International Organization for Standardization — publishes **ISO/IEC 42001** (certifiable AIMS) and **23894** (AI risk guidance) (4.3).

**52. OECD**
> Organisation for Economic Co-operation and Development — issued the non-binding **OECD AI Principles** that shaped later regulation (4.3).

**53. EU**
> European Union — author/jurisdiction of the **EU AI Act**, the binding risk-tiered AI regulation (4.3).

**54. GDPR**
> General Data Protection Regulation — EU privacy law; Article 22 (solely-automated decisions), DPIAs, controller/processor roles (4.3).

**55. SOC 2**
> System and Organization Controls 2 — a trust/security attestation; used when evaluating AI vendors (third-party compliance, 4.3). *Note: unrelated to a Security Operations Center.*

**56. PCI DSS**
> Payment Card Industry Data Security Standard — cardholder-data security standard; a compliance regime AI systems may fall under.

**57. IP**
> Intellectual Property — IP-related risks: training-data copyright, output ownership, model/data leakage (4.2). *Context decides:* here it's **Intellectual Property**, not Internet Protocol.

---

## AI tooling & integration (Domain 3)

**58. MCP**
> Model Context Protocol — the standard for connecting AI agents to external tools/data; a privileged, injection-prone integration (3.1). High-yield.

**59. IDE**
> Integrated Development Environment — the editor where AI coding plug-ins (e.g., Copilot) run (3.1).

**60. CLI**
> Command-Line Interface — terminal where AI plug-ins explain commands/generate scripts; review before running destructive output (3.1).

**61. MLOps**
> Machine Learning Operations — CI/CD, deployment, monitoring, and drift/retraining automation for models; also a Domain 4 role (4.1). High-yield.

**62. WAF**
> Web Application Firewall — the classic web control; the standard **analogy for a prompt firewall** ("a WAF for LLM traffic") (2.2).

---

## Quick self-test (expand the acronym, then place it)

1. ATLAS → **Adversarial Threat Landscape for AI Systems** (MITRE threat-modeling, 2.1)
2. MDLC vs. SDLC → **Model** Development Life Cycle vs. **Software** Development Life Cycle
3. RMF → **Risk Management Framework** (NIST AI RMF — voluntary, 4 functions, 4.3)
4. MCP → **Model Context Protocol** (agent↔tool integration; injection surface, 3.1)
5. SCA → **Software Composition Analysis** (scan dependencies for CVEs, 3.3)
6. SLM → **Small Language Model** (edge/on-prem; keeps data private, 1.1)
7. SOC 2 vs. SOC → **System and Organization Controls 2** (attestation) vs. **Security Operations Center**
8. IP (this exam) → **Intellectual Property** (IP-related risks, 4.2)

---

## Anki / Quizlet import (TSV — acronym &lt;TAB&gt; expansion + placement)

Copy the block below into a `.txt` and import as **Tab-separated** (Anki: *File → Import*; field 1 = Front, field 2 = Back). Anki can auto-generate reverse cards.

```tsv
AI	Artificial Intelligence — the umbrella field
ML	Machine Learning — systems that learn patterns from data; subset of AI (1.1)
NLP	Natural Language Processing — AI for human language; includes LLMs/SLMs (1.1)
LLM	Large Language Model — transformer predicting next token; prompt-injection target (1.1)
SLM	Small Language Model — compact edge/on-prem model; keeps data private (1.1)
GAN	Generative Adversarial Network — generator vs discriminator; deepfakes (1.1, 3.2)
RAG	Retrieval-Augmented Generation — LLM augmented with retrieved docs at inference (1.2)
MDLC	Model Development Life Cycle — the end-to-end model lifecycle; security across it (1.3)
OWASP	Open Worldwide Application Security Project — LLM Top 10 & ML Security Top 10 (2.1)
ATLAS	Adversarial Threat Landscape for AI Systems — MITRE ATT&CK-style AI catalog (2.1)
MIT	Massachusetts Institute of Technology — MIT AI Risk Repository (2.1)
CVE	Common Vulnerabilities and Exposures — public vuln IDs; CVE AI Working Group (2.1)
CWE	Common Weakness Enumeration — taxonomy of software weakness types
DoS	Denial of Service — resource exhaustion; Model DoS attack (2.6)
DDoS	Distributed Denial of Service — DoS from many sources; AI-orchestrated (3.2)
PII	Personally Identifiable Information — drives data-security/privacy controls (2.4)
IAM	Identity and Access Management — who can access what; AI access controls (2.3)
IdP	Identity Provider — authenticates users and issues identity assertions
OAuth	Open Authorization — delegated, scoped-token authorization standard
LDAP	Lightweight Directory Access Protocol — directory queries for access control
MFA	Multifactor Authentication — two+ independent auth factors
NACL	Network Access Control List — allow/deny rules on network traffic
API	Application Programming Interface — call surface; agent/API access controls (2.3)
VPC	Virtual Private Cloud — isolated cloud network; private/in-region deployment (4.3)
IDS	Intrusion Detection System — monitors for malicious activity/policy violations
TLS	Transport Layer Security — encrypts data in transit (2.4)
HTTPS	Hypertext Transfer Protocol Secure — HTTP over TLS; encryption in transit
SSH	Secure Shell — encrypted remote-access protocol (lab/server access)
SOC	Security Operations Center — detection/response team augmented by AI (3.x)
SIEM	Security Information and Event Management — log aggregation/correlation/alerting (3.1)
SOAR	Security Orchestration, Automation, and Response — automated response playbooks (3.3)
EDR	Endpoint Detection and Response — endpoint telemetry + detection/response (3.1)
MSSP	Managed Security Service Provider — outsourced security operations
CI/CD	Continuous Integration / Continuous Deployment — automated build-test-deploy pipeline (3.3)
SDLC	Software Development Life Cycle — app-dev lifecycle (contrast MDLC = model lifecycle)
DAST	Dynamic Application Security Testing — probing the running app in CI/CD
SCA	Software Composition Analysis — scan third-party dependencies for CVEs (3.3)
IaC	Infrastructure as Code — provisioning infra via code; scanned for misconfig
ETL	Extract, Transform, Load — data-pipeline pattern feeding training/inference
CDN	Content Delivery Network — edge cache; over-blocking pitfall in auto-response
ITSM	Information Technology Service Management — IT-as-services; AI IR ticket mgmt (3.3)
ITIL	Information Technology Infrastructure Library — best-practice framework for ITSM
CRM	Customer Relationship Management — common business system agents integrate with
CPU	Central Processing Unit — general-purpose compute
GPU	Graphics Processing Unit — parallel compute for training/inference
LAN	Local Area Network — local network segment (lab/network scenarios)
SQL	Structured Query Language — DB query language; insecure-output-handling sink (2.6)
GRC	Governance, Risk, and Compliance — the whole of Domain 4
NIST	National Institute of Standards and Technology — author of NIST AI RMF (4.3)
RMF	Risk Management Framework — NIST AI RMF; voluntary, four functions (4.3)
ISO	International Organization for Standardization — ISO/IEC 42001 & 23894 (4.3)
OECD	Organisation for Economic Co-operation and Development — non-binding AI Principles (4.3)
EU	European Union — author/jurisdiction of the EU AI Act (4.3)
GDPR	General Data Protection Regulation — EU privacy law; Art. 22, DPIA, controller/processor (4.3)
SOC 2	System and Organization Controls 2 — trust/security attestation; vendor evaluation (4.3)
PCI DSS	Payment Card Industry Data Security Standard — cardholder-data security standard
IP	Intellectual Property — IP-related risks: copyright, output ownership, leakage (4.2)
MCP	Model Context Protocol — agent↔tool/data integration; injection-prone (3.1)
IDE	Integrated Development Environment — editor for AI coding plug-ins (3.1)
CLI	Command-Line Interface — terminal AI plug-ins; review destructive output (3.1)
MLOps	Machine Learning Operations — model CI/CD, deploy, monitor, retrain; also a role (4.1)
WAF	Web Application Firewall — classic web control; analogy for a prompt firewall (2.2)
```

---

*Acronym deck. Cross-cutting — drill alongside the weekly decks until every expansion is automatic. CompTIA assumes you know all 62. Log weak cards in `99-PROGRESS-TRACKER.md`.*
