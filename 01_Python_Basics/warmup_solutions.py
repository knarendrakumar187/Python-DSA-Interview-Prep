"""Day 1 warmup SOLUTIONS — check only after trying."""


def reverse_list(arr):
    out = []
    for i in range(len(arr) - 1, -1, -1):
        out.append(arr[i])
    return out


def find_max_and_second_max(arr):
    first = second = float("-inf")
    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return first, second


def frequency_map(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def is_sorted_non_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
