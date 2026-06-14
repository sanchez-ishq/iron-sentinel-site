# CompTIA SecAI+ (CY0-001 V1) — Domain 4 Practice Question Bank

Domain 4 bank — 55 questions, objectives 4.1–4.3.

**Coverage:** AI Governance, Risk, and Compliance (19%)
**Objectives mapped:** 4.1 Organizational governance structures | 4.2 Risks associated with AI | 4.3 Impact of compliance
**Format:** Single best answer unless labeled (Choose two). ~5 performance-based scenarios labeled (PBQ).
**Instructions:** Complete all 55 questions before checking the Answer Key. Aim for ~1 minute per question to simulate exam pace.

> Note: All questions are original and are not reproduced from CompTIA materials. They are grounded in the official SecAI+ CY0-001 V1 Exam Objectives Document v2.0 (© 2025 CompTIA). This bank supplements — and does not duplicate — the 18 in-module questions in `04-domain4-ai-governance-risk-compliance.md`.

---

## Domain 4.1 — Organizational Governance Structures (Questions 1–18)

---

**Q1.** A company discovers that its marketing, finance, and HR departments are independently procuring and deploying separate AI tools with no coordination, shared standards, or centralized oversight. Which governance structure is MOST appropriate to remedy this situation?

A. Appoint an AI risk analyst to maintain a risk register for each department's tools independently  
B. Establish an AI Center of Excellence with cross-functional membership and an AI tool approval mandate  
C. Require each department to publish a model card for its AI systems  
D. Deploy a SIEM to monitor API calls from each AI tool  

---

**Q2.** An AI Center of Excellence (AI CoE) has just been established at a mid-size financial services firm. Which of the following activities falls MOST squarely within the CoE's mandate?

A. Writing the Python code to train the firm's credit-risk model  
B. Configuring the compute cluster on which AI models run  
C. Establishing an AI tool vetting and approval process that all departments must follow  
D. Responding to adversarial prompt injection attempts against the firm's customer chatbot  

---

**Q3.** Which of the following BEST describes the primary function of an AI governance engineer within an AI team?

A. Independently evaluating AI systems to determine whether they comply with applicable regulations  
B. Assessing and tracking AI-specific risks and maintaining the AI risk register  
C. Implementing policy guardrails, automated controls, and enforcement mechanisms in the AI technology stack  
D. Designing the overall AI solution architecture for new projects  

---

**Q4.** A company's legal team is concerned that AI-generated outputs are used in client deliverables without any review, and that employees are submitting confidential client data to unapproved AI tools. Which governance artifact MOST directly governs this employee behavior?

A. AI Bill of Materials (AI-BOM)  
B. Datasheet for datasets  
C. AI acceptable-use policy  
D. AI impact assessment  

---

**Q5.** An organization needs an individual who will independently assess whether its deployed AI credit-scoring model is operating within policy, producing fair outputs, and meeting regulatory obligations — without being part of the team that developed or operates the model. Which role BEST fits this description?

A. AI risk analyst  
B. AI auditor  
C. AI governance engineer  
D. MLOps engineer  

---

**Q6.** A company is building a real-time fraud detection pipeline. One team member builds and maintains the CI/CD pipelines that automatically retrain the model when performance degrades and deploy new versions to production. Which role BEST describes this person?

A. Data scientist  
B. Machine learning engineer  
C. MLOps engineer  
D. Platform engineer  

---

**Q7.** Which of the following role descriptions BEST matches a data engineer on an AI project?

A. Selects model architecture, defines training objectives, and evaluates model performance metrics  
B. Designs the AI solution to integrate with enterprise systems and defines the overall technical approach  
C. Builds and maintains data pipelines, data lakes, and the data infrastructure that feeds model training and inference  
D. Deploys the trained model to a serving endpoint and optimizes inference latency  

---

**Q8.** An organization's AI governance committee is reviewing a new use case in which the company wants to deploy a generative AI system to assist HR staff in screening resumes. Which of the following actions represents the PRIMARY function of an AI risk analyst in this context?

A. Implementing technical guardrails in the AI pipeline to prevent biased outputs  
B. Auditing the AI system after deployment to assess compliance with the firm's AI policy  
C. Identifying, assessing, and documenting risks associated with the proposed AI system and its expected impact on applicants  
D. Writing the AI acceptable-use policy that HR staff will sign before using the system  

---

**Q9.** A platform engineer's role on an AI project is BEST described as:

A. Translating a trained model from a research notebook into a production-ready, scalable serving architecture  
B. Building and maintaining the underlying compute, networking, and storage infrastructure on which AI workloads run  
C. Designing security controls specifically for the AI system to resist adversarial attacks  
D. Coordinating cross-functional AI governance and setting risk tolerance thresholds  

---

**Q10.** Which pairing of role and responsibility is CORRECT?

A. AI architect — builds and maintains the data pipelines feeding model training  
B. AI security architect — independently evaluates AI systems for regulatory compliance  
C. Machine learning engineer — productionizes trained models, including optimization and serving  
D. AI governance engineer — maintains the AI risk register and tracks residual risk  

---

**Q11.** An enterprise's AI policy requires that all AI systems processing personal data be registered in a central AI system inventory before go-live. An employee in the sales department deploys a third-party AI lead-scoring tool without registering it or seeking approval. This behavior is BEST described as:

A. Shadow AI  
B. Model drift  
C. Prompt injection  
D. IP-related risk  

---

**Q12.** The AI CoE at a healthcare organization has published an approved tools list, defined prohibited data inputs for each tool tier, and established a required review process for new AI use cases. Which element of organizational AI governance does this PRIMARILY represent?

