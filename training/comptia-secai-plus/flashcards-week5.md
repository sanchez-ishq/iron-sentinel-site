# SecAI+ (CY0-001) — Week 5 Flashcards: Domain 4 Terminology

**Scope:** Domain 4 — AI Governance, Risk & Compliance (objectives 4.1–4.3), 19% of the exam.
**How to use:** Cover the indented answer, read the **bold front**, recall aloud, reveal. ~60 cards. (Anki TSV at bottom.)

> This domain rewards *precise* terminology — NIST AI RMF functions, EU AI Act tiers, and the role taxonomy are near-certain question fodder.

---

## Objective 4.1 — Governance Structures & Roles

**1. AI Center of Excellence (AI CoE)**
> A central, cross-functional team that sets AI standards, vets/approves AI tools and use cases, and provides oversight — the structural fix for fragmented/shadow AI adoption.

**2. AI policies and procedures**
> The AI policy, acceptable-use policy, and model-risk/data-governance procedures the CoE enforces.

**3. Data scientist**
> Builds, trains, and evaluates models; feature and metric selection.

**4. AI architect**
> Designs the overall AI solution architecture.

**5. Machine learning engineer**
> Productionizes models (training-to-serving), performance and optimization.

**6. Platform engineer**
> Builds the underlying compute/data platform AI runs on.

**7. MLOps engineer**
> CI/CD, deployment, monitoring, and drift/retraining automation for models.

**8. AI security architect**
> Designs and implements security controls for AI systems (Domain 2).

**9. AI governance engineer**
> Implements governance controls, guardrails, and policy enforcement within the AI stack.

**10. AI risk analyst**
> Identifies, assesses, and tracks AI risks; maintains the AI risk register.

**11. AI auditor**
> Independently assesses AI systems/controls for compliance and effectiveness.

**12. Data engineer**
> Builds and maintains the data pipelines feeding training and inference.

---

## Objective 4.2 — Responsible AI & Risks

**13. Fairness**
> The system treats people equitably and avoids discriminatory outcomes.

**14. Reliability and safety**
> The system performs consistently and safely under expected and edge conditions.

**15. Transparency**
> Stakeholders can understand how the system works and its limitations.

**16. Privacy and security**
> The system protects data and resists attack throughout its lifecycle.

**17. Explainability**
> The system's outputs/decisions can be explained to relevant stakeholders.

**18. Inclusiveness**
> The system is designed to serve and be accessible to diverse people, including the marginalized.

**19. Accountability**
> People remain answerable for AI outcomes; clear ownership exists.

**20. Consistency**
> The system behaves predictably across similar inputs and over time.

**21. Awareness training**
> Users/operators are trained to recognize they're interacting with AI and understand its proper use, limits, and risks.

**22. Introduction of bias (risk)**
> Bias entering the model via skewed data, feedback, or fine-tuning — accidental or deliberate.

**23. Accidental data leakage**
> Sensitive data unintentionally exposed via model outputs, logs, or third-party tools.

**24. Reputational loss**
> Harm to brand/trust from AI failures, bias incidents, or misuse.

**25. Accuracy & performance risk**
> The model's outputs are wrong or degrade over time, causing harm from decisions made on them.

**26. IP-related risks**
> Training-data copyright, output ownership, and leakage of proprietary data/models.

**27. Autonomous systems (risk)**
> Systems acting without adequate human oversight, causing outsized or unintended harm.

**28. Shadow IT / Shadow AI**
> Tools (Shadow IT) or AI tools (Shadow AI) adopted without IT/security knowledge or approval — a major governance risk.

---

## Objective 4.3 — Compliance Impact

**29. EU AI Act**
> The EU's binding, risk-tiered AI regulation. Applies to AI placed on the EU market or whose output is used in the EU.

**30. EU AI Act — Unacceptable risk**
> Prohibited practices (e.g., government social scoring) — banned outright. (Prohibitions took effect first, Feb 2025.)

**31. EU AI Act — High risk**
> Consequential systems (hiring, credit, medical, law enforcement). Require risk management, data governance, human oversight, documentation, and registration.

**32. EU AI Act — Limited risk**
> Transparency obligations (e.g., chatbots and deepfakes must disclose AI).

**33. EU AI Act — Minimal risk**
> Most AI (spam filters, game AI) — no mandatory obligations.

**34. OECD AI Principles**
> Non-binding intergovernmental principles that influenced later AI regulation including the EU AI Act.

