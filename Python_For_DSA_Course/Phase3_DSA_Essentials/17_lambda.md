# Topic 17 — lambda
**Phase 3 · DSA Essentials · DSA relevance: ★★★★☆**

## Why this matters for DSA
Sorting, heaps, and custom comparators often need a **small one-line function**.  
`lambda` creates anonymous functions — perfect for `key=` in `sorted()` and `heapq`.

---

## Theory (simple)
A **lambda** is a tiny function without a name:

```python
lambda arguments: expression
```

Only **one expression** — no `return` keyword (expression value is returned).

```python
add = lambda a, b: a + b
print(add(2, 3))  # 5
```

Same as:
```python
def add(a, b):
    return a + b
```

---

## Syntax
```python
lambda x: x * 2
lambda x, y: x + y
lambda p: p[1]          # for tuples
lambda d: d["score"]    # for dicts in sort
```

| Use | Example |
|-----|---------|
| Sort by length | `sorted(words, key=lambda w: len(w))` |
| Sort pairs | `sorted(pairs, key=lambda p: p[1])` |
| Filter | `filter(lambda x: x > 0, nums)` |
| Map | `map(lambda x: x**2, nums)` |

---

## Examples

### 1) Sort strings by length
```python
words = ["hi", "hello", "hey"]
print(sorted(words, key=lambda w: len(w)))
# ['hi', 'hey', 'hello']
```

### 2) Sort list of tuples by second item
```python
pairs = [(1, 5), (2, 1), (3, 3)]
print(sorted(pairs, key=lambda p: p[1]))
# [(2, 1), (3, 3), (1, 5)]
```

### 3) Custom max with lambda
```python
students = [("Ann", 90), ("Bob", 85)]
top = max(students, key=lambda s: s[1])
print(top)  # ('Ann', 90)
```

### 4) When NOT to use lambda — use def
```python
# Bad for complex logic — use def instead
def is_valid(x):
    return x > 0 and x % 2 == 0
```

---

## C++ / Java compare

**C++** — function pointer / lambda:
```cpp
sort(v.begin(), v.end(), [](int a, int b){ return a > b; });
```

**Java** — Comparator:
```java
Arrays.sort(arr, (a, b) -> a - b);
```

**Python**
```python
sorted(arr, key=lambda x: x, reverse=True)
```

---

## DSA use cases
- `sorted(intervals, key=lambda x: x[0])` — merge intervals
- `heapq` with tuples `(priority, item)` — no lambda needed often
- `max/min` with custom key
- Quick transforms in `map` / `filter` (list comp often cleaner)

---

## 3 LeetCode-style examples

### Example A — Merge intervals (sort by start)
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out

print(merge([[1,3],[2,6],[8,10],[15,18]]))
```

### Example B — Sort people by height then name
```python
people = [["Alice", 160], ["Bob", 170], ["Ann", 160]]
people.sort(key=lambda p: (-p[1], p[0]))
print(people)
```

### Example C — Closest points (sort by distance squared)
```python
def dist2(p):
    return p[0]**2 + p[1]**2

points = [[3,3], [5,-1], [-2,4]]
points.sort(key=lambda p: p[0]**2 + p[1]**2)
print(points[:2])
```

---

## 1) Summary
- `lambda args: expr` — one-line anonymous function
- Main DSA use: `key=` in `sorted`, `min`, `max`
- Keep lambdas short; use `def` for complex logic
- Cannot contain statements (if/else only as expression: `a if cond else b`)

## 2) Common interview questions
1. Lambda vs normal function?
2. Can lambda have multiple lines? No — single expression only.
3. Why use lambda in sorting?
4. Is lambda slower than def? Similar; readability matters more.
5. Ternary in lambda: `lambda x: "big" if x > 10 else "small"`

## 3) Common mistakes
- Using `:` and `return` inside lambda (invalid)
- Sorting tuples without `key` — sorts by first element only
- Overusing lambda when named `def` is clearer
- Forgetting `key=` applies to each item, not the whole list

## 4) Practice problems (Easy → Hard)
1. **Easy:** Sort numbers by absolute value using lambda.
2. **Easy:** Sort words alphabetically by last character.
3. **Medium:** Given `[name, age, score]`, sort by score desc, then age asc.
4. **Medium:** Find word with max length using `max(..., key=lambda ...)`.
5. **Harder:** Sort intervals by end time (activity selection pattern).

## 5) Mini quiz
1. What does `lambda x: x[1]` return for input `(3, 7)`?
2. Can lambda assign variables? No.
3. `(lambda a, b: a + b)(2, 3)` = ?
4. Sort `[3,1,2]` descending with lambda?
5. Is `lambda: 0` valid?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 17 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 18
