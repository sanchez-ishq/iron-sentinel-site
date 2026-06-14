# CompTIA SecAI+ (CY0-001) — Full-Length Mock Exam #2

**Full-length mock exam #2 — 60 questions, weighted 17/40/24/19, interleaved. Time yourself: 60 minutes.**

> Questions are based on the official SecAI+ Exam Objectives Document v2.0 (© 2025 CompTIA).
> These are original exam-preparation questions and do not reproduce real CompTIA items, and are distinct from Mock #1.
> Domain distribution: D1 = 10, D2 = 24, D3 = 14, D4 = 12. Performance-based questions are labeled (PBQ).

---

**Q1.** A customer-service LLM follows an instruction hidden inside a product-review document it was asked to summarize, leaking another customer's order data. The attacker never used the chat interface directly. Which attack is this?

A) Direct prompt injection
B) Indirect prompt injection
C) Model inversion
D) Training-data poisoning

**Q2.** Which architectural mechanism lets a transformer weigh the relevance of every token to every other token regardless of their distance in the sequence?

A) The tokenizer
B) The self-attention mechanism
C) The loss function
D) Backpropagation

**Q3.** An organization stands up a cross-functional body to set AI standards, vet and approve AI use cases, and share best practices firm-wide. Which governance structure is this?

A) A data processing agreement
B) An AI Center of Excellence
C) A model registry
D) A bug bounty program

**Q4.** An attacker queries a deployed face-recognition model and iteratively optimizes inputs until they reconstruct approximate images of faces in the training set. Which attack is this?

A) Membership inference
B) Model extraction
C) Model inversion
D) Adversarial example

**Q5.** A SOC deploys a model that learns each user's normal login times, locations, and data-access volume, then scores deviations. Which AI use case is this?

A) Signature matching
B) Anomaly detection / UEBA
C) Automated penetration testing
D) Code linting

**Q6.** A bank must run LLM inference on shared cloud infrastructure but cannot allow the cloud provider to read prompts or model weights *while they are being processed*. Which control applies?

A) TLS for data in transit
B) AES-256 encryption at rest
C) Confidential computing in a trusted execution environment (encryption in use)
D) Data minimization

**Q7.** A team trains a model on 200,000 transactions each labeled "fraud" or "legitimate." Which learning paradigm is this?

A) Unsupervised learning
B) Reinforcement learning
C) Supervised learning
D) Transfer learning

**Q8. (PBQ)** An AI agent for IT support can (1) look up users in the directory, (2) reset passwords, and (3) write to the ticketing system. Monitoring shows it reset 30 privileged accounts in an hour and posted the new passwords into public ticket comments; the trigger was text embedded in a wiki page the agent read. Select the TWO findings that BEST explain this. (Choose two)

A) Excessive agency — the agent should not autonomously reset privileged accounts
B) Model denial of service
C) Indirect prompt injection via retrieved wiki content
D) Membership inference
E) Differential-privacy failure

**Q9.** Under the EU AI Act, an AI tool that screens and ranks job applicants for hiring managers is classified as which risk tier?

A) Minimal risk
B) Limited risk
C) High risk
D) Unacceptable risk

**Q10.** A security copilot needs to call the SIEM, ticketing system, and threat-intel feeds through a standardized connector interface rather than bespoke integrations. Which technology provides this?

A) A vector database
B) An MCP (Model Context Protocol) server
C) A SOAR playbook
D) A diffusion model

**Q11.** Over months, an attacker feeds gamed "this was legitimate" signals into a fraud model's online retraining loop until its decision boundary drifts to approve a class of fraud. The training set was never breached in one event. Which attack is this?

A) Clean-label poisoning
B) Model skewing
C) Membership inference
D) Insecure output handling

**Q12.** In a RAG pipeline, what is stored in the vector database and used to find semantically similar content?

A) Raw plaintext documents only
B) Embeddings (high-dimensional vector representations)
C) Model weights
D) System prompts

**Q13.** A team wants a single enforcement point in front of all LLM traffic that inspects every prompt for injection and exfiltration patterns before it reaches the model. Which gateway control is this?

A) A prompt firewall
B) Model alignment
C) A model card
D) Differential privacy

**Q14.** Under the NIST AI RMF, selecting metrics, running red-team tests, and quantifying a system's trustworthiness characteristics falls under which function?

A) GOVERN
B) MAP
C) MEASURE
D) MANAGE

