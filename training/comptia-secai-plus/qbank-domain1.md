# CompTIA SecAI+ (CY0-001 V1) — Domain 1 Practice Question Bank

Domain 1 bank — 55 questions, weighted to objectives 1.1–1.3 (official CY0-001 V1 v2.0).

**Domain:** 1 — Basic AI Concepts Related to Cybersecurity
**Exam weight:** 17%
**Questions:** Q1–Q55 (includes 5 Performance-Based Questions marked PBQ)
**Coverage:** Objectives 1.1 (AI types/techniques, model training, prompt engineering), 1.2 (data security for AI), 1.3 (AI life cycle security)

> Instructions: Select the single best answer unless the question specifies "(Choose two)." Allow approximately 90 seconds per standard question and 3–4 minutes per PBQ. Target 85% or better before sitting the exam.

---

## Objective 1.1 — AI Types, Techniques, Model Training, and Prompt Engineering

---

**Q1.** A security vendor markets its product as using "machine learning." A competing vendor claims its product uses "artificial intelligence." Which statement BEST describes the relationship between these two terms?

A) Machine learning and artificial intelligence describe the same field and the terms are interchangeable.
B) Artificial intelligence is the broader field; machine learning is a subset in which systems learn patterns from data rather than following explicit rules.
C) Machine learning is the broader field; artificial intelligence specifically refers to systems that use neural networks.
D) Artificial intelligence requires labeled training data; machine learning does not.

---

**Q2.** A SOC analyst is reviewing a model that groups network connections into clusters of similar behavior without being told in advance how many categories exist or what they mean. Which machine learning paradigm does this MOST accurately describe?

A) Supervised learning
B) Reinforcement learning
C) Unsupervised learning
D) Transfer learning

---

**Q3.** A threat-hunting team deploys an autonomous red-team agent that attempts attack paths, receives a score indicating how far it progressed before detection, and adjusts its strategy to maximize that score over repeated runs. Which machine learning paradigm is this?

A) Supervised learning — the agent learns from labeled attack data
B) Unsupervised learning — the agent clusters attack paths by similarity
C) Reinforcement learning — the agent learns by maximizing a reward signal from the environment
D) Fine-tuning — the agent adapts a pre-trained model to new targets

---

**Q4.** An email gateway uses a model trained on 2 million emails labeled "phishing" or "legitimate." The model correctly classifies 94% of new emails. Which combination of learning paradigm and output type BEST describes this system?

A) Unsupervised learning producing an anomaly score
B) Supervised learning producing a classification label
C) Reinforcement learning producing a policy
D) Generative AI producing a text prediction

---

**Q5.** Which of the following BEST distinguishes statistical learning from machine learning as named AI techniques in the CompTIA CY0-001 objectives?

A) Statistical learning uses neural networks; machine learning uses rule-based decision trees.
B) Statistical learning is only applicable to structured tabular data; machine learning can handle images and text.
C) Statistical learning emphasizes the underlying mathematical and probabilistic modeling of data relationships; machine learning emphasizes the algorithmic engineering practice of building systems that learn.
D) Statistical learning requires no training data; machine learning always requires a labeled dataset.

---

**Q6.** A generative AI system creates synthetic phishing emails indistinguishable from real ones. Into which portion of the AI hierarchy does generative AI fall?

A) A sibling category to machine learning — generative AI and ML are parallel fields
B) A subset of deep learning, which is a subset of machine learning, which is a subset of artificial intelligence
C) A subset of statistical learning that exists outside the machine learning hierarchy
D) A synonym for large language models — all generative AI systems are LLMs

---

**Q7.** A vendor's AI system produces detailed security reports by generating new text based on learned patterns from millions of incident reports. This is an example of which model category?

A) Regression model
B) Clustering model
C) Generative AI
D) Anomaly detector

---

**Q8.** What is the defining architectural feature of a transformer that distinguishes it from earlier recurrent neural networks?

A) The transformer uses reinforcement learning; recurrent networks use supervised learning
B) The transformer applies a self-attention mechanism that computes relevance between all tokens in a sequence simultaneously, regardless of their distance
C) The transformer can only process structured tabular data; recurrent networks handle text
D) The transformer uses a discriminator to evaluate generator outputs

---

**Q9.** A security team wants to run a language model locally on a laptop with 16 GB of RAM to analyze incident logs without sending data to an external API. Which model type is MOST appropriate?

A) A large language model (LLM) with 70 billion parameters
B) A generative adversarial network (GAN)
C) A small language model (SLM) designed for edge or on-premises deployment
D) A diffusion model fine-tuned on log data

---

