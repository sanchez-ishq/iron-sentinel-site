# Domain 4 — AI Governance, Risk & Compliance

**Exam weight:** 19% (approximately 11–12 questions out of 60)
**Estimated study time:** 8–10 hours (Week 5 per master plan)
**Module owner:** CSO, Iron Sentinel LLC

> CSO note: This domain is highly testable on *precise terminology*. The NIST AI RMF
> four functions and the EU AI Act risk tiers are near-certain question fodder. Know
> every term in the glossary cold before exam day.

---

## Learning Objectives Checklist

Before moving on, you should be able to:

- [ ] Name and describe the four NIST AI RMF core functions (GOVERN, MAP, MEASURE, MANAGE) and state what each accomplishes
- [ ] List the six trustworthy-AI characteristics defined in NIST AI RMF 1.0 and give an example of each
- [ ] Describe what the NIST AI RMF Generative AI Profile adds to the base framework
- [ ] Distinguish ISO/IEC 42001 from NIST AI RMF (management system vs. voluntary framework)
- [ ] State the purpose of ISO/IEC 23894 and how it relates to 42001
- [ ] Identify the four EU AI Act risk tiers and give one example system for each tier
- [ ] Describe the obligations that attach to "high-risk" AI systems under the EU AI Act
- [ ] Apply GDPR Article 22 to an AI scenario (automated decision-making, right to explanation)
- [ ] Differentiate controller from processor in an AI supply chain context
- [ ] Explain when a DPIA is required and what it must cover for an AI system
- [ ] Define model card, datasheet for datasets, system card, and AI-BOM and know what each documents
- [ ] Explain shadow AI and why it creates governance risk
- [ ] Describe the key elements of an AI acceptable-use policy
- [ ] Identify bias/fairness measurement concepts (demographic parity, equal opportunity)
- [ ] Explain explainability methods (SHAP, LIME) at a conceptual level
- [ ] Describe how AI incident response differs from traditional IR
- [ ] Map a given AI control scenario to the correct NIST AI RMF function
- [ ] Describe AI governance structures (**AI Center of Excellence**, committees) and the **AI roles taxonomy** (data scientist, data/ML/MLOps engineer, AI/platform/security architect, AI governance/risk/audit)
- [ ] List the **Responsible AI principles** (incl. inclusiveness, consistency, awareness) and distinguish them from the NIST trustworthy-AI characteristics
- [ ] Decide **private/self-hosted vs. public/third-party models** by data sensitivity, and explain **data sovereignty/residency** and its controls

---

## Section 1 — NIST AI Risk Management Framework (AI RMF 1.0)

### 1.1 Background and Purpose

The **NIST AI RMF 1.0** was published by NIST in January 2023. It is a *voluntary*, non-prescriptive framework that helps organizations identify, assess, and manage AI-specific risks throughout the AI lifecycle. It is audience-agnostic — it applies to AI developers, deployers, and operators regardless of sector or size.

The AI RMF complements (but does not replace) NIST SP 800-53, the Cybersecurity Framework (CSF), and the Privacy Framework. CompTIA tests you on AI RMF specifically, not on those others.

### 1.2 The Four Core Functions

The AI RMF organizes AI risk management into four high-level functions. They are meant to be used *iteratively*, not sequentially.

| Function | One-line Definition | Key Question Answered |
|----------|--------------------|-----------------------|
| **GOVERN** | Establishes organizational policies, accountability structures, culture, and processes for AI risk management | "How does our organization set the rules?" |
| **MAP** | Identifies and categorizes AI risks in context — for a specific AI system and its deployment environment | "What risks exist for this AI system?" |
| **MEASURE** | Analyzes and assesses the identified risks using metrics, evaluation methods, and testing | "How big are those risks and how do we quantify them?" |
| **MANAGE** | Implements plans and controls to address prioritized risks; tracks residual risk; includes response & recovery | "What do we do about those risks?" |

**Memory anchor:** G-M-M-M or "Govern first, then Map-Measure-Manage the specifics." GOVERN is the only function that applies organization-wide rather than to a specific AI system.

### 1.3 GOVERN in Depth

GOVERN is the foundational function. Key subcategories (called **categories** in RMF language):

- Policies and accountability for AI risk are established and maintained
- Roles and responsibilities for AI risk (including third-party AI) are defined
- Organizational risk tolerance for AI is determined
- Culture of AI risk awareness is fostered
- AI risk management processes are integrated with enterprise risk management (ERM)

### 1.4 MAP in Depth

MAP contextualizes risk for a specific AI system. Activities include:

- Defining the intended purpose, context, and beneficiaries of the AI system
- Identifying stakeholders (impacted individuals, not just deployers)
- Categorizing the AI system by risk level
- Identifying where in the AI lifecycle risk arises (design, training, deployment, decommission)

### 1.5 MEASURE in Depth

MEASURE quantifies and evaluates risk. Activities include:

- Selecting and applying metrics for trustworthy-AI characteristics (see Section 1.7)
- Conducting testing, red-teaming, benchmarking
- Evaluating third-party AI component risk
- Tracking AI system performance drift over time (this is a distinct AI-specific concern)

### 1.6 MANAGE in Depth

MANAGE addresses risks that have been mapped and measured. Activities include:

- Prioritizing and implementing risk treatments (mitigate, avoid, transfer, accept)
- Documenting residual risk
- Planning for AI incident response and recovery
- Decommissioning AI systems that cannot be adequately managed
- Monitoring for new risks as the system or environment changes (continuous monitoring)

### 1.7 Trustworthy-AI Characteristics

NIST AI RMF 1.0 defines **seven characteristics** of trustworthy AI. These are explicitly tested on the exam — know all seven and a one-line definition of each.

| Characteristic | Definition |
|---------------|-----------|
| **Accountable** | Clear ownership and responsibility exist for AI decisions and outcomes |
| **Explainable** | The AI system's outputs and reasoning can be understood by relevant stakeholders |
| **Interpretable** | The mechanism by which the model produces a given output can be described (more technical than explainable) |
| **Privacy-Enhanced** | AI design and operation protects data privacy throughout the AI lifecycle |
| **Reliable** | The AI system performs consistently and accurately across expected inputs and conditions |
| **Safe** | The AI system does not pose undue physical, psychological, financial, or societal harm |
| **Secure & Resilient** | The AI system resists adversarial attack, maintains performance under stress, and recovers from failures |

> Exam tip: NIST AI RMF lists **Explainable** and **Interpretable** as *separate* characteristics. Many candidates conflate them. Interpretable = the model mechanism is understandable (e.g., a decision tree). Explainable = the outputs are understandable to stakeholders, even if the mechanism is opaque (e.g., a post-hoc SHAP explanation of a black-box model). Both are required for trustworthy AI; they serve different audiences.

> Exam tip: "Valid and Reliable" are sometimes listed together in NIST source material as a paired concept. The exam may present "Valid" as part of "Reliable" — do not be surprised. The full phrase is often "valid, reliable, and robust."