**Q15.** Finance receives an urgent video call from someone who looks and sounds exactly like the CEO, directing a wire transfer. The "CEO" is AI-generated. Which AI-enabled attack is this?

A) Reconnaissance
B) Deepfake impersonation
C) Membership inference
D) Obfuscation

**Q16.** An attacker subtly perturbs a malware sample at submission time so a deployed classifier labels it benign, without changing the malware's behavior or retraining the model. When does this attack occur and what is it?

A) Training time; data poisoning
B) Inference time; evasion / input manipulation
C) Training time; backdoor insertion
D) Inference time; model extraction

**Q17.** A model trained on HIV-patient records is queried such that an attacker confirms a specific person's record was in the training set. Which attack and harm is this?

A) Model extraction; IP theft
B) Membership inference; individual privacy disclosure
C) Model inversion; data reconstruction
D) Prompt injection; instruction override

**Q18.** A team needs to add 5,000 curated Q&A pairs of domain knowledge to a chatbot but cannot afford ongoing GPU training. Which approach BEST fits?

A) Train a foundation model from scratch
B) Fine-tune the model on the 5,000 pairs
C) Use RAG with the pairs in a vector store
D) Increase the context window to hold all pairs every call

**Q19. (PBQ)** A DevSecOps pipeline runs: (1) a scanner against source code pre-build, (2) a scanner that probes the running app in staging, and (3) a scanner of third-party dependencies for known CVEs. Match the three to SAST, DAST, and SCA respectively.

A) (1) DAST, (2) SAST, (3) SCA
B) (1) SAST, (2) DAST, (3) SCA
C) (1) SCA, (2) SAST, (3) DAST
D) (1) SAST, (2) SCA, (3) DAST

**Q20.** An AI coding assistant's output — a generated SQL string built from user input — is passed straight to the database with no parameterization, and a crafted input yields a malicious query. Which vulnerability class is this?

A) Excessive agency
B) Insecure output handling
C) Training-data poisoning
D) Model denial of service

**Q21.** A vendor markets its AI as "Responsible AI" and highlights that the system is designed to serve and be accessible to diverse and marginalized users. Which Responsible AI principle is this?

A) Accountability
B) Consistency
C) Inclusiveness
D) Reliability

**Q22.** An AI travel-booking agent still has standing write access to the HR system from a removed legacy feature. Which principle does this violate, and what is the OWASP LLM category?

A) Separation of duties; LLM01 Prompt Injection
B) Least privilege; LLM08 Excessive Agency
C) Defense in depth; LLM07 Insecure Plugin Design
D) Need to know; LLM06 Sensitive Information Disclosure

**Q23.** A security team lets non-developer analysts build automation by describing tasks in natural language and having AI generate the scripts/glue. Which automation capability is this, and a key governance caution?

A) Model testing; overfitting
B) Low-code/no-code scripting; ungoverned "citizen automation"/shadow AI
C) Regression testing; false negatives
D) Document synthesis; hallucination

**Q24.** A developer runs `torch.load("model.pt")` on a model pulled from a public hub and the workstation is immediately compromised. What is the MOST likely cause?

A) A backdoor trigger activated during inference
B) Malicious code executed via Python pickle deserialization
C) The model performed model inversion on the developer
D) Membership inference leaked credentials

**Q25.** An auditor asks: "Where did this training record originally come from?" versus "What is the full trail of every transformation applied to it since?" Which two concepts, in order, answer these?

A) Lineage; provenance
B) Provenance; lineage
C) Integrity; minimization
D) Provenance; integrity

**Q26. (PBQ)** A RAG knowledge assistant indexes 80,000 chunks at three classification levels (General, Confidential, Restricted). A junior analyst's query returns content from a Restricted HR document. What is the single MOST important fix?

A) Add a system-prompt instruction to keep HR data secret
B) Apply output filtering on the response only
C) Enforce document-level access control at the vector-store retrieval step, filtered by the user's authorization
D) Lower the model temperature

**Q27.** An organization wants a certifiable, third-party-auditable AI management system standard. Which applies, and how does it differ from NIST AI RMF?

A) NIST AI RMF; it is certifiable while ISO 42001 is voluntary
B) ISO/IEC 42001; it is a certifiable AIMS, whereas NIST AI RMF is voluntary and non-certifiable
C) ISO/IEC 23894; it replaces the EU AI Act
D) OECD principles; they are binding law