**Q10.** An AI system generates photorealistic "deepfake" images of executives to use in spear-phishing campaigns. The system consists of two neural networks: one that creates synthetic images and another that tries to distinguish them from real photographs. Which architecture is this?

A) Transformer with self-attention
B) Retrieval-Augmented Generation (RAG)
C) Generative Adversarial Network (GAN)
D) Diffusion model

---

**Q11.** A researcher is building synthetic training images by starting with random noise and iteratively applying a learned denoising process until recognizable images emerge. Which generative architecture does this describe?

A) Generative Adversarial Network (GAN)
B) Diffusion model
C) Large Language Model (LLM)
D) Variational autoencoder used with supervised labels

---

**Q12.** Which of the following BEST explains the difference between a GAN and a diffusion model in the context of generating synthetic phishing media?

A) A GAN uses a denoising process; a diffusion model uses a generator-discriminator contest
B) A GAN pits a generator against a discriminator; a diffusion model learns to reverse a noise-adding process
C) A GAN operates only on text; a diffusion model operates only on images
D) A GAN requires reinforcement learning; a diffusion model uses unsupervised clustering

---

**Q13.** A natural language processing pipeline converts raw text alerts into vector representations so an LLM can reason about their semantic meaning. Which sub-field of AI does this pipeline MOST directly implement?

A) Reinforcement learning
B) Natural language processing (NLP)
C) Computer vision
D) Statistical process control

---

**Q14.** During model training, an engineer runs the entire training dataset through the model 50 times before stopping. What does each complete pass through the training dataset represent?

A) A batch
B) A hyperparameter
C) An epoch
D) A gradient

---

**Q15.** A model development team reduces a 7-billion-parameter language model to the 30% of weights that contribute most to prediction accuracy and removes the rest. What technique is this, and what is the PRIMARY security consideration?

A) Quantization; it reduces memory but may leak training data
B) Pruning; the optimized artifact is a new build artifact that must be integrity-checked and is subject to supply-chain controls
C) Fine-tuning; it re-trains the model on task-specific data and adds new weights
D) Data balancing; it corrects class imbalance in the training set

---

**Q16.** An MLOps engineer converts a model's stored weights from 32-bit floating-point (FP32) to 8-bit integer (INT8) format before shipping it to embedded network sensors. Which optimization technique is this, and what is the key security concern?

A) Pruning; low-importance neurons may retain sensitive training data
B) Augmentation; synthetic data may introduce label errors
C) Quantization; the precision reduction can subtly shift the model's safety or guardrail behavior, requiring integrity verification of the new artifact
D) Watermarking; the compressed model may be identifiable by the marker

---

**Q17.** In the CompTIA CY0-001 objectives, epoch, pruning, and quantization are grouped under fine-tuning. Which statement BEST distinguishes epoch from pruning and quantization?

A) An epoch is a compression technique; pruning and quantization are training iterations
B) An epoch measures data provenance; pruning and quantization measure model accuracy
C) An epoch is one complete pass through the training data during the learning process; pruning and quantization are post-training optimization/compression operations
D) Epoch, pruning, and quantization all refer to different stages of the reinforcement learning reward cycle

---

**Q18.** A security analyst wants to guide an LLM to analyze a SIEM alert without providing any examples — only an instruction. Which prompt technique is this?

A) Multi-shot prompting
B) One-shot prompting
C) Zero-shot prompting
D) System role prompting

---

**Q19.** A SOC automation platform embeds a single example of a correctly formatted alert triage report before presenting the live alert to the LLM. Which prompt technique does this represent?

A) Zero-shot prompting
B) One-shot prompting
C) Multi-shot prompting
D) Fine-tuning

---

**Q20.** A threat intelligence workflow provides the LLM with five representative examples of indicator extraction before asking it to extract indicators from a new threat report. Which prompt technique BEST describes this approach?

A) Zero-shot prompting
B) One-shot prompting
C) Multi-shot (few-shot) prompting
D) System role assignment only

---

**Q21.** A developer builds a vulnerability triage copilot and sets instructions that define the model's persona, restrict it to vulnerability-management topics, and prohibit it from running code — all before the user sends any message. Which prompt component is the developer configuring?

A) User prompt
B) System prompt
C) One-shot example
D) Temperature

---

**Q22.** A prompt template reads: "You are a cybersecurity analyst. Classify the following SIEM alert as Critical, High, Medium, or Low. Alert: {alert_text}". Which statement BEST describes the security value of using this template rather than free-form user input?

