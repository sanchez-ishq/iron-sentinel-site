# SecAI+ (CY0-001) — Week 3 Flashcards: Domain 2 Applied Defense & Controls

**Scope:** Domain 2 — Securing AI Systems, **Pass B** (objectives 2.2–2.6, applied). Defense-in-depth, attack→control mapping, secure AI lifecycle, agent/RAG hardening, red-teaming, and **evidence-analysis scenarios**. **40% of the exam — and the performance-based questions live here.**
**How to use:** Cover the indented answer, read the **bold front**, recall aloud, reveal. ~55 cards. (Anki TSV at bottom.)

> Week 2 = Domain 2 *terminology* (what each attack/control **is**). Week 3 = *applying* it: which control stops which attack, how the layers stack, and reading attack evidence. This is the scenario half of Domain 2 — expect "given these symptoms, what's the attack / what's the fix?" questions.

---

## Defense-in-depth for AI (the layered model)

**1. The five control layers (front to back)**
> **Gateway** (firewall, rate/token limits, quotas, endpoint auth) → **Model** (guardrails, evaluation, prompt templates) → **Data** (encryption, classification, secure RAG) → **Access** (least privilege, agent scoping) → **Monitoring** (prompt/log/cost/confidence). No single layer is sufficient — layer them.

**2. Why one control is never enough**
> Each control fails to some bypass (encoding tricks defeat a firewall; jailbreaks defeat guardrails; etc.). Defense-in-depth means a payload that slips one layer is caught/contained by another.

**3. Prevent vs. detect vs. contain (for AI)**
> Prevent = input validation, guardrails, least privilege. Detect = monitoring, confidence/drift alerts, audits. Contain = scoped agent permissions, human-in-the-loop confirmation, rate caps. A good design has all three.

**4. The single highest-leverage agent control**
> **Least privilege** — scope the agent's tools, permissions, and data to the minimum the task needs. It doesn't prevent a compromise but it caps the blast radius of one (mitigates excessive agency).

---

## Attack → primary control mapping (high-yield for scenarios)

**5. Direct prompt injection → ?**
> Prompt firewall (gateway) + hardened system prompt/prompt templates + output validation. Treat all user input as untrusted instructions.

**6. Indirect prompt injection → ?**
> Treat **retrieved content as untrusted data, never instructions**: sanitize/segregate retrieved text, content provenance, output validation, and least-privilege agents so a hijacked instruction can't do much.

**7. Data poisoning → ?**
> Data integrity controls: dataset hashing/signing, provenance tracking, outlier/anomaly detection, curated/trusted sources, and dataset access control.

**8. Model poisoning / backdoor → ?**
> Model provenance + signing, scan/evaluate models before deploy, SafeTensors over pickle, AI-BOM, and behavioral evaluation against trigger inputs.

**9. Model inversion / membership inference → ?**
> Limit output detail (no raw confidence/logits), differential privacy in training, data minimization, rate limiting, and query monitoring.

**10. Model theft / extraction → ?**
> Rate/quota limits, query monitoring for systematic probing, watermarking, and authentication on the endpoint.

**11. Sensitive information disclosure → ?**
> Output filtering/redaction, secure RAG access control (retrieval-time authz), data minimization in context, and system-prompt protection.

**12. Insecure output handling → ?**
> Output encoding/sanitization before any sink (HTML/SQL/shell) — treat model output like untrusted user input. Context-aware escaping.

**13. Excessive agency → ?**
> Least privilege on tools/permissions, human-in-the-loop for high-impact actions, action allow-lists, and per-action authorization.

**14. Model DoS / sponge inputs → ?**
> Rate limits, token/input-size quotas, cost monitoring with alerts, and timeouts/circuit breakers.

**15. AI supply-chain attack → ?**
> AI-BOM, model/dependency signing + verification, trusted registries, SafeTensors, and scanning artifacts before load.

---

## Secure AI lifecycle (secure MLOps)

**16. Security across the AI life cycle (objective 1.3 applied)**
> Security is built into **every** phase — design, data sourcing, training, evaluation, deployment, monitoring, and retirement — not bolted on at the end.

**17. Design-phase controls**
> Threat-model the system (OWASP LLM/ML Top 10, MITRE ATLAS), define data classification, choose architecture (gateway + guardrails), and set the agent's privilege scope.

**18. Data-phase controls**
> Provenance/lineage, dataset signing + integrity checks, classification labeling, anonymization/minimization, and access control on training corpora.

