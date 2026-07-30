"""Sorting / Binary Search solutions."""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def search_insert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


def first_and_last(nums: List[int], target: int) -> List[int]:
    def leftmost():
        l, r, ans = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def rightmost():
        l, r, ans = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    return [leftmost(), rightmost()]


def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
