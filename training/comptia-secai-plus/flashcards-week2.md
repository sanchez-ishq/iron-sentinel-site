# SecAI+ (CY0-001) — Week 2 Flashcards: Domain 2 Terminology

**Scope:** Domain 2 — Securing AI Systems (objectives 2.1–2.6). **40% of the exam — over-study this.**
**How to use:** Cover the indented answer, read the **bold front**, recall aloud, reveal. ~72 cards. (Anki TSV at bottom.)

> Domain 2 spans Weeks 2–3 in the plan (Pass A: attacks; Pass B: controls). Target 85%+ recall here.

---

## Objective 2.1 — Threat-Modeling Resources

**1. OWASP Top 10 for LLM Applications**
> The 10 most critical LLM-app risks (prompt injection, insecure output handling, excessive agency, etc.). Use when threat-modeling a generative/LLM app.

**2. OWASP Machine Learning Security Top 10**
> A *separate* OWASP list for classic ML risks (input manipulation, data poisoning, model inversion, model theft). Use for traditional ML/classifier systems, not LLM apps.

**3. MIT AI Risk Repository**
> A large curated database of documented AI risks aggregated from many frameworks; a governance-grade risk catalog for broad risk enumeration.

**4. MITRE ATLAS**
> ATT&CK-style catalog of adversary tactics/techniques against AI systems (AML.Txxxx). Use to map real adversary behaviors and build detections.

**5. CVE AI Working Group**
> The effort extending the CVE vulnerability-tracking program to AI/ML components and flaws.

---

## Objective 2.2 — Security Controls (Model vs. Gateway)

**6. Model controls**
> Controls at/around the model itself: model evaluation, model guardrails, and prompt templates.

**7. Gateway controls**
> Controls at the entry point in front of the model: prompt firewall, rate/token limits, input quotas, modality limits, endpoint access.

**8. Model guardrails**
> Behavioral/content constraints wrapped around a model at the application layer (do not change weights). Block harmful/out-of-scope input or output.

**9. Prompt firewall**
> A gateway component that inspects every prompt (and often response) before it reaches the model, blocking injection/jailbreak/exfiltration patterns. A "WAF for LLM traffic."

**10. Rate limits**
> Caps on how many requests a user/key/IP may send — limits abuse and economic DoS.

**11. Token limits**
> Caps on tokens per request/response — limits context flooding and cost.

**12. Input quotas (size & quantity)**
> Limits on input **size** (max tokens/characters) and **quantity** (max requests/prompts) to curb abuse and cost.

**13. Modality limits**
> Restricting which input types the system accepts (e.g., text only, reject images/files) to shrink the attack surface.

**14. Endpoint access controls**
> Restricting who/what can reach the model endpoint at all — auth, IP allow-listing, API gateway, private endpoints.

**15. Guardrail testing and validation**
> Systematically probing guardrails with known jailbreak/injection payloads to confirm they hold before/after deployment.

---

## Objective 2.3 — Access Controls

**16. Model access**
> Authentication/authorization governing who can call which model and with what parameters.

**17. Data access**
> Controls over who/what can read training data, RAG corpora, and vector stores (e.g., document-level access in RAG).

**18. Agent access**
> Scoping the tools, permissions, and data an AI agent can use — the primary defense for excessive agency.

**19. Network / API access**
> Controls on network paths and API calls to/from the AI system (segmentation, mTLS, gateways, allow-lists).

**20. Least privilege (for AI)**
> Granting an AI agent/model only the minimum tools, permissions, and data scope needed for its task.

---

## Objective 2.4 — Data Security Controls

**21. Encryption in transit**
> Protecting data moving to/from training, vector stores, and endpoints (TLS/mTLS).

**22. Encryption at rest**
> Protecting stored datasets, model artifacts, vector stores, and logs.

**23. Encryption in use**
> Protecting data *while it is being processed* via a hardware Trusted Execution Environment (TEE) / confidential computing. The control candidates most often miss.

**24. Data anonymization**
> Irreversibly removing identity from data so individuals can't be re-identified (vs. reversible pseudonymization).

