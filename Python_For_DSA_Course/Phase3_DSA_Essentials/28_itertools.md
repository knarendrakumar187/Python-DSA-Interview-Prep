# Topic 28 — itertools
**Phase 3 · DSA Essentials · DSA relevance: ★★★★☆**

## Why this matters for DSA
Combinatorics, subsets, permutations, pairwise comparisons, infinite counters — **`itertools`** gives memory-efficient iterators for brute-force and greedy setups.

---

## Theory (simple)
`itertools` builds **lazy iterators** — great for large search spaces when you don't want full lists in memory.

Most used in DSA interviews:
- `combinations`, `permutations`
- `product` (Cartesian product)
- `accumulate` (prefix sums)
- `pairwise` (Python 3.10+)
- `chain` (flatten)

---

## Syntax
```python
from itertools import combinations, permutations, product
from itertools import accumulate, chain, pairwise, count, cycle
```

| Tool | Yields |
|------|--------|
| `combinations(s, r)` | r-length combos, order doesn't matter |
| `permutations(s, r)` | r-length arrangements, order matters |
| `product(a, b)` | all pairs (a[i], b[j]) |
| `accumulate(nums)` | running totals |
| `chain(a, b)` | concatenate iterables |

---

## Examples

### 1) combinations — subsets of size k
```python
from itertools import combinations

print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]
```

### 2) permutations
```python
from itertools import permutations

print(list(permutations("ab", 2)))
# [('a','b'), ('b','a')]
```

### 3) accumulate — prefix sums
```python
from itertools import accumulate

nums = [1, 2, 3, 4]
print(list(accumulate(nums)))  # [1, 3, 6, 10]
print(list(accumulate(nums, max)))  # prefix max
```

### 4) product — all pairs
```python
from itertools import product

print(list(product([0, 1], repeat=2)))
# [(0,0),(0,1),(1,0),(1,1)] — binary strings length 2
```

### 5) pairwise — adjacent pairs (3.10+)
```python
from itertools import pairwise

nums = [1, 3, 2, 4]
print(list(pairwise(nums)))  # [(1,3), (3,2), (2,4)]
# Older Python: zip(nums, nums[1:])
```

---

## C++ / Java compare

**C++** — `next_permutation`, nested loops for combos

**Java** — manual recursion or libraries

**Python**
```python
from itertools import combinations
for combo in combinations(nums, 3):
    ...
```

---

## DSA use cases
- Generate all subsets (power set) — combinations of all lengths
- Letter combinations of phone number — product
- Prefix sum with accumulate
- Compare adjacent elements — pairwise
- Brute force small n (n ≤ 20) subset problems

---

## 3 LeetCode-style examples

### Example A — Subsets (use combinations per size)
```python
from itertools import combinations

def subsets(nums):
    res = []
    for r in range(len(nums) + 1):
        for combo in combinations(nums, r):
            res.append(list(combo))
    return res

print(subsets([1, 2, 3]))
```

### Example B — Permutation in string (check permutations of pattern length)
```python
from itertools import permutations

def check(s1, s2):
    n = len(s1)
    if n > len(s2):
        return False
    targets = set("".join(p) for p in permutations(s1))
    for i in range(len(s2) - n + 1):
        if s2[i:i+n] in targets:
            return True
    return False
# Note: Counter/sliding window is faster — itertools for small n
```

### Example C — Prefix sum range query setup
```python
from itertools import accumulate

def range_sum(nums, queries):
    pref = [0] + list(accumulate(nums))
    return [pref[r+1] - pref[l] for l, r in queries]

nums = [1, 2, 3, 4]
print(range_sum(nums, [(0,1), (1,3)]))  # [3, 9]
```

---

## 1) Summary
- `combinations` — choose r; `permutations` — arrange r
- `accumulate` — prefix sums / running max
- `product` — Cartesian product
- All lazy — wrap in `list()` when you need all at once

## 2) Common interview questions
1. combinations vs permutations?
2. How to generate all subsets?
3. accumulate vs manual prefix loop?
4. Memory cost of list(combinations(n, k))?
5. When is brute force with itertools OK?

## 3) Common mistakes
- Using permutations for subset problems (wrong count)
- Materializing huge itertools — blows memory
- Forgetting combos don't repeat same set in different order
- Using itertools when n is large (TLE)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Print all 2-element pairs from a list using combinations.
2. **Easy:** Prefix sums with accumulate; answer range sum query.
3. **Medium:** Generate all binary strings of length n with product.
4. **Medium:** Check if any permutation of s1 is substring of s2 (small inputs).
5. **Harder:** Letter combinations of a phone number (product over digit letters).

## 5) Mini quiz
1. `len(list(combinations(5,2)))` = ?
2. `list(accumulate([1,2,3]))` = ?
3. permutations("abc", 3) count?
4. product([1,2],[10,20]) length?
5. pairwise needs Python version?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 28 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 29
