# Topic 25 — deque (collections)
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
BFS queues, sliding window max, palindrome checks, and **O(1) append/pop from both ends** — lists are slow at front pops.  
**`deque`** (double-ended queue) is the standard tool.

---

## Theory (simple)
`deque` = double-ended queue — fast operations at **left and right**.

| Operation | deque | list |
|-----------|-------|------|
| append right | O(1) | O(1) |
| pop left | O(1) | O(n) |
| append left | O(1) | O(n) |

---

## Syntax
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)           # right
dq.appendleft(0)       # left
x = dq.pop()           # from right
x = dq.popleft()       # from left
dq[0], dq[-1]          # peek
len(dq), rotate(1)     # rotate right by 1
```

---

## Examples

### 1) BFS queue pattern
```python
from collections import deque

def bfs(start, graph):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

### 2) Sliding window (store indices)
```python
def max_sliding_window(nums, k):
    dq = deque()  # indices, decreasing nums value
    out = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
```

### 3) Palindrome check with deque
```python
def is_palindrome(s):
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
```

### 4) Never use list as queue
```python
# BAD for big n:
q = []
q.append(1)
q.pop(0)  # O(n) — slow!

# GOOD:
q = deque()
q.append(1)
q.popleft()  # O(1)
```

---

## C++ / Java compare

**C++**
```cpp
deque<int> dq;
dq.push_back(x);
dq.push_front(x);
dq.pop_front();
```

**Java**
```java
Deque<Integer> dq = new ArrayDeque<>();
dq.addLast(x);
dq.addFirst(x);
dq.pollFirst();
```

**Python**
```python
from collections import deque
dq = deque()
dq.append(x); dq.appendleft(x); dq.popleft()
```

---

## DSA use cases
- BFS shortest path in unweighted graph
- Sliding window maximum (monotonic deque)
- 0-1 BFS with deque (front/back push)
- Undo/redo, recent items LRU-ish patterns
- Rotating array simulation with rotate()

---

## 3 LeetCode-style examples

### Example A — Number of islands (BFS with deque)
```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                q = deque([(r, c)])
                grid[r][c] = "0"
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
    return count
```

### Example B — Shortest path in binary matrix
```python
def shortest_path(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    q = deque([(0, 0, 1)])
    grid[0][0] = 1
    while q:
        r, c, d = q.popleft()
        if r == n-1 and c == n-1:
            return d
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                grid[nr][nc] = 1
                q.append((nr, nc, d+1))
    return -1
```

### Example C — Recent counter (queue of timestamps)
```python
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```

---

## 1) Summary
- `deque` — O(1) append/pop both ends
- BFS: `popleft` + `append`
- Never `list.pop(0)` in hot loops
- Monotonic deque for sliding window max

## 2) Common interview questions
1. deque vs list for queue?
2. BFS template with deque?
3. What is monotonic deque?
4. Can deque maxlen? `deque(maxlen=n)` auto drops old
5. Is deque thread-safe? No.

## 3) Common mistakes
- Using list.pop(0) as queue — TLE on big inputs
- Forgetting `from collections import deque`
- Confusing stack (append/pop) with queue (append/popleft)
- Not storing indices in sliding window deque

## 4) Practice problems (Easy → Hard)
1. **Easy:** Implement queue using deque — enqueue/dequeue.
2. **Easy:** Reverse first k elements using deque operations.
3. **Medium:** BFS shortest path in unweighted graph.
4. **Medium:** Sliding window maximum.
5. **Harder:** Shortest path in 0-1 weighted graph with deque (0-weight front).

## 5) Mini quiz
1. `deque([1,2]).popleft()` = ?
2. Complexity of list.pop(0)?
3. BFS uses pop from which end?
4. `deque(maxlen=3)` after 4 appends — size?
5. Import line for deque?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 25 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 26
