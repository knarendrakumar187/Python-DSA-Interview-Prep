"""Day 2 solutions — open only after trying."""

from typing import List
from collections import Counter


def running_sum(nums: List[int]) -> List[int]:
    # Time: O(n)  Space: O(1) extra (output not counted sometimes) / O(n) for result
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


def find_max_average(nums: List[int], k: int) -> float:
    # Time: O(n)  Space: O(1)
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k


def majority_element(nums: List[int]) -> int:
    # Time: O(n)  Space: O(n)
    freq = Counter(nums)
    return max(freq, key=freq.get)


def missing_number(nums: List[int]) -> int:
    # Time: O(n)  Space: O(1)
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


def single_number(nums: List[int]) -> int:
    # Time: O(n)  Space: O(1) with XOR
    x = 0
    for num in nums:
        x ^= num
    return x
