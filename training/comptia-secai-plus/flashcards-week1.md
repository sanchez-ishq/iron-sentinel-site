# SecAI+ (CY0-001) — Week 1 Flashcards: Domain 1 Terminology

**Scope:** Domain 1 — Basic AI Concepts Related to Cybersecurity (objectives 1.1, 1.2, 1.3).
**How to use:** Cover the indented answer, read the **bold front**, recall it aloud, then reveal. Mark misses and re-drill. ~55 cards. (Anki-importable TSV at the bottom.)

> Goal for Week 1: be *fluent* in this vocabulary before Domain 2 — every later domain assumes it.

---

## Objective 1.1 — AI Types & Techniques

**1. Generative AI**
> A class of (usually deep-learning) models that *create* new content — text, images, code, audio — rather than only classify or predict. LLMs and diffusion models are examples.

**2. Machine learning (ML)**
> A subset of AI in which a system learns patterns from data instead of following hand-coded rules.

**3. Statistical learning**
> The mathematical foundation under ML — theory/methods (regression, classification, inference) for learning relationships from data. CompTIA lists it as a distinct AI technique.

**4. Deep learning**
> A subset of ML using multi-layer neural networks to learn representations from raw data. Drives modern vision, speech, and language.

**5. Transformer**
> The neural-network architecture built on **self-attention** that scores the relevance of every token to every other token regardless of distance. Backbone of modern LLMs.

**6. Natural language processing (NLP)**
> AI techniques for understanding/generating human language. Encompasses LLMs, SLMs, and related models.

**7. Large language model (LLM)**
> A transformer trained at massive scale to generate text by predicting the next token. Primary target of prompt injection/jailbreaks.

**8. Small language model (SLM)**
> A compact language model for edge / on-prem / low-cost use. Keeps data off third-party APIs (privacy win) but often has weaker guardrails.

**9. Generative adversarial network (GAN)**
> Two networks trained in competition — a **generator** makes fakes, a **discriminator** detects them. Powers deepfakes and synthetic data. (Diffusion *denoises*; a GAN *competes*.)

**10. Supervised learning**
> Training on **labeled** input→output pairs. Security uses: malware classification, phishing detection.

**11. Unsupervised learning**
> Training on **unlabeled** data to find structure/anomalies. Security uses: anomaly detection, UEBA, clustering.

**12. Reinforcement learning (RL)**
> An agent learns by trial-and-error to maximize a **reward** signal; no labeled data.

**13. Model validation**
> Evaluating a model on held-out data to confirm it generalizes (not just memorizes) before trust/deployment.

**14. Fine-tuning**
> Additional training of a pre-trained model on a smaller task-specific dataset to adapt its weights. (A form of transfer learning.)

**15. Epoch**
> One complete pass through the training dataset during training.

**16. Pruning**
> Removing redundant weights/neurons to shrink a model with minimal accuracy loss. (Optimization, not training.)

**17. Quantization**
> Reducing weight numeric precision (e.g., FP32→INT8) to shrink and speed a model. Can subtly alter safety behavior — integrity-check the artifact.

**18. System prompt**
> Developer-set instructions defining the model's persona, scope, and constraints; usually hidden from the user. A target of extraction/override attacks.

**19. User prompt**
> The end user's input at inference time — the primary channel for prompt injection.

**20. System roles**
> The labeled roles structuring a conversation (system / user / assistant) that the model uses to interpret instructions vs. dialogue.

**21. Zero-shot prompting**
> Giving the model an instruction with **no** examples.

**22. One-shot prompting**
> Providing exactly **one** worked example in the prompt before the task.

**23. Multi-shot (few-shot) prompting**
> Providing **several** examples in the prompt to steer behavior — without changing weights.

**24. Prompt template**
> A reusable, parameterized prompt with placeholders. A prompt-engineering technique that doubles as a guardrail control in Domain 2.

**25. Training vs. inference**
> Training updates weights from data (offline, expensive); inference uses fixed weights to produce output (real-time). Prompt injection is an inference-time attack.

**26. Parameters / weights**
> The learned numeric values inside a model (its "knowledge"). A "7B" model has 7 billion weights.

