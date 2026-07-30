"""
DAY 12 — Mixed practice (Easy/Medium mix)
Folder: Day12_16_Mocks
Do all. Then retry with 45-min timer.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # TODO
    pass


def is_valid(s: str) -> bool:
    # TODO
    pass


def max_profit(prices: List[int]) -> int:
    # TODO
    pass


def length_of_longest_substring(s: str) -> int:
    # TODO
    pass


def reverse_list_vals(arr: List[int]) -> List[int]:
    """Reverse linked-list style using array simulation is fine here:
    just reverse list values and explain real pointer reverse in interview."""
    # TODO
    pass


if __name__ == "__main__":
    print("two_sum", "PASS" if set(two_sum([2, 7, 11, 15], 9)) == {0, 1} else "FAIL")
    print("valid", "PASS" if is_valid("{[]}") is True else "FAIL")
    print("profit", "PASS" if max_profit([7, 1, 5, 3, 6, 4]) == 5 else "FAIL")
    print("substr", "PASS" if length_of_longest_substring("pwwkew") == 3 else "FAIL")
    print("rev", "PASS" if reverse_list_vals([1, 2, 3]) == [3, 2, 1] else "FAIL")
