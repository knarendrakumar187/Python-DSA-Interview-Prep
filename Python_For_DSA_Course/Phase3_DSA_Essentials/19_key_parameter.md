# Topic 19 — The key Parameter
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
The **`key`** argument tells Python *how to compare* items — by length, by second field, by negative score for descending order.  
Master `key=` and you unlock clean sorting, min/max, and heap problems.

---

## Theory (simple)
Instead of comparing whole objects, Python computes `key(item)` for each item and compares those values.

```text
  items:  ["bob", "a", "hi"]
  key=len:   3     1    2
  sorted order by key: "a", "hi", "bob"
```

Works in: `sorted`, `list.sort`, `min`, `max`, `heapq` (via tuple first element), `nlargest`/`nsmallest`.

---

## Syntax
```python
sorted(items, key=function)
min(items, key=function)
max(items, key=function)
```

`function` takes one argument (each item) and returns a comparable value.

---

## Examples

### 1) Sort by length
```python
words = ["python", "go", "java"]
print(sorted(words, key=len))
```

### 2) Descending via negative (numbers only)
```python
nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda x: -x))  # [5, 4, 3, 1, 1]
# Better: reverse=True for simple cases
print(sorted(nums, reverse=True))
```

### 3) Multiple sort keys with tuple
```python
# Primary: score high, secondary: name low
players = [("Ann", 10), ("Bob", 10), ("Cal", 12)]
players.sort(key=lambda p: (-p[1], p[0]))
print(players)
```

### 4) min/max with key
```python
words = ["apple", "pi", "banana"]
shortest = min(words, key=len)
longest = max(words, key=len)
print(shortest, longest)  # pi apple
```

### 5) Sort dict items by value
```python
freq = {"a": 3, "b": 1, "c": 2}
top = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
print(top)  # [('a', 3), ('c', 2), ('b', 1)]
```

---

## C++ / Java compare

**C++** — custom comparator:
```cpp
sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
    return a.second < b.second;
});
```

**Java**
```java
list.sort(Comparator.comparingInt(p -> p.score));
```

**Python** — simpler mental model: extract sort field with `key`.

---

## DSA use cases
- Intervals: `key=lambda x: x[0]` or `x[1]`
- Closest points: `key=lambda p: p[0]**2 + p[1]**2`
- Top k frequent: sort `Counter.items()` by count
- Meeting rooms: sort by start or end time
- Custom string order (Largest Number problem)

---

## 3 LeetCode-style examples

### Example A — Meeting rooms (sort by start)
```python
def can_attend(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

print(can_attend([[0,30],[5,10],[15,20]]))  # False
```

### Example B — K closest points to origin
```python
def k_closest(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

print(k_closest([[1,3],[-2,2]], 1))
```

### Example C — Reorder by custom rank
```python
def relative_sort(arr, order):
    rank = {v: i for i, v in enumerate(order)}
    arr.sort(key=lambda x: rank.get(x, len(order)))
    return arr

print(relative_sort([2,3,1,3,2], [2,3,1]))
```

---

## 1) Summary
- `key=f` means "compare f(item) values"
- Tuple keys handle multi-level sort: `(primary, secondary)`
- Use `-value` or `reverse=True` for descending
- Works with sorted, min, max, heapq.nsmallest/largest

## 2) Common interview questions
1. What is the `key` parameter?
2. Sort strings by last character?
3. Sort by two fields?
4. Difference between `cmp` (old Python 2) and `key`?
5. Can key return a list? Yes, lists compare lexicographically.

## 3) Common mistakes
- Using `-x` on strings (TypeError — use reverse or invert rank)
- Sorting dict directly — sorts keys only
- Forgetting `key` receives the whole item, not index
- `sorted(d, key=d.get)` wrong — need `.items()` for value sort

## 4) Practice problems (Easy → Hard)
1. **Easy:** Sort words by length, then alphabetically for ties.
2. **Easy:** Find the tuple with smallest second value using min+key.
3. **Medium:** Sort students by grade desc, name asc.
4. **Medium:** Given word list, return top 3 longest using sorted+key.
5. **Harder:** Custom sort string digits for "Largest Number" — key comparator trick.

## 5) Mini quiz
1. `sorted([3,1,2], key=lambda x: -x)` = ?
2. `min(["aa","b"], key=len)` = ?
3. How to sort list of dicts by key `"age"`?
4. Does key function change the list elements?
5. `sorted([(1,2),(3,1)], key=lambda p: p[1])` = ?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 19 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 20
