"""DAY 9 — Recursion / light backtracking. Folder: Day09_Recursion"""

from typing import List


def factorial(n: int) -> int:
    """n! using recursion."""
    # TODO
    pass


def fib(n: int) -> int:
    """Fibonacci using recursion (ok for small n in interviews explanation)."""
    # TODO
    pass


def subsets(nums: List[int]) -> List[List[int]]:
    """LeetCode 78. All subsets."""
    # TODO
    pass


def generate_parenthesis(n: int) -> List[str]:
    """LeetCode 22. Generate all valid parentheses for n pairs."""
    # TODO
    pass


if __name__ == "__main__":
    print("fact", "PASS" if factorial(5) == 120 else "FAIL")
    print("fib", "PASS" if fib(7) == 13 else "FAIL")
    got = subsets([1, 2])
    got_set = {tuple(sorted(x)) for x in got}
    exp = {(), (1,), (2,), (1, 2)}
    print("subsets", "PASS" if got_set == exp else f"FAIL {got}")
    gp = set(generate_parenthesis(2))
    print("paren", "PASS" if gp == {"(())", "()()"} else f"FAIL {gp}")
