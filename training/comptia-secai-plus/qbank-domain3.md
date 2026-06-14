# CompTIA SecAI+ (CY0-001 V1) — Question Bank: Domain 3

Domain 3 bank — 70 questions, objectives 3.1–3.3.

**Domain:** 3 — AI-Assisted Security | **Weight:** 24%
**Objectives covered:** 3.1 (AI-enabled tools/use cases), 3.2 (AI-enabled attack vectors), 3.3 (AI security automation)
**Source anchor:** CompTIA SecAI+ CY0-001 V1 Exam Objectives, Document Version 2.0 (© 2025 CompTIA)

> These are original practice questions only. They do not reproduce real CompTIA exam items.
> PBQ = Performance-Based Question (scenario/workflow style). All others are single best answer unless "(Choose two)" is indicated.

---

## Objective 3.1 — Use AI-Enabled Tools for Security Tasks

---

**Q1.** A security engineer wants to add AI-assisted vulnerability scanning directly inside VS Code so that flagged code is highlighted before a developer even commits. Which AI tool form factor is being described?

A) MCP server  
B) Browser plug-in  
C) IDE plug-in  
D) CLI plug-in  

---

**Q2.** An analyst uses a terminal-based AI assistant that can explain unfamiliar bash commands, generate one-liner scripts for log parsing, and answer questions about running processes during an incident. Which AI tool form factor is this?

A) Personal assistant  
B) CLI plug-in  
C) MCP server  
D) Chatbot  

---

**Q3.** A threat intelligence team deploys a connector that lets their AI security copilot call the SIEM's search API, pull threat intel from an external feed, and open ITSM tickets — all through one standardized interface instead of custom integrations for each system. Which technology does this describe?

A) SOAR playbook webhook  
B) DAST engine  
C) MCP (Model Context Protocol) server  
D) Vector database query API  

---

**Q4 (PBQ).** You are deploying an MCP server that gives your AI security agent write access to the SIEM, the firewall change-request queue, and the vulnerability scanner. A colleague suggests exposing the MCP server on an unauthenticated internal endpoint to "simplify agent connectivity." You reject this proposal.

Which TWO risks does an unauthenticated, over-scoped MCP server introduce? (Choose two.)

A) The agent could be manipulated by an indirect prompt injection in SIEM results to issue unauthorized firewall changes.  
B) Any user or process on the internal network could call the MCP server and trigger privileged actions.  
C) The MCP server would be unable to return structured data to the AI model.  
D) The AI model would lose the ability to summarize security alerts.  

---

**Q5.** An AI tool reads a running application's web traffic, automatically highlights malicious URLs before they load, and warns the analyst when a site's content may be a phishing page. Which AI tool form factor is this?

A) IDE plug-in  
B) Browser plug-in  
C) MCP server  
D) Personal assistant  

---

**Q6.** A SOC team wants their AI assistant to continuously monitor email, calendar, ticketing, messaging, and SIEM — taking automated actions like scheduling meetings, escalating tickets, and summarizing overnight alerts when the on-call analyst wakes up. Which AI tool form factor BEST describes this capability?

A) CLI plug-in  
B) Chatbot  
C) Personal assistant  
D) Browser plug-in  

---

**Q7.** Which AI use case is MOST directly associated with scanning source code and flagging insecure patterns such as missing input sanitization, hard-coded secrets, and insecure cipher choices before the code is compiled?

A) Anomaly detection  
B) Automated penetration testing  
C) Code quality and linting  
D) Fraud detection  

---

**Q8.** A financial services firm uses an AI platform that ingests thousands of daily transactions, flags those that deviate from the account holder's historical spending geography, time-of-day patterns, and merchant category, and queues flagged transactions for step-up authentication. Which AI use case is this?

A) Pattern recognition for threat modeling  
B) Fraud detection  
C) Signature matching  
D) Incident management  

---

**Q9.** An analyst receives a 120-page threat actor report written in Mandarin. They use an AI tool to produce an English-language synopsis covering attribution, TTPs, indicators, and recommended defensive actions. Which TWO AI use cases are being combined? (Choose two.)

A) Translation  
B) Fraud detection  
C) Summarization  
D) Automated penetration testing  

---

**Q10.** A security team uses an AI tool to automatically generate an initial threat model for a newly designed microservices architecture by analyzing the architecture diagram, identifying trust boundaries, and proposing potential attack paths. Which AI use case does this represent?

A) Anomaly detection  
B) Threat modeling  
C) Signature matching  
D) Vulnerability analysis  

---

**Q11.** An AI-powered SIEM co-pilot ingests raw network flow data and flags a host that begins connecting to 47 previously uncontacted internal hosts over SMB within a 30-minute window. No known malware signature matches the traffic. Which AI use case BEST describes the capability that detected this?

A) Signature matching  
B) Fraud detection  
C) Anomaly detection  
D) Summarization  

---

**Q12.** A development team uses an AI tool integrated into their CI/CD pipeline that automatically executes parameterized attack payloads against a staging web application, evaluates responses for evidence of injection vulnerabilities, and generates a finding report — without a human tester directing each test. Which AI use case does this describe?

A) Code quality and linting  
B) Automated penetration testing  
C) Pattern recognition  
D) Incident management  

---

**Q13.** Which AI use case involves training a model on millions of historical network packets labeled "normal" and "malicious," then deploying it to score new packets in real time and surface those most likely to represent C2 beaconing, lateral movement, or data exfiltration?

A) Threat modeling  
B) Translation  
C) Pattern recognition  
D) Summarization  

---

**Q14 (PBQ).** A security analyst is evaluating four AI tool proposals for the SOC. Match each tool to its CORRECT form factor.

| Tool | Description |
|---|---|
| Tool 1 | An AI assistant embedded in the developer's code editor that flags insecure function calls inline |
| Tool 2 | A standardized server exposing SIEM search and threat-intel APIs to an AI agent |
| Tool 3 | A conversational AI interface where analysts type questions like "What were the top 5 alert types last week?" |
| Tool 4 | An AI assistant that monitors the analyst's email, tickets, and SIEM, proactively surfacing critical items each morning |

Which option correctly maps all four tools to their form factors?

A) Tool 1 = Browser plug-in; Tool 2 = SOAR; Tool 3 = Personal assistant; Tool 4 = Chatbot  
B) Tool 1 = IDE plug-in; Tool 2 = MCP server; Tool 3 = Chatbot; Tool 4 = Personal assistant  
C) Tool 1 = CLI plug-in; Tool 2 = Vector database; Tool 3 = MCP server; Tool 4 = Browser plug-in  
D) Tool 1 = IDE plug-in; Tool 2 = Chatbot; Tool 3 = CLI plug-in; Tool 4 = MCP server  

---

**Q15.** An AI copilot inside a SIEM automatically generates a plain-English summary of a complex incident involving 47 correlated alerts, lists the affected hosts in order of criticality, and drafts a one-paragraph executive brief — all before an analyst opens the ticket. Which AI use case does this PRIMARILY represent?