A) The template eliminates the need for model fine-tuning, reducing training costs
B) The template constrains where and how user input is inserted, reducing the prompt-injection surface area
C) The template converts unstructured alert text into a structured database record
D) The template automatically watermarks all outputs with the analyst's identity

---

**Q23.** A model is given a "system role" specifying it is a senior threat intelligence analyst who speaks only in structured JSON. What is the PRIMARY purpose of assigning a system role?

A) To change the model's underlying weights to match an analyst persona
B) To define the model's behavioral context, scope, and output format for the session without modifying its parameters
C) To grant the model access to external threat intelligence APIs
D) To perform one-shot prompting by providing a single analyst example

---

**Q24 (PBQ).** You are evaluating a malware-classification model before deployment. You observe the following results:

- Training set: precision 98%, recall 97%, F1 98%
- Validation set: precision 96%, recall 95%, F1 95%
- Test set (held-out, unseen): precision 61%, recall 58%, F1 59%
- The training dataset contained 600,000 samples collected over three years.
- No samples from the past six months are represented.

A colleague proposes simply applying dropout regularization and resubmitting the same training data. A second colleague proposes collecting fresh samples from the past six months and retraining.

Which analysis is MOST accurate?

A) The gap between training and test accuracy indicates underfitting. Applying dropout will improve test-set performance by simplifying the model.
B) The gap indicates overfitting and potential distribution shift. Dropout alone will not address the missing six months of data. Retraining with current samples is the higher-priority fix.
C) The test-set scores are acceptable for a cybersecurity classifier. No action is needed.
D) The issue is insufficient epochs. Running additional training iterations on the existing data will close the accuracy gap.

---

**Q25.** A security team trains a language model on 2 years of internal security policy documents to answer employee questions. After deployment, users report the model invents policy clauses that do not exist. Which ML phenomenon BEST describes this behavior?

A) Overfitting — the model memorized the policy documents exactly
B) Underfitting — the model is too simple to understand the policies
C) Hallucination — the model generates plausible but fabricated content
D) Label poisoning — the training labels were corrupted by an attacker

---

**Q26.** Which of the following lists the correct hierarchy from BROADEST to MOST specific?

A) Machine learning → Deep learning → Artificial intelligence → Generative AI
B) Generative AI → Deep learning → Machine learning → Artificial intelligence
C) Artificial intelligence → Machine learning → Deep learning → Generative AI
D) Deep learning → Machine learning → Artificial intelligence → Generative AI

---

**Q27.** An LLM processes a 2,000-token user prompt and a 500-token system prompt. The context window limit is 4,096 tokens. The model's response is 2,000 tokens. What happens?

A) The model automatically discards the system prompt to fit the response
B) The total (4,500 tokens) exceeds the 4,096-token limit, which may cause the model to truncate input or refuse to generate a full response
C) The response expands the context window dynamically without consequence
D) The model converts excess tokens into embeddings stored in a vector database

---

**Q28.** A security engineer fine-tunes a foundation model on a dataset of 10,000 curated threat intelligence reports. After fine-tuning, the model shows improved accuracy on threat-intel tasks. A red teamer later discovers that 200 of the 10,000 reports were subtly modified to cause the model to misclassify a specific threat actor's tools as benign. What attack does this represent?

A) Prompt injection at inference time
B) Model inversion during training
C) Fine-tune poisoning — a backdoor injected through the fine-tuning dataset
D) Quantization-induced guardrail bypass

---

**Q29.** Which of the following is a hyperparameter rather than a learned model parameter?

A) The attention weights in a transformer's self-attention heads
B) The bias neurons in a hidden layer
C) The number of hidden layers specified before training begins
D) The token embedding produced for the word "malware"

---

**Q30.** An intrusion detection system is evaluated and found to perform poorly on both its training data and on live network traffic. Which condition does this MOST likely indicate?

A) Overfitting — the model memorized the training data
B) Underfitting — the model is too simple to capture attack patterns in the data
C) Data poisoning — the training labels were flipped by an attacker
D) Hallucination — the model is generating false detections

---

## Objective 1.2 — Data Security in Relation to AI

---

**Q31.** A data engineering team ingesting threat feeds notices duplicate records, malformed IP addresses, and corrupted timestamps. Before using this data to train a detection model, they systematically identify and remove these errors. Which data-preparation activity is this?

A) Data augmentation
B) Data balancing
C) Data cleansing
D) Data provenance

---

**Q32.** A machine learning team confirms that every IP address in the training dataset is a valid IPv4 address, that timestamps fall within the expected range, and that protocol fields match allowed values. Which data-preparation activity BEST describes what they are doing?

A) Data lineage tracking
B) Data verification
C) Data balancing
D) Data watermarking