**25. Data classification labels**
> Tagging data/chunks with sensitivity levels so downstream controls (RAG retrieval, output checks, retention) enforce by label.

**26. Data redaction**
> Removing sensitive fields (SSNs, secrets) entirely from data, prompts, outputs, or logs.

**27. Data masking**
> Obscuring sensitive data while showing partial values (e.g., ****-1234).

**28. Data minimization**
> Collecting/retaining/exposing only the minimum data the purpose requires — smaller blast radius.

---

## Objective 2.5 — Monitoring & Auditing

**29. Prompt monitoring (query/response)**
> Logging inputs, retrieval queries, and outputs (with PII controls) for abuse detection and investigation.

**30. Log monitoring**
> Watching system/AI logs for signs of abuse, anomalies, or attacks.

**31. Log sanitization**
> Stripping/redacting injected content, secrets, and PII from logs so logs don't become a second leak path or replay vector.

**32. Log protection**
> Access-controlling, encrypting, and integrity-protecting logs so an attacker can't erase tracks.

**33. Response confidence level monitoring**
> Tracking the model's confidence/probability scores; confident-but-wrong answers or confidence drops signal drift/attack. Route low-confidence to human review.

**34. Rate monitoring**
> Watching request rates per user/key for spikes indicating abuse or DoS.

**35. AI cost monitoring (4 drivers)**
> Tracking cost across **prompts** (input), **storage** (vectors/logs), **response** (output), and **processing** (compute). A spike localizes the abuse.

**36. Auditing for quality & compliance**
> Periodic audits for **hallucinations**, **accuracy**, **bias/fairness**, and **access** (who queried/retrieved/called what).

---

## Objective 2.6 — Attacks

**37. Prompt injection (direct)**
> The attacker is the user, embedding adversarial instructions in their own input to override the system prompt.

**38. Prompt injection (indirect)**
> Malicious instructions hidden in content the model *retrieves/processes* (web page, doc, email, RAG corpus). Attacker never touches the interface. Dangerous in agentic settings.

**39. Data poisoning**
> Corrupting the training **dataset** to degrade or bias the model. Training-time attack.

**40. Model poisoning**
> Tampering with the **model** itself (weights/artifact) to embed malicious behavior, e.g., a backdoor.

**41. Jailbreaking**
> Bypassing a model's safety alignment/content policy to elicit suppressed output (role-play, hypothetical framing, many-shot). A subset of prompt injection.

**42. Input manipulation (adversarial/evasion)**
> Perturbing an input at inference time to cause a wrong output without changing the model. Inference-time attack.

**43. Introducing biases (as an attack)**
> Deliberately injecting bias via skewed data/feedback to make a model systematically unfair or create a blind spot.

**44. Circumventing AI guardrails**
> Techniques that defeat the application-layer guardrails (encoding tricks, obfuscation, multi-turn escalation).

**45. Manipulating application integrations**
> Abusing the AI's connected tools/plugins/APIs/downstream systems to reach or damage systems beyond the model. (CompTIA's term; overlaps insecure plug-ins + excessive agency.)

**46. Model inversion**
> Reconstructing approximate **training data** from model outputs. Confidentiality attack on training data.

**47. Model theft / extraction**
> Querying a model enough to clone its functionality into a surrogate. IP theft; enables further attacks.

**48. Membership inference**
> Determining whether a specific record was in the **training set**. Individual privacy disclosure.

**49. AI supply chain attack**
> Compromise via a model hub, poisoned model, malicious serialization (pickle RCE), or vulnerable dependency.

**50. Transfer-learning attack**
> Malicious behavior (backdoor/bias) inherited from a pre-trained base model that survives fine-tuning.

**51. Model skewing**
> Slowly corrupting a model's **feedback/retraining loop** over time so it drifts toward attacker-desired behavior. (Continuous, not one-shot.)

**52. Output integrity attack**
> Tampering with or manipulating the model's outputs so downstream systems/users act on falsified results.

**53. Insecure output handling**
> Consuming model output unsanitized into a sink (HTML/SQL/shell), enabling XSS/SQLi/command injection.