A) Signature matching  
B) Automated penetration testing  
C) Incident management and summarization  
D) Fraud detection  

---

**Q16.** A development team installs an AI coding assistant plug-in. A security review determines that when developers prompt the plug-in, the full content of their open source file — including any hard-coded credentials or proprietary algorithms present in the file — is transmitted to the vendor's cloud inference endpoint. Which risk does this PRIMARILY represent?

A) The plug-in will generate code with SQL injection vulnerabilities  
B) Sensitive source code and secrets may be exfiltrated to a third-party AI vendor  
C) The plug-in will cause the IDE to crash during compilation  
D) The generated code will always pass SAST scanning without human review  

---

**Q17.** Signature matching as an AI use case is BEST described as:

A) Training a GAN to generate new attack signatures for red team exercises  
B) Automatically applying known indicators of compromise — file hashes, IP addresses, domain patterns — against security telemetry to identify matches  
C) Building a statistical baseline of normal user behavior and alerting on deviations  
D) Generating a natural-language summary of an alert before analyst review  

---

## Objective 3.2 — How AI Enables/Enhances Attack Vectors

---

**Q18.** A CFO receives a voice message that uses AI-generated audio to perfectly replicate the CEO's voice, accent, and speech pattern, directing the CFO to immediately approve a wire transfer. The audio was generated from publicly available interview recordings. Which AI-enabled attack is this?

A) Data poisoning — the attacker corrupted the voice authentication model's training data  
B) Deepfake impersonation — the attacker used AI to generate a synthetic voice for social engineering  
C) Model inversion — the attacker extracted the CEO's voiceprint from the authentication system  
D) Adversarial example — the attacker perturbed the audio file to evade voice detection  

---

**Q19.** Which of the following BEST distinguishes an AI-enabled attack (Domain 3, objective 3.2) from an attack on an AI system (Domain 2)?

A) An AI-enabled attack targets a specific AI model's parameters; an attack on an AI system targets humans  
B) An AI-enabled attack uses AI as a weapon to attack people or infrastructure; an attack on an AI system targets the integrity, availability, or confidentiality of an AI model itself  
C) Both categories describe the same class of threat and belong to the same exam domain  
D) An AI-enabled attack always involves deepfakes; an attack on an AI system always involves prompt injection  

---

**Q20.** A threat actor uses AI to automatically scrape breach dumps, dark web forums, and social media, correlate the data to build comprehensive profiles of 50,000 target employees — including home addresses, interests, colleagues, and recent life events — and then generate personalized spear-phishing emails for each target. Which AI-enabled attack technique does this combine?

A) Deepfake impersonation and model extraction  
B) Automated data correlation and AI-generated social engineering content  
C) Honeypot evasion and DDoS orchestration  
D) Obfuscation and adversarial network training  

---

**Q21.** A nation-state group trains a GAN to produce synthetic profile photos, fabricate news articles about a political candidate, and generate realistic video clips of the candidate making statements they never made, all for a coordinated influence operation. Which AI-enabled attack category does this MOST closely represent?

A) AI-enabled reconnaissance  
B) Adversarial networks and deepfake disinformation  
C) Automated attack generation  
D) Honeypot deception  

---

**Q22.** A malware author uses an LLM to rewrite a Trojan's code on every deployment so that each compiled binary has a unique byte sequence and file hash while retaining identical malicious functionality. Traditional AV signature databases fail to detect any of the variants. Which AI-enabled attack technique is this?

A) DDoS orchestration  
B) Automated data correlation  
C) Obfuscation / AI-generated polymorphic malware  
D) Deepfake audio impersonation  

---

**Q23.** An attacker uses AI to autonomously probe a target organization's internet-facing assets, identifying exposed APIs, misconfigured cloud storage, unpatched web servers, and orphaned subdomains, producing a prioritized list of exploitable entry points within hours. Which phase of the attack lifecycle does this represent, and which AI-enabled capability enables it?

A) Exploitation; AI-generated payload delivery  
B) Reconnaissance; AI-accelerated automated attack surface discovery  
C) Command and control; AI-driven botnet orchestration  
D) Lateral movement; AI-assisted privilege escalation  

---

**Q24.** Which of the following is an example of AI being used to enhance a DDoS attack rather than a traditional volumetric flood?

A) Using an LLM to write spear-phishing emails targeting network engineers  
B) Training a GAN to generate synthetic user credentials for credential stuffing  
C) Deploying an AI-orchestrated botnet that adaptively shifts attack vectors and traffic patterns to evade DDoS mitigation systems in real time  
D) Using ML to correlate breach dump data with LinkedIn profiles to identify ISP engineers as targets  

---

**Q25.** A red team uses an AI tool to automatically generate hundreds of unique exploit payloads targeting a specific buffer overflow vulnerability, test each payload in a sandboxed environment, and return the three payloads with the highest bypass rate against the target's defenses. Which AI-enabled attack capability does this represent?

A) Reconnaissance and OSINT aggregation  
B) Automated attack generation — AI-assisted payload generation  
C) Deepfake social engineering  
D) Adversarial network training  

---

**Q26.** Security operations deploys a high-interaction honeypot that mimics the organization's actual database server, complete with fake but realistic-looking records. An attacker's AI recon tool scans the environment, detects that the "database" never changes, has anomalously clean logs, and receives no legitimate query traffic — and flags it as a probable honeypot before interacting with it. This scenario BEST illustrates:

A) AI-enabled attack: using AI to evade and detect deceptive honeypot defenses  
B) AI-enabled defense: using AI to generate the honeypot content  
C) An attack on AI: poisoning the honeypot's ML model  
D) Social engineering: tricking the attacker's AI into revealing itself  

---

**Q27.** A threat actor purchases access to 15 stolen corporate email accounts. Using an AI-driven platform, the actor analyzes the email threads, identifies the CFO, maps her communication patterns, and automatically generates a spear-phishing email that mimics her colleagues' writing style, references a real ongoing project, and creates a sense of urgency about a pending contract. Which two AI-enabled techniques are combined? (Choose two.)

A) Automated data correlation (mining email threads to profile targets)  
B) DDoS orchestration  
C) AI-generated social engineering content (personalized spear-phishing at scale)  
D) Adversarial example generation  

---

**Q28.** An AI system is used to generate a realistic video of a company's CEO making a statement about a data breach that never occurred, which is then distributed on social media to manipulate the company's stock price. This BEST represents:

A) Deepfake-based misinformation / disinformation  
B) Prompt injection targeting the CEO's AI assistant  
C) Model extraction to steal the CEO's behavioral profile  
D) Automated attack generation against stock trading algorithms  

---

**Q29.** Which of the following BEST describes how adversarial networks (GANs) are weaponized as an AI-enabled attack vector?

A) GANs are used to inject adversarial prompts into enterprise chatbots  
B) The GAN's generator learns to produce synthetic content — identities, images, audio, text — realistic enough to fool both humans and automated detection systems, while the discriminator trains the generator to improve  
C) GANs perform gradient-based attacks on the target model's weights  
D) GANs are used exclusively for password spraying at scale  

---

