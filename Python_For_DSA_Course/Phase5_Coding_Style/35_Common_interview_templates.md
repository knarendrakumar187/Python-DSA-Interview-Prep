# Topic 35 — Common Interview Templates
**Phase 5 · Coding Style · DSA relevance: ★★★★★**

## Why this matters for DSA
Most interview problems match **patterns**. Memorize templates — then adapt small parts.  
This topic collects the highest-frequency Python templates for DSA interviews.

---

## Theory (simple)
Learn template → recognize pattern → tweak 5–10 lines.

Patterns covered:
1. Two pointers
2. Sliding window
3. Prefix sum
4. Hash map
5. Binary search
6. BFS / DFS
7. Heap top-k
8. Monotonic stack
9. DP 1D
10. Union-Find (basic)

---

## Syntax — Template library

### 1) Two pointers
```python
def two_pointer_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2) Sliding window (variable size)
```python
def sliding_window(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        seen[ch] = seen.get(ch, 0) + 1
        while seen[ch] > 1:  # shrink until valid
            seen[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

### 3) Prefix sum
```python
def prefix_sum(nums):
    pref = [0]
    for x in nums:
        pref.append(pref[-1] + x)
    # sum nums[l..r] = pref[r+1] - pref[l]
    return pref
```

### 4) Hash map frequency
```python
from collections import Counter

def freq_pattern(nums):
    cnt = Counter(nums)
    for x in nums:
        if cnt[x] == something:
            ...
```

### 5) Binary search
```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### 6) BFS
```python
from collections import deque

def bfs(start, graph):
    q = deque([start])
    dist = {start: 0}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in dist:
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist
```

### 7) DFS (graph)
```python
def dfs(node, graph, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, graph, visited)
```

### 8) Heap top-k
```python
import heapq

def top_k(nums, k):
    return heapq.nlargest(k, nums)
```

### 9) Monotonic stack (next greater)
```python
def next_greater(nums):
    stack = []
    res = [-1] * len(nums)
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            j = stack.pop()
            res[j] = x
        stack.append(i)
    return res
```

### 10) DP 1D (House Robber style)
```python
def rob(nums):
    if not nums:
        return 0
    prev2 = prev1 = 0
    for x in nums:
        cur = max(prev1, prev2 + x)
        prev2, prev1 = prev1, cur
    return prev1
```

---

## C++ / Java compare
Same patterns — syntax differs. Python wins on brevity for hash map + heap.

---

## DSA use cases
| Pattern | Example problems |
|---------|------------------|
| Two pointers | Two Sum II, container water |
| Sliding window | Longest substring, min window |
| Prefix sum | Range sum, subarray sum equals k |
| Hash map | Two Sum, anagram |
| BFS | Shortest path, islands |
| Heap | Kth largest, merge k lists |
| BS | Search insert, rotated array |
| DP | Climbing stairs, rob |

---

## 3 LeetCode-style examples

### Example A — Two Sum (hash map template)
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
```

### Example B — Level order BFS (tree)
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    q = deque([root])
    out = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out
```

### Example C — Climbing stairs DP
```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

---

## 1) Summary
- Recognize pattern in first 3 minutes
- Copy mental template, adapt condition
- Combine patterns (prefix + hash, BFS + visited set)
- Practice writing each template from memory

## 2) Common interview questions
1. Name 5 common patterns?
2. Two pointers vs sliding window?
3. BFS vs DFS when?
4. When heap beats sort?
5. DP vs recursion?

## 3) Common mistakes
- Wrong pattern forced on problem
- Forgetting visited set in BFS/DFS
- Off-by-one in sliding window
- Binary search infinite loop (lo/hi update)
- DP wrong base case

## 4) Practice problems (Easy → Hard)
1. **Easy:** Write two-pointer palindrome check from template.
2. **Easy:** Climbing stairs from DP template.
3. **Medium:** Longest substring without repeat — sliding window.
4. **Medium:** Number of islands — BFS template.
5. **Harder:** Daily temperatures — monotonic stack template.

## 5) Mini quiz
1. BFS uses which collection?
2. Prefix sum range formula?
3. Two Sum pattern name?
4. nlargest uses which module?
5. monotonic stack solves "next ___" problems?

---

## Homework
- Write all 10 templates from memory (no peeking)
- Solve 1 problem per pattern on LeetCode
- Mark Topic 35 done in `PROGRESS.md`
- Review `Final/` revision pack
- When course complete, say **`Next`** for mock interview help
