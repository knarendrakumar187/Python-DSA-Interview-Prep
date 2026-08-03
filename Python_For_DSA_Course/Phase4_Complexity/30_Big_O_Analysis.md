# Topic 30 — Big O Analysis
**Phase 4 · Complexity · DSA relevance: ★★★★★**

## Why this matters for DSA
Interviewers ask **time and space complexity** for every solution.  
Big O describes how runtime grows when input size **n** grows — not exact seconds.

---

## Theory (simple)
**Big O** = upper bound on growth rate (worst case usually).

Common orders (fast → slow):

```text
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)
```

| Notation | Meaning |
|----------|---------|
| O(1) | constant — same time any n |
| O(n) | linear — double n → double time |
| O(n²) | quadratic — nested loops over n |
| O(log n) | halve problem each step — binary search |

Drop constants and lower terms: O(2n + 5) → **O(n)**.

---

## Syntax (how to analyze code)
Count **dominant operations** in terms of n.

```python
# O(1)
x = nums[0]

# O(n)
for x in nums:
    ...

# O(n²)
for i in range(n):
    for j in range(n):
        ...

# O(log n)
while n > 1:
    n //= 2
```

---

## Examples

### 1) Single loop — O(n)
```python
def sum_arr(nums):
    total = 0
    for x in nums:      # n times
        total += x
    return total
# Time O(n), Space O(1)
```

### 2) Nested loop — O(n²)
```python
def pairs(nums):
    out = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            out.append((nums[i], nums[j]))
    return out
# Time O(n²), Space O(n²) for output
```

### 3) Binary search — O(log n)
```python
def bs(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# Time O(log n), Space O(1)
```

### 4) Hidden loop — O(n) total
```python
s = ""
for c in "hello":       # each += may copy string
    s += c              # avoid — use list join
# Naive string concat can be O(n²); join is O(n)
```

---

## C++ / Java compare
Same Big O rules apply in all languages.  
Python may have higher **constants** (interpreted) but complexity class is what interviews test.

---

## DSA use cases
- Two pointers — often O(n)
- Hash map lookup — O(1) average per op
- Sort then scan — O(n log n)
- DFS/BFS on graph — O(V + E)
- DP table fill — O(n * m)

---

## 3 LeetCode-style examples

### Example A — Two Sum
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
# Time O(n), Space O(n)
```

### Example B — Bubble-style scan O(n²)
```python
def contains_duplicate_slow(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
# Time O(n²) — set version is O(n)
```

### Example C — Merge sort level O(n log n)
```python
def sort_and_scan(intervals):
    intervals.sort()           # O(n log n)
    # one pass merge O(n)
    ...
# Total O(n log n)
```

---

## 1) Summary
- Big O = growth rate, not exact time
- Keep fastest-growing term only
- Count loops, recursion depth, map ops
- State time AND space in interviews

## 2) Common interview questions
1. What is O(1)? O(n)? O(log n)?
2. Why drop constants?
3. Time vs space tradeoff example?
4. Complexity of binary search?
5. Amortized O(1) — Python list append?

## 3) Common mistakes
- Saying O(2n) instead of O(n)
- Ignoring hidden loops (string +=, list insert at 0)
- Confusing best vs worst case without stating
- Forgetting space for hash map / recursion stack

## 4) Practice problems (Easy → Hard)
1. **Easy:** State complexity of one loop printing n items.
2. **Easy:** State complexity of binary search on n elements.
3. **Medium:** Analyze: two nested loops, inner runs i times (triangle) — O(?)
4. **Medium:** BFS on graph — express in V and E.
5. **Harder:** Recursive fib without memo — time? With memo?

## 5) Mini quiz
1. O(n + n²) simplifies to?
2. Sorting n items — typical complexity?
3. dict lookup average?
4. Two pointer on sorted array — typical time?
5. Space of recursive DFS depth d?

---

## Homework
- Analyze 5 solutions you wrote in Phase 3
- Solve practice 1–5
- Mark Topic 30 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 31
