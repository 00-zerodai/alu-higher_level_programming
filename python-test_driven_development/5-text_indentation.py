#!/usr/bin/python3
"""Provide a function for indenting text at sentence delimiters."""


def text_indentation(text):
    """Print text with two newlines after sentence-ending punctuation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = "\n".join(line.strip() for line in text.splitlines())
    for delimiter in ".?:":
        text = text.replace(delimiter, delimiter + "\n\n")
        text = "\n".join(line.strip() for line in text.split("\n"))
    print(text, end="")
