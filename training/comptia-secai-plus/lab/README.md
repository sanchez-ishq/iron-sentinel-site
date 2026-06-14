# SecAI+ Local Lab (runs against Ollama on SENTRY)

Hands-on tooling for the CompTIA SecAI+ study kit, designed to run on **SENTRY**
(Pop!_OS, RTX 5060 Ti 16 GB) against a **local DeepSeek-R1 model in Ollama** — fully
offline, nothing leaves the box. Running a self-hosted model *is itself* the Domain 4
"private model / data sovereignty" concept in practice.

## Prerequisites
- Ollama running with a model pulled (default `deepseek-r1:14b`):
  ```bash
  ollama pull deepseek-r1:14b
  ollama ps            # confirm PROCESSOR shows ~100% GPU
  ```
- Python 3 (stdlib only — no pip installs needed).

## Tools

### 1. `quiz.py` — offline question-bank drill
Parses the `qbank-*.md` files in the kit, quizzes you, grades you, and (optionally)
asks the local model to explain anything you miss.

```bash
# 50 random questions across all banks:
python3 quiz.py --n 50

# focus a domain (matches the filename), e.g. Domain 2:
python3 quiz.py --domain domain2 --n 30

# have the local model explain every miss:
python3 quiz.py --n 20 --explain

# just show how many questions parsed per bank:
python3 quiz.py --list
```
Answer with a letter (`B`), or comma/space for multi-select (`B,D`). `s` to skip, `q` to quit.

### 2. `injection_demo.py` — Domain 2 attack/defense sandbox
A deliberately under-guarded "assistant" backed by the local model, so you can *run*
the attacks the exam describes and then watch the controls stop them:
- **direct** prompt injection (system-prompt / secret extraction)
- **indirect** prompt injection (malicious instructions hidden in a "document")
- a **hardened** version with a prompt-firewall input check, an output filter, and a
  **RAG access-control** check (retrieval filtered by the user's clearance)

```bash
python3 injection_demo.py            # run all scenarios
python3 injection_demo.py --interactive   # type your own attacks at the vulnerable bot
```

## Config
Both tools read these env vars (sensible defaults):
- `OLLAMA_URL` (default `http://localhost:11434`)
- `SECAI_MODEL` (default `deepseek-r1:14b`)

```bash
SECAI_MODEL=deepseek-r1:8b python3 quiz.py --n 30
```

> Teaching note: because this all runs on SENTRY's local model, none of your prompts,
> the question banks, or the "documents" ever leave the machine — the same control you'd
> recommend to a client handling regulated data (Domain 4: private vs. public models).
