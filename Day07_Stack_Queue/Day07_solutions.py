"""Stack & Queue solutions."""

from typing import List


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


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    next_map = {}
    st = []
    for x in nums2:
        while st and st[-1] < x:
            next_map[st.pop()] = x
        st.append(x)
    return [next_map.get(x, -1) for x in nums1]


class MyQueue:
    def __init__(self):
        self.in_st = []
        self.out_st = []

    def push(self, x: int) -> None:
        self.in_st.append(x)

    def _move(self):
        if not self.out_st:
            while self.in_st:
                self.out_st.append(self.in_st.pop())

    def pop(self) -> int:
        self._move()
        return self.out_st.pop()

    def peek(self) -> int:
        self._move()
        return self.out_st[-1]

    def empty(self) -> bool:
        return not self.in_st and not self.out_st


def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    ans = [0] * n
    st = []  # indices
    for i, t in enumerate(temperatures):
        while st and temperatures[st[-1]] < t:
            j = st.pop()
            ans[j] = i - j
        st.append(i)
    return ans
