"""DAY 3 — Hashing problems (Easy). Folder: Day03_Hashing"""

from typing import List


def is_anagram(s: str, t: str) -> bool:
    """LeetCode 242. Valid Anagram."""
    # TODO
    pass


def first_uniq_char(s: str) -> int:
    """LeetCode 387. First unique character index, else -1."""
    # TODO
    pass


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """LeetCode 349. Unique intersection of two arrays (any order)."""
    # TODO
    pass


def two_sum(nums: List[int], target: int) -> List[int]:
    """LeetCode 1 again — must be fluent."""
    # TODO
    pass


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    LeetCode 49. Group Anagrams.
    Example: ["eat","tea","tan","ate","nat","bat"]
    """
    # TODO
    pass


if __name__ == "__main__":
    print("anagram", "PASS" if is_anagram("anagram", "nagaram") is True else "FAIL")
    print("uniq", "PASS" if first_uniq_char("leetcode") == 0 else "FAIL")
    print("uniq2", "PASS" if first_uniq_char("loveleetcode") == 2 else "FAIL")
    inter = set(intersection([1, 2, 2, 1], [2, 2]))
    print("inter", "PASS" if inter == {2} else f"FAIL {inter}")
    ans = two_sum([3, 2, 4], 6)
    print("two_sum", "PASS" if set(ans) == {1, 2} else f"FAIL {ans}")
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = {frozenset(g) for g in groups}
    expected = {frozenset(["eat", "tea", "ate"]), frozenset(["tan", "nat"]), frozenset(["bat"])}
    print("group", "PASS" if normalized == expected else f"FAIL {groups}")