---

**Q33.** A security analyst asks: "Where did this training record originally come from, and who produced it?" Which data-security concept answers this question?

A) Data lineage
B) Data integrity
C) Data augmentation
D) Data provenance

---

**Q34.** An auditor asks the ML team to produce a document showing every transformation, processing step, and system the training data passed through from its original source to the current model. Which concept does the auditor need?

A) Data provenance
B) Data lineage
C) Data integrity
D) Data augmentation

---

**Q35.** A model training pipeline uses cryptographic hashing to verify that training dataset files have not been altered since they were approved by the data governance team. Which data-security property is being enforced?

A) Data provenance
B) Data lineage
C) Data integrity
D) Data augmentation

---

**Q36.** A security team improves a phishing-detection model by paraphrasing existing phishing emails into new variations, adding slight spelling differences, and generating alternative subject lines — all without collecting new real samples. Which data-preparation technique is this?

A) Data cleansing
B) Data balancing
C) Data verification
D) Data augmentation

---

**Q37.** A network anomaly detection dataset contains 2,000,000 normal connection records and only 1,800 records of known lateral movement. The resulting model almost never alerts on lateral movement. Which data-preparation technique MOST directly addresses this problem?

A) Data cleansing to remove duplicate normal records
B) Data augmentation with synthetic normal connections
C) Data balancing using resampling or SMOTE to increase representation of the lateral-movement class
D) Data lineage tracking to identify the source of missing records

---

**Q38 (PBQ).** A compliance officer is reviewing the AI development process for a new fraud-detection model. She identifies the following issues:

1. The raw transaction data came from three external feeds, but there is no record of which feed each record came from.
2. The data passed through five ETL transformations, but only two are documented.
3. After the data was approved, a junior analyst made undocumented edits to 12,000 records.
4. The model training dataset has 50x more non-fraud samples than fraud samples.

Match each issue to the CORRECT data-security concept it violates.

Issue 1 — unknown origin of records:
Issue 2 — incomplete transformation documentation:
Issue 3 — undocumented post-approval edits:
Issue 4 — class imbalance:

A) 1=Lineage, 2=Provenance, 3=Integrity, 4=Balancing
B) 1=Provenance, 2=Lineage, 3=Integrity, 4=Balancing
C) 1=Integrity, 2=Provenance, 3=Lineage, 4=Augmentation
D) 1=Provenance, 2=Integrity, 3=Lineage, 4=Cleansing

---

**Q39.** A CISO reviewing training data asks the team to categorize the data types present. Network flow records in a relational database table, JSON-formatted firewall logs, and raw email body text are all present. Which classification correctly maps these three data types?

A) All three are unstructured data
B) Relational table = structured; JSON logs = semi-structured; email body text = unstructured
C) Relational table = semi-structured; JSON logs = structured; email body text = unstructured
D) All three are semi-structured because they can be parsed programmatically

---

**Q40.** An AI company wants to both identify AI-generated content in news articles and prove ownership if a proprietary model is stolen. Which single technique addresses both goals?

A) Quantization
B) Data provenance tracking
C) Watermarking
D) Data augmentation

---

**Q41.** A security researcher explains how a RAG system works to a junior analyst. Which sequence CORRECTLY describes the RAG inference pipeline?

A) The LLM generates an answer → the vector database searches for relevant documents → the answer is appended with citations
B) The query is embedded → the vector database retrieves similar document chunks → retrieved chunks are added to the LLM's context → the LLM generates a grounded answer
C) The training data is updated with new documents → the model is retrained → the retrained model answers the query
D) The query is tokenized → the system prompt is replaced with retrieved documents → the user prompt is discarded

---

**Q42.** A threat intelligence platform stores vectorized representations of threat reports so the LLM can retrieve semantically relevant documents at query time. What are these vector representations called, and where are they stored?

A) Tokens stored in a relational database
B) Embeddings stored in a vector database
C) Hyperparameters stored in a model checkpoint
D) Labels stored in a training dataset

---

**Q43.** An attacker gains write access to the document corpus of a RAG-powered security assistant and embeds hidden instructions in several documents telling the assistant to exfiltrate retrieved content. Which attack technique is this?

A) Direct prompt injection through the user turn
B) Model inversion of the vector database
C) Indirect prompt injection via the RAG retrieval corpus
D) Membership inference through embedding queries

---

## Objective 1.3 — Security Throughout the AI Life Cycle

---

**Q44.** A security team is building an AI-powered alert triage system. Before selecting a model architecture or gathering data, the project lead insists on a formal document that defines the business problem, links the AI system to corporate risk appetite, and identifies the regulatory constraints. Which AI life-cycle stage is being completed?

