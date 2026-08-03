# Topic 12 — Sets
**Phase 2 · Collections · DSA relevance: ★★★★★**

## Why this matters for DSA
Sets give **O(1) average** lookup for "have I seen this?" — duplicates, cycles, anagrams, graph visited nodes.  
Essential for turning O(n²) into O(n).

---

## Theory (simple)
A **set** holds **unique** items with **no order** (don't rely on order).

```python
s = {1, 2, 3}
s = set([1, 2, 2, 3])   # {1, 2, 3}
```

Duplicates removed automatically.

---

## Syntax

```python
s = set()
s = {1, 2, 3}
s.add(x)
s.remove(x)      # KeyError if missing
s.discard(x)     # no error if missing
x in s           # O(1) average
len(s)
s.clear()

a | b            # union
a & b            # intersection
a - b            # difference
a ^ b            # symmetric difference

# empty set must be set(), not {} (that's dict)
```

---

## Compare with C++/Java

| Python | C++ | Java |
|--------|-----|------|
| `set` | `unordered_set` (hash) | `HashSet` |
| `in` O(1)* | `.count()` | `.contains()` |
| `{1,2}` | `{1,2}` | `Set.of(1,2)` |

Python also has `frozenset` — immutable, hashable set.

---

## Examples

### 1) Remove duplicates
```python
nums = [1, 2, 2, 3, 1]
unique = list(set(nums))
print(unique)   # order not guaranteed
```

### 2) Seen set in loop
```python
nums = [1, 2, 3, 1]
seen = set()
for x in nums:
    if x in seen:
        print("duplicate", x)
        break
    seen.add(x)
```

### 3) Set operations
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)   # {3} intersection
print(a | b)   # {1,2,3,4,5} union
print(a - b)   # {1, 2}
```

### 4) Visited in graph DFS
```python
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei)

dfs(2)
print(visited)
```

---

## DSA use cases
- Duplicate detection
- Visited nodes in BFS/DFS
- Two-sum complement check with set
- Union/find style with sets (small problems)

---

## 3 LeetCode-style examples

### Example A — Contains duplicate
```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

print(contains_duplicate([1, 2, 3, 1]))   # True
```

### Example B — Intersection of two arrays
```python
def intersection(a, b):
    return list(set(a) & set(b))

print(intersection([1, 2, 2, 1], [2, 2]))   # [2] (order may vary)
```

### Example C — Longest consecutive sequence
```python
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for x in num_set:
        if x - 1 not in num_set:   # start of streak
            length = 1
            while x + length in num_set:
                length += 1
            best = max(best, length)
    return best

print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4
```

---

## 1) Summary
- Set = unique items; fast `in` / `add`
- Use `set()` for empty set, not `{}`
- `discard` safe remove; `remove` raises if missing
- Set ops: `|`, `&`, `-` for union/intersection/difference

## 2) Common interview questions
1. Average time of `x in set`?
2. Set vs list for membership?
3. Is set ordered?
4. Can set contain lists?
5. What is `frozenset`?

## 3) Common mistakes
- `{}` creates empty dict, not set
- Expecting preserved insertion order in old mental models (Py 3.7+ dict ordered; set still unordered)
- Putting unhashable types (list) in set
- Converting to set when you need duplicate counts (use dict/Counter)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Remove duplicates from list using set.
2. **Easy:** Check if two lists have any common element.
3. **Medium:** Find intersection and union of two arrays.
4. **Medium:** Happy number (cycle detection with set).
5. **Harder:** Longest consecutive sequence (set streak method).

## 5) Mini quiz
1. How create empty set?
2. `{1,2,2,3}` size?
3. Is list hashable?
4. `discard` vs `remove`?
5. Time complexity of `x in set` (average)?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/12_sets_practice.py` (create file)
- Mark Topic 12 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 13