A. AI risk register  
B. AI policies and procedures  
C. AI-BOM  
D. NIST AI RMF MAP function  

---

**Q13.** (Choose two) Which of the following are responsibilities that distinguish the AI auditor role from the AI risk analyst role?

A. Maintaining the ongoing AI risk register  
B. Performing independent assessments of AI controls and systems  
C. Identifying and prioritizing new AI risks for the risk register  
D. Producing audit reports with findings and recommendations for remediation  
E. Implementing policy guardrails in the AI technology stack  

---

**Q14.** An AI architect is asked to design a new AI-powered document classification system. Which of the following activities is MOST aligned with this role?

A. Writing the data ingestion scripts that pull documents from the content management system  
B. Selecting the model type, defining integration patterns with existing enterprise systems, and specifying deployment topology  
C. Retraining the model monthly and monitoring production performance metrics  
D. Reviewing the model's outputs quarterly to assess compliance with the document classification policy  

---

**Q15.** A company wants to ensure its AI development and deployment practices have a formal governance structure that prevents individual teams from bypassing security reviews. Which of the following BEST serves as the organizational mechanism to enforce this?

A. A model card for each AI system  
B. An AI Center of Excellence with a mandatory review-and-approval workflow  
C. A DPIA conducted for every AI project  
D. A SHAP-based explanation log attached to every model output  

---

**Q16.** An organization's AI CoE charter requires that employees who use company-approved AI tools complete periodic training on AI limitations, bias risks, output verification, and safe use. This requirement maps to which Responsible AI principle?

A. Consistency  
B. Inclusiveness  
C. Awareness training  
D. Reliability and safety  

---

**Q17.** Which of the following statements about the AI Center of Excellence (CoE) and shadow AI is MOST accurate?

A. Shadow AI is an expected outcome of a well-functioning CoE because the CoE processes approvals slowly  
B. The AI CoE is the governance structure whose existence and approval function is the primary organizational defense against shadow AI adoption  
C. Shadow AI only occurs in organizations without a SIEM capable of monitoring API traffic  
D. The AI CoE is responsible for responding to adversarial attacks on AI systems, not for preventing shadow AI  

---

**Q18. (PBQ)** Read the following scenario and answer the question.

*Apex Corp. has 4,000 employees and no centralized AI governance. Over the past year, usage of AI tools has grown organically: the customer support team uses one chatbot platform, the sales team uses an AI CRM enrichment tool, the engineering team uses a code-generation assistant, and the HR team uses an AI resume screener. None of these tools were vetted by security or legal. Employees in three teams have submitted customer data to public AI APIs. No one has an inventory of which tools process personal data.*

Which combination of immediate governance actions would MOST effectively bring this environment under control? (Choose two)

A. Immediately retrain all AI models in use to remove customer data from training sets  
B. Establish an AI Center of Excellence with cross-functional membership to own governance, vetting, and approval going forward  
C. Require each team to produce a SHAP explanation report for every AI output used in a business decision  
D. Conduct an AI system inventory to identify all AI tools in use, what data they process, and who owns each  
E. Deploy a decision tree model to replace all neural-network models, since decision trees are inherently interpretable  

---

## Domain 4.2 — Risks Associated with AI (Questions 19–35)

---

**Q19.** A health insurance company trains an AI model to predict patient readmission risk using historical claims data. An analysis later reveals that the model assigns higher risk scores to patients in certain ZIP codes, which correlate strongly with race due to historical residential segregation patterns. Which type of bias BEST explains this outcome?

A. Representation bias — the training set underrepresents high-income ZIP codes  
B. Measurement bias — a proxy variable (ZIP code) correlates with a protected characteristic (race)  
C. Aggregation bias — a single model is used for a population that is too large  
D. Label bias — human annotators applied labels inconsistently across patient groups  

---

**Q20.** An employee at a law firm pastes a confidential client legal brief into a public LLM to generate a summary. The employee did not realize the public model's terms of service permit the provider to use submitted content for model improvement. Which AI-specific risk does this MOST directly represent?

A. Introduction of bias  
B. Reputational loss  
C. Accidental data leakage  
D. Autonomous systems risk  

---

**Q21.** A financial services firm's AI fraud detection model produces significantly different false positive rates for customers in rural areas compared to urban customers. Customers flagged as fraudulent are temporarily blocked from making transactions. Which Responsible AI principle is MOST directly violated?

A. Consistency  
B. Fairness  
C. Awareness training  
D. Reliability and safety  

---

**Q22.** A company deploys an AI-powered customer service chatbot that, over several months, begins producing responses that are increasingly off-brand, occasionally provides incorrect pricing information, and in one instance gave a customer erroneous medical advice. Which AI risk does this scenario MOST closely reflect?

A. IP-related risk  
B. Shadow AI  
C. Accuracy and performance of the model  
D. Accidental data leakage  

---

**Q23.** A developer asks an internal code-generation AI to help write a function, and the AI produces output that closely reproduces a section of GPL-licensed open-source code without attribution or disclosure. Which category of AI risk does this MOST directly represent?

A. Introduction of bias  
B. IP-related risk  
C. Shadow AI  
D. Reputational loss  

---

**Q24.** An AI system is deployed at a manufacturing plant to automatically adjust conveyor belt speeds and machinery settings based on real-time sensor readings. A sensor malfunction causes the model to receive corrupted input data, and the model autonomously raises speeds to unsafe levels before any human can intervene. Which risk category MOST accurately describes the primary concern?

A. Accidental data leakage  
B. Introduction of bias  
C. Autonomous systems risk  
D. IP-related risk  

---

