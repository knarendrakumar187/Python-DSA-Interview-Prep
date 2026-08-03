# Topic 14 — List Comprehensions
**Phase 2 · Collections · DSA relevance: ★★★★★**

## Why this matters for DSA
Comprehensions build lists in one readable line — fast to write in timed tests.  
You'll see them for filtering, mapping, and building grids — but know when a plain loop is clearer.

---

## Theory (simple)
**List comprehension** = compact loop that builds a list.

```python
# instead of:
squares = []
for x in range(5):
    squares.append(x * x)

# write:
squares = [x * x for x in range(5)]
```

Same logic, fewer lines.

---

## Syntax

```python
[expr for item in iterable]
[expr for item in iterable if condition]

# nested
[row for row in matrix]

# dict comprehension
{k: v for k, v in pairs}

# set comprehension
{x for x in nums}

# generator (lazy) — parentheses
(x * x for x in range(10**6))
```

---

## Compare with C++/Java
C++ / Java use loops or streams (`map`, `filter`).  
Python comprehensions are idiomatic and often faster than manual append loops.

```java
// Java stream style
list.stream().map(x -> x*x).collect(...)
// Python
[x*x for x in lst]
```

---

## Examples

### 1) Squares and evens
```python
squares = [x * x for x in range(6)]
evens = [x for x in range(20) if x % 2 == 0]
print(squares)   # [0,1,4,9,16,25]
print(evens[:5]) # [0,2,4,6,8]
```

### 2) Transform strings
```python
words = ["hello", "world"]
upper = [w.upper() for w in words]
lengths = [len(w) for w in words]
```

### 3) Flatten 2D matrix
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)   # [1,2,3,4,5,6]
```

### 4) Build adjacency from edges
```python
edges = [(0, 1), (1, 2), (0, 2)]
n = 3
graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
print(graph)
```

---

## DSA use cases
- Build result list from traversal
- Filter positives / valid values
- Initialize `[[0]*cols for _ in range(rows)]` grid
- Quick map: indices where condition holds

---

## 3 LeetCode-style examples

### Example A — Squares of sorted array (two pointers + comprehension)
```python
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    lo, hi = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[lo]) > abs(nums[hi]):
            result[i] = nums[lo] ** 2
            lo += 1
        else:
            result[i] = nums[hi] ** 2
            hi -= 1
    return result

print(sorted_squares([-4, -1, 0, 3, 10]))
```

### Example B — Filter anagram lengths
```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}
for w in words:
    key = tuple(sorted(w))
    groups.setdefault(key, []).append(w)
result = [v for v in groups.values() if len(v) > 1]
print(result)
```

### Example C — All indices where value equals target
```python
nums = [1, 2, 3, 2, 2]
target = 2
indices = [i for i, x in enumerate(nums) if x == target]
print(indices)   # [1, 3, 4]
```

---

## 1) Summary
- `[expr for x in it]` and `[expr for x in it if cond]`
- Nested: `[x for row in m for x in row]`
- Dict/set comps: `{k:v ...}`, `{x ...}`
- Prefer clarity — nested comps can get hard to read

## 2) Common interview questions
1. What is list comprehension?
2. Comprehension vs for-loop append?
3. How flatten 2D list in one line?
4. What is generator expression?
5. When NOT to use comprehension?

## 3) Common mistakes
- Wrong order in nested: `[x for x in row for row in m]` (NameError)
- Side effects inside comprehension (avoid)
- Building huge list when generator enough
- `[[0]*n]*m` shared rows trap — use `[[0]*n for _ in range(m)]`

## 4) Practice problems (Easy → Hard)
1. **Easy:** List of squares 0..9 using comprehension.
2. **Easy:** List of even numbers from 1..20.
3. **Medium:** Flatten 3×3 matrix to 1D list.
4. **Medium:** Build list of (index, value) pairs where value > 0.
5. **Harder:** Generate all pairs (i,j) with i<j for range(n) using comprehension.

## 5) Mini quiz
1. Rewrite: `[x for x in range(5) if x % 2 == 0]` — first three values?
2. Dict comp: `{x: x*x for x in range(3)}` result?
3. Set comp: `{x % 3 for x in range(6)}`?
4. Generator vs list comp memory?
5. Correct flatten: `[x for row in m for x in row]` — True?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/14_comprehensions_practice.py` (create file)
- Mark Topic 14 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 15