**Fairness** is also a heavily discussed concept in AI ethics but note that NIST AI RMF frames it under the broader trustworthy-AI characteristics rather than as a standalone eighth characteristic. The framework explicitly acknowledges that fairness is context-dependent and sociotechnical.

### 1.8 AI RMF Profiles and Playbooks

The AI RMF includes the concept of **Profiles** — customized prioritizations of framework categories for specific use cases or sectors. The most important Profile for the exam is the Generative AI Profile (see Section 1.9). Organizations create a **Current Profile** (where they are) and a **Target Profile** (where they want to be), then close the gap — exactly the same concept as in the NIST CSF.

### 1.9 NIST AI RMF Generative AI Profile (NIST AI 600-1)

Published by NIST in July 2024 as **NIST AI 600-1**, the Generative AI Profile addresses unique risks introduced by generative AI systems (LLMs, image generators, etc.) that are not fully captured by the base AI RMF. Key additions:

**Unique GenAI risks identified:**
- **Confabulation (hallucination):** Model generates plausible-sounding but false or unsupported content
- **Data privacy violations:** GenAI can memorize and regurgitate training data, including PII
- **Harmful content generation:** Toxic, violent, or CSAM content generation
- **Homogenization:** Overreliance on a small number of foundation models reduces diversity and creates systemic risk
- **Intellectual property concerns:** Training data copyright, output ownership
- **Obscured provenance:** Difficulty attributing AI-generated content; deepfakes
- **Data poisoning:** Malicious manipulation of training data
- **Human-AI configuration:** Over-reliance or under-reliance by human operators

**Key takeaway for exam:** NIST AI 600-1 maps these GenAI-specific risks back to the four AI RMF functions and provides suggested mitigations. If a question describes a generative AI risk scenario and asks which framework applies, NIST AI 600-1 / the GenAI Profile is the answer.

---

## Section 2 — ISO/IEC Standards for AI

### 2.1 ISO/IEC 42001 — AI Management System

**ISO/IEC 42001:2023** is an international standard that specifies requirements for establishing, implementing, maintaining, and continually improving an **Artificial Intelligence Management System (AIMS)**. It was published in December 2023 by ISO/IEC JTC 1/SC 42.

Key points:
- It follows the **Annex SL** high-level structure common to ISO 27001, ISO 9001, and ISO 22301 — making it directly integrable with existing management systems
- It is **certifiable** — organizations can obtain third-party ISO/IEC 42001 certification, unlike the NIST AI RMF which is voluntary and non-certifiable
- It covers the organization's *use* of AI as well as the *development* of AI
- Core clauses include: Context of the Organization, Leadership, Planning, Support, Operation, Performance Evaluation, Improvement
- It requires an **AI policy**, definition of AI objectives, risk treatment for AI systems, and documented evidence

### 2.2 ISO/IEC 23894 — AI Risk Management Guidance

**ISO/IEC 23894:2023** provides guidance on managing risk specific to AI systems. It is a *guidance* standard (not requirements-based), intended to be used alongside ISO 42001. It maps closely to ISO 31000 (the general risk management standard) and adapts it for AI-specific risk factors including:

- AI lifecycle risk (data collection through decommission)
- Emergent behavior and unpredictability
- Interaction risks (human-AI teaming)
- Third-party AI component risk

### 2.3 ISO/IEC 42001 vs. NIST AI RMF — Comparison

| Attribute | ISO/IEC 42001 | NIST AI RMF 1.0 |
|-----------|--------------|-----------------|
| Type | Requirements standard (AIMS) | Voluntary framework |
| Certifiable? | Yes (third-party audit) | No |
| Structure | Annex SL (plan-do-check-act) | Four functions: GOVERN, MAP, MEASURE, MANAGE |
| Geographic origin | International (ISO/IEC) | US (NIST) |
| Primary audience | Organizations deploying or developing AI | AI developers, deployers, operators |
| Companion risk doc | ISO/IEC 23894 | AI 600-1 (GenAI Profile) |
| Integration with existing frameworks | Integrates with ISO 27001, ISO 9001 | Integrates with NIST CSF, SP 800-53 |

---

## Section 3 — OECD AI Principles

The **OECD AI Principles** (first adopted 2019, updated 2024) are intergovernmental, non-binding principles endorsed by 46 countries. They are the conceptual foundation for many national AI regulations, including the EU AI Act. Key principles:

1. **Inclusive growth, sustainable development & well-being** — AI should benefit people and planet
2. **Human-centered values & fairness** — AI should respect rule of law, human rights, and democratic values
3. **Transparency & explainability** — AI actors should provide meaningful information about AI systems
4. **Robustness, security & safety** — AI systems should be robust, secure, and safe throughout the lifecycle
5. **Accountability** — AI actors should be accountable for proper functioning of AI systems

> Exam relevance: The OECD principles appear on the exam primarily as the *conceptual underpinning* for EU regulation. If a question asks which international body produced foundational AI principles that influenced the EU AI Act, the answer is OECD.

---

## Section 4 — EU AI Act

### 4.1 Overview

The **EU AI Act** (Regulation (EU) 2024/1689) is the world's first comprehensive binding AI regulation. It entered into force **August 1, 2024**, with a phased implementation timeline. It applies to any organization that *places AI systems on the EU market or puts them into service in the EU* — including non-EU companies whose AI outputs are used in the EU. This is a jurisdictional point the exam tests.

### 4.2 Risk-Tier Classification (Exam Critical)

The EU AI Act classifies AI systems into four risk tiers with different obligations:

| Risk Tier | Definition | Examples | Obligations |
|-----------|-----------|---------|-------------|
| **Unacceptable Risk** (Prohibited) | Systems that pose an unacceptable threat to fundamental rights or safety | Social scoring by governments; real-time remote biometric surveillance in public spaces (with narrow exceptions); subliminal manipulation; exploitation of vulnerabilities | **Banned outright** — cannot be placed on the market |
| **High Risk** | Systems used in critical infrastructure, safety, consequential decisions about individuals | Medical devices, credit scoring, hiring/recruitment AI, educational assessment, law enforcement, border control, critical infrastructure management | Conformity assessment, technical documentation, risk management system, human oversight, transparency, registration in EU database, post-market monitoring |
| **Limited Risk** | Systems with specific transparency obligations | Chatbots, deepfake generators, emotion recognition systems | Must disclose AI nature to users; deepfakes must be labeled |
| **Minimal Risk** | All other AI systems | Spam filters, AI in video games, recommendation engines (most cases) | No mandatory obligations (voluntary codes of practice encouraged) |

> Exam tip: "Unacceptable risk" = *prohibited*. Examiners sometimes use "banned," "forbidden," or "prohibited" — all mean the same tier. Social scoring by public authorities is the canonical prohibited example.

> Exam tip: GPAI (General-Purpose AI) models — including foundation models like large LLMs — have their own obligations under the EU AI Act separate from the four-tier system. GPAI models with systemic risk (e.g., trained with compute above 10^25 FLOPs) face additional requirements including adversarial testing. The exam may test this distinction.