**27. Hyperparameters**
> Settings chosen *before* training (learning rate, batch size, layers) — not learned from data.

**28. Overfitting**
> Model memorizes training data; high training accuracy but poor on new data. Remedy: regularization, more/representative data.

**29. Underfitting**
> Model too simple; poor accuracy on both training and test data.

**30. Hallucination**
> An LLM generating plausible but factually incorrect/unsupported output. Mitigate with grounding (RAG), output validation, and human review.

**31. Foundation model / transfer learning**
> Foundation model = large model pre-trained on broad data as a base. Transfer learning = adapting such a model to a new task instead of training from scratch.

---

## Objective 1.2 — Data Security for AI

**32. Data cleansing**
> Removing errors, duplicates, corrupt records, and noise from data before training.

**33. Data verification**
> Confirming the data is correct and accurate before it's trusted for training.

**34. Data provenance**
> The **origin** of data — where it came from and who produced it. (A point: the source.)

**35. Data lineage**
> The full documented **journey** of data — every transformation from origin to current state. (A path: the trail.)

**36. Data integrity**
> Assurance that data remains accurate, consistent, and unaltered over time.

**37. Data augmentation**
> Synthetically expanding a dataset (paraphrasing, noise, image transforms) to improve robustness and reduce overfitting.

**38. Data balancing**
> Correcting class imbalance (e.g., few malicious vs. many benign) via resampling or SMOTE — critical for security datasets.

**39. Structured / semi-structured / unstructured data**
> Structured = tables/DB rows; semi-structured = JSON/XML/logs; unstructured = free text, images, PCAP. Most security AI data is semi-/unstructured.

**40. Watermarking**
> Embedding a detectable marker in AI outputs (flag machine-generated content) or in models/data (prove theft / establish provenance).

**41. Retrieval-augmented generation (RAG)**
> Augmenting an LLM at inference time with documents retrieved from an external store, extending knowledge without retraining.

**42. Embedding**
> A high-dimensional vector representation of data where semantically similar items are geometrically close. Enables semantic search.

**43. Vector storage (vector database)**
> A database optimized to store embeddings and query them via approximate nearest-neighbor search. A sensitive data store — must be access-controlled.

---

## Objective 1.3 — Security Throughout the AI Lifecycle

**44. Business use-case alignment**
> The first secure-lifecycle activity: define the use case and align it to corporate objectives, risk appetite, and compliance *before* gathering data.

**45. Data-collection trustworthiness**
> Collecting data only from reliable, vetted sources so it can be trusted downstream.

**46. Data-collection authenticity**
> Ensuring collected data is genuinely what it claims to be — not spoofed, forged, or AI-fabricated.

**47. Data preparation**
> Cleaning, labeling, transforming, and splitting data for training.

**48. Model development / selection**
> Choosing and building the model/architecture appropriate to the use case.

**49. Model evaluation**
> Measuring performance (accuracy, bias, robustness) on held-out data before deployment.

**50. Deployment & validation**
> Releasing the model into production and validating it behaves correctly in the real environment.

**51. Monitoring & maintenance**
> Ongoing tracking for drift, degradation, and new risks after deployment; retraining as needed.

**52. Feedback & iteration**
> Feeding production results and corrections back into data/retraining — making the lifecycle a **loop, not a line**.

**53. Human-in-the-loop (HITL)**
> A human reviews and approves an AI decision/action *before* it is executed.

**54. Human oversight**
> Humans monitor the AI and can intervene, override, or shut it down.

**55. Human validation**
> A human verifies AI-generated outputs/quality before they are trusted or acted upon.

---

## Quick self-test (recall the term from the clue)

1. Origin of data vs. its full transformation trail → **provenance** vs. **lineage**
2. FP32→INT8 to shrink a model → **quantization**
3. Generator vs. discriminator in competition → **GAN**
4. No examples in the prompt → **zero-shot**
5. High training accuracy, low real-world accuracy → **overfitting**
6. Store embeddings for semantic search → **vector database**
7. Human verifies AI output before it's trusted → **human validation**

---

## Anki / Quizlet import (TSV — term &lt;TAB&gt; definition)

