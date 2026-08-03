# Topic 20 — map() and filter()
**Phase 3 · DSA Essentials · DSA relevance: ★★★★☆**

## Why this matters for DSA
`map` transforms each element; `filter` keeps elements that pass a test.  
In interviews, **list comprehensions** often replace them — but you must read map/filter in others' code and use them for quick transforms.

---

## Theory (simple)

| Function | Does | Returns |
|----------|------|---------|
| `map(f, iterable)` | apply f to each item | iterator of results |
| `filter(pred, iterable)` | keep items where pred(item) is True | iterator |

Both are **lazy** — wrap in `list()` to see all values.

---

## Syntax
```python
map(function, iterable)
filter(function, iterable)   # None as function = keep truthy
list(map(int, ["1", "2"]))
list(filter(lambda x: x > 0, nums))
```

---

## Examples

### 1) map — square numbers
```python
nums = [1, 2, 3, 4]
sq = list(map(lambda x: x * x, nums))
print(sq)  # [1, 4, 9, 16]
```

### 2) map — parse input strings to int
```python
line = "1 2 3 4"
nums = list(map(int, line.split()))
print(nums)  # [1, 2, 3, 4]
```

### 3) filter — keep evens
```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]
```

### 4) List comprehension equivalents (preferred in DSA)
```python
sq = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]
```

---

## C++ / Java compare

**C++** — transform / copy_if (STL):
```cpp
transform(v.begin(), v.end(), out.begin(), [](int x){ return x*x; });
```

**Java** — streams:
```java
list.stream().map(x -> x * 2).filter(x -> x > 0).collect(toList());
```

**Python**
```python
list(filter(lambda x: x > 0, map(lambda x: x * 2, nums)))
```

---

## DSA use cases
- Parse competitive programming input: `map(int, input().split())`
- Convert char grid to int matrix
- Filter valid moves / neighbors
- Strip and process lines from file
- Quick transform before sort

---

## 3 LeetCode-style examples

### Example A — Parse matrix from strings
```python
def parse_matrix(lines):
    return [list(map(int, row.split())) for row in lines]

grid = parse_matrix(["1 2 3", "4 5 6"])
print(grid)
```

### Example B — Filter positive then sum
```python
def sum_positive(nums):
    return sum(filter(lambda x: x > 0, nums))

print(sum_positive([-1, 2, 3, -4, 5]))  # 10
```

### Example C — Normalize scores to 0–100 scale
```python
def normalize(scores):
    mx = max(scores)
    return list(map(lambda s: s * 100 // mx, scores))

print(normalize([10, 20, 50]))  # [20, 40, 100]
```

---

## 1) Summary
- `map(f, it)` → apply f to each element
- `filter(p, it)` → keep truthy p(item)
- Both return iterators — use `list()` if needed
- List comprehensions are usually clearer for DSA

## 2) Common interview questions
1. map vs list comprehension?
2. What does `filter(None, lst)` do? Keeps truthy items.
3. Can map take multiple iterables? Yes — `map(max, a, b)`.
4. Are map/filter lazy in Python 3? Yes.
5. When to use map for input parsing?

## 3) Common mistakes
- Forgetting `list(map(...))` — get map object, not list
- Using filter when list comp is clearer
- `map(int, input())` wrong — need `.split()` first
- Side effects in map (use loop instead)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Double each number using map.
2. **Easy:** Remove zeros from list using filter.
3. **Medium:** Read "n" then n integers — parse with map.
4. **Medium:** Filter words longer than 3 chars, then map to uppercase.
5. **Harder:** Apply map to nested list — matrix transpose with zip is often better.

## 5) Mini quiz
1. `list(map(str, [1,2,3]))` = ?
2. `list(filter(lambda x: x%2, [0,1,2,3]))` = ?
3. Equivalent list comp for `map(lambda x: x+1, a)`?
4. Does filter return bool list? No — filtered items.
5. `list(map(int, "123"))` valid? No — int needs iterable of strings.

---

## Homework
- Type all examples in this file yourself
- Rewrite each map/filter example as list comprehension
- Solve practice 1–5
- Mark Topic 20 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 21
