# Topic 22 — min(), max(), sum()
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
These builtins find extremes and totals in **O(n)** — kadane setup, greedy choices, sliding window bounds, subarray sums.  
Combine with **`key=`** for custom comparisons.

---

## Theory (simple)

| Function | Purpose | Empty iterable? |
|----------|---------|-----------------|
| `min(it)` | smallest item | Error unless `default=` (3.4+) |
| `max(it)` | largest item | Same |
| `sum(it, start=0)` | total | Returns start (0) |

For lists of numbers, `sum` is fast and readable.

---

## Syntax
```python
min(iterable)
max(iterable)
sum(iterable, start=0)

min(a, b, c)                    # multiple args
min(items, key=lambda x: x[1])
max(nums, default=float('-inf'))  # safe empty
```

---

## Examples

### 1) Basic
```python
nums = [3, 1, 4, 1, 5]
print(min(nums), max(nums), sum(nums))  # 1 5 14
```

### 2) Multiple arguments
```python
print(min(5, 2, 8))   # 2
print(max(5, 2, 8))   # 8
```

### 3) With key
```python
words = ["apple", "pi", "banana"]
print(min(words, key=len))  # pi
print(max(words, key=len))  # banana
```

### 4) sum with start
```python
print(sum([1, 2, 3]))       # 6
print(sum([1, 2, 3], 10))   # 16 — start offset
```

### 5) Initial value pattern for DSA
```python
best = float("-inf")
for x in nums:
    best = max(best, x)

mini = float("inf")
for x in nums:
    mini = min(mini, x)
```

---

## C++ / Java compare

**C++**
```cpp
*min_element(v.begin(), v.end());
accumulate(v.begin(), v.end(), 0);
```

**Java**
```java
Collections.min(list);
Arrays.stream(arr).sum();
```

**Python** — one line:
```python
min(nums); max(nums); sum(nums)
```

---

## DSA use cases
- Kadane / max subarray sum uses max in loop
- Two pointers: track min/max window
- Greedy: pick min remaining, max profit
- Prefix sums built with running sum (or sum on slice — slower)
- `max(heights)` for container problems

---

## 3 LeetCode-style examples

### Example A — Maximum subarray (Kadane)
```python
def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
```

### Example B — Best time to buy/sell stock
```python
def max_profit(prices):
    mini = float("inf")
    best = 0
    for p in prices:
        mini = min(mini, p)
        best = max(best, p - mini)
    return best

print(max_profit([7,1,5,3,6,4]))  # 5
```

### Example C — Min cost path (simple 1D)
```python
def min_cost(cost):
    return sum(min(cost[i], cost[i+1]) for i in range(0, len(cost)-1, 2))

# Note: real "Min Cost Climbing Stairs" uses DP, not plain sum
```

---

## 1) Summary
- `min`, `max`, `sum` work on any iterable
- Use `key=` for custom min/max
- `float("inf")` / `float("-inf")` for initial best in loops
- `sum` only for numbers; strings need join

## 2) Common interview questions
1. Complexity of min/max on list?
2. min vs sorted()[0]?
3. How to max empty list safely?
4. sum of empty list?
5. min of two values without if?

## 3) Common mistakes
- `sum` on strings without start str (TypeError with int start)
- Using max on empty list (ValueError)
- Forgetting `key=` when comparing tuples
- `max(a, b)` vs `max([a,b])` — both work

## 4) Practice problems (Easy → Hard)
1. **Easy:** Find min, max, average of a list (average = sum/len).
2. **Easy:** Find longest word using max+key=len.
3. **Medium:** Maximum product of two elements in array.
4. **Medium:** Kadane — max subarray sum.
5. **Harder:** Max sum of non-adjacent elements (House Robber — DP, not plain max).

## 5) Mini quiz
1. `sum([])` = ?
2. `min("cba")` = ?
3. `max([], default=0)` = ?
4. `min([[1,2],[0,5]], key=lambda x: x[1])` = ?
5. Kadane uses max how many times per step?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 22 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 23