**54. Model denial of service (DoS)**
> Exhausting inference resources via token flooding, sponge inputs, or amplification — causes outage or cost blowup.

**55. Sensitive information disclosure**
> The model reveals data it shouldn't — memorized training data, system prompt, or unauthorized RAG content.

**56. Insecure plug-in design**
> Tools/plugins an agent calls lack input validation, scoping, or auth — enabling SSRF, injection, or privilege abuse.

**57. Excessive agency**
> An agent has more functionality, permissions, or autonomy than its task needs, so a compromise/injection causes outsized harm.

**58. Overreliance**
> Humans (or systems) trusting AI output without verification, so errors become decisions. The "why it matters" enabler.

---

## Objective 2.6 — Compensating Controls

**59. Compensating controls (the set)**
> Prompt firewalls, model guardrails, access controls, data integrity controls, encryption, prompt templates, rate limiting, and least privilege.

**60. Data integrity controls**
> Hashing/signing datasets, outlier detection, and provenance tagging to prevent/detect poisoning.

**61. Secure RAG access control**
> Document-level access control enforced **at retrieval time** by the user's authorization — the fix for RAG leaking unauthorized content. (Output filtering alone is the wrong layer.)

---

## Commonly-confused discriminators (high-yield)

**62. Inversion vs. extraction vs. membership inference**
> Inversion = reconstruct training data; Extraction/theft = clone the model; Membership inference = "was this record in training?"

**63. Poisoning vs. evasion (timing)**
> Poisoning = training-time (corrupt the data/model). Evasion/input manipulation = inference-time (fool the running model).

**64. Model skewing vs. poisoning**
> Skewing = slow corruption of the *feedback/retraining loop* over time. Poisoning = up-front corruption of the training set.

**65. Direct vs. indirect prompt injection**
> Direct = from the user's own input. Indirect = from content the model retrieves/processes.

**66. Model controls vs. gateway controls**
> Model controls = evaluation, guardrails, prompt templates (at the model). Gateway controls = prompt firewall, rate/token limits, quotas, modality limits, endpoint access (in front of the model).

**67. Excessive agency vs. insecure plug-in design**
> Excessive agency = the agent *has* too much capability/permission. Insecure plug-in design = the *tools/APIs* it calls are built insecurely.

**68. The three encryption states**
> In transit (TLS) / at rest (storage encryption) / in use (TEE / confidential computing).

**69. Masking vs. redaction vs. anonymization**
> Masking = obscure but show partial (****-1234). Redaction = remove entirely. Anonymization = irreversibly de-identify.

**70. Prompt firewall vs. model guardrails**
> Prompt firewall = gateway-layer inspection point in front of the model. Guardrails = constraints wrapped around the model at the app layer. (Defense in depth — use both.)

**71. OWASP LLM Top 10 vs. ML Security Top 10**
> LLM Top 10 = generative/LLM apps. ML Security Top 10 = classic ML/classifiers.

**72. Malicious pickle deserialization**
> `torch.load`/pickle executes arbitrary code on load — a supply-chain RCE. Mitigate with SafeTensors, signing, and AI-BOM.

---

## Anki / Quizlet import (TSV — term &lt;TAB&gt; definition)

Import as **Tab-separated** (Anki: *File → Import*; field 1 = Front, field 2 = Back).

