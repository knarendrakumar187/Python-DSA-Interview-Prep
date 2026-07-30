"""Reference solutions for mixed + mock1 (use only after attempt)."""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    st = []
    for ch in s:
        if ch in "([{":
            st.append(ch)
        else:
            if not st or st[-1] != pairs[ch]:
                return False
            st.pop()
    return not st


def max_profit(prices: List[int]) -> int:
    mn, best = float("inf"), 0
    for p in prices:
        mn = min(mn, p)
        best = max(best, p - mn)
    return best


def length_of_longest_substring(s: str) -> int:
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def reverse_list_vals(arr: List[int]) -> List[int]:
    return arr[::-1]


def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
