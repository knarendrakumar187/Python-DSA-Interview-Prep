"""
Topic 01 — Variables and Data Types — Homework Practice
Solve each function. Run: python Practice/01_variables_practice.py
"""

# =============================================================================
# Practice 1 (Easy)
# Create variables for name (str), age (int), is_student (bool).
# Return a dict with keys "name", "age", "is_student", "types" where "types"
# is a dict mapping each field name to its type name as string (e.g. "int").
# =============================================================================
def practice_01_create_profile(name, age, is_student):
    # TODO: implement
    pass


# =============================================================================
# Practice 2 (Easy)
# Given a, b, c — rotate left: a,b,c -> b,c,a
# Return tuple (a, b, c) after rotation.
# =============================================================================
def practice_02_rotate_left(a, b, c):
    # TODO: implement
    pass


# =============================================================================
# Practice 3 (Medium)
# Given list of ints, return maximum WITHOUT using built-in max().
# Return None if list is empty.
# =============================================================================
def practice_03_find_max(nums):
    # TODO: implement
    pass


# =============================================================================
# Practice 4 (Medium)
# Count how many values in lst are falsy (bool(x) is False).
# =============================================================================
def practice_04_count_falsy(lst):
    # TODO: implement
    pass


# =============================================================================
# Practice 5 (Harder)
# Simulate score tracker. start at 0.
# operations is list of strings like "+5", "-2", "+10"
# Apply each in order. Return final score as int.
# =============================================================================
def practice_05_score_tracker(operations):
    # TODO: implement
    pass


# =============================================================================
# Tests — do not edit below until your functions pass
# =============================================================================
def _test():
    # Practice 1
    p = practice_01_create_profile("Ram", 20, True)
    assert p is not None, "practice_01: implement function"
    assert p["name"] == "Ram" and p["age"] == 20 and p["is_student"] is True
    assert p["types"]["age"] == "int"

    # Practice 2
    assert practice_02_rotate_left(1, 2, 3) == (2, 3, 1)

    # Practice 3
    assert practice_03_find_max([3, 1, 4, 1, 5]) == 5
    assert practice_03_find_max([-5, -1, -10]) == -1
    assert practice_03_find_max([]) is None

    # Practice 4
    assert practice_04_count_falsy([0, 1, "", "hi", [], [0], None, False]) == 5

    # Practice 5
    assert practice_05_score_tracker(["+5", "-2", "+10"]) == 13
    assert practice_05_score_tracker(["-3", "+3"]) == 0
    assert practice_05_score_tracker([]) == 0

    print("All Topic 01 practice tests passed!")


if __name__ == "__main__":
    _test()
