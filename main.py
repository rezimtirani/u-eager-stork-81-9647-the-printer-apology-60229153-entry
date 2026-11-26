"""The Printer Apology — a one-line entry for make.fun.

The printer writes a short apology for the documents it has
mangled over the years: the boarding pass it ate, the tax
return it jammed on, and the resignation letter it turned
into confetti. Only the Python standard library is used.
"""

import os
import sys

APOLOGY = "Sorry I ate your boarding pass, jammed on the tax return, and printed your resignation letter as confetti. Forgive me."

# Sealed gate from the kit's RULES.txt ("## The gate"): the scorer
# takes UTF-8 text of 1 to 120 characters. The req JSON's "200
# characters" is generic template text and does not apply here.
MAX_CHARS = 120


def check_apology(text):
    """Return the apology once it passes the sealed gate, else raise.

    The gate counts characters, not bytes; the line must be a single
    line, not only whitespace, with no trailing newline in the file.
    """
    if not isinstance(text, str):
        raise TypeError("apology must be text")
    if not text.strip():
        raise ValueError("apology must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "apology is {} characters, over the {}-character gate".format(
                len(text), MAX_CHARS
            )
        )
    if "\n" in text or "\r" in text:
        raise ValueError("apology must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("apology must not contain control characters")
    return text


def describe_apology(text):
    """Summarise the apology's size the way the sealed gate measures it.

    The gate counts characters, so a multi-byte character still counts
    as one; the byte count is reported only to show the file size.
    """
    chars = len(text)
    raw = len(text.encode("utf-8"))
    return "{} characters, {} UTF-8 bytes".format(chars, raw)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(check_apology(APOLOGY))
    print("wrote {} ({})".format(target, describe_apology(APOLOGY)))


if __name__ == "__main__":
    main()
