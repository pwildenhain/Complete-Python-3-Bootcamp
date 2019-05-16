"""
Test helper functions for working with text
"""

import cap


def test_cap_all_text():
    """Capitalize all text in a string"""
    assert cap.cap_all_text("hello world") == "Hello World"
