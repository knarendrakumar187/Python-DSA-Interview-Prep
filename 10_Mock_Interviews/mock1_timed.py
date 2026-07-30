"""
MOCK 1 — Timed DSA (70 minutes)
Do in order. Don't jump to solutions.

Problem A (Easy, ~15 min): Contains Duplicate
Problem B (Easy, ~20 min): Valid Palindrome
Problem C (Medium, ~35 min): Longest Substring Without Repeating Characters

Write approach comments before code.
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """A"""
    # Approach:
    # TODO
    pass


def is_palindrome(s: str) -> bool:
    """B"""
    # Approach:
    # TODO
    pass


def length_of_longest_substring(s: str) -> int:
    """C"""
    # Approach:
    # TODO
    pass


if __name__ == "__main__":
    print("A", "PASS" if contains_duplicate([1, 2, 3, 1]) is True else "FAIL")
    print("B", "PASS" if is_palindrome("A man, a plan, a canal: Panama") is True else "FAIL")
    print("C", "PASS" if length_of_longest_substring("abcabcbb") == 3 else "FAIL")