**35. ISO/IEC 42001**
> A **certifiable** AI Management System (AIMS) standard (Annex SL). Third-party auditable — unlike the voluntary NIST AI RMF.

**36. ISO/IEC 23894**
> Guidance standard for AI risk management; used alongside ISO 42001 (adapts ISO 31000 for AI).

**37. NIST AI RMF**
> A voluntary, non-certifiable US framework for managing AI risk via four functions and trustworthy-AI characteristics.

**38. NIST AI RMF — GOVERN**
> Establishes org-wide AI policies, accountability, culture, and risk tolerance. (Only function that's organization-wide.)

**39. NIST AI RMF — MAP**
> Contextualizes risk for a *specific* AI system — stakeholders, risk tier, where in the lifecycle risk arises.

**40. NIST AI RMF — MEASURE**
> Analyzes/quantifies risk via metrics, testing, red-teaming, benchmarking.

**41. NIST AI RMF — MANAGE**
> Implements treatments, tracks residual risk, change management, monitoring, and incident response.

**42. Sanctioned vs. unsanctioned AI**
> Sanctioned = approved, governed tools on the list. Unsanctioned = shadow AI used without approval.

**43. Private vs. public models**
> Private/self-hosted keeps data in your control (preferred for sensitive data). Public/third-party is fast/cheap but data leaves your environment. Data sensitivity drives the choice.

**44. Sensitive data governance**
> Classifying data and defining what may be sent to which model tier.

**45. Third-party compliance evaluations**
> Assessing AI vendors for certifications/attestations (ISO 42001, SOC 2), data-use/training terms, and incident obligations.

**46. Data sovereignty**
> Data is subject to the laws of the jurisdiction where it is stored/processed. Sending data abroad can violate residency rules. Control: in-region or private deployment.

---

## Supporting GRC terms

**47. GDPR Article 22**
> Right not to be subject to a *solely automated* decision with legal/similarly significant effect. Triggers when BOTH conditions hold (e.g., automated loan denial).

**48. Controller vs. processor**
> Controller decides the purposes/means of processing; processor acts on the controller's instructions. A vendor using your data for its *own* model becomes a controller for that purpose.

**49. DPIA**
> Data Protection Impact Assessment — required before high-risk processing; assesses necessity, risks, and safeguards.

**50. Model card**
> Documents the *model* — intended use, training data, evaluation results, limitations, biases.

**51. Datasheet for datasets**
> Documents the *dataset* — composition, collection, representation, preprocessing, intended uses.

**52. System card**
> Documents the deployed *system* — context, integrated models/tools, safety evals, oversight mechanisms.

**53. AI-BOM**
> AI Bill of Materials — inventory of an AI system's components (base models, datasets, frameworks, plugins, APIs). Key for supply-chain risk.

**54. SHAP vs. LIME**
> Post-hoc explainability methods. SHAP = Shapley-value feature contributions (game theory). LIME = local approximation with a simpler model.

**55. HITL vs. HOTL vs. human-in-command**
> HITL = human approves each decision. HOTL = AI decides, human monitors/can intervene. Human-in-command = humans can override/shut down overall.

---

## Commonly-confused discriminators

**56. ISO/IEC 42001 vs. NIST AI RMF**
> 42001 = international, **certifiable** management system. NIST AI RMF = US, **voluntary**, non-certifiable.

**57. GOVERN vs. MAP**
> GOVERN = organization-wide policy/accountability. MAP = risk for a *specific* system.

**58. Prohibited vs. high-risk (EU AI Act)**
> Prohibited = banned outright (social scoring). High-risk = allowed but heavily regulated (credit, hiring, medical).

**59. Responsible AI principles vs. NIST trustworthy characteristics**
> Responsible AI = value set incl. inclusiveness, consistency, awareness training. NIST = the framework's trustworthy-AI characteristics. Fairness/accountability/explainability appear in both.

**60. Model card vs. datasheet vs. system card vs. AI-BOM**
> Model = the model; datasheet = the dataset; system card = the deployment; AI-BOM = the component inventory.

---

## Anki / Quizlet import (TSV — term &lt;TAB&gt; definition)

```tsv
AI Center of Excellence	Central cross-functional team setting AI standards and vetting/approving use cases
AI policies and procedures	The AI policy, AUP, and model-risk/data-governance procedures enforced by the CoE
Data scientist	Builds, trains, and evaluates models; feature/metric selection
AI architect	Designs the overall AI solution architecture
Machine learning engineer	Productionizes models (training-to-serving), performance/optimization
Platform engineer	Builds the underlying compute/data platform AI runs on
MLOps engineer	CI/CD, deployment, monitoring, and drift/retraining automation for models
AI security architect	Designs and implements security controls for AI systems
AI governance engineer	Implements governance controls, guardrails, and policy enforcement in the AI stack
AI risk analyst	Identifies, assesses, and tracks AI risks; maintains the risk register
AI auditor	Independently assesses AI systems/controls for compliance and effectiveness
Data engineer	Builds and maintains data pipelines feeding training/inference
Fairness	Treats people equitably; avoids discriminatory outcomes
Reliability and safety	Performs consistently and safely under expected and edge conditions
Transparency	Stakeholders understand how the system works and its limits
Privacy and security	Protects data and resists attack across the lifecycle
Explainability	Outputs/decisions can be explained to relevant stakeholders
Inclusiveness	Designed to serve and be accessible to diverse/marginalized people
Accountability	People remain answerable for AI outcomes; clear ownership
Consistency	Behaves predictably across similar inputs and over time
Awareness training	Users trained to recognize AI and understand its proper use and limits
Introduction of bias	Bias entering via skewed data/feedback/fine-tuning
Accidental data leakage	Sensitive data unintentionally exposed via outputs/logs/tools
Reputational loss	Brand/trust harm from AI failures, bias, or misuse
Accuracy and performance risk	Model outputs wrong or degrading, causing harm from decisions
IP-related risks	Training-data copyright, output ownership, proprietary leakage
Autonomous systems risk	Systems acting without adequate human oversight causing harm
Shadow AI	AI tools adopted without IT/security knowledge or approval
EU AI Act	Binding risk-tiered EU AI regulation; applies to AI used in the EU
EU AI Act unacceptable risk	Prohibited practices (e.g., social scoring) banned outright
EU AI Act high risk	Consequential systems requiring oversight, documentation, registration
EU AI Act limited risk	Transparency obligations (chatbots/deepfakes must disclose AI)
EU AI Act minimal risk	Most AI; no mandatory obligations
OECD AI Principles	Non-binding intergovernmental principles influencing AI regulation
ISO/IEC 42001	Certifiable AI Management System (AIMS) standard
ISO/IEC 23894	Guidance standard for AI risk management, used with 42001
NIST AI RMF	Voluntary US framework; four functions + trustworthy characteristics
NIST AI RMF GOVERN	Establishes org-wide AI policy, accountability, risk tolerance
NIST AI RMF MAP	Contextualizes risk for a specific AI system
NIST AI RMF MEASURE	Analyzes/quantifies risk via metrics, testing, red-teaming
NIST AI RMF MANAGE	Implements treatments, tracks residual risk, monitoring, IR
Sanctioned vs unsanctioned	Approved governed tools vs shadow AI used without approval
Private vs public models	Self-hosted keeps data in control vs third-party where data leaves; sensitivity decides
Sensitive data governance	Classifying data and defining what may go to which model tier
Third-party compliance evaluations	Assessing AI vendors for certifications, data-use terms, incident obligations
Data sovereignty	Data governed by the laws where it is stored/processed; use in-region/private deployment
GDPR Article 22	Right not to be subject to a solely automated decision with significant effect
Controller vs processor	Controller decides purposes/means; processor acts on instructions
DPIA	Data Protection Impact Assessment for high-risk processing
Model card	Documents the model: use, training data, evaluation, limitations
Datasheet for datasets	Documents the dataset: composition, collection, representation
System card	Documents the deployed system: context, integrations, safety evals
AI-BOM	Inventory of an AI system's components; key for supply-chain risk
SHAP vs LIME	Shapley-value feature contributions vs local simpler-model approximation
HITL vs HOTL	Human approves each decision vs AI decides and human monitors/intervenes
ISO 42001 vs NIST AI RMF	Certifiable international standard vs voluntary US framework
Prohibited vs high-risk	Banned outright vs allowed but heavily regulated
Responsible AI vs NIST characteristics	Value set (incl. inclusiveness/consistency/awareness) vs framework's trustworthy traits
```

---

*Week 5 deck (Domain 4 = 19%). Memorize the NIST AI RMF functions, EU AI Act tiers, and the role taxonomy cold. Log weak cards in `99-PROGRESS-TRACKER.md`.*