**Q30 (PBQ).** A threat intelligence analyst receives a report about a sophisticated campaign. The report describes the following attacker behaviors:

- Step 1: AI tools scraped the target's corporate website, job postings, LinkedIn, and GitHub repositories to build an organizational profile.
- Step 2: A GAN generated synthetic profile photos for fake LinkedIn personas used to connect with employees.
- Step 3: An LLM generated personalized email lures for 200 employees referencing their specific projects.
- Step 4: A custom malware variant was automatically rewritten on each delivery so no two samples shared a hash.
- Step 5: After initial access, the attacker's automated correlation tool identified the highest-privilege accounts by correlating Active Directory data with the OSINT profile from Step 1.

Match each step to the CORRECT AI-enabled attack category from objective 3.2.

A) Step 1 = Social engineering; Step 2 = Obfuscation; Step 3 = Reconnaissance; Step 4 = Deepfake; Step 5 = DDoS  
B) Step 1 = Reconnaissance; Step 2 = Adversarial networks (GAN synthetic identities); Step 3 = AI-generated social engineering; Step 4 = Obfuscation / polymorphic malware; Step 5 = Automated data correlation  
C) Step 1 = Automated data correlation; Step 2 = Deepfake impersonation; Step 3 = DDoS; Step 4 = Reconnaissance; Step 5 = Social engineering  
D) Step 1 = Obfuscation; Step 2 = Social engineering; Step 3 = Deepfake; Step 4 = Automated attack generation; Step 5 = Reconnaissance  

---

**Q31.** A defender sets up an AI-generated honeypot environment — a fake cloud storage bucket with synthetic but convincing-looking intellectual property documents, designed to attract and fingerprint attackers. This is BEST described as:

A) An AI-enabled attack — the defender is attacking the attacker's infrastructure  
B) An AI-assisted defensive use of honeypot generation to detect and profile intruders  
C) A deepfake deployment targeting the attacker's AI recon tool  
D) An adversarial example designed to fool the attacker's malware classifier  

---

**Q32.** Which control MOST directly counters AI-generated deepfake impersonation used in high-value wire-transfer fraud?

A) Deploying an AI-powered email spam filter  
B) Training the AI model on more diverse audio samples  
C) Requiring out-of-band verification via a known, pre-established callback number for any wire-transfer authorization  
D) Increasing the CVSS score threshold for patch prioritization  

---

**Q33.** An attacker leverages AI to automatically identify the ideal timing, source IPs, and request patterns for an application-layer DDoS attack that will evade the target's rate-limiting rules — adapting in real time as the target's mitigation systems respond. This is an example of:

A) AI-assisted vulnerability analysis  
B) AI-enabled automated attack generation — attack vector discovery and DDoS optimization  
C) Anomaly detection being defeated by signature evasion  
D) Deepfake-based service disruption  

---

## Objective 3.3 — Use AI to Automate Security Tasks

---

**Q34.** A small security team with no dedicated developers uses a drag-and-drop visual platform to build an automated threat-hunting workflow that collects SIEM alerts, enriches them with threat intel lookups, and sends a Slack notification — without writing a single line of code. Which AI automation capability does this represent?

A) AI-assisted change management  
B) No-code scripting / automation  
C) CI/CD automated deployment  
D) Model testing  

---

**Q35.** During an active incident, an AI agent automatically creates an ITSM ticket, populates it with the alert details, assigns it to the on-call analyst, updates the ticket with each new artifact discovered (additional IOCs, affected hosts, log snippets), and marks the ticket resolved when the analyst closes the investigation. Which AI automation use case is this?

A) Document synthesis  
B) Change management  
C) IR ticket management  
D) CI/CD code scanning  

---

**Q36.** An AI system automatically drafts a post-incident report containing an executive summary, a technical timeline, root cause analysis, affected assets, and recommended remediations — generated from structured incident data, analyst notes, and SIEM query results. Which AI automation use case does this represent?

A) IR ticket management  
B) Document synthesis and summarization  
C) Regression testing  
D) Automated deployment  

---

**Q37.** A change advisory board (CAB) integrates an AI tool that scores each proposed change by analyzing its scope, affected systems, change history, recent vulnerability scan results, and current threat intelligence, then recommends "Approve," "Approve with conditions," or "Defer for human review." Which AI automation capability is this?

A) Automated deployment and rollback  
B) Unit testing  
C) AI-assisted change management approvals  
D) Document synthesis  

---

**Q38.** A platform engineering team configures their CI/CD pipeline so that when a new container image is built, an AI agent automatically runs SAST on the code, SCA on the dependencies, secrets scanning on the commit, and container image scanning — blocking the pipeline and notifying the team if any gate fails. Which two objective 3.3 automation capabilities does this pipeline implement? (Choose two.)

A) Code scanning (SAST integrated into CI/CD)  
B) IR ticket management  
C) Software composition analysis (SCA in CI/CD)  
D) AI-assisted change management approvals  

---

**Q39.** An AI agent monitors a newly deployed microservice. When error rates exceed 5% and a security anomaly is simultaneously detected, the agent automatically rolls back to the previous container image, raises an incident ticket, and notifies the on-call engineer. Which AI automation capability does this PRIMARILY describe?

A) Document synthesis  
B) No-code scripting  
C) Automated deployment and rollback triggered by health and security signals  
D) Unit testing  

---

**Q40.** An AI tool generates 300 unit test cases for a newly written authentication module, covering boundary conditions, invalid input handling, and expected error states — tasks that would have taken a developer several days to write manually. Which AI automation use case is this?

A) Regression testing  
B) Model testing  
C) AI-generated unit testing  
D) Software composition analysis  

---

**Q41.** After an AI model used in fraud detection is updated with new training data, an automated pipeline runs a suite of tests to verify that the model's performance on known fraud patterns has not degraded and that it still meets minimum precision/recall thresholds. Which CI/CD automation capability does this represent?

A) SAST code scanning  
B) Model testing (AI model regression validation in CI/CD)  
C) Software composition analysis  
D) Change management approval  

---

**Q42 (PBQ).** A DevSecOps team wants to build a complete AI-assisted security pipeline from code commit to production deployment. They have identified the following gates they want to automate:

- Gate A: Scan source code for known vulnerability patterns before merge.  
- Gate B: Scan third-party open-source libraries for known CVEs.  
- Gate C: Fire attack payloads against the running application in the test environment.  
- Gate D: Verify the new ML model's detection accuracy has not dropped below baseline.  
- Gate E: Automatically revert to the previous version if post-deploy health checks fail.  

Match each gate to its CORRECT CI/CD automation capability from objective 3.3.

A) Gate A = DAST; Gate B = Unit testing; Gate C = SAST; Gate D = Regression testing; Gate E = SCA  
B) Gate A = SAST; Gate B = SCA; Gate C = DAST; Gate D = Model testing; Gate E = Automated rollback  
C) Gate A = SCA; Gate B = DAST; Gate C = SAST; Gate D = Automated rollback; Gate E = Model testing  
D) Gate A = SAST; Gate B = Unit testing; Gate C = SCA; Gate D = DAST; Gate E = Model testing  

