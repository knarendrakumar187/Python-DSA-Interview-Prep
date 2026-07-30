"""DAY 7 — Stack & Queue problems. Folder: Day07_Stack_Queue"""

from typing import List


def is_valid(s: str) -> bool:
    """LeetCode 20. Valid Parentheses."""
    # TODO
    pass


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    LeetCode 496.
    For each x in nums1, find next greater in nums2 to the right. Else -1.
    """
    # TODO
    pass


class MyQueue:
    """LeetCode 232. Queue using two stacks."""

    def __init__(self):
        # TODO
        pass

    def push(self, x: int) -> None:
        # TODO
        pass

    def pop(self) -> int:
        # TODO
        pass

    def peek(self) -> int:
        # TODO
        pass

    def empty(self) -> bool:
        # TODO
        pass


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    LeetCode 739.
    For each day, how many days until a warmer temperature? Else 0.
    """
    # TODO
    pass


if __name__ == "__main__":
    print("valid", "PASS" if is_valid("()[]{}") is True else "FAIL")
    print("valid2", "PASS" if is_valid("(]") is False else "FAIL")
    print("nge", "PASS" if next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1] else "FAIL")

    q = MyQueue()
    try:
        q.push(1)
        q.push(2)
        ok = q.peek() == 1 and q.pop() == 1 and q.empty() is False
        print("queue", "PASS" if ok else "FAIL")
    except Exception as e:
        print("queue", f"FAIL {e}")

    print(
        "temps",
        "PASS"
        if daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
        else "FAIL",
    )