**19. Training-phase controls**
> Trusted/curated data, poisoning detection, differential privacy where needed, isolated training environment, and reproducible/auditable pipelines.

**20. Evaluation-phase controls**
> Red-team the model, test guardrails with known payloads, benchmark for bias/accuracy/safety, and check for backdoors with trigger inputs **before** deploy.

**21. Deployment-phase controls**
> Gateway (firewall, rate limits, endpoint auth), guardrails, prompt templates, secure RAG access, and a documented rollback.

**22. Monitoring-phase controls**
> Prompt/response logging, drift + confidence monitoring, cost monitoring, anomaly/abuse detection, and periodic quality/compliance audits.

**23. Retirement-phase controls**
> Securely decommission models/data, revoke endpoint access and keys, retain audit logs per policy, and purge sensitive data (data minimization through end-of-life).

---

## Guardrails, prompts & I/O validation (applied)

**24. System-prompt hardening**
> Clearly delimit and label trusted instructions, instruct the model to ignore embedded instructions in user/retrieved content, and never put secrets in the system prompt (it can leak).

**25. Prompt templates (as a control)**
> Fixed, parameterized prompt structures that separate trusted instructions from untrusted user input — reduces injection by not concatenating raw user text into the instruction.

**26. Input validation for LLMs**
> Check size/quantity (quotas), modality, and known injection/jailbreak patterns at the gateway **before** the model sees the prompt.

**27. Output validation/schema enforcement**
> Constrain and validate output (expected format/JSON schema, allowed values), sanitize for the downstream sink, and block disclosure patterns before returning.

**28. Allow-list vs. deny-list guardrails**
> Deny-lists block known-bad (bypassable by novel payloads). Allow-lists permit only known-good (more robust, but can over-block). Prefer allow-listing for high-risk actions/tools.

**29. Guardrail testing/validation (applied)**
> Continuously probe guardrails with a corpus of jailbreak/injection payloads (and after every model/prompt change) to confirm they still hold — guardrails are not "set and forget."

---

## RAG & agent hardening (applied)

**30. Secure RAG access control (the RAG fix)**
> Enforce document-level authorization **at retrieval time** by the requesting user's identity. Output filtering alone is the wrong layer — the unauthorized chunk should never be retrieved.

**31. RAG content provenance**
> Tag retrieved chunks with source/trust level so the app can treat low-trust sources as data-only and resist indirect injection from poisoned documents.

**32. Agent tool scoping (sandboxing)**
> Give each tool the narrowest permission/credential, run tools in least-privilege sandboxes, and validate tool inputs/outputs — defends excessive agency + insecure plug-in design.

**33. Human-in-the-loop (HITL)**
> Require human confirmation before high-impact or irreversible agent actions (sending money, deleting data, external posts). The containment control for excessive agency.

**34. Insecure plug-in design fixes**
> Input validation + output validation on every tool, scoped auth/credentials, no raw URL/SSRF reachability, and parameterized calls — build the *tools* securely, not just the agent.

---

## Monitoring, detection & evidence analysis (objective 2.6)

**35. What "analyze attack evidence" tests**
> Given logs/symptoms, identify (a) the attack, and (b) the compensating control that would have prevented/detected it. Practice mapping symptoms → attack → control.

**36. Evidence: output reveals the system prompt / other users' data**
> Attack: sensitive information disclosure (or RAG authz failure). Control: output filtering, secure RAG retrieval-time authz, data minimization, system-prompt protection.

**37. Evidence: a retrieved document contained hidden "ignore previous instructions"**
> Attack: indirect prompt injection. Control: treat retrieved content as untrusted data, sanitize/segregate it, provenance tags, least-privilege agent.

**38. Evidence: sudden compute/cost spike with huge inputs**
> Attack: model DoS / sponge inputs (economic DoS). Control: token/input quotas, rate limits, cost-monitoring alerts, timeouts.

**39. Evidence: thousands of systematic queries cloning behavior**
> Attack: model theft/extraction. Control: rate/quota limits, query-pattern monitoring, authentication, watermarking.

**40. Evidence: model accuracy quietly degrades after each retrain**
> Attack: model skewing (poisoned feedback loop) or data poisoning. Control: data integrity controls, feedback validation, drift monitoring, human review of retraining data.

**41. Evidence: model output ran as a command/SQL downstream**
> Attack: insecure output handling. Control: output sanitization/encoding for the sink; treat output as untrusted.

