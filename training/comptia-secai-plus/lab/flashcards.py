#!/usr/bin/env python3
"""SecAI+ flashcard drill.

Parses the kit's flashcards-*.md decks and runs an interactive, self-graded
spaced-recall session in the terminal. Stdlib only, fully offline — no Ollama,
no network. Works the same on Windows (double-clicked via the launcher) as on
SENTRY.

Card format in the decks:
    **12. Term or question**
    > The answer, which may span
    > more than one quoted line.

Usage:
    python flashcards.py                 # all decks, shuffled
    python flashcards.py --deck week1    # one deck (filename substring)
    python flashcards.py --deck acronyms --n 20
    python flashcards.py --order linear  # keep deck order instead of shuffling
    python flashcards.py --list          # show parsed card counts and exit
"""
import argparse
import glob
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)

FRONT = re.compile(r"^\*\*(\d+)\.\s+(.+?)\*\*\s*$")


def parse_deck(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    deck = os.path.basename(path).replace("flashcards-", "").replace(".md", "")
    cards = []
    i = 0
    while i < len(lines):
        m = FRONT.match(lines[i])
        if not m:
            i += 1
            continue
        num, front = int(m.group(1)), m.group(2).strip()
        i += 1
        back = []
        while i < len(lines):
            ln = lines[i]
            if ln.strip() == "" or FRONT.match(ln):
                break
            if ln.lstrip().startswith(">"):
                back.append(ln.lstrip()[1:].strip())
                i += 1
            else:
                break
        if back:
            cards.append({
                "deck": deck,
                "num": num,
                "front": front,
                "back": " ".join(back),
            })
    return cards


def load_cards(deck_filter=None):
    files = sorted(glob.glob(os.path.join(KIT, "flashcards-*.md")))
    cards = []
    per_deck = {}
    for f in files:
        name = os.path.basename(f)
        if deck_filter and deck_filter.lower() not in name.lower():
            continue
        c = parse_deck(f)
        per_deck[name] = len(c)
        cards.extend(c)
    return cards, per_deck


def run(args):
    cards, per_deck = load_cards(args.deck)
    if not cards:
        where = "matching '%s' " % args.deck if args.deck else ""
        print("No cards %sparsed. Check flashcards-*.md in %s" % (where, KIT))
        return
    if args.order == "shuffle":
        random.shuffle(cards)
    if args.n:
        cards = cards[:args.n]

    print("\n" + "=" * 70)
    print("SecAI+ flashcards — %d cards%s" % (
        len(cards), " (" + args.deck + ")" if args.deck else " across all decks"))
    print("Read the front, recall the answer aloud, press Enter to reveal,")
    print("then grade yourself: [Enter]=got it · m=missed · s=skip · q=quit")
    print("=" * 70)

    correct = seen = 0
    missed = []
    for i, c in enumerate(cards, 1):
        print("\n[%d/%d]  %s" % (i, len(cards), c["deck"]))
        print("  ?  %s" % c["front"])
        try:
            input("     (Enter to reveal) ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        print("  ->  %s" % c["back"])
        try:
            grade = input("     [Enter]=got it · m=missed · s=skip · q=quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if grade == "q":
            break
        if grade == "s":
            continue
        seen += 1
        if grade in ("m", "n", "no"):
            missed.append(c)
        else:
            correct += 1

    print("\n" + "=" * 70)
    if seen:
        pct = 100.0 * correct / seen
        print("Recall: %d/%d (%.0f%%) graded." % (correct, seen, pct))
    else:
        print("No cards graded.")
    if missed:
        print("\nMissed %d — log these in 99-PROGRESS-TRACKER.md (Weak-area log):" % len(missed))
        for c in missed:
            print("  - [%s #%d] %s" % (c["deck"], c["num"], c["front"]))
    elif seen:
        print("Clean run — nothing missed. ✓")


def main():
    ap = argparse.ArgumentParser(description="SecAI+ flashcard drill (offline)")
    ap.add_argument("--deck", help="filter by filename substring, e.g. week1 / acronyms")
    ap.add_argument("--n", type=int, help="limit to N cards")
    ap.add_argument("--order", choices=["shuffle", "linear"], default="shuffle",
                    help="card order (default shuffle)")
    ap.add_argument("--list", action="store_true", help="show parsed card counts and exit")
    args = ap.parse_args()
    if args.list:
        _, per_deck = load_cards(args.deck)
        total = 0
        for f, n in sorted(per_deck.items()):
            print("%4d  %s" % (n, f))
            total += n
        print("----")
        print("%4d  TOTAL parsed" % total)
        return
    run(args)


if __name__ == "__main__":
    main()