**Q25.** A company's marketing team has been quietly using an AI content generation tool that is not on the approved tools list, not reviewed by legal or security, and not disclosed to the IT department. The tool's vendor privacy policy allows the vendor to use submitted content for model training. Which term BEST describes the governance failure represented by the marketing team's use of this tool?

A. Model drift  
B. Shadow AI  
C. Overfitting  
D. Prompt injection  

---

**Q26.** Under the Responsible AI framework, the principle of **inclusiveness** MOST directly requires an AI system to:

A. Resist adversarial manipulation and maintain performance under stress  
B. Provide post-hoc explanations for its outputs using methods such as SHAP or LIME  
C. Be designed and tested to serve diverse users, including those with disabilities or from underrepresented populations  
D. Produce the same output when given the same input across different sessions  

---

**Q27.** A media company's AI-generated news article summarization service produces an article that falsely attributes a controversial statement to a public figure. The story is published and shared widely before the error is caught. Which AI risk category does this MOST directly represent?

A. Introduction of bias  
B. Autonomous systems risk  
C. Reputational loss  
D. IP-related risk  

---

**Q28.** Which of the following BEST describes the Responsible AI principle of **consistency**?

A. The AI system's outputs can be explained to business stakeholders in plain language  
B. The AI system behaves predictably across similar inputs and does not produce erratic, unpredictable outputs over time  
C. The AI system is designed to include diverse user populations in its testing and deployment planning  
D. The AI system protects personal data and resists unauthorized access  

---

**Q29.** A company's AI product recommendation engine is found to systematically recommend premium products to users identified as high-income while suggesting budget alternatives to users identified as lower-income, based on inferred demographic signals in browsing history. Which TWO Responsible AI principles are MOST directly at risk? (Choose two)

A. Awareness training  
B. Fairness  
C. Consistency  
D. Inclusiveness  
E. Privacy and security  

---

**Q30.** An organization's AI policy requires that any AI system capable of taking autonomous action — such as executing transactions, sending external communications, or modifying records — must require human approval before the action is executed. This policy MOST directly mitigates which AI risk?

A. Accidental data leakage  
B. Introduction of bias  
C. Autonomous systems risk  
D. Shadow AI  

---

**Q31.** A company is deploying an AI chatbot that answers customer questions about its banking products. The Responsible AI team requires that at the start of every conversation, the chatbot discloses to customers that they are speaking with an AI system, not a human agent. This requirement maps to which Responsible AI principle?

A. Explainability  
B. Fairness  
C. Consistency  
D. Awareness training  

---

**Q32.** (PBQ) Read the following scenario and answer the question.

*DataDriven Inc. trained a resume-screening model using 10 years of historical hiring data from the company. Analysis of the historical data reveals that 78% of the people hired into technical roles during that period were men, and that the model now assigns significantly lower "fit scores" to resumes with women's college names and traditionally female names. The company is unaware of this behavior until a rejected candidate complains.*

Which TWO actions directly address the AI risks demonstrated in this scenario? (Choose two)

A. Deploy the model to a private self-hosted environment to prevent accidental data leakage  
B. Conduct a bias evaluation (e.g., demographic parity or equal opportunity testing) to quantify the disparity before the next deployment  
C. Implement awareness training for HR employees explaining how to verify and challenge AI-generated scores  
D. Encrypt the model weights at rest using AES-256  
E. Apply output filtering to remove the model's confidence score from the HR UI  

---

**Q33.** Which Responsible AI principle MOST directly requires that users of an AI system be trained to understand they are interacting with AI, know its limitations, and know how to verify its outputs?

A. Transparency  
B. Accountability  
C. Awareness training  
D. Explainability  

---

**Q34.** An organization discovers that a third-party AI vendor's model — which the organization has embedded in its customer-facing product — was trained on a dataset that systematically underrepresents non-English-speaking users. As a result, the model performs significantly worse for those users. Which Responsible AI principle does the organization's continued use of this model MOST directly violate?

A. Accountability  
B. Consistency  
C. Inclusiveness  
D. Reliability and safety  

---

**Q35.** Which of the following scenarios MOST clearly represents an IP-related risk introduced by AI?

A. An AI model produces outputs that are less accurate for users in rural ZIP codes compared to urban ZIP codes  
B. An employee submits the company's proprietary product roadmap to a public LLM for summarization, and the LLM's provider retains and potentially uses that content  
C. An autonomous AI agent executes a financial transaction without waiting for human approval  
D. An AI model's performance degrades over time because the real-world data distribution has shifted from the training distribution  

---

## Domain 4.3 — Impact of Compliance (Questions 36–55)

---

**Q36.** Under the EU AI Act, which of the following AI systems would be classified in the PROHIBITED (unacceptable risk) tier?

A. An AI system that analyzes creditworthiness to support lending decisions  
B. An AI chatbot that recommends products to e-commerce customers  
C. A government-operated system that scores citizens' behavior across multiple domains to restrict access to public services  
D. An AI system used in university admissions screening  

---

**Q37.** A US-based company licenses an AI hiring tool and begins deploying it to screen job applicants in Germany. The EU AI Act applies to this deployment because:

A. The EU AI Act applies only to AI companies headquartered in the EU  
B. The EU AI Act applies to any AI system placed on the EU market or put into service in the EU, regardless of where the provider is based  
C. The EU AI Act applies only if the company has more than 500 employees  
D. The EU AI Act applies only if the AI system processes biometric data  

---

**Q38.** An organization subject to the EU AI Act has deployed a high-risk AI system. Which of the following is NOT listed as a mandatory obligation for high-risk AI systems under the Act?

A. Implementing a risk management system documented throughout the lifecycle  
B. Ensuring automatic logging and record-keeping of operations  
C. Obtaining ISO/IEC 42001 certification before market placement  
D. Registering the system in the EU AI database  

