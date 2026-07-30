"""
DAY 1 — Array problems (Easy)
Folder: Day01_02_Arrays
Solve in order. After each: write Time and Space in a comment above the function.

Problems:
1) Two Sum (return indices)
2) Contains Duplicate
3) Move Zeroes (in-place)
4) Best Time to Buy and Sell Stock (1 transaction)
5) Rotate Array right by k (in-place preferred)

When stuck > 20 min: write brute force first, then improve.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """LeetCode 1. Return indices i, j such that nums[i] + nums[j] == target."""
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def contains_duplicate(nums: List[int]) -> bool:
    """LeetCode 217. True if any value appears at least twice."""
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def move_zeroes(nums: List[int]) -> None:
    """LeetCode 283. Move all 0s to end, keep relative order of non-zeros. In-place."""
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def max_profit(prices: List[int]) -> int:
    """LeetCode 121. Max profit from one buy + one sell. Else 0."""
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def rotate(nums: List[int], k: int) -> None:
    """LeetCode 189. Rotate array to the right by k steps. In-place."""
    # Time: O(?)  Space: O(?)
    # TODO
    pass


# -------------------- tests --------------------
def _eq(a, b):
    return a == b


if __name__ == "__main__":
    # two_sum
    ans = two_sum([2, 7, 11, 15], 9)
    print("two_sum", "PASS" if ans in ([0, 1], [1, 0]) else f"FAIL {ans}")

    print("dup_true", "PASS" if contains_duplicate([1, 2, 3, 1]) is True else "FAIL")
    print("dup_false", "PASS" if contains_duplicate([1, 2, 3]) is False else "FAIL")

    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    print("move_zeroes", "PASS" if a == [1, 3, 12, 0, 0] else f"FAIL {a}")

    print("profit", "PASS" if max_profit([7, 1, 5, 3, 6, 4]) == 5 else "FAIL")
    print("profit0", "PASS" if max_profit([7, 6, 4, 3, 1]) == 0 else "FAIL")

    r = [1, 2, 3, 4, 5, 6, 7]
    rotate(r, 3)
    print("rotate", "PASS" if r == [5, 6, 7, 1, 2, 3, 4] else f"FAIL {r}")