```tsv
OWASP LLM Top 10	The 10 most critical LLM-app risks; threat-model generative/LLM apps with it
OWASP ML Security Top 10	Separate OWASP list for classic ML risks (input manipulation, poisoning, inversion, theft)
MIT AI Risk Repository	Curated database of documented AI risks; broad governance-grade risk catalog
MITRE ATLAS	ATT&CK-style catalog of adversary tactics/techniques against AI (AML.Txxxx)
CVE AI Working Group	Effort extending the CVE program to AI/ML components and flaws
Model controls	Controls at the model: model evaluation, guardrails, prompt templates
Gateway controls	Controls in front of the model: prompt firewall, rate/token limits, quotas, modality, endpoint access
Model guardrails	App-layer behavioral/content constraints wrapped around a model (no weight change)
Prompt firewall	Gateway component inspecting prompts/responses before the model; WAF for LLM traffic
Rate limits	Caps on requests per user/key/IP to limit abuse and economic DoS
Token limits	Caps on tokens per request/response to limit context flooding and cost
Input quotas	Limits on input size (tokens) and quantity (requests) to curb abuse/cost
Modality limits	Restricting accepted input types (e.g., text only) to shrink attack surface
Endpoint access controls	Restricting who/what can reach the model endpoint (auth, IP allow-list, private endpoint)
Guardrail testing and validation	Probing guardrails with jailbreak/injection payloads to confirm they hold
Least privilege for AI	Granting an agent/model only the minimum tools, permissions, and data scope
Encryption in transit	Protecting data in motion with TLS/mTLS
Encryption at rest	Protecting stored datasets, models, vector stores, logs
Encryption in use	Protecting data during processing via TEE / confidential computing
Data anonymization	Irreversibly removing identity so individuals can't be re-identified
Data classification labels	Tagging data/chunks with sensitivity so controls enforce by label
Data redaction	Removing sensitive fields entirely from data/outputs/logs
Data masking	Obscuring sensitive data while showing partial values (****-1234)
Data minimization	Collecting/retaining/exposing only the minimum data needed
Prompt monitoring	Logging inputs, queries, and outputs for abuse detection and investigation
Log sanitization	Stripping injected content/secrets/PII from logs to prevent leakage/replay
Log protection	Access-control, encrypt, and integrity-protect logs against tampering
Response confidence monitoring	Tracking confidence scores; route low-confidence/confident-wrong output to human review
AI cost monitoring	Tracking cost across prompts, storage, response, and processing to localize abuse
Auditing for quality/compliance	Auditing for hallucinations, accuracy, bias/fairness, and access
Direct prompt injection	Attacker embeds adversarial instructions in their own input to override the system prompt
Indirect prompt injection	Malicious instructions hidden in content the model retrieves/processes
Data poisoning	Corrupting the training dataset to degrade/bias the model (training-time)
Model poisoning	Tampering with the model/weights to embed malicious behavior (e.g., backdoor)
Jailbreaking	Bypassing safety alignment to elicit suppressed output; a subset of prompt injection
Input manipulation	Perturbing input at inference time to cause wrong output without changing the model
Introducing biases	Deliberately injecting bias to make a model unfair or create a blind spot
Circumventing AI guardrails	Defeating app-layer guardrails via encoding/obfuscation/multi-turn escalation
Manipulating application integrations	Abusing connected tools/plugins/APIs to reach systems beyond the model
Model inversion	Reconstructing approximate training data from model outputs
Model theft/extraction	Cloning a model's functionality from query/response pairs
Membership inference	Determining whether a specific record was in the training set
AI supply chain attack	Compromise via model hubs, poisoned models, malicious pickle, or bad dependencies
Transfer-learning attack	Backdoor/bias inherited from a base model that survives fine-tuning
Model skewing	Slowly corrupting the feedback/retraining loop over time
Output integrity attack	Tampering with model outputs so downstream systems act on falsified results
Insecure output handling	Consuming model output unsanitized into a sink, enabling XSS/SQLi/command injection
Model denial of service	Exhausting inference resources via token flooding/sponge/amplification
Sensitive information disclosure	Model reveals memorized data, the system prompt, or unauthorized RAG content
Insecure plug-in design	Agent tools/plugins lacking validation/scoping/auth, enabling SSRF/injection
Excessive agency	Agent has more functionality/permissions/autonomy than its task needs
Overreliance	Trusting AI output without verification so errors become decisions
Data integrity controls	Hashing/signing datasets, outlier detection, provenance tagging to stop poisoning
Secure RAG access control	Document-level access control enforced at retrieval time by user authorization
Malicious pickle deserialization	torch.load/pickle executes arbitrary code on load; a supply-chain RCE
```

---

*Week 2 deck (Domain 2 = 40%). Spend two weeks here; aim for 85%+ recall before Domain 3. Log weak cards in `99-PROGRESS-TRACKER.md`.*