A) Data collection
B) Model evaluation
C) Business use-case alignment with corporate objectives
D) Deployment

---

**Q45.** An organization's AI governance policy states that all training data must come from "trustworthy and authentic sources." A data engineer interprets this as meaning data must be from vetted, reputable sources and must genuinely represent what it claims to be — not spoofed, forged, or AI-fabricated. Which life-cycle stage does this control apply to?

A) Model evaluation
B) Deployment
C) Data collection
D) Feedback and iteration

---

**Q46.** A model for detecting insider threats is deployed and begins producing recommendations, but no analyst reviews its outputs before cases are opened and employees are notified. A compliance officer flags this as a violation of a core human-centric AI principle. Which principle is violated?

A) Human-in-the-loop — a human should approve decisions before they trigger action
B) Model pruning — the model should be compressed before deployment
C) Zero-shot prompting — the model should not act without an example
D) Data lineage — the source of the model's recommendations must be documented

---

**Q47.** After an AI fraud-detection model is deployed, the security team sets up dashboards to track the model's precision, recall, and false-positive rate daily, with alerts if metrics drop outside acceptable ranges. Which AI life-cycle stage does this represent?

A) Model development and selection
B) Data preparation
C) Monitoring and maintenance
D) Feedback and iteration

---

**Q48.** Six months after a phishing-detection model is deployed, performance degrades because attackers have changed their tactics. Analysts flag newly missed phishing emails, which are added to a retrained dataset. The model is then updated. Which life-cycle stage best describes incorporating those analyst corrections back into the model?

A) Business use-case alignment
B) Deployment
C) Human validation only — no life-cycle stage is triggered
D) Feedback and iteration leading to retraining

---

**Q49 (PBQ).** Your organization's security AI review board is auditing an ML-powered vulnerability-prioritization tool. The board has the following findings:

Finding 1: The tool was built because a developer found it interesting — there is no documented alignment to the organization's vulnerability management policy or risk framework.
Finding 2: Training data was pulled from a public exploit database with no verification of authenticity. Several records were later found to be community-submitted with no validation.
Finding 3: The model was deployed directly to production after training, with no held-out test evaluation.
Finding 4: There is no process to update the model when new CVEs are published.
Finding 5: All vulnerability closure decisions are automated with no analyst review.

For each finding, identify the AI life-cycle stage or human-centric design principle that was omitted or violated.

A) 1=Data collection, 2=Business use-case, 3=Monitoring, 4=Feedback, 5=Human-in-the-loop
B) 1=Business use-case alignment, 2=Data collection (authenticity), 3=Model evaluation, 4=Monitoring and maintenance, 5=Human-in-the-loop
C) 1=Model development, 2=Data preparation, 3=Deployment, 4=Validation, 5=Human oversight
D) 1=Deployment, 2=Data lineage, 3=Model selection, 4=Feedback, 5=Human validation

---

**Q50.** A red team discovers that an AI model retired six months ago still has its weight files accessible on a network share with no access controls, and the training dataset is stored alongside it. Which life-cycle stage gap does this represent?

A) The data collection stage was skipped
B) The retirement/decommissioning stage was not completed — model artifacts were not secured or destroyed
C) The monitoring stage failed to detect the model's performance degradation
D) The human-in-the-loop principle was violated because no human approved the retirement

---

**Q51.** Which statement BEST distinguishes human oversight from human-in-the-loop as human-centric AI design principles?

A) Human-in-the-loop means a human monitors aggregate model metrics; human oversight means a human approves each individual AI decision before it takes effect
B) Human-in-the-loop means a human approves individual decisions before they are executed; human oversight means humans monitor, can intervene, and can override the system — but are not required to approve every single action
C) Human-in-the-loop and human oversight are synonymous; the terms are used interchangeably in the CompTIA objectives
D) Human oversight applies only during the training stage; human-in-the-loop applies only during deployment

---

**Q52 (PBQ).** A healthcare organization is deploying an AI system to flag anomalous access to patient records. The security architect must design the system to comply with human-centric AI design requirements. The following design choices are proposed:

Option A: The AI flags anomalies and automatically disables the user account with no further review.
Option B: The AI flags anomalies and a human analyst reviews each flag before any account action is taken.
Option C: The AI flags anomalies, a senior analyst reviews the overall flagging rate weekly, and individual flags trigger automated account lockout.
Option D: The AI flags anomalies, each flag requires analyst approval before account action, and a weekly executive report shows overall model accuracy and any edge cases for governance review.

