"""
DAY 1 drills — Python skills that appear in DSA every day
Run: python Day01_drills.py

Write Time/Space in comments when you finish each function.
"""

from typing import List, Dict


def has_duplicate(arr: List[int]) -> bool:
    """True if any value appears twice. Use set."""
    # TODO
    pass


def count_vowels(s: str) -> int:
    """Count vowels aeiou (case-insensitive)."""
    # TODO
    pass


def reverse_words(s: str) -> str:
    """'hello world python' -> 'python world hello'"""
    # TODO
    pass


def intersect_unique(a: List[int], b: List[int]) -> List[int]:
    """Unique common values. Any order OK in tests we sort."""
    # TODO
    pass


def char_frequency(s: str) -> Dict[str, int]:
    """Frequency of each character."""
    # TODO
    pass


def move_zeros_copy(arr: List[int]) -> List[int]:
    """
    Return NEW list: non-zeros first (same order), zeros at end.
    Example: [0,1,0,3,12] -> [1,3,12,0,0]
    """
    # TODO
    pass


def two_sum_indices(nums: List[int], target: int) -> List[int]:
    """
    Return two indices i,j such that nums[i]+nums[j]==target.
    Use dict. Assume exactly one answer.
    """
    # TODO
    pass


def is_palindrome_alpha(s: str) -> bool:
    """
    Ignore non-alphanumeric, ignore case.
    'A man, a plan, a canal: Panama' -> True
    Use two pointers.
    """
    # TODO
    pass


def max_subarray_sum_k(arr: List[int], k: int) -> int:
    """
    Max sum of any contiguous window of size k.
    Example: [2,1,5,1,3,2], k=3 -> 9 (5+1+3)
    """
    # TODO
    pass


def _check(name, got, expected):
    ok = got == expected
    print(f"{'PASS' if ok else 'FAIL'} | {name} | got={got} expected={expected}")


if __name__ == "__main__":
    _check("dup_yes", has_duplicate([1, 2, 3, 1]), True)
    _check("dup_no", has_duplicate([1, 2, 3]), False)
    _check("vowels", count_vowels("Interview"), 4)
    _check("rev_words", reverse_words("hello world python"), "python world hello")

    inter = sorted(intersect_unique([1, 2, 2, 3], [2, 3, 4]))
    _check("intersect", inter, [2, 3])
    _check("char_freq", char_frequency("aab"), {"a": 2, "b": 1})
    _check("move0", move_zeros_copy([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    ans = two_sum_indices([2, 7, 11, 15], 9)
    _check("two_sum", sorted(ans) == [0, 1], True)

    _check("pal", is_palindrome_alpha("A man, a plan, a canal: Panama"), True)
    _check("pal2", is_palindrome_alpha("race a car"), False)
    _check("window", max_subarray_sum_k([2, 1, 5, 1, 3, 2], 3), 9)

    print("\nIf all PASS → go to Day01_02_Arrays/Day01_problems.py")
