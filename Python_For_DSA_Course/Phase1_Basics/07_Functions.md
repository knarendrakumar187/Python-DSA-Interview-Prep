# Topic 07 — Functions
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Interviews expect clean functions: `def twoSum(nums, target)`.  
Splitting logic into helpers (DFS, backtrack) is how you pass medium/hard problems.

---

## Theory (simple)
A **function** is a reusable block with a name.  
You pass **parameters**, it **returns** a result (or `None`).

```text
def name(params):
    body
    return value
```

---

## Syntax

```python
def add(a, b):
    return a + b

def greet(name="User"):      # default argument
    return f"Hi {name}"

def log(*args):              # variable args tuple
    print(args)

def info(**kwargs):          # keyword args dict
    print(kwargs)

# Multiple return (actually a tuple)
def min_max(arr):
    return min(arr), max(arr)
```

### Pass by object reference
Lists/dicts passed to functions can be modified inside (same object).

```python
def append_one(lst):
    lst.append(1)

a = [0]
append_one(a)
print(a)   # [0, 1]
```

---

## Compare with C++/Java

| C++/Java | Python |
|----------|--------|
| `int add(int a, int b)` | `def add(a, b):` |
| `return x;` | `return x` (no type required) |
| Method in class | `def method(self, ...):` (OOP later) |
| Overloading by types | Not really — use default args / *args |

Python functions are first-class: assign to variable, pass as argument.

---

## Examples

### 1) Basic helper
```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
```

### 2) Early return (guard)
```python
def first_positive(nums):
    if not nums:
        return -1
    for x in nums:
        if x > 0:
            return x
    return -1
```

### 3) Default parameter
```python
def clamp(x, lo=0, hi=100):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
```

### 4) Docstring (good habit)
```python
def binary_search(arr, target):
    """Return index of target in sorted arr, else -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## DSA use cases
- `def dfs(node, visited):` for graphs/trees
- `def backtrack(path):` for subsets/permutations
- Helper: `def valid(r, c):` for grid bounds
- Return `(found, index)` or use class / nonlocal for state

---

## 3 LeetCode-style examples

### Example A — Two Sum as function
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
```

### Example B — Reverse string helper
```python
def reverse_string(s):
    chars = list(s)
    lo, hi = 0, len(chars) - 1
    while lo < hi:
        chars[lo], chars[hi] = chars[hi], chars[lo]
        lo += 1
        hi -= 1
    return "".join(chars)

print(reverse_string("hello"))   # olleh
```

### Example C — Merge two sorted arrays (function)
```python
def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out

print(merge([1, 3, 5], [2, 4, 6]))   # [1,2,3,4,5,6]
```

---

## 1) Summary
- `def name(params):` + indented body + `return`
- Default args: `def f(x, n=0):`
- Functions can modify mutable args (lists, dicts)
- Write small helpers — one job per function

## 2) Common interview questions
1. Difference between parameter and argument?
2. What does a function return if no `return`?
3. Can you modify a list passed to a function?
4. What are default arguments? Mutable default trap?
5. Why use helper functions in recursion?

## 3) Common mistakes
- Mutable default: `def f(lst=[])` — shared list! Use `None` instead
- Forgetting `return` → get `None`
- Not returning result, only printing inside function
- Wrong parameter order when calling

## 4) Practice problems (Easy → Hard)
1. **Easy:** Write `square(n)` returning n².
2. **Easy:** Write `count_vowels(s)` returning int.
3. **Medium:** Write `is_palindrome(s)` ignoring case (only letters).
4. **Medium:** Write `merge_sorted(a, b)` without using `sort()`.
5. **Harder:** Write `max_subarray_sum(nums)` (Kadane) as a function.

## 5) Mini quiz
1. What is return type if no return statement?
2. How call `add(2, 3)`?
3. Can function return two values?
4. Is `def f(x=[]):` safe? Why not?
5. Keyword call: `greet(name="Ali")` — what is `name`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/07_functions_practice.py` (create file)
- Mark Topic 07 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 08
