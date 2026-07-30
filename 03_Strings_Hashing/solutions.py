"""Solutions for hashing + strings."""

from typing import List
from collections import Counter, defaultdict


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def first_uniq_char(s: str) -> int:
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def is_subsequence(s: str, t: str) -> bool:
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)


def compress(chars: List[str]) -> int:
    write = 0
    i = 0
    n = len(chars)
    while i < n:
        j = i
        while j < n and chars[j] == chars[i]:
            j += 1
        chars[write] = chars[i]
        write += 1
        count = j - i
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
        i = j
    return write