---

**Q39.** Under the EU AI Act's implementation timeline, which obligation took effect FIRST?

A. Mandatory conformity assessments for high-risk AI systems  
B. General-Purpose AI (GPAI) model obligations  
C. Prohibited practices bans  
D. Mandatory registration of high-risk systems in the EU AI database  

---

**Q40.** An organization wants to pursue formal, third-party certified AI governance to demonstrate to enterprise clients and regulators that its AI management system meets an internationally recognized standard. Which framework MOST directly supports this goal?

A. NIST AI RMF 1.0  
B. OECD AI Principles  
C. ISO/IEC 42001  
D. NIST AI 600-1 (Generative AI Profile)  

---

**Q41.** ISO/IEC 23894 is BEST described as:

A. A certifiable requirements standard for establishing an AI Management System (AIMS)  
B. Guidance on managing risk specific to AI systems, complementing ISO/IEC 42001  
C. A binding EU regulation governing the use of AI in high-risk sectors  
D. A NIST publication providing a voluntary framework for AI risk management  

---

**Q42.** A company already holds ISO 27001 certification and wants to extend its management system to cover AI governance. Which ISO standard is MOST directly designed for integration with ISO 27001 due to its shared Annex SL high-level structure?

A. ISO/IEC 23894  
B. NIST AI RMF 1.0  
C. ISO/IEC 42001  
D. NIST AI 600-1  

---

**Q43.** Which of the following BEST describes the NIST AI RMF GOVERN function?

A. It assesses and quantifies AI risks using metrics, testing, and benchmarking for a specific AI system  
B. It establishes organization-wide AI policies, accountability structures, risk tolerance, and a culture of AI risk awareness  
C. It identifies and categorizes AI risks in the context of a specific AI system and its deployment environment  
D. It implements and monitors controls that address prioritized AI risks for a specific system  

---

**Q44.** A company is using the NIST AI RMF and has just completed an activity in which it identified the intended purpose of a new AI content moderation system, characterized the deployment context, listed all stakeholders who could be affected by the system's decisions, and assigned the system an initial risk category. Which NIST AI RMF function does this MOST closely represent?

A. GOVERN  
B. MAP  
C. MEASURE  
D. MANAGE  

---

**Q45.** An AI risk manager is tracking performance metrics for a deployed AI system, conducting red-team evaluations to test for bias and adversarial vulnerability, and assessing the outputs of third-party AI component testing. Which NIST AI RMF function does this activity MOST closely represent?

A. GOVERN  
B. MAP  
C. MEASURE  
D. MANAGE  

---

**Q46.** An organization has identified that its AI fraud detection model is producing a high rate of false positives for a specific customer segment and has decided to retrain the model, implement additional output monitoring thresholds, and document the residual risk. Which NIST AI RMF function does this MOST closely represent?

A. GOVERN  
B. MAP  
C. MEASURE  
D. MANAGE  

---

**Q47.** Which of the following MOST accurately states the relationship between ISO/IEC 42001 and the NIST AI RMF?

A. They are equivalent frameworks; an organization achieving NIST AI RMF compliance is automatically eligible for ISO/IEC 42001 certification  
B. ISO/IEC 42001 is a certifiable management system standard with requirements (shalls); NIST AI RMF is a voluntary, non-certifiable framework — both can be used together but neither replaces the other  
C. NIST AI RMF supersedes ISO/IEC 42001 for US-based organizations  
D. ISO/IEC 42001 applies only to AI providers; NIST AI RMF applies only to AI deployers  

---

**Q48.** The OECD AI Principles are BEST described in relation to the EU AI Act as:

A. The binding enforcement mechanism for the EU AI Act  
B. Non-binding intergovernmental principles that served as a conceptual foundation and influenced the development of the EU AI Act  
C. A certifiable framework that organizations must meet before submitting to EU AI Act conformity assessment  
D. An updated version of the EU AI Act incorporating OECD-member country amendments  

---

**Q49.** A hospital system wants to use a large language model to assist physicians in drafting clinical notes using EU patient data. The IT team is evaluating whether to use a public third-party API or a self-hosted private model. The compliance team's primary concern is that patient health data must be processed only within the EU and must never be transmitted to or stored by a third-party service provider in another country. Which concept MOST directly governs this requirement, and which deployment approach satisfies it?

A. Data minimization; use a public API with output filtering  
B. Purpose limitation; use a public API with contractual data-use restrictions  
C. Data sovereignty/residency; use a private self-hosted in-region model  
D. Model accuracy; use the public API because it has more parameters and will produce better clinical notes  

---

**Q50.** An organization's AI policy specifies that employees may use only tools appearing on the IT-approved AI tools list, and that using any AI tool not on that list is a policy violation subject to disciplinary action. Tools on the approved list have been vetted by security and legal, have signed data processing agreements in place, and meet the firm's data-handling requirements. Which policy concept does the approved list represent?

A. The distinction between private and public models  
B. Sanctioned AI tools, as opposed to unsanctioned (shadow) AI  
C. The NIST AI RMF MEASURE function  
D. A third-party compliance evaluation  

---

**Q51.** (PBQ) Read the following scenario.

*GlobalBank Corp. operates in the EU, US, and Singapore. It is evaluating a third-party AI vendor's model for use in loan underwriting decisions. The model is hosted on cloud infrastructure in the United States. The vendor's contract does not restrict the vendor from using GlobalBank's customer data to improve its own models. GlobalBank's EU customers include individuals whose personal data is protected under GDPR. Singapore has enacted data residency requirements mandating that financial customer data be processed locally.*

Which combination of compliance concerns does this scenario MOST directly raise? (Choose two)

