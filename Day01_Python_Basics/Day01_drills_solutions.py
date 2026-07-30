"""DAY 1 drills SOLUTIONS — open only after trying."""

from typing import List, Dict


def has_duplicate(arr: List[int]) -> bool:
    # Time O(n) Space O(n)
    return len(arr) != len(set(arr))


def count_vowels(s: str) -> int:
    # Time O(n) Space O(1)
    vowels = set("aeiou")
    return sum(1 for ch in s.lower() if ch in vowels)


def reverse_words(s: str) -> str:
    # Time O(n) Space O(n)
    return " ".join(s.split()[::-1])


def intersect_unique(a: List[int], b: List[int]) -> List[int]:
    # Time O(n+m) Space O(n+m)
    return list(set(a) & set(b))


def char_frequency(s: str) -> Dict[str, int]:
    # Time O(n) Space O(k)
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def move_zeros_copy(arr: List[int]) -> List[int]:
    # Time O(n) Space O(n)
    non_zero = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(non_zero))
    return non_zero + zeros


def two_sum_indices(nums: List[int], target: int) -> List[int]:
    # Time O(n) Space O(n)
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


def is_palindrome_alpha(s: str) -> bool:
    # Time O(n) Space O(1)
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


def max_subarray_sum_k(arr: List[int], k: int) -> int:
    # Time O(n) Space O(1)
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best
