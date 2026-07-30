"""
Day 2 — Arrays (still Easy / Easy-Medium)
Solve yourself. Write Time and Space above each function.
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """
    LeetCode 1480. Running Sum.
    Example: [1,2,3,4] -> [1,3,6,10]
    Idea: prefix sum.
    """
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def find_max_average(nums: List[int], k: int) -> float:
    """
    LeetCode 643. Max average of any contiguous subarray of length k.
    Example: nums=[1,12,-5,-6,50,3], k=4 -> 12.75
    Idea: window sum of size k.
    """
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def majority_element(nums: List[int]) -> int:
    """
    LeetCode 169. Element that appears more than n/2 times.
    Example: [2,2,1,1,1,2,2] -> 2
    Easy way: hash map count. (Boyer-Moore later optional)
    """
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def missing_number(nums: List[int]) -> int:
    """
    LeetCode 268. Array has numbers from 0..n with one missing.
    Example: [3,0,1] -> 2
    Idea: sum formula or set.
    """
    # Time: O(?)  Space: O(?)
    # TODO
    pass


def single_number(nums: List[int]) -> int:
    """
    LeetCode 136. Every element appears twice except one.
    Example: [4,1,2,1,2] -> 4
    Easy way: hash map. (XOR is bonus)
    """
    # Time: O(?)  Space: O(?)
    # TODO
    pass


if __name__ == "__main__":
    print("running_sum", "PASS" if running_sum([1, 2, 3, 4]) == [1, 3, 6, 10] else "FAIL")
    print("max_avg", "PASS" if abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-6 else "FAIL")
    print("majority", "PASS" if majority_element([2, 2, 1, 1, 1, 2, 2]) == 2 else "FAIL")
    print("missing", "PASS" if missing_number([3, 0, 1]) == 2 else "FAIL")
    print("single", "PASS" if single_number([4, 1, 2, 1, 2]) == 4 else "FAIL")