### 4.3 High-Risk AI System Obligations (Detail)

Organizations deploying high-risk AI systems must:

- Implement a **risk management system** (documented, continuous throughout lifecycle)
- Conduct **data governance** — training data must be relevant, representative, and free from errors
- Produce **technical documentation** before market placement
- Implement automatic **logging/record-keeping** of operations (for post-incident audit)
- Provide **transparency** to deployers — instructions for use, capabilities, limitations
- Ensure **human oversight** — humans must be able to monitor, intervene, or override
- Achieve appropriate **accuracy, robustness, and cybersecurity**
- **Register** the system in the EU AI database (publicly accessible for most high-risk systems)

### 4.4 Implementation Timeline (High Level)

| Date | Milestone |
|------|-----------|
| August 1, 2024 | EU AI Act entered into force |
| February 2, 2025 | Prohibited practices provisions apply (unacceptable risk bans effective) |
| August 2, 2025 | GPAI model obligations apply; governance bodies operational |
| August 2, 2026 | High-risk AI system obligations fully apply (Annex I systems) |
| August 2, 2027 | High-risk AI obligations apply to systems regulated under other EU product safety laws |

> Note for exam: Questions may test whether a candidate knows that prohibited systems were the FIRST provisions to take effect (February 2025), not high-risk systems.

---

## Section 5 — GDPR Applied to AI

### 5.1 Lawful Basis for AI Processing

The **GDPR** (Regulation (EU) 2016/679) does not mention AI explicitly, but all AI systems that process personal data of EU residents must comply. Processing must have one of six lawful bases (Article 6):

- Consent
- Contract performance
- Legal obligation
- Vital interests
- Public task
- **Legitimate interests** (commonly used for AI analytics — requires a balancing test)

For AI, **consent** is often impractical as a lawful basis because AI systems process data at scale and purposes can be broad. Legitimate interests is frequently used but requires a Legitimate Interests Assessment (LIA).

### 5.2 Automated Decision-Making and Profiling — Article 22

**Article 22** is the most exam-tested GDPR provision for AI. It gives data subjects the right **not to be subject to a decision based solely on automated processing**, including profiling, which produces legal or similarly significant effects.

Key definitions:
- **Profiling:** Any automated processing of personal data to evaluate, analyze, or predict aspects of a natural person (financial situation, behavior, location, health, preferences, etc.)
- **Solely automated decision:** No meaningful human involvement in the decision — a rubber-stamp review does not count as human oversight

**Exceptions to Article 22** (automated decisions ARE permitted when):
1. Necessary for entering into or performance of a contract
2. Authorized by EU or member state law
3. Based on explicit consent

When an exception applies, the controller must still:
- Provide meaningful information about the logic involved
- Allow the data subject to obtain human intervention
- Allow the data subject to express their point of view and contest the decision

> Exam tip: Article 22 applies when the decision is *both* solely automated *and* has legal or similarly significant effects. An automated content recommendation does not trigger Article 22. An automated loan denial does.

### 5.3 Data Subject Rights Relevant to AI

| Right | Article | AI Relevance |
|-------|---------|-------------|
| Right to information | Arts. 13-14 | Must disclose existence of automated decision-making and logic |
| Right of access | Art. 15 | Must provide information about automated processing and its logic |
| Right to rectification | Art. 16 | Correct inaccurate data used to train/operate AI |
| Right to erasure ("right to be forgotten") | Art. 17 | Delete personal data from training sets (technically complex) |
| Right to data portability | Art. 20 | Applicable where processing is by automated means |
| Right not to be subject to automated decisions | Art. 22 | See Section 5.2 above |

### 5.4 Data Protection Impact Assessment (DPIA)

A **DPIA** (Article 35) is mandatory before processing that is "likely to result in a high risk" to individuals. AI systems almost always require a DPIA when they:

- Perform profiling to make decisions with significant effects
- Process special categories of data at scale (biometric, health, political opinion)
- Use systematic monitoring of publicly accessible areas
- Apply new technologies where the privacy implications are unclear

A DPIA must include:
- Systematic description of the processing and its purposes
- Assessment of necessity and proportionality
- Assessment of risks to rights and freedoms of individuals
- Measures to address those risks (including safeguards and security measures)

If the DPIA reveals high residual risk that cannot be mitigated, the controller must consult the supervisory authority (Data Protection Authority) before processing.

### 5.5 Controller vs. Processor in AI Contexts

| Role | Definition | AI Example | Key Obligation |
|------|-----------|-----------|----------------|
| **Controller** | Determines purposes and means of processing | Enterprise using an AI vendor's model to make hiring decisions | Full GDPR compliance; enters into DPA with processor |
| **Processor** | Processes personal data on behalf of the controller | AI model vendor processing HR data for the enterprise | Must only act on controller's documented instructions; Article 28 contract required |
| **Joint Controllers** | Two or more parties jointly determine purposes and means | Two companies co-developing an AI product that processes user data | Must arrange responsibilities between them; Art. 26 agreement required |

> Exam tip: When an AI vendor *also* uses your data to train or improve their model, they may be acting as a controller for that additional purpose — not just a processor. This is a common audit finding and a likely exam scenario.

### 5.6 Key GDPR Principles for AI

- **Data minimization:** Only collect and use the minimum personal data needed for the AI's purpose
- **Purpose limitation:** Data collected for one purpose cannot be repurposed to train an AI without a compatible legal basis
- **Storage limitation:** Personal data used for AI training cannot be retained indefinitely
- **Accuracy:** Inaccurate training data must be corrected or erased — links directly to AI fairness
- **Integrity and confidentiality:** AI systems must implement appropriate security measures

---

## Section 6 — US AI Regulatory Landscape

### 6.1 Federal Level

The US does **not** have a single comprehensive federal AI law (as of 2026). The landscape is:

- **Executive Order 14110 (October 2023):** President Biden's EO on Safe, Secure, and Trustworthy AI — directed agencies to develop AI safety standards, required safety testing disclosures from developers of powerful models, and instructed NIST to develop AI safety guidance. This EO was *rescinded* by President Trump's Executive Order on January 20, 2025. The Trump administration issued its own EO directing agencies to remove "barriers to American AI leadership."
- **NIST AI RMF and AI 600-1:** The main practical voluntary governance tools at federal level; still in effect and still the reference standard for AI risk management
- **Sector-specific agency guidance:** The FTC, FDA, CFPB, EEOC, and HHS have all issued AI-related guidance applying existing statutory authority to AI systems in their sectors (e.g., FTC unfair/deceptive practices, EEOC on employment discrimination)

### 6.2 State Privacy Laws with AI Relevance

Several US states have enacted comprehensive privacy laws with automated decision-making provisions that parallel GDPR Article 22:

| State Law | Effective | Automated Decision / Profiling Provision |
|-----------|----------|----------------------------------------|
| Colorado Privacy Act (CPA) | July 2023 | Right to opt out of profiling for consequential decisions |
| Connecticut Data Privacy Act (CTDPA) | July 2023 | Right to opt out of profiling for consequential decisions |
| Texas Data Privacy & Security Act (TDPSA) | July 2024 | Right to opt out of profiling for consequential decisions |
| Virginia Consumer Data Protection Act (VCDPA) | January 2023 | Right to opt out of automated processing for profiling |
| California CPRA (amends CCPA) | January 2023 | Right to opt out of automated decision-making; DPIA-equivalent required for high-risk processing |

> Exam tip: The US exam questions will not test deep knowledge of individual state laws. Know that multiple states have GDPR-inspired automated decision-making opt-out rights and that these create compliance complexity for AI systems deployed in the US.

### 6.3 AI-Specific US Legislative Efforts (2025–2026)

Congress has introduced numerous AI bills but has not passed comprehensive federal AI legislation as of mid-2026. Key themes being legislated at state level:
- Algorithmic impact assessments
- AI transparency disclosures
- Prohibitions on specific high-risk uses (facial recognition, employment screening)
- AI labeling requirements (synthetic content)

---

## Section 6A — AI Governance Structures & Roles (Objective 4.1)

Objective 4.1 expects you to know *how organizations structure* AI governance and *who does what*.

### Governance structures
- **AI Center of Excellence (AI CoE):** a central, cross-functional team that sets AI standards, vets and approves AI tools/use cases, shares best practices, and provides governance oversight across the organization. It is the hub that prevents fragmented, ungoverned AI adoption (the structural answer to shadow AI).
- **Policies and procedures:** the AI policy, AI acceptable-use policy (7.5), model-risk and data-governance procedures, and review/approval workflows the CoE enforces.
- **Committees / boards:** an AI governance committee or review board that approves high-risk use cases and owns risk tolerance (ties to NIST AI RMF GOVERN).

### AI roles and responsibilities

The official objective (4.1) names **ten** AI-related roles — know each:

| Role | Responsibility |
|---|---|
| **Data scientist** | Builds, trains, and evaluates models; feature/metric selection |
| **AI architect** | Designs the overall AI solution architecture |
| **Machine learning engineer** | Productionizes models (training-to-serving), performance/optimization |
| **Platform engineer** | Builds the underlying compute/data platform AI runs on |
| **MLOps engineer** | CI/CD, deployment, monitoring, drift/retraining automation for models |
| **AI security architect** | Designs and implements security controls for AI systems (Domain 2) |
| **AI governance engineer** | Implements governance controls, guardrails, and policy enforcement in the AI stack |
| **AI risk analyst** | Identifies, assesses, and tracks AI risks; maintains the AI risk register |
| **AI auditor** | Independently assesses AI systems/controls for compliance and effectiveness |
| **Data engineer** | Builds and maintains data pipelines feeding training/inference |