**42. Response confidence monitoring (in practice)**
> Track confidence/probability; route low-confidence or confident-but-wrong outputs to human review. Confidence drops/anomalies can flag drift or an active attack.

**43. Drift detection**
> Monitor input/output distributions vs. a baseline; significant drift signals data/model issues, skewing, or a changing threat — trigger re-evaluation/retraining.

**44. AI cost monitoring as a detection tool**
> Watch the four cost drivers — prompts, storage, response, processing. A spike localizes the abuse (e.g., processing spike → sponge/DoS; prompt spike → flooding).

**45. Log sanitization + protection (why both)**
> Sanitize: strip injected content/secrets/PII so logs aren't a second leak or replay vector. Protect: encrypt + integrity-protect + access-control so an attacker can't read or erase them.

---

## Governance-grade controls for models & data

**46. AI-BOM (AI Bill of Materials)**
> An inventory of models, datasets, dependencies, and their provenance — enables supply-chain risk tracking and fast response when a component is found vulnerable.

**47. Model/dataset signing & verification**
> Cryptographically sign artifacts and verify on load to detect tampering (model poisoning, supply-chain swaps). Pair with trusted registries.

**48. SafeTensors over pickle**
> Use SafeTensors (data-only) instead of pickle/`torch.load`, which executes arbitrary code on load (RCE). The standard fix for malicious deserialization.

**49. Red-teaming AI**
> Structured adversarial testing of the deployed system (injection, jailbreaks, extraction, evasion) to find gaps before attackers do — a core evaluation-phase control.

**50. Differential privacy**
> Adds calibrated noise during training/aggregation so individual records can't be reverse-engineered — mitigates membership inference and model inversion.

---

## Commonly-confused discriminators (high-yield)

**51. "Prevent the attack" vs. "limit the damage"**
> Input validation/guardrails *prevent*; least privilege + HITL *limit damage* if prevention fails. Scenario asking to "reduce impact of a compromised agent" → least privilege/HITL, not a better firewall.

