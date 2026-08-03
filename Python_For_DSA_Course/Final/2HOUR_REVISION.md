# 2-Hour Before-Interview Revision Guide
**Complete timed plan — follow in order**

---

## Before you start (2 min)
- [ ] Water, quiet space, cheat sheet printed
- [ ] Open `Final/CHEATSHEET_ONE_PAGE.md`
- [ ] Timer ready — **strict times below**

---

## Block 1 — Python DSA toolkit (20 min) ⏱ 0:00–0:20

### 0:00–0:05 — Imports & structures
Write from memory:
```python
from collections import Counter, defaultdict, deque
import heapq, bisect
INF = float("inf")
```
Say aloud: deque for BFS, Counter for freq, defaultdict for graph, heap for top-k.

### 0:05–0:10 — Slow vs fast
| Slow | Fast |
|------|------|
| list.pop(0) | deque.popleft |
| x in big_list | x in set |
| s += c in loop | "".join |
| sort every iteration | sort once |

### 0:10–0:15 — One-liners drill
Say what each does:
- `a, b = b, a`
- `len(nums) != len(set(nums))`
- `for i, x in enumerate(nums)`
- `heapq.nlargest(k, nums)`
- `bisect.bisect_left(arr, x)`

### 0:15–0:20 — Big O flash
O(1), O(log n), O(n), O(n log n), O(n²) — one example each aloud.

---

## Block 2 — Core templates (35 min) ⏱ 0:20–0:55

Write **skeleton only** (no full solve) for each — 3–4 min each:

### 0:20–0:24 — Hash map (Two Sum)
```python
seen = {}
for i, x in enumerate(nums):
    ...
```

### 0:24–0:28 — Two pointers (sorted pair)
```python
left, right = 0, len(nums)-1
while left < right:
    ...
```

### 0:28–0:32 — Sliding window
```python
left = 0
for right in range(len(s)):
    # expand, while invalid: shrink left
    ...
```

### 0:32–0:36 — Prefix sum
```python
pref = [0]
for x in nums: pref.append(pref[-1]+x)
# sum l..r = pref[r+1]-pref[l]
```

### 0:36–0:40 — Binary search
```python
lo, hi = 0, len(nums)-1
while lo <= hi:
    mid = (lo+hi)//2
    ...
```

### 0:40–0:45 — BFS
```python
q = deque([start])
visited = {start}
while q:
    node = q.popleft()
    ...
```

### 0:45–0:50 — DFS (recursive)
```python
def dfs(node):
    if base: return
    for nei in graph[node]:
        if nei not in visited:
            ...
```

### 0:50–0:55 — Heap top-k + DP rob
```python
heapq.nlargest(k, items, key=...)
# DP: prev2, prev1 = 0, 0; for x: cur = max(prev1, prev2+x)
```

---

## Block 3 — Pattern → problem map (15 min) ⏱ 0:55–1:10

Match problem name to pattern (say pattern first):
| Problem | Pattern |
|---------|---------|
| Two Sum | Hash map |
| Valid Parentheses | Stack |
| Best Time Buy/Sell Stock | One pass min/max |
| Longest Substring No Repeat | Sliding window |
| Number of Islands | BFS/DFS grid |
| Merge Intervals | Sort + scan |
| Course Schedule | Topo BFS |
| Kth Largest | Heap |
| Search Rotated Array | Binary search |
| House Robber | DP 1D |
| Climbing Stairs | DP fib |
| Group Anagrams | defaultdict + key |

Pick **3 weakest** — note LeetCode # from `TOP_50_LEETCODE.md`.

---

## Block 4 — Edge cases & interview script (10 min) ⏱ 1:10–1:20

### Edge checklist (say each)
- Empty input `[]`
- Single element
- All duplicates
- All negative numbers
- Already sorted / reverse sorted
- Integer overflow (use INF in Python rarely issue)

### Interview script (practice once aloud)
1. "Let me clarify input size and edge cases…"
2. "Brute force would be O(…) — I'll optimize with …"
3. Code while narrating
4. "Let me test with empty and one element…"
5. "Time O(…), space O(…)"

---

## Block 5 — Quick Q&A sprint (20 min) ⏱ 1:20–1:40

Answer **20 random** from `TOP_100_PYTHON_INTERVIEW.md` (pick #5, #12, #23, #41, #56, #73, #86, #96, etc.).

Focus categories you miss:
- [ ] collections (Counter, deque, defaultdict)
- [ ] heapq & bisect
- [ ] complexity traps
- [ ] mutable default args
- [ ] sort vs sorted

---

## Block 6 — One timed mock (20 min) ⏱ 1:40–2:00

**Pick ONE medium** (no peeking):
- Longest Substring Without Repeating Characters, OR
- Number of Islands, OR
- Top K Frequent Elements

**Rules:**
- 2 min clarify + plan
- 15 min code on paper or editor
- 3 min test + complexity

### Self-score
- [ ] Stated approach before coding
- [ ] Handled empty input
- [ ] Correct main pattern
- [ ] Stated time/space
- [ ] No list.pop(0) / no x in list in loop

---

## After 2 hours — final 5 min checklist
- [ ] Cheat sheet in bag / on desk
- [ ] Templates in muscle memory: hash, BFS, BS, sliding window
- [ ] Calm — you only need one clear solution per question

---

## Emergency cram (last 10 min only)
1. Read `CHEATSHEET_ONE_PAGE.md` twice  
2. Write BFS + hash map templates  
3. Say 5 complexities aloud  
4. Deep breath — start interview with clarify step  

---
*Good luck. After real interview, note 2 weak patterns and drill them next week.*
