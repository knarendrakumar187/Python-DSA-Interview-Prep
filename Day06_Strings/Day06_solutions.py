"""DAY 6 solutions — Strings only."""

from typing import List


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
