"""Day 5 — Sliding window."""

from typing import List


def max_sum_subarray_k(arr: List[int], k: int) -> int:
    """Max sum of any contiguous subarray of size k."""
    # TODO
    pass


def length_of_longest_substring(s: str) -> int:
    """LeetCode 3. Longest substring without repeating characters."""
    # TODO
    pass


def longest_ones(nums: List[int], k: int) -> int:
    """LeetCode 1004. Max consecutive 1s if you can flip at most k zeros."""
    # TODO
    pass


def find_max_average(nums: List[int], k: int) -> float:
    """LeetCode 643 again — must be fluent."""
    # TODO
    pass


if __name__ == "__main__":
    print("maxsum", "PASS" if max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9 else "FAIL")
    print("substr", "PASS" if length_of_longest_substring("abcabcbb") == 3 else "FAIL")
    print("substr2", "PASS" if length_of_longest_substring("bbbbb") == 1 else "FAIL")
    print("ones", "PASS" if longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6 else "FAIL")
    print("avg", "PASS" if abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-6 else "FAIL")