**Q28.** An assistant begins returning confident but wrong answers, and its internal probability scores have dropped sharply versus baseline. Which monitoring control targets this, and a reasonable response?

A) Cost monitoring; throttle the key
B) Response confidence monitoring; route low-confidence outputs to human review
C) Tenant isolation; rotate credentials
D) Log sanitization; redact the outputs

**Q29.** An analyst closes a real intrusion's alerts as benign because "the AI scored them low-risk," without checking the evidence. Which defensive-AI limitation is this?

A) Hallucination
B) Automation bias
C) Adversarial evasion
D) Explainability gap

**Q30.** A community foundation model is fine-tuned for malware triage; a hidden trigger from the *base* model causes it to mislabel malware as benign. Which attack class is this, and the best control?

A) Insecure output handling; output encoding
B) Transfer-learning attack; vet base-model provenance (AI-BOM/signing) and test for backdoors before fine-tuning
C) Model DoS; rate limiting
D) Membership inference; differential privacy

**Q31.** An engineer shrinks a model for edge devices by reducing weight precision from 32-bit float to 8-bit integer with minimal accuracy loss. Which technique is this?

A) Pruning
B) Quantization
C) Data balancing
D) Epoch tuning

**Q32.** A text-only security assistant should not accept image or file uploads, which could carry image-based injection or malicious files. Which gateway control enforces this?

A) Rate limiting
B) Modality limits
C) Token limits
D) Endpoint encryption

**Q33. (PBQ)** A firm must decide where to send three data classes to AI models: (A) published regulatory guidance, (B) customer SSNs and credit histories, (C) board-level M&A documents. Which decision is correct?

A) All three to a public hosted LLM API for speed
B) A to public is acceptable; B and C require a private/self-hosted model due to sensitivity and data sovereignty
C) All three require a public model with a longer context window
D) C is fine for public cloud because it is not personal data

**Q34.** Malware authors use an LLM to rewrite a payload on every build so its signature constantly changes while behavior stays identical. Which AI-enabled attack technique is this?

A) Reconnaissance
B) Obfuscation / polymorphic malware generation
C) Automated data correlation
D) Honeypot evasion

**Q35.** An AI tool compares file hashes and byte patterns against a database of known-bad indicators to flag malware. Which use case is this?

A) Anomaly detection
B) Signature matching
C) Fraud detection
D) Threat modeling

**Q36. (PBQ)** A CISO asks you to design monitoring for a production customer-service LLM to (1) detect plausible-but-wrong answers, (2) detect economic abuse via disproportionate API cost, (3) ensure injection payloads in inputs do not persist in logs or get replayed, and (4) detect demographic disparities in response quality. Which set BEST maps to these needs?

A) (1) hallucination auditing, (2) AI cost monitoring, (3) log sanitization, (4) bias/fairness auditing
B) (1) rate limiting, (2) tenant isolation, (3) encryption at rest, (4) red-teaming
C) (1) SHAP, (2) DPIA, (3) watermarking, (4) DAST
D) (1) guardrails, (2) MFA, (3) SBOM, (4) model card

**Q37.** A hospital wants an AI assistant whose prompts (containing PHI) never leave its infrastructure, accepting reduced capability. Which choice BEST fits?

A) A frontier LLM via public cloud API
B) A small language model (SLM) self-hosted on-premises
C) A diffusion model
D) A GAN trained on alerts

**Q38.** An enterprise uses an AI vendor's SaaS model to process its customers' data; the vendor then uses that data to improve its own model without permission. Under GDPR, how is the vendor's improvement use classified?

A) Processor only; the contract suffices
B) Controller for that new purpose; the enterprise must restrict it or establish a lawful basis
C) The enterprise bears no liability since it outsourced the function
D) Permitted under legitimate interests with no further action

**Q39.** A threat-intel team uses NLP to automatically extract IOCs and map behaviors to MITRE ATT&CK techniques from hundreds of daily reports. Which AI capability is this?

A) Diffusion-based report generation
B) Reinforcement learning over the ATT&CK matrix
C) NLP information extraction and classification
D) Vector nearest-neighbor storage only

**Q40.** An attacker submits thousands of queries to a proprietary classification API, collects input-output pairs, and trains a surrogate that mimics it. Which attack is this?

A) Model inversion
B) Membership inference
C) Model extraction / theft
D) Data poisoning

**Q41.** A pipeline must protect data so SSNs show only the last four digits in outputs and logs, while training data has identity irreversibly removed. Which two controls map to these, respectively?

