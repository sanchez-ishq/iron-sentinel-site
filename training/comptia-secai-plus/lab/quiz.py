#!/usr/bin/env python3
"""SecAI+ local quiz runner.

Drills the kit's qbank-*.md question banks offline. Optionally uses a local
Ollama model (default deepseek-r1:14b) to explain missed questions.

Stdlib only. Intended to run on SENTRY where Ollama serves the model, but it
also works without Ollama (the --explain feature is simply skipped).

Usage:
    python3 quiz.py --n 50
    python3 quiz.py --domain domain2 --n 30 --explain
    python3 quiz.py --list
"""
import argparse
import glob
import json
import os
import random
import re
import sys
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
MODEL = os.environ.get("SECAI_MODEL", "deepseek-r1:14b")

ANSWER_HDR = re.compile(r"^#{1,4}\s*Answer Key", re.I | re.M)
Q_START = re.compile(r"^\*\*Q(\d+)\b", re.M)
OPT = re.compile(r"^\s*([A-E])[\).]\s+(.*\S)\s*$", re.M)
TBL_ANS = re.compile(r"^\|\s*Q(\d+)\s*\|\s*([A-E](?:\s*,\s*[A-E])*)", re.M)
INLINE_ANS = re.compile(r"^\*\*Q(\d+)\s*[—\-:]+\s*([A-E](?:\s*(?:,|and|&)\s*[A-E])*)", re.M)


def strip_think(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()


def ollama_generate(prompt, model=None, timeout=180):
    model = model or MODEL
    body = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(
        OLLAMA_URL + "/api/generate", data=body,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return strip_think(json.loads(resp.read().decode()).get("response", ""))


def ollama_available():
    try:
        urllib.request.urlopen(OLLAMA_URL + "/api/tags", timeout=4)
        return True
    except Exception:
        return False


def parse_answers(block):
    ans = {}
    for m in TBL_ANS.finditer(block):
        ans[int(m.group(1))] = set(re.findall(r"[A-E]", m.group(2)))
    for m in INLINE_ANS.finditer(block):
        ans.setdefault(int(m.group(1)), set(re.findall(r"[A-E]", m.group(2))))
    return ans


def parse_file(path):
    text = open(path, encoding="utf-8").read()
    m = ANSWER_HDR.search(text)
    qpart = text[:m.start()] if m else text
    answers = parse_answers(text[m.start():]) if m else parse_answers(text)
    starts = [(int(mm.group(1)), mm.start()) for mm in Q_START.finditer(qpart)]
    out = []
    for i, (num, s) in enumerate(starts):
        e = starts[i + 1][1] if i + 1 < len(starts) else len(qpart)
        blk = qpart[s:e]
        first_opt = OPT.search(blk)
        if not first_opt or num not in answers:
            continue
        opts = dict(OPT.findall(blk))
        if not opts:
            continue
        stem = blk[:first_opt.start()]
        stem = re.sub(r"^\*\*Q\d+[^\n]*?\*\*\s*", "", stem, flags=re.S).strip()
        stem = stem.replace("(PBQ)", "").strip()
        out.append({
            "id": "%s#Q%d" % (os.path.basename(path), num),
            "src": os.path.basename(path),
            "stem": stem,
            "options": opts,
            "answer": answers[num],
        })
    return out


def load_questions(domain_filter=None):
    files = sorted(glob.glob(os.path.join(KIT, "qbank-*.md")))
    questions = []
    per_file = {}
    for f in files:
        if domain_filter and domain_filter.lower() not in os.path.basename(f).lower():
            continue
        qs = parse_file(f)
        per_file[os.path.basename(f)] = len(qs)
        questions.extend(qs)
    return questions, per_file


def normalize(raw):
    return set(re.findall(r"[A-E]", raw.upper()))


def explain(q):
    opts = "\n".join("%s) %s" % (k, v) for k, v in sorted(q["options"].items()))
    correct = ", ".join(sorted(q["answer"]))
    prompt = (
        "You are a CompTIA SecAI+ tutor. In 3-4 sentences, explain why the correct "
        "answer is %s for this question, and why the main distractor is wrong. Be concise.\n\n"
        "Question: %s\n%s\nCorrect answer: %s" % (correct, q["stem"], opts, correct))
    try:
        print("\n  …asking %s to explain (local, offline)…\n" % MODEL)
        print("  " + ollama_generate(prompt).replace("\n", "\n  "))
    except Exception as e:
        print("  (explanation unavailable: %s)" % e)


def run_quiz(args):
    questions, per_file = load_questions(args.domain)
    if not questions:
        print("No questions parsed. Check that qbank-*.md files are in %s" % KIT)
        return
    random.shuffle(questions)
    quiz = questions[:args.n]
    use_ai = args.explain and ollama_available()
    if args.explain and not use_ai:
        print("(Ollama not reachable at %s — running without AI explanations.)\n" % OLLAMA_URL)

    score = 0
    asked = 0
    for i, q in enumerate(quiz, 1):
        print("\n" + "=" * 70)
        print("Q%d/%d  [%s]" % (i, len(quiz), q["src"]))
        print(q["stem"])
        print()
        for k in sorted(q["options"]):
            print("  %s) %s" % (k, q["options"][k]))
        multi = len(q["answer"]) > 1
        prompt = "\nYour answer%s (or s=skip, q=quit): " % (" — choose %d" % len(q["answer"]) if multi else "")
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if raw.lower() == "q":
            break
        if raw.lower() == "s":
            print("  -> skipped. Answer: %s" % ", ".join(sorted(q["answer"])))
            continue
        asked += 1
        picked = normalize(raw)
        if picked == q["answer"]:
            score += 1
            print("  ✓ Correct.")
        else:
            print("  ✗ Incorrect. Correct answer: %s" % ", ".join(sorted(q["answer"])))
            if use_ai:
                explain(q)
    print("\n" + "=" * 70)
    if asked:
        print("Score: %d/%d (%.0f%%) over %d answered." % (
            score, asked, 100.0 * score / asked, asked))
        if 100.0 * score / asked >= 85:
            print("✓ At/above the 85%% target on this set.")
    else:
        print("No questions answered.")


def main():
    ap = argparse.ArgumentParser(description="SecAI+ local quiz runner")
    ap.add_argument("--n", type=int, default=25, help="number of questions (default 25)")
    ap.add_argument("--domain", help="filter by filename substring, e.g. domain2 / mock")
    ap.add_argument("--explain", action="store_true", help="use local Ollama to explain misses")
    ap.add_argument("--model", help="override model (default $SECAI_MODEL or deepseek-r1:14b)")
    ap.add_argument("--list", action="store_true", help="show parsed question counts and exit")
    args = ap.parse_args()
    if args.model:
        global MODEL
        MODEL = args.model
    if args.list:
        _, per_file = load_questions(args.domain)
        total = sum(per_file.values())
        for f, n in sorted(per_file.items()):
            print("%4d  %s" % (n, f))
        print("----")
        print("%4d  TOTAL parsed" % total)
        return
    run_quiz(args)


if __name__ == "__main__":
    main()
