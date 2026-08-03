# Topic 10 — Lists
**Phase 2 · Collections · DSA relevance: ★★★★★**

## Why this matters for DSA
Lists are Python's dynamic arrays — the #1 structure in interviews.  
Master indexing, append, pop, slicing, and in-place updates.

---

## Theory (simple)
A **list** is an ordered, **mutable** collection.

```python
nums = [1, 2, 3]
nums[0] = 10      # OK — mutable
nums.append(4)
nums.pop()        # remove last
```

Think: resizable array with O(1) amortized append at end.

---

## Syntax

```python
lst = [1, 2, 3]
lst[i], lst[-1]
lst[i:j]          # slice → new list
lst.append(x)
lst.pop()         # last; lst.pop(i) at index
lst.insert(i, x)
lst.remove(x)     # first match
len(lst)
lst.sort()        # in-place
sorted(lst)       # new sorted list
lst.reverse()
x in lst
lst + lst2        # concat
lst * 2           # repeat
```

### Copy traps
```python
a = [1, 2]
b = a             # same object
c = a[:]          # shallow copy
c = list(a)
```

---

## Compare with C++/Java

| Python list | C++ `vector` | Java `ArrayList` |
|-------------|--------------|------------------|
| Dynamic | Dynamic | Dynamic |
| Mixed types OK | Same type | Same type (generics) |
| `append` O(1)* | `push_back` | `add` |
| `pop()` end | `pop_back` | `remove(size-1)` |

---

## Examples

### 1) Two sum with list scan (slow)
```python
nums = [3, 2, 4]
target = 6
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
```

### 2) In-place remove duplicates (sorted)
```python
nums = [1, 1, 2, 2, 3]
k = 1
for i in range(1, len(nums)):
    if nums[i] != nums[k - 1]:
        nums[k] = nums[i]
        k += 1
print(nums[:k])   # [1, 2, 3]
```

### 3) Stack using list
```python
stack = []
stack.append(1)
stack.append(2)
top = stack.pop()
print(top)   # 2
```

### 4) Queue (slow at front — use deque later)
```python
from collections import deque
q = deque([1, 2, 3])
q.append(4)
front = q.popleft()
```

---

## DSA use cases
- Dynamic array problems: two pointers, prefix sum
- Stack: `append` / `pop`
- Sort then two pointers
- In-place overwrite for "remove element" style

---

## 3 LeetCode-style examples

### Example A — Best time to buy/sell stock
```python
prices = [7, 1, 5, 3, 6, 4]
mini = float("inf")
best = 0
for p in prices:
    mini = min(mini, p)
    best = max(best, p - mini)
print(best)   # 5
```

### Example B — Merge intervals (sort by start)
```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
print(merged)
```

### Example C — Rotate array (reverse trick)
```python
def rotate(nums, k):
    k %= len(nums)
    def rev(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
    rev(0, len(nums) - 1)
    rev(0, k - 1)
    rev(k, len(nums) - 1)

arr = [1, 2, 3, 4, 5]
rotate(arr, 2)
print(arr)   # [4, 5, 1, 2, 3]
```

---

## 1) Summary
- Lists = mutable ordered arrays; `append`, `pop`, slice
- `sort()` in-place; `sorted()` returns new list
- Copy with `[:]` or `list()` — not `b = a`
- Stack: append/pop end; queue: use `deque`

## 2) Common interview questions
1. List vs array in other languages?
2. Time to append? Pop from end? Pop from front?
3. Difference `sort()` vs `sorted()`?
4. Shallow vs deep copy?
5. How remove item while iterating safely?

## 3) Common mistakes
- `b = a` then mutate both
- `lst.remove(x)` in loop over same list
- Index out of range on empty list
- Using list as queue with `pop(0)` — O(n) each time

## 4) Practice problems (Easy → Hard)
1. **Easy:** Find max and min in list.
2. **Easy:** Reverse list in-place (two pointers).
3. **Medium:** Remove all occurrences of val in-place.
4. **Medium:** Sort colors (0,1,2) in-place — Dutch flag.
5. **Harder:** Three sum (return triplets summing to 0).

## 5) Mini quiz
1. What is `[1,2] + [3]`?
2. `pop()` removes from which end?
3. Does slice `[1:3]` include index 3?
4. `[0] * 5` result?
5. Is `[1,2,3].sort()` return value useful?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/10_lists_practice.py` (create file)
- Mark Topic 10 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 11