A) Encryption; tokenization
B) Masking; anonymization
C) Redaction; classification
D) Minimization; watermarking

**Q42. (PBQ)** An AI agent wired into CI/CD auto-rolls-back a deployment when post-release security checks fail. For which action should the team MOST likely keep a human approval gate?

A) Generating unit tests
B) Summarizing the deploy log
C) Promoting a high-impact change to a critical production system
D) Linting source code

**Q43.** A company wants to (a) prove a leaked proprietary model was stolen from them and (b) flag when content was machine-generated. Which Domain 1 technique supports both?

A) Tokenization
B) Watermarking
C) Quantization
D) Few-shot prompting

**Q44.** A team is threat-modeling a traditional fraud-detection **classifier** (not an LLM app). Which resource is the MOST appropriate starting framework?

A) OWASP Top 10 for LLM Applications
B) OWASP Machine Learning Security Top 10
C) The EU AI Act high-risk annex
D) The SBOM specification

**Q45.** Employees across departments quietly use unapproved public AI tools to process company data with no IT oversight. Which risk is this?

A) Shadow AI
B) Model drift
C) Excessive agency
D) Data residency compliance

**Q46.** A defender wants to cap economic denial-of-service and abuse by limiting both how large each request can be and how many requests a key may send. Which controls apply?

A) Token/size input quotas and rate limits
B) Model signing and AI-BOM
C) Differential privacy and federated learning
D) mTLS and an API gateway only

**Q47.** A multinational SOC uses AI to convert multilingual threat-intel and analyst notes into a single working language and condense long incident records. Which two use cases are these?

A) Signature matching and fraud detection
B) Translation and summarization
C) Anomaly detection and linting
D) Pattern recognition and pentesting

**Q48.** An LLM reproduces verbatim API keys and PII that appeared in its training corpus when prompted. Which risk is this, and the OWASP LLM category?

A) Excessive agency; LLM08
B) Sensitive information disclosure (training-data memorization); LLM06
C) Model DoS; LLM04
D) Insecure plugin design; LLM07

**Q49. (PBQ)** An EU hospital wants an LLM to summarize patient records but the data must never be processed outside the EU or leave its control. Which deployment and concept are MOST relevant?

A) Public third-party API; data minimization
B) Private/self-hosted in-region model; data sovereignty/residency
C) Any public model with output filtering; purpose limitation
D) A larger context window; homogenization

**Q50.** In the secure AI lifecycle, which human-centric design principle has a person verify AI-generated outputs/quality before they are trusted or acted on?

A) Human validation
B) Reinforcement learning
C) Data augmentation
D) Statistical learning

**Q51.** Before deploying an LLM app, a team systematically attempts known jailbreaks and injection payloads to confirm the guardrails hold. Which activity is this?

A) Guardrail testing and validation
B) Data balancing
C) Fine-tuning
D) Tokenization

**Q52.** A "Responsible AI" review flags that a model gives noticeably different answers to near-identical inputs across sessions with no explanation. Which principle is most directly implicated?

A) Inclusiveness
B) Consistency
C) Accountability
D) Privacy and security

**Q53. (PBQ)** A team is building an adversary-behavior playbook for an LLM agent and wants an ATT&CK-style catalog of AI-specific adversary tactics and techniques (AML.Txxxx) to map detections. Which resource fits BEST?

A) OWASP ML Security Top 10
B) MITRE ATLAS
C) MIT AI Risk Repository
D) ISO/IEC 23894

**Q54.** A red team uses AI to aggregate DNS records, certificate transparency logs, and employee profiles into a prioritized attack-surface map. Which use case/phase is this?

A) Automated penetration testing / reconnaissance
B) Fraud detection
C) Incident management
D) Model testing

**Q55.** An attacker abuses an AI system's connected downstream tools and APIs to reach systems beyond the model itself. Using CompTIA's objective-2.6 term, what is this?

A) Manipulating application integrations
B) Membership inference
C) Output integrity attack
D) Model skewing

**Q56. (PBQ)** A data-science team retrained a credit model and pushed it to production without updating the model card, notifying the risk committee, or re-running bias evaluation. Which NIST AI RMF function is MOST deficient?

A) GOVERN
B) MAP
C) MEASURE
D) MANAGE

**Q57.** A change-management workflow uses AI to risk-score proposed changes and recommend approval, and triggers automated rollback when health checks fail. Which Domain 3 capability is this?