A. EU AI Act classification concern: the loan underwriting AI is high-risk and requires a conformity assessment before deployment  
B. NIST AI RMF certification gap: GlobalBank cannot deploy the model without NIST AI RMF certification  
C. Data sovereignty/residency concern: EU customer data sent to US-hosted inference violates GDPR cross-border transfer requirements and Singapore data must be processed locally  
D. Responsible AI concern: the model lacks SHAP explainability output and therefore violates the OECD AI Principles  
E. Shadow AI concern: because the vendor is a third party, the model is automatically classified as shadow AI  

---

**Q52.** An organization discovers that its AI vendor is using the organization's proprietary customer transaction data to improve the vendor's general-purpose model, which is then sold to other customers including competitors. The organization's contract with the vendor did not prohibit this use. Which of the following BEST describes the compliance and governance failures present?

A. The vendor violated the EU AI Act's high-risk conformity assessment requirement  
B. The organization failed to conduct a third-party compliance evaluation that included data-use terms review, and the vendor's activity may constitute a GDPR controller relationship for which the organization bears accountability as data controller  
C. The organization is in violation of NIST AI RMF GOVERN because it did not publish an AI policy  
D. The vendor committed shadow AI by using the data without disclosure  

---

**Q53.** A company's AI governance policy states that AI models processing confidential business data, PII, or regulated data must be deployed in private self-hosted environments, while models processing only non-sensitive internal data may use approved public APIs. This policy is BEST described as:

A. A sanctioned vs. unsanctioned AI tool classification  
B. A data sovereignty framework  
C. A private vs. public model governance policy driven by data sensitivity  
D. A third-party compliance evaluation process  

---

**Q54. (PBQ)** Read the following scenario.

*ManuLogix, a supply chain analytics company, has developed an AI system that predicts shipment delays and automatically reroutes shipments, notifies customers, and updates ERP records — all without human review of individual decisions. The system processes data from EU-based shipper customers. ManuLogix's CTO argues that the system is low-risk because it handles supply chain logistics, not personal data about individuals. The legal team disagrees. The EU AI Act compliance team has been asked to classify the system and determine applicable obligations.*

(A) The legal team's concern most likely relates to which EU AI Act concept?

A. The system is a GPAI model and therefore subject to separate GPAI model obligations regardless of risk tier  
B. Even if the system is not high-risk under Annex III, the automation of consequential decisions without human oversight may implicate EU AI Act transparency obligations if customers are affected, and GDPR obligations if any personal data is processed  
C. The system is automatically prohibited because it uses autonomous decision-making  
D. The system is high-risk because all logistics AI systems are listed in Annex III of the EU AI Act  

---

**Q55. (PBQ)** Read the following scenario.

*A regional hospital network is deploying an AI triage system that assigns priority scores to emergency room patients based on vital signs and reported symptoms. The system is designed to present scores to nursing staff who then make final triage decisions. The network's compliance officer wants to know: (1) what EU AI Act risk tier applies; (2) what NIST AI RMF function governs the establishment of the human oversight policy; (3) whether ISO/IEC 42001 or NIST AI RMF provides a path to third-party certification of the hospital's AI governance program; and (4) which Responsible AI principle specifically requires that the system be usable and appropriately designed for patients and staff of all backgrounds, including those with limited English proficiency.*

Select the answer that correctly addresses ALL FOUR questions.

A. High risk | GOVERN | ISO/IEC 42001 | Inclusiveness  
B. Minimal risk | MAP | NIST AI RMF | Fairness  
C. High risk | MANAGE | NIST AI RMF | Transparency  
D. Limited risk | GOVERN | ISO/IEC 42001 | Awareness training  

---

## Answer Key

**Q1 — B. Establish an AI Center of Excellence**
A cross-functional AI CoE with an approval mandate is the structural governance solution for fragmented, uncoordinated AI adoption across departments. An AI risk analyst (A) tracks risks but does not govern procurement. A model card (C) documents a model but does not govern adoption. A SIEM (D) is a security monitoring tool, not a governance structure.

**Q2 — C. Establishing an AI tool vetting and approval process**
The CoE's core governance function is setting standards and controlling which AI tools are approved for use. Coding the model (A) is a data scientist or ML engineer function. Configuring compute (B) is a platform engineer function. Responding to adversarial attacks (D) is a security function.

**Q3 — C. Implementing policy guardrails, automated controls, and enforcement mechanisms**
The AI governance engineer implements governance controls in the tech stack. The AI auditor (A) independently evaluates compliance. The AI risk analyst (B) assesses and tracks risks. The AI architect (D) designs the overall solution architecture.

**Q4 — C. AI acceptable-use policy**
An AI AUP governs which tools employees may use and prohibits submitting confidential data to unapproved tools. The AI-BOM (A) inventories AI components. A datasheet (B) documents training data. A DPIA (D) is a pre-processing privacy risk assessment.

**Q5 — B. AI auditor**
The AI auditor independently assesses AI systems against policy and regulatory requirements. The AI risk analyst (A) identifies and tracks risks but is typically embedded in the operational team. The AI governance engineer (C) implements controls. The MLOps engineer (D) manages deployment pipelines.

**Q6 — C. MLOps engineer**
The MLOps engineer owns the CI/CD pipelines for model retraining and deployment, monitoring, and automation. The data scientist (A) trains and evaluates models. The ML engineer (B) productionizes models but is not specifically focused on CI/CD automation for retraining cycles. The platform engineer (D) builds the underlying compute infrastructure.

**Q7 — C. Builds and maintains data pipelines, data lakes, and data infrastructure**
This is the data engineer role. The data scientist (A) trains models. The AI architect (B) designs the overall solution. The ML engineer (D) deploys and optimizes the serving layer.

