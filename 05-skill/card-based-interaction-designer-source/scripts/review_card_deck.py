#!/usr/bin/env python3
"""Quick structural review for card decks in simple Markdown or CSV.

This script gives a deterministic first-pass summary only. It does not replace qualitative safety review.
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

RISK_TERMS = [
    "afraid", "fear", "worried", "hate", "regret", "secret", "trauma", "shame",
    "fault", "blame", "worst", "least favourite", "lazy", "annoying", "stupid",
    "salary", "debt", "money", "health", "divorce", "addiction", "mental health",
]

WORKPLACE_RISK_TERMS = [
    "resist", "resistance", "commitment", "blocker", "who is blocking", "leadership got wrong",
    "performance", "job security", "redundancy", "restructure", "manager", "fear of change",
]

CARD_TYPES = [
    "Pick One", "Would You Rather", "Pick 2 of 5", "Rank Them", "Build Your Kit",
    "Build Your Team", "One Rule", "Superpower With a Catch", "Scenario", "Wildcard"
]


def parse_markdown(text):
    pattern = re.compile(
        r"### Card\s+(?P<num>\d+)\s+\*\*Type:\*\*\s+(?P<type>.*?)\s+\*\*Category:\*\*\s+(?P<category>.*?)\s+\*\*Front:\*\*\s+(?P<prompt>.*?)\s+\*\*Back:\*\*\s+(?P<followup>.*?)(?=\n\n### Card|\Z)",
        re.S,
    )
    cards = []
    for m in pattern.finditer(text):
        cards.append({
            "card_id": m.group("num").strip(),
            "card_type": m.group("type").strip().replace("  ", " "),
            "category": m.group("category").strip(),
            "prompt": m.group("prompt").strip(),
            "followup": m.group("followup").strip(),
        })
    return cards


def parse_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        cards = []
        for i, row in enumerate(reader, start=1):
            lower = {k.lower().strip(): v for k, v in row.items() if k}
            cards.append({
                "card_id": lower.get("card id") or lower.get("id") or str(i),
                "card_type": lower.get("card type") or lower.get("type") or "",
                "category": lower.get("category") or "",
                "prompt": lower.get("prompt") or lower.get("question") or lower.get("front") or "",
                "followup": lower.get("follow-up") or lower.get("followup") or lower.get("back") or "",
            })
    return cards


def flag_card(card, workplace=False):
    text = f"{card.get('prompt','')} {card.get('followup','')}".lower()
    hits = [term for term in RISK_TERMS if term in text]
    if workplace:
        hits.extend([term for term in WORKPLACE_RISK_TERMS if term in text])
    flags = []
    if hits:
        flags.append("risk terms: " + ", ".join(sorted(set(hits))))
    if len(card.get("prompt", "")) > 240:
        flags.append("long prompt")
    if "why" not in text and card.get("card_type") in {"Pick One", "Would You Rather", "Pick 2 of 5"}:
        flags.append("may need a why/follow-up")
    return flags


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to Markdown or CSV deck")
    parser.add_argument("--workplace", action="store_true", help="Apply extra workplace risk terms")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    cards = parse_csv(path) if path.suffix.lower() == ".csv" else parse_markdown(text)

    type_counts = Counter(c.get("card_type", "Unknown") for c in cards)
    category_counts = Counter(c.get("category", "Uncategorised") for c in cards)
    flagged = []
    for c in cards:
        flags = flag_card(c, workplace=args.workplace)
        if flags:
            flagged.append({"card_id": c.get("card_id"), "card_type": c.get("card_type"), "category": c.get("category"), "flags": flags, "prompt": c.get("prompt")})

    report = {
        "card_count": len(cards),
        "type_counts": dict(type_counts),
        "top_categories": dict(category_counts.most_common(20)),
        "flagged_count": len(flagged),
        "flagged_cards": flagged,
        "note": "This is a first-pass structural review. Use the skill safety review for qualitative judgement.",
    }

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Cards: {report['card_count']}")
        print("Types:")
        for k, v in type_counts.most_common():
            print(f"  - {k}: {v}")
        print("Top categories:")
        for k, v in category_counts.most_common(10):
            print(f"  - {k}: {v}")
        print(f"Flagged cards: {len(flagged)}")
        for item in flagged[:30]:
            print(f"  - Card {item['card_id']} ({item['card_type']} / {item['category']}): {'; '.join(item['flags'])}")

if __name__ == "__main__":
    main()