---

**Q43.** A security automation platform allows a compliance analyst to describe a desired workflow in plain English ("When a severity-high alert fires, look up the affected asset in the CMDB, check if it is in scope for PCI DSS, and if so, escalate to the compliance team within 15 minutes"). The platform then builds and deploys the automation. Which AI automation category does this BEST represent?

A) No-code / low-code AI scripting  
B) Model testing  
C) Regression testing  
D) Automated deployment  

---

**Q44.** An AI agent is granted permissions to create firewall rules, modify IAM policies, and deploy container images without any human approval required. A security architect raises an objection. Which specific risk from AI automation does the architect MOST likely have in mind?

A) The AI agent will hallucinate threat intelligence and create useless firewall rules  
B) Excessive AI agency without human-in-the-loop controls for high-impact, irreversible actions creates unacceptable operational and security risk  
C) The agent will perform model testing instead of deployment  
D) No-code automation tools cannot be used for IAM changes  

---

**Q45.** An AI system is used to generate a regression test suite that runs after every code change to verify that previously working security features — such as authentication flows, session timeout enforcement, and RBAC checks — have not been broken by the new change. Which automation capability is this?

A) SAST scanning  
B) Regression testing  
C) Software composition analysis  
D) Model testing  

---

**Q46.** An AI agent manages the full lifecycle of incident response tickets: auto-creating them from SIEM alerts, enriching them with threat intel, routing them to the correct team, tracking SLA deadlines, escalating overdue tickets, and generating the post-incident summary when an analyst marks the incident resolved. The agent operates 24/7 with no weekend staffing gaps. Which MOST accurately describes the risk this eliminates and the risk it introduces?

A) Eliminates alert fatigue; introduces prompt injection into the SIEM  
B) Eliminates staffing gaps in ticket lifecycle management; introduces automation bias if analysts blindly accept AI ticket summaries without reviewing evidence  
C) Eliminates false positive alerts; introduces hallucination in the firewall rule set  
D) Eliminates SAST scanning latency; introduces SCA false positives  

---

## Limitations and Risks of Defensive AI (High-Yield)

---

**Q47.** An AI security copilot in a SOC states in an alert summary: "This traffic pattern is definitively associated with the Lazarus Group based on C2 infrastructure overlap." The analyst checks the underlying threat intel sources and finds no such attribution — the IP in question has no prior threat intel associations. Which AI limitation is this?

A) Automation bias  
B) Adversarial evasion  
C) Hallucination — the AI generated a confident but factually unsupported attribution claim  
D) Temporal bias in the training data  

---

**Q48.** An analyst notices that when the AI triage system marks an alert as "Benign — close," she automatically closes it without reading the alert details, even on high-severity events. Six weeks later an auditor finds that 12 real intrusion alerts were closed this way. Which failure mode does this MOST accurately describe?

A) Hallucination — the AI was generating incorrect verdicts  
B) Automation bias — the analyst delegated her judgment to the AI without independent verification  
C) Adversarial evasion — the attacker crafted inputs to score as benign  
D) Data poisoning — the attacker corrupted the AI's training data  

---

**Q49.** A ML-based malware classifier is deployed at a financial services firm. Security researchers discover that by making imperceptible byte-level changes to a malware binary — changes that do not affect the malware's runtime behavior — the classifier's confidence score drops from 0.97 (malicious) to 0.08 (benign). Which AI limitation does this exploit?

A) Hallucination  
B) Automation bias  
C) Adversarial evasion of AI detectors  
D) The black box / explainability problem  

---

**Q50.** A UEBA platform trained during normal office-hours operations begins generating thousands of daily false positive alerts after the company transitions to a fully remote-first model. Employees are now working across four time zones at irregular hours. Which limitation of defensive AI MOST likely caused this?

A) Hallucination — the model is generating fake user identities  
B) Adversarial evasion — employees are crafting inputs to avoid detection  
C) Temporal / distributional bias — the model's baseline no longer reflects the current operating environment  
D) The black box problem — analysts cannot explain why the alerts are firing  

---

**Q51.** A compliance officer demands that the AI-based intrusion detection system produce a detailed explanation for every alert it fires — specifying exactly which features drove the risk score — so that decisions can be documented for audit purposes. The vendor responds that the underlying model is a deep neural network and cannot produce feature-level explanations without additional tooling. Which post-hoc explainability techniques could ADDRESS this requirement? (Choose two.)

A) Retraining the model using only signature-based rules  
B) SHAP (SHapley Additive exPlanations) values for per-feature contribution analysis  
C) LIME (Local Interpretable Model-agnostic Explanations) to produce local approximations of model decisions  
D) Deleting the model weights to force a rule-based fallback  

---

**Q52.** An organization sends full content of security analyst chat messages — including sensitive case details, witness names, and preliminary legal findings — to a cloud-based AI summarization tool for incident report drafting. The legal team raises an objection. Which specific risk is MOST relevant?

A) The AI tool will produce hallucinated summaries that make analysts faster but less accurate  
B) Sensitive PII and privileged case information is being transmitted to a third-party AI vendor, creating privacy and data-handling risk  
C) The AI-generated reports will contain SQL injection vulnerabilities  
D) The chat messages will train the vendor's adversarial evasion model  

---

**Q53.** A SOC manager measures that analysts agree with AI triage verdicts 97% of the time. She considers this a success metric. A security researcher visiting the SOC argues the 97% agreement rate could be a warning sign rather than a positive indicator. What is the researcher's MOST likely concern?

A) A 97% agreement rate means the AI is only 97% accurate, which is too low for a security use case  
B) The high agreement rate may indicate analysts are rubber-stamping AI verdicts without critical review — a manifestation of automation bias — rather than independently verifying each decision  
C) A 97% agreement rate suggests the model is overfitting to test data  
D) The AI should be replaced with a model that achieves 100% agreement  

---

**Q54.** When deploying a cloud-based AI-powered EDR platform that receives full endpoint telemetry, which control MOST directly mitigates the telemetry data privacy risk for a healthcare organization governed by HIPAA?

A) Enabling the AI platform's hallucination-reduction feature  
B) Reviewing and executing a data processing agreement with the vendor specifying data residency, retention, and prohibition on using customer data for model training  
C) Deploying SAST on the EDR agent code  
D) Requiring the AI platform to run regression tests on all telemetry  

---

**Q55.** An AI-based anomaly detection system's training dataset consists of 99.9% benign events and 0.1% malicious events. The model achieves 99.9% accuracy by predicting "benign" for every input. Which AI limitation is this, and what is the CORRECT term for this type of training data problem?

A) Hallucination; data poisoning  
B) Class imbalance / imbalance bias; the model has learned to predict the majority class without learning to detect attacks  
C) Automation bias; overfitting  
D) Adversarial evasion; model drift  

---

**Q56.** A security team relies solely on an AI-powered UEBA platform for insider threat detection, disabling older DLP and access logging tools to reduce costs. An insider threat actor learns the organization uses ML-based behavioral analytics and deliberately keeps their exfiltration volume and timing within what they estimate is the model's normal range. Which failure scenario does this illustrate?