**Q8 — C. Identifying, assessing, and documenting risks**
The AI risk analyst identifies, assesses, and maintains the risk register for a proposed system. Implementing technical guardrails (A) is the AI governance engineer. Post-deployment auditing (B) is the AI auditor. Policy writing (D) is typically led by the governance team or legal, not the risk analyst.

**Q9 — B. Building and maintaining the underlying compute, networking, and storage infrastructure**
This is the platform engineer. Productionizing models (A) is the ML engineer. Designing security controls (C) is the AI security architect. Setting risk tolerance (D) is a governance/CoE function.

**Q10 — C. Machine learning engineer — productionizes trained models, including optimization and serving**
This is correct. The AI architect designs solutions, not the data pipelines (A). The AI security architect designs AI security controls, not audits (B). The AI risk analyst, not the AI governance engineer, maintains the risk register (D).

**Q11 — A. Shadow AI**
Deploying an AI tool without IT/security approval and without registering it in the AI inventory is the definition of shadow AI. Model drift (B) is performance degradation over time. Prompt injection (C) is an adversarial attack. IP-related risk (D) involves intellectual property exposure.

**Q12 — B. AI policies and procedures**
An approved tools list, prohibited input rules, and review procedures are the substance of AI policies and procedures. An AI risk register (A) tracks risks. An AI-BOM (C) inventories components. The NIST AI RMF MAP function (D) contextualizes risk for specific systems; it is not an organizational policy artifact.

**Q13 — B and D. (Choose two)**
The AI auditor performs independent assessments (B) and produces audit reports with findings (D). Maintaining the ongoing risk register (A) and identifying/prioritizing new risks (C) are AI risk analyst functions. Implementing stack guardrails (E) is the AI governance engineer.

**Q14 — B. Selecting model type, defining integration patterns, and specifying deployment topology**
This is AI architect work. Writing data ingestion scripts (A) is data engineering. Monthly retraining and monitoring (C) is MLOps. Quarterly compliance review (D) is auditing.

**Q15 — B. An AI Center of Excellence with a mandatory review-and-approval workflow**
The CoE provides the organizational enforcement mechanism. A model card (A) documents a model. A DPIA (C) assesses privacy risk; it is not a bypass-prevention mechanism. A SHAP log (D) is an explainability tool.

**Q16 — C. Awareness training**
Periodic training for AI users on limitations, bias risks, output verification, and safe use is the Responsible AI principle of awareness training. Consistency (A) is about predictable behavior. Inclusiveness (B) is about serving diverse users. Reliability and safety (D) is about consistent, harm-free performance.

**Q17 — B. The AI CoE is the governance structure that is the primary organizational defense against shadow AI**
The CoE's approval function prevents ungoverned adoption. Shadow AI is not expected from a functioning CoE (A). Shadow AI does not require absence of SIEM (C). The CoE's role is governance, not adversarial defense (D).

**Q18 — B and D. (Choose two)**
Establishing an AI CoE (B) provides the governance structure going forward. Conducting an AI system inventory (D) identifies what already exists and what data it touches — the essential first step. Retraining existing models (A) is not the immediate governance priority and may not be feasible. SHAP reports (C) are explainability tools, not governance controls. Replacing all neural networks with decision trees (E) is operationally unrealistic and not a governance action.

**Q19 — B. Measurement bias — a proxy variable (ZIP code) correlates with a protected characteristic**
ZIP code is a proxy variable that encodes racial segregation due to historical housing discrimination. This is measurement bias. Representation bias (A) relates to underrepresentation of groups in training data, not proxy encoding. Aggregation bias (C) occurs when a single model performs poorly for subgroups. Label bias (D) involves inconsistent human annotation.

**Q20 — C. Accidental data leakage**
Submitting confidential client data to a public LLM that retains it for training is accidental data leakage — the data leaves the organization's control unintentionally through an AI tool. Introduction of bias (A) is about discriminatory model outputs. Reputational loss (B) is a downstream consequence, not the primary risk category. Autonomous systems risk (D) involves uncontrolled AI action.

**Q21 — B. Fairness**
Differential false positive rates across geographic/demographic groups resulting in disparate impacts on customers is a fairness violation. Consistency (A) is about predictable behavior across similar inputs. Awareness training (C) is about user education. Reliability and safety (D) is about consistent, harm-free performance broadly.

**Q22 — C. Accuracy and performance of the model**
The chatbot's degrading output quality, incorrect information, and harmful responses over time represent accuracy and performance risk — the model is not performing as intended. IP-related risk (A) involves intellectual property. Shadow AI (B) is ungoverned adoption. Accidental data leakage (D) involves data leaving the organization.

**Q23 — B. IP-related risk**
A model reproducing GPL-licensed code without attribution exposes the organization to intellectual property liability. Introduction of bias (A) involves discriminatory outputs. Shadow AI (C) is ungoverned adoption of AI tools. Reputational loss (D) may be a consequence but is not the primary risk category.

**Q24 — C. Autonomous systems risk**
An AI that autonomously controls physical machinery, takes harmful actions based on corrupted input, and does so without human intervention before harm occurs is the definition of autonomous systems risk. Accidental data leakage (A) involves data exposure. Introduction of bias (B) involves discriminatory outputs. IP-related risk (D) involves intellectual property.

**Q25 — B. Shadow AI**
Using an AI tool without IT/security knowledge, approval, or contractual protections is shadow AI. Model drift (A) is performance degradation. Overfitting (C) is a training deficiency. Prompt injection (D) is an adversarial attack technique.