**52. Output filtering vs. secure RAG access control**
> For RAG leaking unauthorized data, the right fix is **retrieval-time authorization** (don't fetch it), not output filtering (catches it too late, at the wrong layer).

**53. Guardrails vs. prompt firewall (which layer)**
> Prompt firewall = gateway, in front of the model. Guardrails = wrapped around the model at the app layer. Defense-in-depth uses **both**.

**54. Signing/AI-BOM vs. data integrity controls**
> Signing + AI-BOM defend the **supply chain / model artifact**. Data integrity controls (hashing, outlier detection, provenance) defend the **training data** from poisoning.

**55. Detect vs. prevent monitoring controls**
> Monitoring/auditing/drift/confidence are **detective** (after the fact). Gateway limits, guardrails, validation, and least privilege are **preventive/containment**. Map the question's verb to the right bucket.

---

## Anki / Quizlet import (TSV — term &lt;TAB&gt; definition)

Import as **Tab-separated** (Anki: *File → Import*; field 1 = Front, field 2 = Back).

```tsv
Five AI control layers	Gateway → Model → Data → Access → Monitoring; layer them (defense-in-depth)
Highest-leverage agent control	Least privilege — scope tools/permissions/data to cap blast radius
Direct prompt injection fix	Prompt firewall + hardened system prompt/templates + output validation
Indirect prompt injection fix	Treat retrieved content as untrusted data; sanitize/segregate, provenance, least-privilege agent
Data poisoning fix	Dataset hashing/signing, provenance, outlier detection, trusted sources, dataset access control
Model poisoning fix	Model provenance/signing, pre-deploy scan/eval, SafeTensors, AI-BOM, trigger-input testing
Model inversion/membership inference fix	Limit output detail, differential privacy, data minimization, rate limits, query monitoring
Model theft/extraction fix	Rate/quota limits, query-pattern monitoring, watermarking, endpoint auth
Sensitive info disclosure fix	Output filtering/redaction, secure RAG authz, data minimization, system-prompt protection
Insecure output handling fix	Encode/sanitize output for the sink; treat output as untrusted input
Excessive agency fix	Least privilege, human-in-the-loop, action allow-lists, per-action authz
Model DoS fix	Rate limits, token/input quotas, cost-monitoring alerts, timeouts/circuit breakers
AI supply chain fix	AI-BOM, signing + verification, trusted registries, SafeTensors, scan before load
Secure AI lifecycle	Build security into design, data, training, evaluation, deployment, monitoring, retirement
Design-phase controls	Threat-model (OWASP/ATLAS), classify data, choose gateway+guardrails, set agent scope
Data-phase controls	Provenance/lineage, signing/integrity, classification, anonymization/minimization, access control
Training-phase controls	Trusted data, poisoning detection, differential privacy, isolated reproducible pipeline
Evaluation-phase controls	Red-team, test guardrails, benchmark bias/accuracy/safety, check backdoors before deploy
Deployment-phase controls	Gateway, guardrails, prompt templates, secure RAG, documented rollback
Monitoring-phase controls	Prompt/response logging, drift+confidence, cost monitoring, anomaly detection, audits
Retirement-phase controls	Decommission securely, revoke access/keys, retain audit logs, purge sensitive data
System-prompt hardening	Delimit trusted instructions, ignore embedded instructions, keep secrets out of the prompt
Prompt templates (control)	Parameterized structure separating trusted instructions from untrusted user input
Input validation (LLM)	Check size/quantity/modality and injection patterns at the gateway before the model
Output validation	Enforce schema/format, sanitize for the sink, block disclosure before returning
Allow-list vs deny-list	Deny-list blocks known-bad (bypassable); allow-list permits known-good (robust); prefer allow-list for high-risk
Guardrail testing (applied)	Continuously probe with jailbreak/injection payloads, esp. after model/prompt changes
Secure RAG access control	Document-level authorization at retrieval time by the requesting user
RAG content provenance	Tag chunks by source/trust so low-trust sources are data-only (resist indirect injection)
Agent tool scoping	Narrowest per-tool permission, sandboxed tools, validated tool I/O
Human-in-the-loop	Require human confirmation before high-impact/irreversible agent actions
Insecure plug-in fixes	Input+output validation per tool, scoped auth, no SSRF reachability, parameterized calls
Analyze attack evidence	Map symptoms → attack → the compensating control that prevents/detects it
Evidence: leaks system prompt/other data	Sensitive info disclosure / RAG authz failure → output filtering, retrieval-time authz, minimization
Evidence: hidden instructions in a doc	Indirect prompt injection → untrusted-data handling, sanitize/segregate, provenance, least privilege
Evidence: huge inputs + cost spike	Model DoS / sponge inputs → quotas, rate limits, cost alerts, timeouts
Evidence: systematic cloning queries	Model theft/extraction → rate/quota limits, query monitoring, auth, watermarking
Evidence: accuracy degrades each retrain	Model skewing / data poisoning → integrity controls, feedback validation, drift monitoring
Evidence: output ran as command/SQL	Insecure output handling → sanitize/encode for the sink
Response confidence monitoring	Track confidence; route low/confident-wrong output to human review; flags drift/attack
Drift detection	Monitor I/O distribution vs baseline; drift signals poisoning/skewing/changing threat
Cost monitoring as detection	Watch prompts/storage/response/processing; a spike localizes the abuse
Log sanitization + protection	Sanitize injected content/secrets/PII; encrypt/integrity-protect/access-control logs
AI-BOM	Inventory of models/datasets/dependencies + provenance for supply-chain tracking
Model/dataset signing	Sign artifacts and verify on load to detect tampering/supply-chain swaps
SafeTensors over pickle	Data-only format vs pickle/torch.load arbitrary-code-execution (RCE)
Red-teaming AI	Structured adversarial testing of the deployed system before attackers find gaps
Differential privacy	Calibrated training noise so records can't be reversed; mitigates inversion/membership inference
Prevent vs limit damage	Validation/guardrails prevent; least privilege + HITL limit damage if prevention fails
Output filtering vs secure RAG	RAG leak fix is retrieval-time authz (don't fetch), not output filtering (wrong layer)
Guardrails vs prompt firewall	Firewall = gateway in front; guardrails = wrapped at app layer; use both
Signing/AI-BOM vs data integrity	Signing/AI-BOM defend the artifact/supply chain; data integrity defends training data
Detect vs prevent controls	Monitoring/audit/drift = detective; gateway limits/guardrails/validation/least privilege = preventive
```

---

*Week 3 deck (Domain 2 = 40%, applied/Pass B). Pair with Week 2 terminology; this is the scenario + performance-based half. Drill the attack→control mappings until automatic, then hit `qbank-domain2-part2.md`. Aim for 85%+; log weak cards in `99-PROGRESS-TRACKER.md`.*
