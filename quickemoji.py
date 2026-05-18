#!/usr/bin/env python3
"""quickemoji.py - Convert plain words to emojis from the command line.

Usage:
    python quickemoji.py "Your text here"
    ./quickemoji.py "Your text here"  # if made executable
"""

import sys
import re

# Simple keyword‑to‑emoji mapping. Extend as needed.
EMOJI_MAP = {
    "love": "❤️",
    "heart": "❤️",
    "python": "🐍",
    "coffee": "☕",
    "cat": "🐱",
    "dog": "🐶",
    "happy": "😊",
    "birthday": "🎂",
    "party": "🥳",
    "star": "⭐",
    "fire": "🔥",
    "thumbs up": "👍",
    "ok": "👌",
    "laugh": "😂",
    "cry": "😢",
    "sun": "☀️",
    "moon": "🌙",
    "music": "🎵",
    "book": "📚",
    "money": "💰",
    "car": "🚗",
    "tree": "🌳",
    "world": "🌍",
    "computer": "💻",
}

def replace_keywords(text: str) -> str:
    """Replace any whole‑word matches in *text* with their emoji equivalents.
    The search is case‑insensitive.
    """
    def repl(match):
        word = match.group(0).lower()
        return EMOJI_MAP.get(word, match.group(0))

    # Build a regex that matches any key as a whole word (word boundaries)
    pattern = r"\\b(" + "|".join(map(re.escape, EMOJI_MAP.keys())) + r")\\b"
    return re.sub(pattern, repl, text, flags=re.IGNORECASE)

def main():
    if len(sys.argv) < 2:
        print("Usage: quickemoji.py \"Your text here\"")
        sys.exit(1)
    input_text = " ".join(sys.argv[1:])
    print(replace_keywords(input_text))

if __name__ == "__main__":
    main()
