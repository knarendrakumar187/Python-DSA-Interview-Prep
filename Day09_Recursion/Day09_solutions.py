"""Recursion solutions."""

from typing import List


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def subsets(nums: List[int]) -> List[List[int]]:
    ans = []

    def dfs(i, path):
        if i == len(nums):
            ans.append(path[:])
            return
        # skip
        dfs(i + 1, path)
        # take
        path.append(nums[i])
        dfs(i + 1, path)
        path.pop()

    dfs(0, [])
    return ans


def generate_parenthesis(n: int) -> List[str]:
    ans = []

    def dfs(open_n, close_n, path):
        if len(path) == 2 * n:
            ans.append("".join(path))
            return
        if open_n < n:
            path.append("(")
            dfs(open_n + 1, close_n, path)
            path.pop()
        if close_n < open_n:
            path.append(")")
            dfs(open_n, close_n + 1, path)
            path.pop()

    dfs(0, 0, [])
    return ans
