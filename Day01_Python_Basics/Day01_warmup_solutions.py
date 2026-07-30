"""DAY 1 warmup SOLUTIONS — open only after trying."""


def reverse_list(arr):
    # Time O(n) Space O(n)
    out = []
    for i in range(len(arr) - 1, -1, -1):
        out.append(arr[i])
    return out


def find_max_and_second_max(arr):
    # Time O(n) Space O(1)
    first = second = float("-inf")
    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return first, second


def frequency_map(arr):
    # Time O(n) Space O(n)
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


def linear_search(arr, target):
    # Time O(n) Space O(1)
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def is_sorted_non_decreasing(arr):
    # Time O(n) Space O(1)
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def swap(arr, i, j):
    # Time O(1) Space O(1)
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def prefix_sums(arr):
    # Time O(n) Space O(n)
    if not arr:
        return []
    out = [arr[0]]
    for i in range(1, len(arr)):
        out.append(out[-1] + arr[i])
    return out
