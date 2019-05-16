"""
Define helpers for working with text
"""


def cap_all_text(text: str):
    """Capitalize all words in a text string"""
    words = [word.capitalize() for word in text.split()]
    return " ".join(words)