A) Hallucination causing the UEBA to miss the exfiltration  
B) Automation bias causing the analyst to close the case prematurely  
C) Adversarial evasion of the ML detector combined with the risk of relying on AI as the sole control layer  
D) Class imbalance bias in the training data  

---

**Q57 (PBQ).** A CISO reviews the following AI-powered SOC capabilities and asks the security architect to identify where each limitation applies:

| Scenario | AI Output |
|---|---|
| 1 | The AI states "Host X is running a Mirai botnet variant" with high confidence. The host is a Linux print server with no internet egress. |
| 2 | An analyst closes 40 tickets flagged low-risk by the AI without reading the details. One of the 40 was a real intrusion. |
| 3 | The AI risk scores an alert 0.02 (benign) because the attacker's lateral movement stayed below the UEBA threshold. |
| 4 | A deep-learning detection model flags an alert but cannot explain which network features triggered it. |

Match each scenario to the CORRECT AI limitation.

A) 1 = Automation bias; 2 = Hallucination; 3 = Adversarial evasion; 4 = Class imbalance  
B) 1 = Hallucination; 2 = Automation bias; 3 = Adversarial evasion; 4 = Black box / explainability  
C) 1 = Adversarial evasion; 2 = Black box; 3 = Hallucination; 4 = Automation bias  
D) 1 = Class imbalance; 2 = Adversarial evasion; 3 = Automation bias; 4 = Hallucination  

---

## Mixed / Integration Questions (3.1 + 3.2 + 3.3)

---

**Q58.** A security team uses a no-code platform to build a workflow: when an AI alert fires, the system automatically queries threat intel, creates an ITSM ticket, and sends a Slack message to the analyst. Two weeks later, the team discovers the workflow was also auto-closing tickets when the AI confidence score exceeded 0.85 — a step no one intentionally configured, apparently added by an AI agent optimizing the workflow. Which risks does this scenario combine?

A) Hallucination in the threat intel lookup and DAST misconfiguration  
B) Excessive AI agent autonomy (unintended automated action) and automation bias risk if the auto-close removes human review  
C) Data poisoning in the no-code platform and SCA false positives  
D) Deepfake impersonation of the Slack notification and regression testing failure  

---

**Q59.** An organization uses an AI coding assistant (IDE plug-in) to write code, AI SAST to scan code in CI, AI SCA to check dependencies, and an AI agent to auto-deploy approved builds to production. A new developer uses the IDE plug-in to generate a login function, the SAST scan returns a false negative (misses a session fixation vulnerability), SCA passes, and the agent deploys to production. Which AI limitation allowed the vulnerability to reach production?

A) Deepfake impersonation of the developer  
B) A SAST false negative — the AI scanner failed to detect the vulnerability — combined with an absence of DAST testing against the running application before production promotion  
C) Automation bias — the developer trusted the AI-generated code without review  
D) Both B and C contribute; the SAST missed it and the developer did not review the generated code before committing  

---

**Q60.** Which objective 3.3 automation scenario would MOST warrant retaining a mandatory human approval gate rather than allowing fully automated execution?

A) Running AI-generated unit tests against a new authentication function  
B) Auto-creating an ITSM ticket from a SIEM alert  
C) Generating a post-incident summary document for analyst review  
D) Promoting a change that disables MFA enforcement on the identity provider to all production users  

---

**Q61.** A SOAR platform uses AI to automatically isolate endpoints, block IPs, and disable user accounts when an alert meets a certain confidence threshold. An analyst later discovers that the AI isolated the CFO's laptop during an all-hands presentation because the CFO's video conferencing traffic matched a C2 beaconing pattern. Which concept does this scenario BEST illustrate?

A) The need for human-in-the-loop controls for high-impact automated actions  
B) The hallucination of the SOAR playbook's threat intel enrichment module  
C) An AI-enabled DDoS attack targeting the video conferencing system  
D) Adversarial evasion of the C2 detection model by the video conferencing vendor  

---

**Q62.** An AI red team tool uses pattern recognition to identify that a target web application's login endpoint responds slightly differently (in HTTP response time) when a valid username is submitted versus an invalid one — a timing oracle — and then automatically enumerates valid usernames. Which AI use case (3.1) is the attacker leveraging offensively?

A) Summarization  
B) Fraud detection  
C) Pattern recognition applied to attack vector discovery  
D) Incident management  

---

**Q63.** Which statement BEST describes the relationship between AI-assisted incident management (objective 3.3) and the hallucination risk (Domain 3 limitations)?

A) Hallucination has no impact on IR ticket management because tickets contain only structured log data  
B) An LLM that hallucinates incident details — inventing affected hosts, fabricating IOCs, or misidentifying root cause — could cause analysts to pursue incorrect remediation paths, making hallucination a direct operational risk in AI-assisted IR  
C) Hallucination only affects code generation tools, not SOC-facing tools  
D) AI-assisted IR ticket management eliminates hallucination because it is grounded in SIEM data  

---

**Q64.** A security team evaluates two approaches to automating daily threat intelligence reporting. Approach 1: an analyst queries the SIEM, compiles findings, and writes the report manually. Approach 2: a no-code AI agent queries the SIEM, enriches findings with external threat intel, and drafts the report automatically. The team selects Approach 2 but adds a mandatory analyst sign-off before distribution. The sign-off requirement addresses which AI risk?

A) Adversarial evasion — the threat intel feed may have been poisoned  
B) Hallucination and automation bias — ensuring a human reviews AI-generated content before it becomes the operational record  
C) Data exfiltration — the report may contain PII sent to external systems  
D) SCA false positives — third-party libraries in the agent may be vulnerable  

---

**Q65 (PBQ).** A security architect is designing the AI automation strategy for a new CI/CD pipeline. The following actions are proposed for full automation with no human gate:

1. Run SAST on every pull request and block merge on critical findings.  
2. Run SCA on every build and block if a known critical CVE is in a direct dependency.  
3. Auto-approve and deploy any change to the production authentication service when SAST and SCA pass.  
4. Auto-rollback the production authentication service if error rates exceed 1%.  
5. Auto-generate and send the post-incident security report to the board of directors.  

Identify the TWO items that should NOT be fully automated and require a mandatory human gate, and explain why.

A) Items 1 and 2, because SAST and SCA should always require human review of each finding before blocking  
B) Items 3 and 5: Item 3 because deploying changes to a critical production authentication service without human approval is an irreversible high-impact action; Item 5 because an AI-generated board report could contain hallucinated findings and should require human review before reaching executive stakeholders  
C) Items 4 and 1: Item 4 because automated rollback is never appropriate; Item 1 because blocking a PR without human approval is not allowed  
D) Items 2 and 4, because SCA and rollback are both irreversible and must be human-gated  

---

**Q66.** A security analyst receives an AI-generated threat hunting query in KQL (Kusto Query Language). The query is syntactically valid and runs without errors but returns zero results despite the analyst being confident the threat is present in the environment. The analyst rewrites the query manually and finds the threat. Which AI limitation does this MOST likely represent?

