"""REFERENCE SOLUTIONS — open only after you attempt. Do not copy blindly."""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # Time: O(n)  Space: O(n)
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


def contains_duplicate(nums: List[int]) -> bool:
    # Time: O(n)  Space: O(n)
    return len(nums) != len(set(nums))


def move_zeroes(nums: List[int]) -> None:
    # Time: O(n)  Space: O(1)
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


def max_profit(prices: List[int]) -> int:
    # Time: O(n)  Space: O(1)
    min_price = float("inf")
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        else:
            best = max(best, p - min_price)
    return best


def rotate(nums: List[int], k: int) -> None:
    # Time: O(n)  Space: O(1)
    n = len(nums)
    k %= n

    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)