> **Exam tip:** an **AI CoE** is the *structure* that centralizes AI governance; the **AI governance engineer, AI risk analyst, and AI auditor** provide policy enforcement, risk tracking, and independent assurance respectively (don't conflate them). If a scenario describes scattered, unapproved AI adoption, the governance fix is standing up a CoE + policy, not a technical control.

---

## Section 7 — AI Risk Management in Practice

### 7.1 AI Risk Assessment

An **AI risk assessment** applies standard risk methodology (likelihood x impact) to AI-specific threat scenarios. Unique AI risk factors include:

- **Model risk:** The risk that an AI model produces inaccurate, biased, or harmful outputs and that decisions based on those outputs cause harm
- **Training data risk:** Biased, poisoned, or unrepresentative training data produces unreliable models
- **Distributional shift:** The model's real-world input data diverges from the training distribution, degrading performance
- **Emergent behavior:** Large models exhibit unexpected capabilities or behaviors not present during testing
- **Interpretability risk:** Inability to explain model decisions creates accountability gaps and regulatory exposure
- **Operational risk:** AI system failures, latency, or unavailability

### 7.2 AI Impact Assessment

An **AI impact assessment (AIA)** is a structured evaluation of the potential impacts of an AI system on individuals and society *before deployment*. It is distinct from a risk assessment in that it focuses on *outcomes for affected parties*, not just organizational risk. Requirements for AIAs appear in:

- EU AI Act (required for high-risk systems, embedded in conformity assessment)
- Some US state laws (algorithmic impact assessment requirements)
- NIST AI RMF MAP function activities

### 7.3 Third-Party and Vendor AI Risk

Using AI systems built by third parties creates governance gaps:

- **Lack of transparency:** Vendors may not disclose training data, model architecture, or known failure modes
- **Contractual gaps:** Standard SaaS contracts rarely include adequate AI-specific terms (data use for training, model versioning, performance SLAs, incident notification)
- **Supply chain risk:** A compromised or biased foundation model propagates risk to all downstream applications built on it
- **Regulatory accountability:** Deploying a third-party AI model does not transfer the deployer's regulatory liability (you remain the controller under GDPR; you remain responsible under the EU AI Act as deployer)

**Vendor AI due diligence should include:**
- Review of model cards and datasheets
- Contractual prohibition on using your data for model training without consent
- SLAs for model performance and drift monitoring
- Incident notification requirements
- Right to audit or receive third-party audit reports

### 7.4 AI Inventory and Shadow AI

**Shadow AI** refers to AI tools adopted by employees or departments without the knowledge, approval, or oversight of IT or security teams — the AI analog to shadow IT. It is a major governance risk because:

- Personal or confidential data may be submitted to external AI APIs
- The organization has no visibility into what data leaves its environment
- Models used may be unvetted for accuracy, bias, or security
- No contractual protections exist for data submitted to unofficial tools

An **AI system inventory** is the foundation of AI governance: you cannot govern what you do not know exists. The inventory should capture:

- System name and vendor
- Business function/use case
- Data processed (especially personal data or sensitive data)
- Model type and version
- Deployment environment (on-premises, SaaS, embedded in product)
- Risk classification
- Owner/accountable party
- Review/renewal date

### 7.5 AI Acceptable-Use Policy (AI AUP)

An **AI acceptable-use policy** governs how employees may use AI tools — both company-provided and personal. Key elements:

- Approved AI tools list (and prohibition on unapproved tools)
- Prohibited inputs (PII, confidential business data, client data, source code, credentials)
- Output verification requirements (human review before using AI-generated content in deliverables)
- Intellectual property considerations (ownership of AI-generated work product)
- Disclosure requirements (when to disclose AI use to clients or in published content)
- Consequences for policy violation

### 7.6 Corporate Policy Choices: Sanctioned vs. Unsanctioned, Private vs. Public Models, and Data Sovereignty (Objective 4.3)

Objective 4.3 tests several corporate-policy and compliance levers:

- **Sanctioned vs. unsanctioned AI:** sanctioned = vetted, approved, contractually governed tools on the approved list; unsanctioned = shadow AI used without approval. Governance directs users to sanctioned tools and blocks/monitors unsanctioned ones.
- **Private vs. public models:** a core data-governance decision.
  - **Public / third-party hosted models** (public API): fast, cheap, powerful — but prompts/data leave your environment, may be retained or used for training, and create third-party data-sharing and residency exposure.
  - **Private / self-hosted models** (on-prem or private-cloud, often SLMs): data stays in your control — preferred for sensitive/regulated data — at higher cost and operational burden.
  - The rule of thumb the exam rewards: **sensitivity of the data drives the choice** — regulated/confidential data → private/self-hosted; low-sensitivity → public may be acceptable.
- **Sensitive-data governance:** classify data and define what may be sent to which model tier (cross-references Domain 2 labeling and data-minimization).
- **Third-party compliance evaluations:** assess AI vendors for their certifications/attestations (ISO 42001, SOC 2), data-use and training terms, and breach/incident obligations (7.3).
- **Data sovereignty / residency:** data is subject to the laws of the jurisdiction where it is **stored and processed**. Sending data to a model hosted in another country can violate residency requirements (GDPR cross-border transfer rules, sectoral/national data-localization laws). Controls: region-pinned/in-region inference, data-residency contractual terms, and private deployment where cross-border transfer is disallowed.

> **Exam tip — data sovereignty:** if a scenario worries about *where* data is physically processed or which country's laws apply (e.g., EU patient data sent to a US-hosted model), the concept is **data sovereignty/residency**, and the control is in-region or private/self-hosted inference plus lawful-transfer mechanisms.

---

## Section 8 — Documentation and Transparency

### 8.1 Model Cards

A **model card** is a standardized document that accompanies an AI model and describes:

- Intended use cases and out-of-scope uses
- Model architecture (at a high level)
- Training data description (sources, size, preprocessing)
- Evaluation results (performance metrics on benchmark datasets)
- Known limitations and failure modes
- Ethical considerations and bias evaluation
- Who should and should not use the model

Model cards were introduced by researchers at Google (Mitchell et al., 2018) and are now a near-universal best practice. The EU AI Act's technical documentation requirements for high-risk AI systems overlap significantly with model card content.

### 8.2 Datasheets for Datasets

A **datasheet for a dataset** (Gebru et al., 2018) documents:

- Motivation for creating the dataset
- Composition (what data, how much, who is represented)
- Collection process (methods, timeframes, consent)
- Preprocessing/cleaning steps
- Uses (intended and prohibited)
- Distribution (how the dataset is shared or restricted)
- Maintenance (updates, known issues)

> Exam tip: Model cards document the *model*. Datasheets document the *dataset*. System cards (see below) document the *deployed system*. These are distinct artifacts — examiners will test whether you know the difference.

### 8.3 System Cards

A **system card** (introduced by Meta AI, adopted broadly) documents an AI system *as deployed*, not just the underlying model. It includes:

- The specific deployment context and use case
- Which models, tools, and data pipelines are integrated
- Safety evaluations conducted before deployment
- Limitations specific to this deployment context
- Human oversight mechanisms in place

### 8.4 AI Bill of Materials (AI-BOM)

An **AI-BOM** (analogous to a Software Bill of Materials / SBOM) inventories all components of an AI system:

- Foundation/base model(s) and versions
- Fine-tuning datasets and sources
- Inference infrastructure (libraries, frameworks: PyTorch, TensorFlow, etc.)
- Third-party APIs called by the model
- Plugins, tools, or agents integrated
- Training compute environment

The AI-BOM is critical for **supply chain risk management** — if a component is found to be compromised or biased, the AI-BOM tells you which systems are affected.

---

## Section 9 — Bias, Fairness, Explainability, and Accountability

### 9.0 Responsible AI Principles (Objective 4.2)

Objective 4.2 frames "Responsible AI" as a named set of principles (widely used in industry, e.g., Microsoft's Responsible AI standard). These overlap with — but are *not identical to* — the NIST trustworthy-AI characteristics (Section 1.7). Know the set:

| Principle | Meaning |
|---|---|
| **Fairness** | Treats people equitably; avoids discriminatory outcomes |
| **Reliability & safety** | Performs consistently and safely under expected and edge conditions |
| **Privacy & security** | Protects data and resists attack throughout the lifecycle |
| **Inclusiveness** | Designed to serve and be accessible to diverse people, including the marginalized |
| **Transparency** | Stakeholders understand how the system works and its limitations |
| **Accountability** | People remain answerable for AI outcomes; clear ownership |
| **Explainability** | Outputs/decisions can be explained to relevant stakeholders |
| **Consistency** | The system behaves predictably across similar inputs and over time |
| **Awareness training** | Users/operators are trained to recognize they are interacting with AI and to understand its proper use, limits, and risks |

Associated **responsible-AI risks** the exam pairs with these: **deliberate bias introduction**, **accidental data leakage**, **reputational loss**, **performance risk** and **intellectual-property risk**, risks of **autonomous systems** acting without adequate oversight, and **shadow IT / shadow AI** (Section 7.4).

> **Exam tip:** if a question uses the term **"Responsible AI"** and lists principles like **inclusiveness, consistency, or awareness**, it's testing this industry principle set — not the NIST trustworthy-AI characteristics. NIST is the *framework*; Responsible AI principles are the *value set*. Fairness/accountability/explainability appear in both.

### 9.1 Bias and Fairness

**Algorithmic bias** occurs when an AI system produces outputs that systematically favor or disadvantage a group. Sources of bias:

- **Historical bias:** Training data reflects past discrimination (e.g., historical hiring data that underrepresents women in technical roles)
- **Representation bias:** Training data underrepresents certain groups
- **Measurement bias:** Proxy variables correlate with protected characteristics (using ZIP code as a proxy for race)
- **Aggregation bias:** A single model performs poorly for specific subgroups

**Key fairness metrics (exam level — conceptual):**

| Metric | Definition |
|--------|-----------|
| **Demographic parity** | The AI system produces positive outcomes at equal rates across demographic groups |
| **Equal opportunity** | True positive rates are equal across groups (e.g., a hiring tool correctly identifies qualified candidates equally for all groups) |
| **Predictive parity** | When the model predicts "positive," the precision is equal across groups |

> Exam tip: No single fairness metric satisfies all criteria simultaneously (the "impossibility theorem" of fairness). The exam may present a scenario where you must choose the *most appropriate* fairness metric for a given context.

### 9.2 Explainability and Interpretability

These are separate NIST AI RMF trustworthy-AI characteristics (see Section 1.7):

- **Interpretable models:** Inherently understandable — decision trees, linear regression, rule-based systems. You can follow the logic step by step.
- **Explainable AI (XAI):** Post-hoc methods that explain black-box model outputs:
  - **SHAP (SHapley Additive exPlanations):** Assigns each feature a contribution value for a specific prediction, based on game theory
  - **LIME (Local Interpretable Model-agnostic Explanations):** Approximates the model locally around a specific prediction with a simpler interpretable model

**Why it matters for GRC:**
- Regulators (especially under GDPR Art. 22 and EU AI Act) require meaningful explanations of AI decisions
- Without explainability, internal audit cannot evaluate whether a model is performing as intended
- Explainability supports human oversight — a human reviewer needs to understand *why* the AI recommended an action to meaningfully oversee it

### 9.3 Human Oversight

**Human oversight** is a requirement in both the NIST AI RMF (GOVERN and MANAGE functions) and the EU AI Act (mandatory for high-risk AI). Key concepts:

- **Human-in-the-loop (HITL):** A human reviews and approves every AI decision before it is acted upon
- **Human-on-the-loop (HOTL):** AI makes decisions automatically, but a human monitors and can intervene
- **Human-in-command:** Humans retain the ultimate ability to shut down, override, or decommission an AI system

> Exam tip: "Human oversight" in the EU AI Act for high-risk systems means the deployer must ensure a human can *understand, monitor, and intervene* — it does not necessarily require human-in-the-loop for every decision. The level of oversight must match the risk.

### 9.4 Accountability

**Accountability** for AI means:
- Clear ownership is assigned for each AI system's outcomes
- Responsibility is not diffused across multiple parties without explicit allocation
- Mechanisms exist to trace a decision back to its source (the model, the data, the configuration, the human who approved it)
- Consequences exist for failures (operational, legal, reputational)

In supply chain contexts, accountability is often tested by asking: *when an AI vendor's model causes harm, who is accountable to the regulator?* The answer under GDPR and the EU AI Act is the **deployer/controller** — not the model vendor/processor — unless the vendor is also acting as a controller.

---

## Section 10 — Audit, Evidence, and Continuous Monitoring for AI

### 10.1 AI Audit

An AI audit evaluates whether an AI system is performing as intended, within policy, and in compliance with applicable obligations. AI audit goes beyond traditional IT audit because it must assess:

- **Model performance:** Are accuracy, precision, recall, and other KPIs within acceptable thresholds?
- **Data quality:** Is the training and operational data representative, accurate, and governed?
- **Bias evaluation:** Has the system been tested for discriminatory outcomes across demographic groups?
- **Documentation completeness:** Do model cards, datasheets, and system cards exist and are they current?
- **Change management:** Are model updates, retraining events, and version changes logged and reviewed?
- **Human oversight effectiveness:** Are oversight mechanisms functioning as designed?

### 10.2 Evidence for AI Assurance

Evidence that an AI system is governed appropriately includes:

- AI system inventory (current and complete)
- Model cards, datasheets, system cards, AI-BOM (documented and version-controlled)
- Risk assessment documentation
- DPIA (where required)
- Bias testing results and remediation records
- Model performance monitoring dashboards and thresholds
- Incident logs for AI-related events
- Training records for employees using AI systems
- Vendor contracts with AI-specific clauses
- Change/version control logs for model updates

### 10.3 Continuous Monitoring for AI

AI systems require *ongoing* monitoring because:
- Models degrade over time as real-world data drifts from training data (**model drift / concept drift**)
- New adversarial attacks emerge that were not present at deployment
- The deployment context can change (new user populations, new regulatory requirements)
- AI outputs can have cumulative bias effects not visible in single-instance evaluation

Monitoring should track:
- Prediction accuracy vs. ground truth (where available)
- Output distribution shifts
- Input data distribution changes
- Alert rates and false positive/negative rates (for security AI)
- Anomalous usage patterns (potential misuse or adversarial probing)

---

## Section 11 — AI Incident Response

### 11.1 What Constitutes an AI Incident

An **AI incident** includes, but is not limited to:
- Model producing outputs that cause harm (financial, physical, reputational, discriminatory)
- Adversarial attack succeeding (prompt injection leading to data exfiltration, model poisoning detected)
- Unauthorized access to AI model weights or training data
- Significant unexplained performance degradation
- Discovery of bias causing discriminatory outcomes
- AI system generating prohibited content (harassment, CSAM, dangerous instructions)
- Misuse by employees (policy violations, feeding confidential data to unapproved AI tools)

### 11.2 How AI IR Differs from Traditional IR

| Aspect | Traditional Cybersecurity IR | AI-Specific IR |
|--------|----------------------------|---------------|
| Detection | Logs, SIEM, EDR alerts | Model monitoring dashboards, output audits, user reports |
| Containment | Isolate affected system, block IOC | Roll back model version, disable AI feature, apply output filters |
| Eradication | Remove malware, patch vulnerability | Retrain model on clean data, correct poisoned training set |
| Recovery | Restore from backup | Redeploy validated model version; validate with held-out test set |
| Root cause | Exploit, vulnerability, misconfiguration | Biased training data, adversarial input, prompt injection, model architecture flaw |
| Notification | GDPR 72-hour, state breach laws | EU AI Act serious incident reporting; sector-specific requirements |

### 11.3 AI Incident Reporting Obligations

- **EU AI Act:** Providers of high-risk AI systems must report "serious incidents" to national market surveillance authorities. A serious incident is one that causes (or could cause) death, serious harm to health, serious damage to property, or significant disruption of critical infrastructure. The timeline for reporting is 15 days for serious incidents, 3 days for life-threatening events.
- **GDPR:** If an AI incident involves a personal data breach, the standard GDPR 72-hour notification to the supervisory authority applies, plus notification to affected individuals if high risk to their rights and freedoms.
- **Sector-specific:** Healthcare AI incidents may trigger HIPAA breach notification; financial AI incidents may trigger SEC or banking regulator reporting.

---

## Section 12 — Glossary of Must-Know Acronyms

| Acronym | Full Term |
|---------|----------|
| AI RMF | AI Risk Management Framework (NIST) |
| AIMS | Artificial Intelligence Management System (ISO/IEC 42001) |
| AIA | AI Impact Assessment |
| AI-BOM | AI Bill of Materials |
| AUP | Acceptable-Use Policy |
| CoE | Center of Excellence (AI CoE — central AI governance structure) |
| CSF | Cybersecurity Framework (NIST) |
| DPIA | Data Protection Impact Assessment (GDPR Art. 35) |
| ERM | Enterprise Risk Management |
| GPAI | General-Purpose AI (EU AI Act term for foundation models) |
| HITL | Human-in-the-Loop |
| HOTL | Human-on-the-Loop |
| LIA | Legitimate Interests Assessment (GDPR) |
| LIME | Local Interpretable Model-agnostic Explanations |
| MLOps | Machine Learning Operations |
| OECD | Organisation for Economic Co-operation and Development |
| PII | Personally Identifiable Information |
| RAG | Retrieval-Augmented Generation |
| SBOM | Software Bill of Materials |
| SHAP | SHapley Additive exPlanations |
| XAI | Explainable AI |

---

## Section 13 — Exam Tips and Commonly Confused Concepts

**Tip 1 — GOVERN vs. MAP**
GOVERN is organization-wide (policies, culture, accountability structures). MAP is system-specific (contextualizing risk for a particular AI deployment). If a question describes writing an enterprise AI policy, that is GOVERN. If it describes identifying the risks of a specific AI hiring tool, that is MAP.

**Tip 2 — EU AI Act tiers vs. GDPR**
The EU AI Act and GDPR are separate laws with separate obligations that often *both* apply to the same AI system. A high-risk AI system under the EU AI Act that processes personal data must comply with both. Do not conflate DPIA (GDPR) with the EU AI Act's conformity assessment — they are different documents serving different laws.

**Tip 3 — Controller vs. Processor**
The question "who is the controller?" is answered by: who decided WHY the data is being processed and HOW? If you decide to use an AI vendor's tool to analyze your customers' data, you are the controller. The vendor is the processor. You cannot contract away controller liability.

**Tip 4 — Model card vs. datasheet vs. system card**
Model card = the model. Datasheet = the dataset. System card = the deployed system. These are tested by describing a scenario and asking which artifact is appropriate. If the scenario involves understanding what training data was used for a model, the answer is datasheet. If it involves understanding how a model performs on specific demographic groups, the answer is model card.

**Tip 5 — NIST AI RMF is not ISO 42001**
NIST AI RMF is voluntary and non-certifiable. ISO/IEC 42001 is a certifiable management system standard. If a question asks which framework an organization would use to *achieve certification* for its AI governance, the answer is ISO/IEC 42001. If it asks which US NIST framework provides voluntary AI risk guidance, the answer is AI RMF 1.0.

**Tip 6 — EU AI Act prohibited vs. high-risk**
"Prohibited" means banned — cannot be used at all. "High-risk" means heavily regulated — can be used but requires extensive controls. Social scoring by governments is prohibited. A credit-scoring AI is high-risk. Candidates confuse these under time pressure.

**Tip 7 — Article 22 trigger**
Article 22 requires BOTH conditions: (1) solely automated AND (2) legal or similarly significant effects. An AI that recommends content without any legal/significant effect does NOT trigger Article 22. An AI that automates a credit decision or parole decision DOES.

---

## Section 14 — Practice Questions

**Instructions:** Choose the best answer. Aim to complete these 18 questions in under 18 minutes to simulate exam pace.

---

**Q1.** An organization is creating an enterprise-wide AI ethics policy, defining accountability structures for AI use, and setting risk tolerance thresholds for AI deployment. Which NIST AI RMF function does this activity primarily correspond to?

A. MAP
B. MEASURE
C. GOVERN
D. MANAGE

---

**Q2.** A financial services company uses an AI model to automatically deny loan applications without any human review. An applicant in the EU receives a denial. Which GDPR article gives the applicant the right to contest this decision?

A. Article 6 — Lawful basis for processing
B. Article 15 — Right of access
C. Article 22 — Automated decision-making and profiling
D. Article 35 — Data protection impact assessment

---

**Q3.** Which of the following EU AI Act risk classifications applies to a government-operated social scoring system that ranks citizens based on behavior?

A. Minimal risk
B. Limited risk
C. High risk
D. Unacceptable risk

---

**Q4.** A security analyst discovers that employees across three departments have been submitting client contracts to a free AI summarization tool without IT approval, creating potential data leakage. What governance artifact would PRIMARILY prevent this behavior?

A. AI Bill of Materials (AI-BOM)
B. AI acceptable-use policy
C. Model card
D. DPIA

---

**Q5.** Which NIST AI RMF trustworthy-AI characteristic specifically addresses the ability of an AI system to resist adversarial attacks and maintain functionality under stress?

A. Reliable
B. Accountable
C. Safe
D. Secure and Resilient

---

**Q6.** An organization is evaluating an AI hiring tool that a vendor provides as a SaaS product. The vendor uses client data to retrain the model without explicit permission. Under GDPR, how should this be classified?

A. The vendor is acting as a processor only, since it provides a service to the organization
B. The vendor is acting as a controller for the retraining purpose, since it determines the means and purpose of that processing
C. The organization bears no liability because it contracted out the AI function
D. This is permitted under the legitimate interests lawful basis without further action

---

**Q7.** Which document would a compliance officer consult to understand what demographic groups were underrepresented in the data used to train a third-party AI model?

A. Model card
B. System card
C. Datasheet for datasets
D. AI-BOM

---

**Q8.** Under the EU AI Act, which obligation for high-risk AI systems became enforceable FIRST?

A. High-risk system conformity assessments (August 2026)
B. Prohibited practices bans (February 2025)
C. GPAI model obligations (August 2025)
D. High-risk system registration in the EU database (August 2027)

---

**Q9.** A data science team retrained a credit-risk model and deployed it without updating the model card, notifying the risk committee, or conducting a new bias evaluation. Which NIST AI RMF function was most deficient in this scenario?

A. GOVERN
B. MAP
C. MEASURE
D. MANAGE

---

**Q10.** An AI system used for real-time emotion recognition on job interview video recordings is deployed in Germany. Under the EU AI Act, what risk classification most likely applies?

A. Minimal risk — emotion recognition is a standard AI feature
B. Limited risk — the system must only disclose it is AI
C. High risk — the system involves biometric data in employment decisions
D. Unacceptable risk — real-time biometric surveillance is prohibited in the EU

---

**Q11.** Which of the following BEST describes the difference between NIST AI RMF 1.0 and ISO/IEC 42001?

A. NIST AI RMF is a certifiable management system; ISO 42001 is a voluntary framework
B. ISO/IEC 42001 is an international certifiable management system standard; NIST AI RMF is a voluntary US framework
C. Both are voluntary frameworks; neither supports third-party certification
D. ISO/IEC 42001 applies only to AI developers; NIST AI RMF applies only to AI deployers

---

**Q12.** A post-hoc explanation method assigns each input feature a contribution value to a specific prediction, using a game-theory-derived approach to fairly attribute model output across features. Which method is described?

A. LIME
B. SHAP
C. Decision tree pruning
D. Gradient-based saliency mapping

---

**Q13.** Under the NIST AI RMF, which trustworthy-AI characteristic is defined as providing the AI system's outputs in a way that stakeholders can understand, even if the underlying model mechanism remains opaque?

A. Interpretable
B. Explainable
C. Accountable
D. Transparent (this is not listed as a separate NIST characteristic)

---

**Q14 — Performance-Based Scenario.** Read the following scenario and answer the two-part question.

*MediAssist Health Corp. uses an AI system that analyzes patient medical records and automatically generates treatment priority scores. The scores are directly used by nursing staff to determine which patients receive care first in a hospital ward. The system processes health records of EU residents. MediAssist licensed the underlying model from a US-based AI vendor. The vendor's contract does not restrict the vendor from using MediAssist's patient data for model improvement.*

**(A)** Under the EU AI Act, what risk classification applies to this AI system, and what is the single most critical operational obligation MediAssist must ensure is in place?

A. Limited risk — disclose to patients that AI is being used
B. High risk — implement a functional human oversight mechanism
C. Unacceptable risk — AI in healthcare is prohibited
D. Minimal risk — clinical decision support tools are exempt

**(B)** Under GDPR, what is the status of the vendor's use of patient data for model improvement, and what must MediAssist do?

A. The vendor is acting as processor; the current contract is sufficient because it is in writing
B. The vendor is acting as a joint controller for model improvement; MediAssist must establish an Article 26 arrangement
C. The vendor is acting as a separate controller for model improvement; MediAssist must obtain a new lawful basis (or restrict the vendor's use contractually), and may need to update the DPIA
D. Patient data can be used for model improvement under the legitimate interests of the vendor without further action

---

**Q15.** A company's AI adoption is fragmented: each department picks its own tools with no shared standards, vetting, or oversight. Which governance structure MOST directly addresses this?

A. A datasheet for each dataset
B. An AI Center of Excellence (CoE) with an approval/standards mandate
C. A model registry
D. A DPIA for each tool

---

**Q16.** A vendor markets its AI as "Responsible AI" and specifically claims **inclusiveness** and **awareness**. Which statement BEST reflects what these principles require?

A. The model must be certifiable under ISO 42001 and registered in the EU database
B. The system must be designed to serve diverse users (inclusiveness) and must inform users they are interacting with AI (awareness)
C. They are identical to the NIST trustworthy-AI characteristics of Secure and Reliable
D. They require differential privacy and federated learning

---

**Q17.** A hospital wants to use an LLM to summarize EU patient records but must ensure the data is never processed outside the EU and never leaves its control. Which deployment choice and concept are MOST relevant?

A. A public third-party model API; data minimization
B. A private/self-hosted (in-region) model; data sovereignty/residency
C. Any public model with output filtering; purpose limitation
D. A public model with a longer context window; homogenization

---

**Q18.** An organization is deciding whether to send a class of data to a public hosted LLM API or to a self-hosted private model. Which factor should MOST drive the decision?

A. The context window size of each model
B. The sensitivity/classification of the data being processed
C. Which model has more parameters
D. The number of MCP servers available

---

### Answer Key

**Q15 — B. AI Center of Excellence.** A cross-functional CoE that sets standards and vets/approves tools is the structural fix for fragmented, ungoverned adoption. The other options are artifacts/assessments, not governing structures.

**Q16 — B.** Inclusiveness = designed to serve diverse people; awareness = users are informed they're interacting with AI and how to use it properly. These are Responsible-AI principles, distinct from NIST characteristics and from certification/PETs.

**Q17 — B.** Keeping EU data processed in-region and under the org's control is a **data sovereignty/residency** requirement, best met by a private/self-hosted in-region deployment.

**Q18 — B.** Data sensitivity/classification is the governing factor: regulated/confidential data → private/self-hosted; low-sensitivity → public may be acceptable. Context window, parameter count, and MCP availability are not the governance driver.

---

**Q1 — C. GOVERN**
GOVERN covers organization-wide policies, accountability, risk tolerance, and culture for AI risk management. MAP, MEASURE, and MANAGE are system-specific activities.

**Q2 — C. Article 22**
Article 22 provides the right not to be subject to solely automated decisions with legal or similarly significant effects. A loan denial is a legally significant decision. Article 35 is the DPIA requirement (incorrect for this question — a DPIA is a pre-processing assessment, not a data subject right).

**Q3 — D. Unacceptable risk**
Government-operated social scoring is explicitly listed as a prohibited (unacceptable risk) practice in the EU AI Act and was among the first provisions to take effect in February 2025.

**Q4 — B. AI acceptable-use policy**
An AI AUP governs which tools employees may use and prohibits submitting sensitive data to unapproved tools. The AI-BOM and model card are documentation artifacts, not employee-behavior governance tools. A DPIA is a pre-processing risk assessment.

**Q5 — D. Secure and Resilient**
The NIST AI RMF explicitly names "Secure and Resilient" as a single trustworthy-AI characteristic covering adversarial resistance and recovery. "Reliable" addresses consistent performance, not adversarial robustness specifically.

**Q6 — B. The vendor is acting as a controller for the retraining purpose**
When the vendor determines a new purpose for processing (improving its own model), it becomes a controller for that purpose — not a processor. The organization cannot contract away its own controller liability and must address this in the DPA or contract.

**Q7 — C. Datasheet for datasets**
Datasheets for datasets document the composition of training data, including representation across demographic groups. Model cards reference this but the primary source of data composition detail is the datasheet.

**Q8 — B. Prohibited practices bans (February 2025)**
The EU AI Act's phased timeline made prohibited practices (unacceptable risk bans) effective first, on February 2, 2025. High-risk system conformity assessment obligations follow in August 2026.

**Q9 — D. MANAGE**
MANAGE covers implementing risk controls, change management, monitoring, and documentation updates for deployed AI systems. Retraining without updating documentation, notifying governance bodies, or re-evaluating bias is a MANAGE deficiency. If the organization had no policy requiring these steps at all, GOVERN would also be implicated, but the most direct deficiency in the *operational* failure described is MANAGE.

**Q10 — C. High risk**
AI systems used in employment decisions (including screening) involving biometric data are classified as high-risk under the EU AI Act. Real-time biometric surveillance in public spaces is prohibited, but a controlled interview setting with employer consent mechanisms is high-risk, not unacceptable. (Note: emotion recognition in the workplace context is explicitly listed as high-risk in EU AI Act Annex III.)

**Q11 — B. ISO/IEC 42001 is an international certifiable management system standard; NIST AI RMF is a voluntary US framework**
ISO/IEC 42001 uses Annex SL structure and supports third-party certification. NIST AI RMF is voluntary and does not support certification. Both apply to developers and deployers — the audience is not the distinguishing factor.

**Q12 — B. SHAP**
SHAP (SHapley Additive exPlanations) uses Shapley values from cooperative game theory to assign each feature a contribution to a specific prediction. LIME uses a locally approximated simpler model and does not use game theory.

**Q13 — B. Explainable**
NIST AI RMF defines Explainable as the characteristic where outputs are understandable to stakeholders even without transparency into the model mechanism. Interpretable requires the mechanism itself to be understandable. "Transparent" is not listed as a separate NIST AI RMF trustworthy-AI characteristic.

**Q14(A) — B. High risk**
Clinical decision support tools that directly influence medical treatment prioritization are high-risk under the EU AI Act (Annex III, medical device context and critical decisions about individuals' health). The system is not unacceptable risk; healthcare AI is not categorically prohibited. The most critical operational obligation for high-risk systems is human oversight — nursing staff must be able to understand, monitor, and override the AI's prioritization.

**Q14(B) — C. The vendor is acting as a separate controller for model improvement**
The vendor is a processor for MediAssist's operational use of the model. However, by using patient health data (a special category under GDPR Art. 9) to improve its own model, the vendor is determining a new purpose — making it a controller for that processing. This is not permitted under GDPR without a valid lawful basis. MediAssist must contractually prohibit this use or ensure a compliant framework exists, and must update its DPIA to reflect this risk. Options A and D both incorrectly allow the data use. Option B is wrong because joint controllers jointly determine purposes — here the vendor is acting independently for its own purpose.

---

*End of Domain 4 — AI Governance, Risk & Compliance*