A) Automation bias  
B) Adversarial evasion — the attacker obfuscated their activity  
C) Hallucination — the AI generated a logically incorrect query that did not actually hunt for the intended behavior  
D) Class imbalance bias in the underlying detection model  

---

**Q67.** A managed security service provider (MSSP) uses an AI-powered platform that ingests telemetry from 200 client organizations and trains a shared detection model on the combined dataset. A client reports that a security investigation by the MSSP's AI platform revealed internal details about one client's network topology — details that appeared to originate from another client's telemetry. Which privacy risk does this represent?

A) Hallucination — the AI invented the network topology details  
B) Cross-tenant telemetry leakage — one client's data surfacing in another client's AI outputs due to shared model training  
C) Deepfake impersonation — the attacker fabricated the network topology report  
D) Adversarial evasion — the client's firewall evaded the shared detection model  

---

**Q68.** Which of the following actions MOST directly improves the explainability of an AI-driven security alert for a SOC analyst who needs to understand why a specific endpoint was flagged as high risk?

A) Retraining the model on a larger dataset to reduce false positives  
B) Applying SHAP values to the specific alert to show the contribution of each input feature (e.g., process creation rate, outbound bytes, login hour) to the risk score  
C) Replacing the model with a rule-based signature detection system  
D) Increasing the alert threshold to reduce the number of alerts requiring explanation  

---

**Q69.** An AI-powered phishing detection gateway has been deployed for 18 months. The security team notes its detection rate for AI-generated phishing emails has declined from 94% to 71% over the past six months, even though the underlying model has not been updated. Which AI limitation BEST explains this degradation?

A) Automation bias — analysts are dismissing too many alerts  
B) Hallucination — the model is generating false negative classifications  
C) Model drift — the threat landscape (AI-generated phishing tactics) has evolved since training, and the model's learned patterns no longer fully match current attack techniques  
D) Class imbalance — there are too many legitimate emails in the training set  

---

**Q70 (PBQ).** A security team is building a comprehensive AI-assisted security program. The CISO presents the following statement: "We will use AI across the entire security lifecycle — AI tools to detect threats, AI automation to respond to incidents, and AI analysis to understand attack techniques. Once we achieve full AI automation, we can significantly reduce analyst headcount."

As the security architect, you are asked to identify the THREE most significant risks in the CISO's statement and recommend mitigations.

Which answer BEST identifies the core risks?

A) Risk 1: AI tools cost too much. Risk 2: Analysts will lose their certifications if replaced by AI. Risk 3: AI cannot perform threat modeling.  
B) Risk 1: Automation bias — removing analyst oversight eliminates the human check that catches AI errors, turning AI mistakes into unreviewed operational decisions. Risk 2: Adversarial evasion — a sophisticated attacker who knows the organization relies solely on AI detection can craft activity designed to evade the AI's learned patterns. Risk 3: Hallucination — AI-generated incident summaries, threat hunting queries, and attack analysis that are wrong but go unverified will lead to missed intrusions and incorrect remediations.  
C) Risk 1: AI agents require too many API keys. Risk 2: No-code platforms cannot perform SAST. Risk 3: Deepfake attacks will target the AI agents directly.  
D) Risk 1: The CISO should not reduce headcount until Domain 4 compliance is achieved. Risk 2: SHAP values must be computed for every alert. Risk 3: Regression testing must precede any headcount reduction.  

---

## Answer Key

**Q1 — C**
An AI assistant embedded inside VS Code (an Integrated Development Environment) that flags code issues inline is an IDE plug-in. This is one of the six tool form factors explicitly listed in objective 3.1.

**Q2 — B**
A terminal-based AI assistant that explains commands, generates scripts, and answers operational questions in the CLI environment is a CLI plug-in — the form factor that lives in the command-line interface rather than a GUI editor or browser.

**Q3 — C**
The Model Context Protocol (MCP) server is the standardized connector that lets an AI agent or copilot call external tools and data sources — SIEM, threat intel, ITSM — through one interface instead of custom point-to-point integrations. This is explicitly named in objective 3.1.

**Q4 — A and B**
An unauthenticated MCP server with write access to privileged systems introduces two distinct risks: (A) indirect prompt injection — malicious content in SIEM results could instruct the agent to issue unauthorized commands through the MCP server; (B) any internal process or user can call the MCP endpoints and trigger privileged actions without going through the AI model at all.

**Q5 — B**
An AI tool that runs inside the web browser, analyzes page content and URLs in real time, and warns the user about malicious or phishing content is a browser plug-in. The browser is its operating environment.

**Q6 — C**
A personal assistant is the agentic form factor that actively monitors multiple systems (email, calendar, SIEM, ticketing), takes autonomous actions, and proactively surfaces insights — distinguishing it from a reactive chatbot that answers questions only when queried.

**Q7 — C**
Scanning source code for insecure patterns, bad practices, and hard-coded secrets before compilation is code quality and linting — one of the explicit use cases listed under objective 3.1. This overlaps with SAST but the 3.1 use case label is "code quality and linting."

**Q8 — B**
Scoring transactions against a behavioral baseline to detect anomalous activity for financial fraud is fraud detection — explicitly listed as a 3.1 AI security use case. The behavioral profile and step-up authentication mechanism are the discriminating details.

**Q9 — A and C**
Converting the document from Mandarin to English is translation; producing a condensed synopsis of its key findings is summarization. Both are named 3.1 AI use cases.

**Q10 — B**
Using AI to analyze an architecture, identify trust boundaries, and propose attack paths is threat modeling — one of the explicit 3.1 use cases. Vulnerability analysis (D) refers to analyzing specific vulnerabilities in code or running systems, not modeling architectural attack paths.

**Q11 — C**
Detecting that a host is connecting to 47 previously uncontacted internal hosts within 30 minutes, with no matching signature, is anomaly detection — the AI identified a deviation from learned baseline behavior rather than matching a known signature.

**Q12 — B**
An AI tool that autonomously fires attack payloads at an application and analyzes responses without a human directing each test is automated penetration testing, explicitly listed in objective 3.1.

**Q13 — C**
Training a model on labeled network packets and deploying it to surface novel malicious traffic patterns in real time is pattern recognition — a 3.1 use case distinct from signature matching (which applies known IOCs) and anomaly detection (which works from an unsupervised baseline).

**Q14 — B**
Tool 1 = IDE plug-in (inside the code editor). Tool 2 = MCP server (standardized tool/data connector for AI agents). Tool 3 = Chatbot (conversational Q&A interface). Tool 4 = Personal assistant (proactive, agentic, monitors multiple systems). This is the only option with all four correct.

**Q15 — C**
Auto-generating a correlated incident summary, prioritized host list, and executive brief from 47 alerts is both incident management (organizing the incident) and summarization (producing the brief). CompTIA's 3.1 use case list includes both; the scenario most directly combines them.

