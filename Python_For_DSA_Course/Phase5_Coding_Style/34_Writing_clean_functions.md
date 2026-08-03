# Topic 34 — Writing Clean Functions
**Phase 5 · Coding Style · DSA relevance: ★★★★★**

## Why this matters for DSA
Interviewers read your code live. **Small, clear functions** with good names show you think systematically — and reduce bugs under pressure.

---

## Theory (simple)
Clean DSA functions:
- One clear job per function
- Descriptive names (`max_profit`, not `mp`)
- Early returns for edge cases
- Type hints optional but helpful
- Docstring one line if logic non-obvious

Avoid 200-line `solve()` monsters.

---

## Syntax
```python
def function_name(args) -> return_type:
    """One-line purpose if needed."""
    if edge_case:
        return default
    # main logic
    return result

# helper for DFS/BFS
def dfs(node):
    ...
```

---

## Examples

### 1) Edge cases first
```python
def max_subarray(nums: list[int]) -> int:
    if not nums:
        return 0
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

### 2) Extract helper
```python
def num_islands(grid):
    if not grid:
        return 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return
        if grid[r][c] != "1":
            return
        grid[r][c] = "0"
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
```

### 3) LeetCode Solution class
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
```

### 4) Constants not magic numbers
```python
MOD = 10**9 + 7
INF = float("inf")

def min_path(grid):
    ...
```

### 5) Return type consistency
```python
def search(nums, target):
    # always return int index OR -1, not None sometimes
    ...
    return -1
```

---

## C++ / Java compare
C++ splits .h/.cpp; Java uses classes.  
Python interviews: **flat functions** or **Solution class** — match LeetCode style.

---

## DSA use cases
- Separate parse / solve / print (competitive)
- BFS/DFS helpers inside main function
- Pure functions easier to test mentally
- Recursion: base case at top

---

## 3 LeetCode-style examples

### Example A — Clean two pointers
```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Example B — Separate build graph + traverse
```python
from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indeg[course] += 1

    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    taken = 0
    while q:
        node = q.popleft()
        taken += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return taken == numCourses
```

### Example C — Recursive with clear base
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

---

## 1) Summary
- Name things clearly; handle edges first
- Helpers OK for DFS/BFS inner logic
- Match LeetCode `Solution` when needed
- Same return type always; avoid side-effect surprises

## 2) Common interview questions
1. How structure a 30-minute solution?
2. Helper function vs nested — when?
3. Type hints required?
4. How long should a function be?
5. Global variables — avoid?

## 3) Common mistakes
- Single-letter names everywhere (except i, j in loops)
- No empty input check
- Mutating input without mentioning
- Mixed return types (None vs -1)
- Dead code left from debugging

## 4) Practice problems (Easy → Hard)
1. **Easy:** Rewrite messy code with good variable names.
2. **Easy:** Add edge case handling to max of list function.
3. **Medium:** Split graph BFS into build_graph + bfs functions.
4. **Medium:** Write LeetCode-style class for valid anagram.
5. **Harder:** Refactor 80-line solution into 3 readable functions.

## 5) Mini quiz
1. First lines of a good DSA function?
2. LeetCode method signature example?
3. Why avoid global state?
4. dfs as nested vs separate?
5. INF constant why?

---

## Homework
- Refactor one old solution for readability
- Mark Topic 34 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 35
