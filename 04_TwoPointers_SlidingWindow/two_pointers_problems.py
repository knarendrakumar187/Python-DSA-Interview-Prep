"""Day 4 — Two pointers."""

from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """LeetCode 167. 1-indexed answer for sorted array."""
    # TODO
    pass


def is_palindrome(s: str) -> bool:
    """LeetCode 125. Ignore non-alphanumeric, case-insensitive."""
    # TODO
    pass


def remove_duplicates(nums: List[int]) -> int:
    """LeetCode 26. In-place unique count for sorted array."""
    # TODO
    pass


def max_area(height: List[int]) -> int:
    """LeetCode 11. Container With Most Water."""
    # TODO
    pass


if __name__ == "__main__":
    print("two_sum", "PASS" if two_sum_sorted([2, 7, 11, 15], 9) == [1, 2] else "FAIL")
    print("pal", "PASS" if is_palindrome("A man, a plan, a canal: Panama") is True else "FAIL")
    print("pal2", "PASS" if is_palindrome("race a car") is False else "FAIL")
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    print("dedup", "PASS" if k == 5 and nums[:k] == [0, 1, 2, 3, 4] else f"FAIL {k} {nums[:k] if k else nums}")
    print("area", "PASS" if max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49 else "FAIL")
