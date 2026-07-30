"""
DAY 1 warmup — Python muscle for DSA
Run: python Day01_warmup.py
Fill each TODO. Get all PASS.
"""


def reverse_list(arr):
    """Return a new reversed list. Practice loop (no arr[::-1] today)."""
    # TODO
    pass


def find_max_and_second_max(arr):
    """Return (max, second_max). len(arr) >= 2. Handle duplicates."""
    # TODO
    pass


def frequency_map(arr):
    """Return dict of value -> count."""
    # TODO
    pass


def linear_search(arr, target):
    """Return index of target or -1."""
    # TODO
    pass


def is_sorted_non_decreasing(arr):
    """True if sorted ascending (duplicates allowed)."""
    # TODO
    pass


def swap(arr, i, j):
    """Swap values at i and j in-place. Return the same list."""
    # TODO
    pass


def prefix_sums(arr):
    """
    Return prefix array.
    Example: [1,2,3,4] -> [1,3,6,10]
    """
    # TODO
    pass


def _check(name, got, expected):
    ok = got == expected
    print(f"{'PASS' if ok else 'FAIL'} | {name} | got={got} expected={expected}")


if __name__ == "__main__":
    _check("reverse", reverse_list([1, 2, 3]), [3, 2, 1])
    _check("max2", find_max_and_second_max([5, 1, 5, 3]), (5, 3))
    _check("freq", frequency_map([1, 1, 2]), {1: 2, 2: 1})
    _check("search", linear_search([4, 7, 9], 7), 1)
    _check("search_miss", linear_search([4, 7, 9], 8), -1)
    _check("sorted_yes", is_sorted_non_decreasing([1, 2, 2, 4]), True)
    _check("sorted_no", is_sorted_non_decreasing([1, 3, 2]), False)
    a = [10, 20, 30]
    _check("swap", swap(a, 0, 2), [30, 20, 10])
    _check("prefix", prefix_sums([1, 2, 3, 4]), [1, 3, 6, 10])
