"""String problems (Easy)."""

from typing import List


def reverse_words(s: str) -> str:
    """LeetCode 151. Reverse words. '  hello world  ' -> 'world hello'"""
    # TODO
    pass


def longest_common_prefix(strs: List[str]) -> str:
    """LeetCode 14. Longest common prefix."""
    # TODO
    pass


def is_subsequence(s: str, t: str) -> bool:
    """LeetCode 392. Is s a subsequence of t?"""
    # TODO
    pass


def compress(chars: List[str]) -> int:
    """
    LeetCode 443 idea (simplified for practice):
    Return length after run-length style compression in-place.
    Example: ['a','a','b','b','c','c','c'] -> length 6 for a2b2c3
    """
    # TODO
    pass


if __name__ == "__main__":
    print("rev", "PASS" if reverse_words("  hello world  ") == "world hello" else "FAIL")
    print("lcp", "PASS" if longest_common_prefix(["flower", "flow", "flight"]) == "fl" else "FAIL")
    print("sub_yes", "PASS" if is_subsequence("abc", "ahbgdc") is True else "FAIL")
    print("sub_no", "PASS" if is_subsequence("axc", "ahbgdc") is False else "FAIL")
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    n = compress(chars)
    print("compress", "PASS" if n == 6 and chars[:n] == ["a", "2", "b", "2", "c", "3"] else f"FAIL {n} {chars[:n] if n else chars}")
