"""DAY 10 — Sorting + Binary Search. Folder: Day10_Sorting_BinarySearch"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """LeetCode 704. Return index or -1."""
    # TODO
    pass


def search_insert(nums: List[int], target: int) -> int:
    """LeetCode 35. Index where target is / should be inserted."""
    # TODO
    pass


def first_and_last(nums: List[int], target: int) -> List[int]:
    """LeetCode 34. First and last position of target. Else [-1,-1]."""
    # TODO
    pass


def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """LeetCode 88. Merge nums2 into nums1 in-place. nums1 has size m+n."""
    # TODO
    pass


if __name__ == "__main__":
    print("bs", "PASS" if binary_search([-1, 0, 3, 5, 9, 12], 9) == 4 else "FAIL")
    print("bs_miss", "PASS" if binary_search([-1, 0, 3, 5, 9, 12], 2) == -1 else "FAIL")
    print("insert", "PASS" if search_insert([1, 3, 5, 6], 2) == 1 else "FAIL")
    print("range", "PASS" if first_and_last([5, 7, 7, 8, 8, 10], 8) == [3, 4] else "FAIL")
    print("range_miss", "PASS" if first_and_last([5, 7, 7, 8, 8, 10], 6) == [-1, -1] else "FAIL")
    a = [1, 2, 3, 0, 0, 0]
    merge_sorted(a, 3, [2, 5, 6], 3)
    print("merge", "PASS" if a == [1, 2, 2, 3, 5, 6] else f"FAIL {a}")