Which option MOST comprehensively satisfies human-in-the-loop, human oversight, AND human validation simultaneously?

A) Option A
B) Option B
C) Option C
D) Option D

---

**Q53.** During which AI life-cycle stage would a team use a held-out test dataset to measure precision, recall, and F1 score — and decide whether the model is ready to go into production?

A) Data collection
B) Model evaluation
C) Monitoring and maintenance
D) Feedback and iteration

---

**Q54.** A security team discovers that the training data for their network anomaly detector was collected by scraping public forums where members posted fabricated "normal" traffic logs to pollute public datasets. Which data-collection security control failure does this represent?

A) The team failed to apply data balancing to the training set
B) The team failed to ensure data authenticity and trustworthiness at the collection stage
C) The team failed to apply watermarking to the training data outputs
D) The team failed to run a sufficient number of training epochs

---

**Q55 (PBQ).** An AI life-cycle governance policy states that "no AI model shall be deployed to a new environment without a re-validation step to confirm the model performs acceptably in that environment." A developer skips this step to meet a launch deadline, and the model begins misclassifying alerts in the new cloud environment. Which life-cycle principle does the policy and this failure scenario illustrate?

A) Data augmentation must be applied before each deployment
B) Validation is a required life-cycle stage that should be repeated at deployment, not only at initial development
C) Quantization must be completed before a model is moved to a new environment
D) The feedback and iteration stage is not needed if the model passed initial evaluation

---

## Answer Key

**Q1 — B**
Artificial intelligence is the umbrella field; machine learning is the subset that learns from data rather than following hand-coded rules. The terms are not interchangeable, and the nesting direction matters on exam scenarios.

**Q2 — C**
Discovering structure from unlabeled data with no predefined categories is the definition of unsupervised learning. Clustering network connections with no labels provided is a canonical unsupervised use case.

**Q3 — C**
An agent that takes actions, receives a reward score based on outcomes, and adjusts strategy to maximize cumulative reward is implementing reinforcement learning. There are no labeled examples, which rules out supervised learning.

**Q4 — B**
Labeled training examples (phishing / legitimate) define supervised learning. Producing a discrete category label (phishing or legitimate) makes the output a classification. This combination is supervised classification.

**Q5 — C**
CompTIA lists both as named AI types/techniques. Statistical learning stresses the mathematical and probabilistic theory; machine learning stresses the engineering practice of building adaptive systems. Both can handle many data types.

**Q6 — B**
Generative AI is a subset of deep learning (requires multi-layer neural networks to generate content), which is a subset of machine learning (pattern learning from data), which is a subset of artificial intelligence (the broadest field). The nesting is AI > ML > DL > GenAI.

**Q7 — C**
A system that generates new text (security reports) from learned patterns is generative AI. Regression produces numeric values; clustering groups data; anomaly detection flags outliers — none of these produce narrative text.

**Q8 — B**
The transformer's defining innovation is the self-attention mechanism, which computes relevance between every pair of tokens in the input simultaneously, eliminating the sequential bottleneck of recurrent networks. Transformers and recurrent networks both use supervised learning and have nothing to do with a discriminator.

**Q9 — C**
A small language model (SLM) is designed specifically for edge, on-premises, or low-cost deployment on constrained hardware. A 70B LLM requires far more than 16 GB RAM. GANs and diffusion models are generative media architectures, not log-analysis assistants.

**Q10 — C**
Two networks — one generator that creates fakes and one discriminator that distinguishes real from fake — competing adversarially defines a Generative Adversarial Network (GAN). Diffusion models work by denoising from random noise, not adversarial competition.

**Q11 — B**
Starting with random noise and iteratively denoising it until an image emerges is exactly how a diffusion model works (the forward process adds noise; the model learns the reverse). A GAN uses a generator-discriminator contest.

**Q12 — B**
GAN: generator versus discriminator adversarial contest. Diffusion model: iterative reversal of a noise-adding process. The exam tests which mechanism belongs to which architecture — they are both generative but mechanically distinct.

**Q13 — B**
Converting text into vector representations for semantic reasoning is natural language processing (NLP). NLP is explicitly listed as an AI type/technique in objective 1.1, and processing text alerts to support LLM reasoning is a core NLP application.

**Q14 — C**
One complete pass through the entire training dataset is called an epoch. A batch is a subset processed in one step. A hyperparameter is a pre-training configuration. A gradient is the derivative used to update weights.

**Q15 — B**
Removing low-importance weights and neurons while retaining model accuracy is pruning. The security point is that the pruned model is a new build artifact distinct from the original and must be integrity-checked as part of supply-chain controls — it cannot simply be assumed to behave identically.

