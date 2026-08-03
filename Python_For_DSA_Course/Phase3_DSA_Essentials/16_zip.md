# Topic 16 — zip()
**Phase 3 · DSA Essentials · DSA relevance: ★★★★☆**

## Why this matters for DSA
Many problems combine **two lists, strings, or columns** — merge intervals, compare rows, pair keys with values, walk two pointers in parallel.  
`zip()` pairs items from multiple iterables together.

---

## Theory (simple)
`zip(a, b, c, ...)` stops at the **shortest** iterable.

```text
  [1, 2, 3]  +  ["a", "b", "c"]
         ↓ zip
  (1,"a"), (2,"b"), (3,"c")
```

---

## Syntax
```python
zip(*iterables)           # iterator of tuples
list(zip(a, b))           # materialize
zip(a, b, strict=True)    # Python 3.10+: error if lengths differ
```

| Function | Result |
|----------|--------|
| `zip([1,2], ["a","b"])` | `(1,"a"), (2,"b")` |
| `zip([1,2,3], [10,20])` | `(1,10), (2,20)` — stops at 2 |
| `zip(*matrix)` | transpose rows → columns |

---

## Examples

### 1) Pair two lists
```python
names = ["Ann", "Bob"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
```

### 2) Build dict from parallel lists
```python
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

### 3) Transpose a matrix
```python
grid = [[1, 2, 3], [4, 5, 6]]
cols = list(zip(*grid))
print(cols)  # [(1, 4), (2, 5), (3, 6)]
```

### 4) Compare two strings char by char
```python
s1, s2 = "abc", "adc"
for i, (a, b) in enumerate(zip(s1, s2)):
    if a != b:
        print("diff at", i)
```

---

## C++ / Java compare

**C++** — manual index loop:
```cpp
for (int i = 0; i < min(a.size(), b.size()); i++) {
    pair(a[i], b[i]);
}
```

**Java**
```java
for (int i = 0; i < Math.min(a.length, b.length); i++) { ... }
```

**Python**
```python
for x, y in zip(a, b):
    ...
```

---

## DSA use cases
- Merge two sorted lists (two pointers with zip-like logic)
- Compare two arrays element-wise
- Transpose matrix / read columns
- Pair coordinates: `zip(xs, ys)`
- Reconstruct lists from keys + values

---

## 3 LeetCode-style examples

### Example A — Merge two sorted lists (concept)
```python
def merge_sorted(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out

print(merge_sorted([1, 3, 5], [2, 4, 6]))
```

### Example B — Find mismatched index in two strings
```python
def first_diff(s, t):
    for i, (a, b) in enumerate(zip(s, t)):
        if a != b:
            return i
    if len(s) != len(t):
        return min(len(s), len(t))
    return -1

print(first_diff("abc", "adc"))  # 1
```

### Example C — Sort pairs by second value
```python
pairs = [(1, 3), (2, 1), (3, 2)]
pairs.sort(key=lambda p: p[1])
# or: sorted(zip([1,2,3], [3,1,2])) after zipping
print(pairs)  # [(2, 1), (3, 2), (1, 3)]
```

---

## 1) Summary
- `zip` pairs elements from multiple iterables
- Stops at shortest length (unless `strict=True`)
- `zip(*matrix)` transposes rows
- `dict(zip(keys, vals))` builds a map fast

## 2) Common interview questions
1. What happens if lengths differ?
2. How to unzip / transpose with `zip(*data)`?
3. Difference between `zip` and `enumerate`?
4. Is zip lazy? Yes — iterator.
5. How to create dict from two lists?

## 3) Common mistakes
- Expecting zip to pad shorter list (it does not)
- Forgetting `zip` returns tuples — need unpacking in loop
- Using zip on dict without `.items()` when you need key+value pairs
- Confusing `zip(a, b)` with concatenation

## 4) Practice problems (Easy → Hard)
1. **Easy:** Add two lists element-wise using zip.
2. **Easy:** Given parallel lists of names and ages, print `"Name is age"`.
3. **Medium:** Transpose a 2D list and print each column sum.
4. **Medium:** Check if two strings are anagrams using sorted zip compare idea.
5. **Harder:** Merge k sorted lists — start with merging two using two-pointer zip logic.

## 5) Mini quiz
1. `list(zip([1,2,3], [10,20]))` = ?
2. How to get columns from `[[1,2],[3,4]]`?
3. Does zip modify original lists?
4. `dict(zip("ab", [1,2]))` = ?
5. What unpacks as `a, b = zip([1],[2])`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 16 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 17
