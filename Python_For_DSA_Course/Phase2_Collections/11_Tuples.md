# Topic 11 — Tuples
**Phase 2 · Collections · DSA relevance: ★★★★☆**

## Why this matters for DSA
Tuples are fixed, hashable pairs — perfect for `(row, col)` grid coords, `(node, dist)` in Dijkstra, and **dict keys**.  
Use when data should not change accidentally.

---

## Theory (simple)
A **tuple** is like a list but **immutable** (cannot add/remove/change elements).

```python
t = (1, 2, 3)
t = 1, 2, 3      # parentheses optional
single = (1,)    # comma required for 1-element tuple
```

Once created, you read and slice — no append.

---

## Syntax

```python
t = (10, 20)
t[0], t[-1]
t[1:3]           # slice → new tuple
len(t)
a, b = t           # unpack
x, y = y, x        # swap via tuple packing
(1, 2) + (3,)      # concat → (1,2,3)
(1,) * 3           # (1,1,1)
hash((1, 2))       # OK — hashable if all items hashable
```

### Tuple vs list
| | Tuple | List |
|---|-------|------|
| Mutable | No | Yes |
| Dict key | Yes (if items hashable) | No |
| Syntax | `(1,2)` | `[1,2]` |

---

## Compare with C++/Java
No exact tuple in older Java; use `Pair` or record. C++ has `std::pair` / `std::tuple`.  
Python tuples are lightweight and built-in — great for returning two values.

```cpp
pair<int,int> p = {1, 2};
// Python: p = (1, 2)
```

---

## Examples

### 1) Return multiple values
```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])
print(lo, hi)   # 1 4
```

### 2) Grid directions (BFS)
```python
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
grid = [[0, 0], [0, 0]]
r, c = 0, 0
for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        print(nr, nc)
```

### 3) Tuple as dict key
```python
count = {}
points = [(1, 2), (1, 2), (3, 4)]
for p in points:
    count[p] = count.get(p, 0) + 1
print(count)   # {(1,2): 2, (3,4): 1}
```

### 4) Sort list of tuples
```python
pairs = [(3, "c"), (1, "a"), (2, "b")]
pairs.sort(key=lambda x: x[0])
print(pairs)   # [(1,'a'), (2,'b'), (3,'c')]
```

---

## DSA use cases
- Coordinates: `(r, c)` in matrix BFS/DFS
- Priority queue items: `(dist, node)` (with heapq)
- Cache key: `(i, j, state)` in DP
- Return `(found, index)` from search helper

---

## 3 LeetCode-style examples

### Example A — Valid sudoku row check (using sets of tuples concept)
```python
def valid_row(board, row):
    seen = set()
    for col in range(9):
        val = board[row][col]
        if val == ".":
            continue
        if val in seen:
            return False
        seen.add(val)
    return True
# Cell position often stored as (r,c) tuples in full solution
```

### Example B — Sort intervals by start (tuple list)
```python
intervals = [(2, 5), (1, 3), (4, 6)]
intervals.sort()   # sorts by first element, then second
print(intervals)   # [(1,3), (2,5), (4,6)]
```

### Example C — BFS queue with (row, col, steps)
```python
from collections import deque

def shortest_path(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])
    visited = {(0, 0)}
    while q:
        r, c, steps = q.popleft()
        if r == rows - 1 and c == cols - 1:
            return steps
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))
    return -1
```

---

## 1) Summary
- Tuples immutable; use for fixed small records
- Unpack: `a, b = t`; swap: `a, b = b, a`
- Hashable → can be set/dict keys (if contents hashable)
- Common in BFS coords and returning two+ values

## 2) Common interview questions
1. Tuple vs list — when use each?
2. Can tuple be dict key? Can list?
3. How create one-element tuple?
4. How unpack tuple?
5. Are tuples faster than lists?

## 3) Common mistakes
- `(1)` is int, not tuple — need `(1,)`
- Trying to mutate: `t[0] = 5` → TypeError
- List inside tuple is mutable — tuple "immutable" but nested list can change
- Forgetting tuple unpacking order

## 4) Practice problems (Easy → Hard)
1. **Easy:** Pack three numbers into tuple; unpack to a,b,c.
2. **Easy:** Given list of (name, score), print highest score name.
3. **Medium:** Count frequency of 2D points given as tuples.
4. **Medium:** Sort students by (grade desc, name asc) using tuple keys.
5. **Harder:** BFS shortest path in grid; return path as list of (r,c) tuples.

## 5) Mini quiz
1. Type of `(1, 2)`?
2. Is `(1, [2])` hashable?
3. What is `(1,) * 3`?
4. How swap a,b in one line?
5. Can you append to tuple?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/11_tuples_practice.py` (create file)
- Mark Topic 11 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 12