**Q16 — C**
Reducing weight numeric precision from FP32 to INT8 is quantization. The key security concern is that precision reduction can subtly alter safety filters or guardrail behavior, so the optimized artifact must be integrity-verified before deployment.

**Q17 — C**
An epoch is a training-time concept: one full pass over the data during the learning process. Pruning and quantization are post-training compression/optimization operations. CompTIA groups all three under fine-tuning, but they are mechanically distinct and the exam tests which is which.

**Q18 — C**
Providing an instruction with no worked examples is zero-shot prompting. The model must generalize purely from the instruction and its pre-training.

**Q19 — B**
Providing exactly one worked example before the real task is one-shot prompting. Zero-shot has no examples; multi-shot has several.

**Q20 — C**
Providing multiple worked examples (five, in this case) to establish the desired output pattern is multi-shot (few-shot) prompting. This is distinct from fine-tuning, which modifies the model's weights.

**Q21 — B**
Instructions that define persona, scope, and restrictions and that are set by the developer before any user interaction are the system prompt. The user has not sent anything yet, so this is not the user prompt, not a shot example, and not temperature.

**Q22 — B**
A prompt template constrains where user input can appear and in what format. This reduces the surface area for prompt injection because an attacker cannot easily break out of the placeholder structure to inject rogue instructions into the instruction portion of the prompt.

**Q23 — B**
A system role defines behavioral context, output format, and scope for the session without changing any underlying model weights. It is a prompt-level configuration, not a training operation.

**Q24 — B**
High training/validation accuracy with dramatically lower test-set accuracy is the signature of overfitting combined with distribution shift (the test set includes recent data the model has not seen). Dropout alone does not add the missing six months of samples. Retraining with current data is the higher-priority corrective action.

**Q25 — C**
Generating plausible but non-existent policy clauses is hallucination — the model produces confident, fabricated content. Overfitting would cause the model to reproduce training text verbatim, not invent new clauses. Underfitting would cause poor performance across the board.

**Q26 — C**
The correct nesting from broadest to most specific is: Artificial Intelligence > Machine Learning > Deep Learning > Generative AI. Every generative AI model is deep learning; every deep learning model is machine learning; all machine learning is a form of AI.

**Q27 — B**
The total token count (system prompt 500 + user prompt 2,000 + response 2,000 = 4,500) exceeds the 4,096-token context window. The model cannot process more tokens than the window allows; input will be truncated or generation will stop early. Context windows do not expand dynamically.