**Q26 — C. Be designed and tested to serve diverse users, including those with disabilities or from underrepresented populations**
Inclusiveness in Responsible AI requires the system to be designed for diverse users. Adversarial resistance (A) is reliability and safety or the NIST secure-and-resilient characteristic. Post-hoc explanations (B) are the explainability principle. Producing the same output for the same input (D) is the consistency principle.

**Q27 — C. Reputational loss**
Falsely attributing a controversial statement to a public figure in a widely distributed article is a reputational harm event for the company. Introduction of bias (A) involves discriminatory outputs. Autonomous systems risk (B) involves uncontrolled AI actions. IP-related risk (D) involves intellectual property.

**Q28 — B. The AI system behaves predictably across similar inputs and does not produce erratic outputs over time**
Consistency is the principle of predictable, stable behavior. Explainability (A) relates to outputs being understandable. Inclusiveness (C) relates to serving diverse populations. Privacy and security (D) relates to data protection.

**Q29 — B and D. (Choose two)**
Systematically recommending different product tiers based on inferred demographic signals violates Fairness (B) — treating users differently based on demographic proxies — and Inclusiveness (D) — failing to serve all user populations equitably. Awareness training (A) is about user education on AI. Consistency (C) is about predictable behavior. Privacy and security (E) is about data protection.

**Q30 — C. Autonomous systems risk**
Requiring human approval before AI agents execute consequential actions is the primary control for autonomous systems risk. Accidental data leakage (A) involves data exposure. Introduction of bias (B) involves discriminatory outputs. Shadow AI (D) is ungoverned AI adoption.

**Q31 — D. Awareness training**
Disclosing to users that they are interacting with an AI rather than a human is an awareness requirement. Explainability (A) involves explaining AI outputs or reasoning. Fairness (B) involves equitable treatment. Consistency (C) involves predictable behavior.

**Q32 — B and C. (Choose two)**
Conducting a bias evaluation (B) directly addresses the fairness/bias risk by quantifying the disparity and informing remediation before next deployment. Implementing awareness training (C) ensures HR staff know to verify and challenge AI scores rather than accepting them uncritically — a key Responsible AI and human oversight control. Private deployment (A) addresses data leakage, not bias. Encrypting model weights (D) is a data security control, not a bias control. Removing the confidence score from the UI (E) obscures information without fixing the underlying bias.

**Q33 — C. Awareness training**
The Responsible AI principle of awareness training specifically requires that users understand they are interacting with AI, its limitations, and how to properly verify its outputs. Transparency (A) is about the system's understandability to stakeholders broadly. Accountability (B) is about ownership and consequences. Explainability (D) is about explaining outputs/decisions.

**Q34 — C. Inclusiveness**
A model that performs significantly worse for non-English-speaking users due to underrepresentation in training data fails the Responsible AI inclusiveness principle — it is not designed to serve all user populations. Accountability (A) relates to clear ownership. Consistency (B) relates to predictable behavior. Reliability and safety (D) is about consistent performance broadly — inclusiveness is the more specific and direct answer here.

**Q35 — B. An employee submits a proprietary product roadmap to a public LLM, and the LLM retains it**
This is IP-related risk: proprietary intellectual property leaves the organization's control via an AI tool. Differential accuracy across demographics (A) is a bias/fairness risk. An autonomous agent executing transactions without approval (C) is autonomous systems risk. Performance degradation from distribution shift (D) is accuracy and performance risk.

**Q36 — C. A government-operated system that scores citizens' behavior across multiple domains to restrict access to public services**
Government-operated social scoring is explicitly prohibited (unacceptable risk) under the EU AI Act. Credit scoring (A) is high-risk. A product recommendation chatbot (B) is limited or minimal risk. University admissions AI (D) is high-risk.

**Q37 — B. The EU AI Act applies to any AI system placed on the EU market or put into service in the EU, regardless of where the provider is based**
The EU AI Act has extraterritorial reach analogous to GDPR — it applies based on where the AI output is used, not where the provider is headquartered. Company size (C) and biometric data (D) are not the jurisdictional triggers.

**Q38 — C. Obtaining ISO/IEC 42001 certification before market placement**
ISO/IEC 42001 certification is not required by the EU AI Act. The Act requires conformity assessment, technical documentation, risk management systems, logging, transparency, human oversight, accuracy/security, and registration (A, B, D) — but does not mandate any specific ISO certification.

**Q39 — C. Prohibited practices bans**
The prohibited practices (unacceptable risk) provisions took effect on February 2, 2025 — the first provisions to be enforced. GPAI obligations (B) applied from August 2, 2025. High-risk conformity assessments (A) apply from August 2, 2026. Registration (D) is part of the high-risk obligations.

**Q40 — C. ISO/IEC 42001**
ISO/IEC 42001 is the only certifiable AI management system standard among the options, supporting formal third-party audit and certification. NIST AI RMF (A) is voluntary and non-certifiable. OECD AI Principles (B) are non-binding intergovernmental principles. NIST AI 600-1 (D) is the NIST Generative AI Profile, not a certifiable standard.

**Q41 — B. Guidance on managing risk specific to AI systems, complementing ISO/IEC 42001**
ISO/IEC 23894:2023 is a guidance standard (not a requirements standard) providing AI-specific risk management guidance intended to be used alongside ISO 42001. ISO/IEC 42001 (A) is the certifiable requirements standard. The EU AI Act (C) is the binding regulation. NIST AI RMF (D) is the US voluntary framework.

**Q42 — C. ISO/IEC 42001**
ISO/IEC 42001 uses the Annex SL high-level structure, which is the same structure used by ISO 27001, ISO 9001, ISO 22301, and other ISO management system standards — enabling direct integration. ISO/IEC 23894 (A) is a guidance standard, not an Annex SL management system. NIST frameworks (B, D) do not share the Annex SL structure.