**Q16 — B**
IDE plug-ins that send the full contents of open files to cloud inference endpoints are transmitting potentially sensitive source code — including hard-coded credentials and proprietary algorithms — to a third-party AI vendor. This is a data exfiltration / intellectual property risk, not a code quality risk.

**Q17 — B**
Signature matching applies known IOCs (file hashes, IP addresses, domain regex patterns) against telemetry in real time. It is the AI-assisted analog of traditional AV signature scanning but applied across broader telemetry at machine speed.

**Q18 — B**
Generating a synthetic replica of a real person's voice from publicly available audio to impersonate them in a fraud scheme is a deepfake impersonation attack — one of the core categories under objective 3.2.

**Q19 — B**
The key distinction: an AI-enabled attack (3.2) uses AI as a weapon against people, systems, or infrastructure. An attack on an AI system (Domain 2) targets an AI model's integrity, confidentiality, or availability. The "direction of attack" defines the domain.

**Q20 — B**
The scenario combines automated data correlation (AI correlating breach dumps and social media to build profiles at scale) and AI-generated social engineering content (LLM-produced personalized phishing emails). Both are explicitly named in objective 3.2.

**Q21 — B**
Using GANs to generate synthetic media (profile photos, video clips) combined with fabricated news articles for a coordinated influence operation is adversarial networks + deepfake disinformation — a 3.2 attack category.

**Q22 — C**
Automatically rewriting a binary on every build to change its signature while preserving behavior is AI-driven obfuscation / polymorphic malware generation — explicitly listed under objective 3.2 obfuscation.

**Q23 — B**
Autonomously probing internet-facing assets to identify exploitable entry points is AI-accelerated reconnaissance. The 3.2 sub-bullet is "reconnaissance" under how AI enables/enhances attack vectors. The defensive implication is that attack surface discovery that once took days now takes hours.

**Q24 — C**
A botnet that uses AI to adaptively shift its attack patterns in real time to evade mitigation is AI-enabled adaptive DDoS — objective 3.2's "DDoS" sub-bullet. The other options describe social engineering (A), credential stuffing via GAN (B), and OSINT correlation (D) — none of which is the DDoS technique.

**Q25 — B**
Automatically generating and testing many exploit payloads against a vulnerability, then selecting the highest-performing ones, is automated attack generation — specifically payload generation, an explicit 3.2 sub-bullet.

**Q26 — A**
The attacker's AI recon tool is analyzing the honeypot and detecting it before engaging — this is an AI-enabled offensive use: using AI to evade and detect deceptive honeypot defenses. Option 3.2 names "honeypot" as a dual-use category; this scenario shows the attacker-side use.

**Q27 — A and C**
Step 1 = automated data correlation (mining email threads to profile targets). Step 2 = AI-generated social engineering content (personalized phishing at scale using the correlated profile). Both are explicit 3.2 sub-bullets.

**Q28 — A**
Generating AI synthetic video of an executive making false statements for distribution on social media to manipulate perception (or stock price) is deepfake-based misinformation / disinformation — objective 3.2's "AI-generated content/deepfake" with "misinformation/disinformation."

**Q29 — B**
GANs weaponized as attack vectors work by training the generator to produce synthetic content (identities, images, audio) that fools both humans and automated systems, with the discriminator as the training adversary. This is the mechanistic description of adversarial networks as an attack tool.

**Q30 — B**
Step 1 = Reconnaissance (AI aggregating OSINT). Step 2 = Adversarial networks (GAN-generated fake personas). Step 3 = AI-generated social engineering (LLM-produced personalized lures). Step 4 = Obfuscation / polymorphic malware (unique hash per delivery). Step 5 = Automated data correlation (correlating AD data with OSINT to identify high-value targets). This is the only option that correctly maps all five to the objective 3.2 taxonomy.

**Q31 — B**
The defender generating a convincing fake environment to attract and profile attackers is an AI-assisted defensive honeypot deployment. Honeypot is listed in 3.2 as dual-use — this is the defensive direction. It is not an "attack" by the defender.

**Q32 — C**
Out-of-band verification via a pre-established callback number addresses deepfake voice/video impersonation by requiring a second, independently authenticated channel to confirm the request. No AI-generated audio can replicate an uncompromised, pre-arranged callback number.

**Q33 — B**
AI that analyzes and adapts DDoS attack timing and patterns in real time to evade rate-limiting is automated attack generation — specifically attack vector discovery and DDoS optimization under objective 3.2.

**Q34 — B**
Building a threat-hunting workflow on a drag-and-drop visual platform with no code written is no-code scripting / automation — one of the explicit automation capabilities in objective 3.3.

**Q35 — C**
The AI agent managing the full lifecycle of an incident ticket — creation, enrichment, updates, routing, and closure — is IR ticket management, explicitly named in objective 3.3.

**Q36 — B**
Auto-drafting a post-incident report (executive summary, timeline, root cause, recommendations) from structured incident data is document synthesis and summarization — an explicit 3.3 automation capability.

**Q37 — C**
An AI tool that scores proposed changes and recommends approval or deferral to the CAB is AI-assisted change management approvals — explicitly named in objective 3.3's change management sub-bullet.

**Q38 — A and C**
The pipeline runs SAST (Gate A = code scanning in CI) and SCA (Gate B = software composition analysis). Both are explicitly listed as CI/CD automation capabilities in objective 3.3. IR ticket management (B) and change management approvals (D) are not pipeline scanning gates.

**Q39 — C**
An agent that automatically rolls back to the previous container image when health and security signals fail is automated deployment and rollback triggered by AI-evaluated signals — a named 3.3 automation capability.

**Q40 — C**
An AI system generating unit test cases covering boundary and error conditions for a function is AI-generated unit testing — one of the named testing capabilities in objective 3.3.

**Q41 — B**
Running a suite of precision/recall threshold tests after a model update to verify the AI model's detection performance has not degraded is model testing — the CI/CD automation capability in objective 3.3 specifically for ML systems.

**Q42 — B**
Gate A = SAST (static source code analysis, runs before/at build). Gate B = SCA (third-party dependency CVE scanning). Gate C = DAST (attack payloads fired at the running application in test). Gate D = Model testing (AI model accuracy validation). Gate E = Automated rollback (revert on failed post-deploy checks). This is the correct mapping to objective 3.3 terminology.

**Q43 — A**
Describing a workflow in plain English and having a platform build and deploy the automation is no-code / low-code AI scripting — the practitioner does not write code; the AI interprets the description and generates the automation.

**Q44 — B**
Granting an AI agent unfettered write access to firewalls, IAM, and container deployments with no human gate is excessive AI agency without human-in-the-loop controls — a core risk for high-impact, irreversible automated actions, consistent with both objective 3.3's governance cautions and the broader HITL principle.

**Q45 — B**
Running automated tests after each change to verify previously working security features are still intact is regression testing — explicitly named in objective 3.3 alongside unit testing and model testing.

**Q46 — B**
The AI agent eliminates staffing gaps in ticket lifecycle management (24/7 coverage). It introduces automation bias risk: if analysts blindly accept AI-generated ticket summaries without reviewing the underlying evidence, errors in the AI's summaries or triage will propagate undetected.