**Q28 — C**
Introducing malicious samples into a fine-tuning dataset to embed a backdoor trigger is fine-tune poisoning. The backdoor causes the model to misclassify specific inputs (the threat actor's tools) in a way that benefits the attacker. This is distinct from inference-time prompt injection.

**Q29 — C**
The number of hidden layers is specified by the practitioner before training — it is a hyperparameter. Attention weights, bias neurons, and token embeddings are all values the model learns or computes during training or inference; they are parameters, not hyperparameters.

**Q30 — B**
Poor performance on BOTH training data and live traffic means the model never learned the patterns well — this is underfitting (model too simple). Overfitting would show high training accuracy. Poisoning and hallucination would show different signatures.

**Q31 — C**
Identifying and removing errors, duplicates, malformed values, and corrupted records from data before training is data cleansing. Augmentation adds new synthetic data; balancing corrects class imbalance; provenance tracks origin.

**Q32 — B**
Confirming that field values are valid, in range, and correctly formatted before trusting data is data verification. Lineage tracks the transformation path; balancing corrects class distribution; watermarking embeds markers.

**Q33 — D**
"Where did it come from and who produced it?" is the data provenance question — it asks about origin and source. Lineage answers what happened to it after it was collected.

**Q34 — B**
A document of every transformation, processing step, and system the data passed through from source to current state is data lineage — the full audit trail of the data's journey. Provenance is only the origin point.

**Q35 — C**
Cryptographic hashing to confirm that data files have not been altered enforces data integrity — assurance that the data remains accurate, consistent, and unaltered. Provenance is origin; lineage is the transformation path.

**Q36 — D**
Synthetically expanding a dataset by creating new variations (paraphrased emails, spelling variants) without collecting new real samples is data augmentation. Its purpose is to improve model robustness and reduce overfitting.

**Q37 — C**
The root cause is severe class imbalance (2,000,000 normal vs. 1,800 lateral movement). Data balancing — via oversampling the minority class (SMOTE) or undersampling the majority — directly addresses this. Cleansing removes errors; augmenting normal records would worsen the imbalance.

**Q38 — B**
Issue 1 (unknown origin) = provenance (where did records come from?). Issue 2 (undocumented transformations) = lineage (the incomplete audit trail of processing steps). Issue 3 (undocumented post-approval edits) = integrity (data was altered without authorization). Issue 4 (class imbalance) = balancing. Answer B maps all four correctly.

**Q39 — B**
Relational database tables with a fixed schema = structured data. JSON firewall logs with tags but flexible structure = semi-structured. Raw email body text with no schema = unstructured. This is the standard three-tier data-type taxonomy CompTIA uses.

**Q40 — C**
Watermarking serves both goals: output watermarking embeds detectable markers in AI-generated content (identifying machine-generated articles), and model/data watermarking embeds markers in proprietary models to prove ownership if stolen. Quantization, provenance, and augmentation do not serve both purposes.

**Q41 — B**
The correct RAG pipeline is: embed the query → vector database retrieves similar document chunks → retrieved chunks are injected into the LLM's context → LLM generates an answer grounded in the retrieved content. RAG does not retrain the model and does not replace the user prompt.

**Q42 — B**
High-dimensional vector representations of data that capture semantic meaning are embeddings. They are stored in a vector database optimized for approximate nearest-neighbor search. Tokens are text units; hyperparameters are pre-training configurations; labels are supervised training answers.

**Q43 — C**
Planting adversarial instructions in documents within the RAG retrieval corpus so that the model executes them when it retrieves those documents is indirect prompt injection (also called retrieval corpus poisoning or stored/second-order prompt injection). Direct injection comes from the user's own input.

**Q44 — C**
Defining the business problem and linking the AI system to corporate objectives and risk appetite before any technical work begins is the business use-case alignment stage — the first stage of the secure AI life cycle in the CompTIA objectives.

**Q45 — C**
Ensuring that training data comes from vetted, reputable sources and that it genuinely represents what it claims to be (not spoofed, forged, or AI-fabricated) is a security control applied at the data collection stage of the AI life cycle.

**Q46 — A**
Requiring a human to approve decisions before they trigger real-world action is the human-in-the-loop principle. When the model issues case-opening notifications with no human review gate, human-in-the-loop is absent. Human oversight (monitoring the system) and human validation (verifying output quality) are related but distinct principles.

**Q47 — C**
Tracking model performance metrics continuously in production, with alerts for degradation, is monitoring and maintenance — the ongoing operational surveillance stage of the AI life cycle after deployment.

**Q48 — D**
Incorporating analyst corrections (new labeled examples of missed phishing) back into a retraining pipeline is feedback and iteration — the stage where production results and human expert input are used to improve the model and re-enter the life cycle.

**Q49 — B**
Finding 1 (no documented alignment) = business use-case alignment omitted. Finding 2 (no authenticity verification of training data) = data collection security (authenticity and trustworthiness) violated. Finding 3 (no test evaluation before production) = model evaluation stage skipped. Finding 4 (no update process for new CVEs) = monitoring and maintenance absent. Finding 5 (fully automated closures with no analyst) = human-in-the-loop principle violated. Answer B maps all five correctly.

**Q50 — B**
Leaving model weight files and training datasets accessible on an uncontrolled share after retirement means the retirement/decommissioning stage was not completed. Secure disposal and access revocation of model artifacts are required at end of life to prevent post-retirement theft.

**Q51 — B**
Human-in-the-loop: a human must approve individual decisions before action is taken. Human oversight: humans monitor the system, can intervene, and can override — but not every individual decision requires approval. These are distinct principles in the CompTIA objectives; conflating them is a common exam trap.

**Q52 — D**
Option D satisfies all three principles: analyst approval before account action (human-in-the-loop), an ongoing executive report that enables intervention and oversight (human oversight), and review of model accuracy and edge cases (human validation). Option B provides only human-in-the-loop. Option C provides only partial oversight without per-decision approval. Option A provides none.

**Q53 — B**
Measuring precision, recall, and F1 on a held-out test dataset to determine production readiness is the model evaluation stage. Monitoring happens after deployment; feedback occurs when production results are fed back; data collection happens before model development.

**Q54 — B**
Scraping public forums without verifying the authenticity of the records (which were fabricated by community members) is a failure to ensure data authenticity and trustworthiness at the data collection stage. This is a life-cycle 1.3 control: data collected without authenticity checks can poison the model at the source.

**Q55 — B**
Validation is an explicit life-cycle stage that confirms the model performs acceptably in its target environment. The CompTIA objectives treat it as a required step that should be repeated when a model moves to a new environment — not a one-time gate only at initial development. Skipping it here directly caused production misclassification.