A) Signature matching
B) AI-assisted change approvals with automated deployment/rollback
C) Fraud detection
D) Anomaly detection

**Q58.** A SOC fully replaces analyst judgment with an AI verdict engine. Besides automation bias, which additional risk is MOST directly created?

A) Overreliance leaving no human fallback if the AI is evaded or wrong
B) Encryption-in-use failure
C) Vector store inversion
D) Token flooding

**Q59.** A prompt engineer asks an LLM to classify text by giving only an instruction and NO examples in the prompt. Which prompting technique is this?

A) One-shot prompting
B) Multi-shot prompting
C) Zero-shot prompting
D) Fine-tuning

**Q60.** Which statement about the OECD AI Principles is MOST accurate for this exam?

A) They are binding EU law that defines the four EU AI Act risk tiers
B) They are non-binding intergovernmental principles that influenced later AI regulation including the EU AI Act
C) They replace the NIST AI RMF in the US
D) They are a certifiable management-system standard

---

## Answer Key

| Q# | Answer | Domain | Explanation |
|----|--------|--------|-------------|
| Q1 | B | [D2] | Malicious instruction came from retrieved content, not the user — indirect prompt injection. |
| Q2 | B | [D1] | Self-attention scores relevance between all token pairs regardless of distance; the transformer's defining mechanism. |
| Q3 | B | [D4] | A cross-functional standards/approval body is an AI Center of Excellence. |
| Q4 | C | [D2] | Reconstructing approximate training data from outputs is model inversion. |
| Q5 | B | [D3] | Learning per-user baselines and scoring deviations is anomaly detection / UEBA. |
| Q6 | C | [D2] | Protecting data *while processed* on untrusted infrastructure requires a TEE — encryption in use. |
| Q7 | C | [D1] | Labeled fraud/legitimate examples define supervised learning. |
| Q8 | A, C | [D2] | Autonomous privileged resets = excessive agency; the wiki-embedded trigger = indirect prompt injection. |
| Q9 | C | [D4] | Employment/recruitment AI is high-risk under EU AI Act Annex III. |
| Q10 | B | [D3] | A standardized connector exposing tools/data to an agent is an MCP server. |
| Q11 | B | [D2] | Slow corruption of the feedback/retraining loop over time is model skewing, not a one-shot poisoning. |
| Q12 | B | [D1] | Vector databases store embeddings and use similarity search over them. |
| Q13 | A | [D2] | A model-independent enforcement point inspecting all prompts at the gateway is a prompt firewall. |
| Q14 | C | [D4] | Selecting metrics, testing, and quantifying risk is the MEASURE function. |
| Q15 | B | [D3] | A synthetic look/sound-alike executive is deepfake impersonation. |
| Q16 | B | [D2] | Inference-time perturbation to flip a classification without retraining is evasion / input manipulation. |
| Q17 | B | [D2] | Confirming a specific record was in the training set is membership inference; harm is individual privacy disclosure. |
| Q18 | C | [D1] | RAG adds knowledge at query time with no GPU training and stays updatable. |
| Q19 | B | [D3] | (1) source pre-build = SAST, (2) running app = DAST, (3) dependencies = SCA. |
| Q20 | B | [D2] | Consuming model output unsanitized into a SQL sink is insecure output handling. |
| Q21 | C | [D4] | Designing to serve diverse/marginalized users is the inclusiveness principle. |
| Q22 | B | [D2] | Standing unused access violates least privilege; an over-privileged agent is LLM08 Excessive Agency. |
| Q23 | B | [D3] | NL-to-script generation by non-developers is low-code/no-code automation; caution is shadow AI / ungoverned automation. |
| Q24 | B | [D2] | `torch.load` uses pickle, which executes arbitrary code on deserialization — supply-chain RCE. |
| Q25 | B | [D1] | Provenance = origin; lineage = the full transformation trail. |
| Q26 | C | [D2] | Enforce document-level access control at retrieval time by the user's authorization — filtering output alone is the wrong layer. |
| Q27 | B | [D4] | ISO/IEC 42001 is a certifiable AIMS; NIST AI RMF is voluntary and non-certifiable. |
| Q28 | B | [D2] | Confident-but-wrong output with falling confidence is caught by response-confidence monitoring; route low-confidence to HITL. |
| Q29 | B | [D3] | Accepting an AI verdict without checking evidence is automation bias (a human failure). |
| Q30 | B | [D2] | A backdoor inherited from the base model is a transfer-learning attack; vet provenance and test before fine-tuning. |
| Q31 | B | [D1] | Reducing weight precision (FP32→INT8) is quantization. |
| Q32 | B | [D2] | Restricting accepted input types (reject images/files) is a modality limit. |
| Q33 | B | [D4] | Data sensitivity drives the choice: public OK for published guidance; SSNs/credit and M&A need private/self-hosted (sovereignty/MNPI). |
| Q34 | B | [D3] | AI rewriting the payload each build to change signatures is obfuscation / polymorphic malware. |
| Q35 | B | [D3] | Matching hashes/byte patterns to known-bad indicators is signature matching. |
| Q36 | A | [D2] | Hallucination auditing, AI cost monitoring, log sanitization, and bias/fairness auditing map to the four needs. |
| Q37 | B | [D1] | An on-prem SLM keeps PHI off third-party APIs at the cost of capability. |
| Q38 | B | [D4] | Using client data for its own model purpose makes the vendor a controller for that processing; the enterprise must restrict it. |
| Q39 | C | [D3] | Extracting IOCs and mapping to ATT&CK from text is NLP information extraction/classification. |
| Q40 | C | [D2] | Cloning a model's function from query/response pairs is model extraction/theft. |
| Q41 | B | [D2] | Showing only last-4 = masking; irreversibly removing identity from training data = anonymization. |
| Q42 | C | [D3] | Reversible/low-impact steps suit automation; promoting a high-impact change to critical prod warrants a human gate. |
| Q43 | B | [D1] | Watermarking marks models/data (prove theft) and outputs (flag machine-generated content). |
| Q44 | B | [D2] | A traditional classifier maps to the OWASP ML Security Top 10, not the LLM Top 10. |
| Q45 | A | [D4] | Unapproved, unsupervised AI use is shadow AI. |
| Q46 | A | [D2] | Capping request size and request count = input quotas (token/size) plus rate limits. |
| Q47 | B | [D3] | Converting languages = translation; condensing records = summarization. |
| Q48 | B | [D2] | Memorized training data leaking PII/keys is sensitive information disclosure (LLM06). |
| Q49 | B | [D4] | Keeping EU data processed in-region and under control is data sovereignty/residency — use a private/self-hosted in-region model. |
| Q50 | A | [D1] | A human verifying AI outputs/quality before they're trusted is human validation. |
| Q51 | A | [D2] | Systematically probing guardrails with jailbreak/injection attempts is guardrail testing and validation. |
| Q52 | B | [D4] | Unpredictable, varying output for similar inputs implicates the consistency principle. |
| Q53 | B | [D2] | MITRE ATLAS is the ATT&CK-style catalog of AI adversary tactics/techniques. |
| Q54 | A | [D3] | AI-aggregated OSINT into an attack-surface map is AI-assisted reconnaissance (pentest phase). |
| Q55 | A | [D2] | Abusing connected tools/APIs to reach beyond the model is "manipulating application integrations." |
| Q56 | D | [D4] | Failing to update docs, notify governance, and re-test after a change is a MANAGE deficiency. |
| Q57 | B | [D3] | AI risk-scoring changes plus automated rollback is AI-assisted change approvals with automated deployment/rollback. |
| Q58 | A | [D3] | Fully replacing analysts creates overreliance — no human fallback when the AI is evaded or wrong. |
| Q59 | C | [D1] | An instruction with no in-prompt examples is zero-shot prompting. |
| Q60 | B | [D4] | OECD AI Principles are non-binding and influenced later regulation including the EU AI Act. |

---

## Scoring guide

| Raw score (/60) | Readiness |
|---|---|
| **51–60 (≥85%)** | Exam-ready on this mock — pair with a second 85%+ sitting to clear the booking gate |
| 45–50 (75–83%) | Borderline — review missed domains, then re-sit |
| < 45 (<75%) | Keep studying — focus the weakest domain(s) before another mock |

**Domain self-score:** tally your misses by tag — [D1] /10, [D2] /24, [D3] /14, [D4] /12. **Domain 2 is 40% of the real exam**, so a low D2 sub-score matters most. Log every missed item in the Weak-Area Log in `99-PROGRESS-TRACKER.md`, grouped by domain.

---

*End of Full-Length Mock Exam #2 — CompTIA SecAI+ CY0-001. Original practice questions for Iron Sentinel training use; not for redistribution.*