**Q47 — C**
The AI generated a specific, confident attribution claim ("definitively Lazarus Group") for which no supporting evidence exists in any threat intel source. This is hallucination — confident, factually unsupported output, the most direct AI limitation in this scenario.

**Q48 — B**
The analyst is accepting AI verdicts automatically without reading the evidence, even for high-severity alerts. This is automation bias — the human cognitive failure of delegating judgment to an automated system without independent verification. Note the distinction: hallucination (Q47) is an AI error; automation bias is a human error enabled by AI.

**Q49 — C**
Imperceptible byte-level modifications that change the model's classification from malicious to benign without altering runtime behavior are adversarial examples crafted to evade an ML detector at inference time — adversarial evasion of AI detectors.

**Q50 — C**
The model was trained on pre-remote-work office-hours behavior. The shift to a remote-first model represents distributional shift / temporal bias — the deployment environment no longer matches the training distribution, causing the model's baseline to be wrong.

**Q51 — B and C**
SHAP (SHapley Additive exPlanations) provides per-feature contribution scores for individual model predictions. LIME (Local Interpretable Model-agnostic Explanations) produces a locally faithful linear approximation of the model's decision at a specific point. Both are the exam-recognized post-hoc explainability techniques. They do not require retraining or discarding the model.

**Q52 — B**
Sending sensitive PII, privileged case details, and witness information to a third-party cloud AI tool is a privacy and data-handling risk — specifically third-party data sharing that may violate confidentiality obligations, attorney-client privilege, and privacy regulations. The telemetry data privacy section of Domain 3's limitations covers exactly this scenario.

**Q53 — B**
A 97% agreement rate may indicate analysts are rubber-stamping AI verdicts — not critically reviewing them — which is the operational signature of automation bias. If analysts were genuinely reviewing each alert independently, some level of disagreement with AI verdicts would be expected (since AI is imperfect). Near-total agreement warrants investigating whether review is actually occurring.

**Q54 — B**
A data processing agreement (DPA) specifying data residency, retention limits, and training data prohibitions directly addresses the third-party privacy risk of sending healthcare telemetry to a cloud AI vendor. This is the contractual and governance control specifically for telemetry data privacy.

**Q55 — B**
A model that learns to predict "benign" for every input because 99.9% of the training data is benign is exhibiting class imbalance bias — it has learned the majority class and ignores the minority (attack) class. This achieves misleadingly high accuracy while providing zero security value.

**Q56 — C**
The attacker is deliberately calibrating their activity to stay within the model's normal range — this is adversarial evasion of the ML detector. The compounding risk is that by disabling other controls (DLP, access logging), the organization has no fallback detection layer when the AI is evaded. This violates defense-in-depth.

**Q57 — B**
Scenario 1 = Hallucination (confident, factually unsupported claim about print server). Scenario 2 = Automation bias (analyst closing tickets without review). Scenario 3 = Adversarial evasion (attacker staying below UEBA threshold). Scenario 4 = Black box / explainability (model cannot explain its alert). This is the only correctly mapped set.

**Q58 — B**
The scenario combines two risks: the AI agent took an unintended autonomous action (auto-closing tickets — excessive agency), and if analysts accepted the auto-closures without review, that is automation bias. The combination of unintended agent behavior and removed human oversight is the core risk.

**Q59 — D**
Both B and C are valid contributing causes. The SAST tool missed the session fixation vulnerability (a false negative — AI limitation of SAST), and the developer accepted the AI-generated code without security review (automation bias). The absence of DAST testing in staging compounds the miss. Both failures together allowed the vulnerability to reach production.

**Q60 — D**
Disabling MFA enforcement on the identity provider for all production users is a high-impact, potentially irreversible change with catastrophic security consequences if wrong. This is the class of change that objective 3.3 identifies as warranting a human gate. Running tests (A), creating tickets (B), and drafting documents (C) are low-impact, reversible, fully automatable.

**Q61 — A**
Automatically isolating the CFO's laptop during an all-hands presentation based on an AI confidence score — without human review — is a high-impact, disruptive action that should require a human-in-the-loop gate. The CFO example illustrates exactly why irreversible and high-visibility automated actions need human approval checkpoints.

**Q62 — C**
The attacker's tool is detecting a timing oracle by observing subtle response-time patterns in HTTP responses — a pattern recognition use case applied offensively to discover an attack vector. This maps to 3.1's "pattern recognition" and 3.2's "attack vector discovery" simultaneously.

**Q63 — B**
An LLM that hallucinates incident details (invents hosts, fabricates IOCs, misidentifies root cause) in an AI-assisted IR workflow will cause analysts to pursue wrong remediation paths — hallucination is a direct operational risk in incident management, not a minor inconvenience.

**Q64 — B**
The mandatory analyst sign-off before distribution addresses hallucination (the AI might fabricate findings or misattribute activity) and automation bias (without sign-off, the report becomes an operational record that no human has verified). The sign-off is the human gate that mitigates both risks.

**Q65 — B**
Item 3 must have a human gate: deploying changes to a production authentication service is a high-impact, potentially irreversible action — exactly the category objective 3.3 reserves for human approval. If the deploy breaks authentication, all users may be locked out. Item 5 must have a human gate: an AI-generated report sent directly to the board of directors without human review risks hallucinated findings reaching the highest executive level, where they could drive incorrect strategic decisions. SAST gate (1), SCA gate (2), and rollback (4) are appropriate for full automation.

**Q66 — C**
A KQL query that is syntactically valid but logically incorrect — hunting for the wrong behavior and returning zero results — is a hallucination: the AI generated confident-looking output (a valid query) that does not actually accomplish the intended task. This is distinct from adversarial evasion (the attacker obfuscated activity, not the query).

**Q67 — B**
One client's telemetry data influencing another client's AI outputs via a shared model is cross-tenant telemetry leakage — a specific privacy risk when multiple clients share an AI training or inference environment. This is the domain 3 telemetry privacy risk applied to a multi-tenant MSSP deployment.

**Q68 — B**
SHAP values provide per-feature contribution scores for a specific prediction, showing the analyst exactly which features (process creation rate, outbound bytes, login hour) drove the risk score. This is the explainability technique CompTIA references for making black-box model decisions interpretable.

**Q69 — C**
Model drift: the threat landscape (AI-generated phishing tactics and evasion techniques) has evolved since the model was trained, and the model's learned patterns no longer fully capture current attack techniques. Performance degradation without model updates is the textbook signature of model drift.

**Q70 — B**
The three core risks in fully replacing analyst judgment with AI are: (1) automation bias — removing oversight means AI errors become operational decisions with no human check; (2) adversarial evasion — sophisticated attackers who know the organization relies solely on AI can craft activity designed to evade learned patterns, with no fallback human analyst; (3) hallucination — unverified AI-generated threat summaries, queries, and analysis will produce incorrect operational decisions at scale. These three risks are the high-yield intersection of objectives 3.1, 3.2, and 3.3 with the Domain 3 limitations section.