**Q43 — B. Establishes organization-wide AI policies, accountability structures, risk tolerance, and a culture of AI risk awareness**
GOVERN is the organization-wide function. Assessing and quantifying risks using metrics (A) is MEASURE. Identifying and categorizing risks for a specific system (C) is MAP. Implementing and monitoring controls (D) is MANAGE.

**Q44 — B. MAP**
Identifying the intended purpose, characterizing the deployment context, listing affected stakeholders, and assigning a risk category for a specific AI system are MAP activities. GOVERN (A) is organization-wide policy and culture. MEASURE (C) involves quantifying risk through metrics and testing. MANAGE (D) involves implementing and monitoring controls.

**Q45 — C. MEASURE**
Tracking performance metrics, conducting red-team evaluations, and assessing third-party component testing are MEASURE activities — quantifying and evaluating risk. GOVERN (A) is organization-wide. MAP (B) contextualizes risk. MANAGE (D) implements controls.

**Q46 — D. MANAGE**
Implementing risk treatments (retraining, additional thresholds), prioritizing response, and documenting residual risk are MANAGE activities. GOVERN (A) is organization-wide. MAP (B) identifies and categorizes risk. MEASURE (C) quantifies risk.

**Q47 — B. ISO/IEC 42001 is a certifiable management system; NIST AI RMF is voluntary and non-certifiable — both can be used together**
This is the key distinguishing fact. They are not equivalent for certification purposes (A). NIST AI RMF does not supersede ISO 42001 (C). Both frameworks apply to developers and deployers — audience is not the distinguishing factor (D).

**Q48 — B. Non-binding intergovernmental principles that served as a conceptual foundation and influenced the EU AI Act**
The OECD AI Principles (first adopted 2019) are non-binding and are the documented conceptual influence on the EU AI Act's structure. They are not an enforcement mechanism (A), not a certification framework (C), and not an amendment vehicle (D).

**Q49 — C. Data sovereignty/residency; use a private self-hosted in-region model**
The requirement that EU patient data be processed only within the EU and not transmitted to a third-party provider in another country is a data sovereignty and residency requirement. The control that satisfies it is a private self-hosted in-region deployment. Data minimization (A) and purpose limitation (B) are GDPR principles but are not the concept that addresses where data is processed. Model parameter count (D) is not a compliance consideration.

**Q50 — B. Sanctioned AI tools, as opposed to unsanctioned (shadow) AI**
An IT-approved tools list with vetted tools and signed data processing agreements represents the concept of sanctioned AI — tools formally approved for organizational use, as opposed to unsanctioned shadow AI tools. Private vs. public model distinction (A) is a separate policy dimension. The NIST MEASURE function (C) quantifies risk. A third-party compliance evaluation (D) is an assessment process.

**Q51 — A and C. (Choose two)**
The loan underwriting AI is high-risk under EU AI Act Annex III (credit scoring is explicitly listed) and requires a conformity assessment before deployment (A). EU customer data sent to a US-hosted model raises GDPR cross-border transfer concerns, and Singapore's data residency laws require local processing of financial customer data (C). NIST AI RMF does not provide a certification requirement (B). SHAP is not an OECD Principles requirement (D). A vetted third-party vendor tool is not automatically shadow AI (E).

**Q52 — B. The organization failed to conduct a third-party compliance evaluation including data-use terms review, and the vendor may be acting as a separate controller**
This is a vendor due diligence failure (no contractual data-use restriction) and a GDPR controller issue (the vendor, by using data for its own model improvement, is acting as a controller for that purpose — making the deployer potentially complicit). The EU AI Act conformity assessment (A) applies to the AI system, not to training data use. NIST AI RMF GOVERN failure (C) is not the most direct compliance issue. Shadow AI (D) refers to ungoverned employee AI adoption, not vendor behavior.

**Q53 — C. A private vs. public model governance policy driven by data sensitivity**
Requiring private self-hosted deployment for sensitive/regulated data and permitting public APIs only for non-sensitive data is the private vs. public model governance policy, driven by data sensitivity. This is distinct from sanctioned vs. unsanctioned (A), which governs whether a tool is approved at all. Data sovereignty (B) addresses geographic jurisdiction of processing. A third-party compliance evaluation (D) is an assessment process.

**Q54 — B. Even if not high-risk under Annex III, the automation of consequential decisions without human oversight may implicate EU AI Act transparency obligations if customers are affected, and GDPR obligations if any personal data is processed**
The legal team's concern is that autonomous decisions affecting customers (delivery timing, notifications) may involve personal data (shipper customer records) triggering GDPR, and that EU AI Act limited-risk transparency obligations may apply even if the system is not Annex III high-risk. The system is not categorically a GPAI model (A) — GPAI refers to foundation models. Autonomous decision-making is not automatically prohibited (C). Logistics AI is not universally listed as Annex III high-risk (D).

**Q55 — A. High risk | GOVERN | ISO/IEC 42001 | Inclusiveness**
(1) An AI triage system in emergency healthcare that assigns priority scores influencing patient care is high-risk under the EU AI Act (Annex III covers AI in medical/healthcare decision support). (2) GOVERN is the NIST AI RMF function that establishes organization-wide policies and accountability structures, including the human oversight policy. (3) ISO/IEC 42001 is the certifiable management system standard; NIST AI RMF is voluntary and non-certifiable. (4) Inclusiveness is the Responsible AI principle requiring the system to serve diverse populations, including patients with limited English proficiency. All four answers in option A are correct.

---

*End of Domain 4 Question Bank — 55 questions covering objectives 4.1, 4.2, and 4.3.*