Copy the block below into a `.txt` and import as **Tab-separated** (Anki: *File → Import*; field 1 = Front, field 2 = Back). Anki can auto-generate reverse cards.

```tsv
Generative AI	Deep-learning models that create new content (text/image/code) rather than only classify/predict
Statistical learning	Mathematical foundation under ML for learning relationships from data; a distinct AI technique
Transformer	Architecture using self-attention to weigh all token pairs regardless of distance; backbone of LLMs
LLM	Large language model — transformer trained at scale to generate text by predicting the next token
SLM	Small language model — compact model for edge/on-prem/low-cost use; keeps data off third-party APIs
GAN	Generative adversarial network — generator vs. discriminator trained in competition; powers deepfakes
Supervised learning	Training on labeled input→output pairs (malware/phishing classification)
Unsupervised learning	Training on unlabeled data to find structure/anomalies (anomaly detection, UEBA)
Reinforcement learning	Learning by trial-and-error to maximize a reward signal; no labeled data
Model validation	Evaluating a model on held-out data to confirm it generalizes before trust/deployment
Fine-tuning	Extra training of a pre-trained model on a task-specific dataset to adapt its weights
Epoch	One complete pass through the training dataset
Pruning	Removing redundant weights/neurons to shrink a model with minimal accuracy loss
Quantization	Reducing weight precision (FP32→INT8) to shrink/speed a model; can alter safety behavior
System prompt	Developer-set hidden instructions defining persona/scope/constraints; target of extraction
Zero-shot prompting	Instruction with no examples in the prompt
One-shot prompting	Exactly one worked example in the prompt
Multi-shot prompting	Several examples in the prompt to steer behavior without changing weights
Prompt template	Reusable parameterized prompt with placeholders; also a guardrail control
Parameters/weights	Learned numeric values inside a model (its knowledge); e.g., 7B weights
Hyperparameters	Settings chosen before training (learning rate, batch size, layers); not learned
Overfitting	Memorizes training data; high train accuracy, poor on new data
Underfitting	Model too simple; poor accuracy on both training and test data
Hallucination	LLM generating plausible but factually wrong/unsupported output
Foundation model	Large model pre-trained on broad data as a base for downstream tasks
Transfer learning	Adapting a pre-trained model to a new task instead of training from scratch
Data cleansing	Removing errors, duplicates, corrupt records, and noise before training
Data verification	Confirming data is correct/accurate before trusting it for training
Data provenance	The origin of data — where it came from and who produced it
Data lineage	The full documented trail of every transformation from origin to current state
Data integrity	Assurance data remains accurate, consistent, and unaltered over time
Data augmentation	Synthetically expanding a dataset to improve robustness and reduce overfitting
Data balancing	Correcting class imbalance (resampling/SMOTE); key for security datasets
Structured data	Fixed-schema data — tables, DB rows, CSV
Semi-structured data	Tagged but flexible data — JSON, XML, logs
Unstructured data	No schema — free text, images, audio, PCAP
Watermarking	Embedding a detectable marker in AI outputs/models to flag origin or prove theft
RAG	Retrieval-augmented generation — augmenting an LLM with retrieved docs at inference time
Embedding	High-dimensional vector representation where similar items are geometrically close
Vector database	Store optimized for embeddings using approximate nearest-neighbor search; access-control it
Use-case alignment	First secure-lifecycle step: align the AI use case to corporate objectives before data work
Data-collection trustworthiness	Collecting data only from reliable, vetted sources
Data-collection authenticity	Ensuring collected data is genuine — not spoofed, forged, or AI-fabricated
Model evaluation	Measuring performance/bias/robustness on held-out data before deployment
Monitoring and maintenance	Tracking drift/degradation/new risks after deployment; retraining as needed
Feedback and iteration	Feeding production results/corrections back into retraining — lifecycle is a loop
Human-in-the-loop	A human approves an AI decision/action before it executes
Human oversight	Humans monitor the AI and can intervene/override/shut it down
Human validation	A human verifies AI outputs/quality before they are trusted or acted upon
```

---

*Week 1 deck. Master these before Domain 2. Log weak cards in `99-PROGRESS-TRACKER.md`.*
