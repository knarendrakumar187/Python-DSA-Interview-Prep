# Topic 06 — range()
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
`range()` generates index sequences without building huge lists in memory.  
You use it for loops, sliding windows, and simulating C-style `for (i=0; i<n; i++)`.

---

## Theory (simple)
`range()` produces numbers in a sequence. It is **lazy** — it does not store all numbers at once (unless you convert to list).

Think: "give me 0, 1, 2, …, n-1" for array indexing.

---

## Syntax

```python
range(stop)              # 0 .. stop-1
range(start, stop)       # start .. stop-1
range(start, stop, step) # step can be negative

list(range(5))           # [0,1,2,3,4]
list(range(2, 8))        # [2,3,4,5,6,7]
list(range(0, 10, 2))    # [0,2,4,6,8]
list(range(10, 0, -1))   # [10,9,...,1]
```

**Rule:** stop is **never included** (half-open interval).

---

## Compare with C++/Java

```cpp
// C++: for (int i = 0; i < n; i++)
for i in range(n):
    ...

// Java: for (int i = start; i < end; i += step)
for i in range(start, end, step):
    ...
```

Python `range(n)` ≈ `0` to `n-1`. No `i++` syntax.

---

## Examples

### 1) Index loop
```python
arr = ["a", "b", "c"]
for i in range(len(arr)):
    print(i, arr[i])
```

### 2) Reverse iteration
```python
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])
# Or later: for x in reversed(arr)
```

### 3) Pairs (i, j) with i < j
```python
n = 4
for i in range(n):
    for j in range(i + 1, n):
        print(i, j)
```

### 4) range vs list — memory
```python
# Good for big n (millions):
for i in range(10**6):
    pass

# Bad — builds full list in RAM:
for i in list(range(10**6)):
    pass
```

---

## DSA use cases
- Loop `0 .. n-1` over array indices
- Subarray loops: `for i in range(n): for j in range(i, n):`
- Step 2 for even indices: `range(0, n, 2)`
- Reverse array processing: negative step

---

## 3 LeetCode-style examples

### Example A — Build index map
```python
nums = [10, 20, 30]
idx_of = {}
for i in range(len(nums)):
    idx_of[nums[i]] = i
print(idx_of)   # {10: 0, 20: 1, 30: 2}
```

### Example B — Sliding window of size k
```python
nums = [1, 2, 3, 4, 5]
k = 3
for start in range(len(nums) - k + 1):
    window = nums[start:start + k]
    print(window)
# [1,2,3], [2,3,4], [3,4,5]
```

### Example C — Prefix sum build
```python
nums = [1, 2, 3, 4]
prefix = [0] * (len(nums) + 1)
for i in range(len(nums)):
    prefix[i + 1] = prefix[i] + nums[i]
print(prefix)   # [0, 1, 3, 6, 10]
```

---

## 1) Summary
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- Stop is exclusive; default start 0, step 1
- Use with `for` — don't convert to list unless you need the list
- `range(len(arr))` = index loop over array

## 2) Common interview questions
1. What is `list(range(3))`?
2. Is `range(5)` inclusive of 5?
3. How to loop backwards over indices?
4. `range(0, n)` vs `range(n)`?
5. Why is `range` memory-efficient?

## 3) Common mistakes
- `range(n+1)` when you meant `range(n)` → off-by-one
- `range(len(arr) - 1)` missing last index
- Negative step: start must be > stop (e.g. `range(5, 0, -1)`)
- Using `range` on empty list: `range(0)` runs zero times (OK)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Print even numbers 0 to 20 using `range` step.
2. **Easy:** Print indices and values of a list using `range(len)`.
3. **Medium:** Print all subarrays using two ranges (i and j).
4. **Medium:** Reverse list in-place using `range` indices (two pointers).
5. **Harder:** Generate all length-k index combinations from 0..n-1 (nested range).

## 5) Mini quiz
1. What is `list(range(2, 6))`?
2. What is `list(range(5, 0, -1))`?
3. How many iterations: `for _ in range(10):`?
4. `range(1, 1)` — how many values?
5. Equivalent of `for i in range(len(a))` without len? (trick: not always — index needed)

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/06_range_practice.py` (create file)
- Mark Topic 06 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 07
