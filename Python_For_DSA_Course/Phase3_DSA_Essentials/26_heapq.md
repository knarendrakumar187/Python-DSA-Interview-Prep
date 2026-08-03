# Topic 26 — heapq (min-heap)
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
Top-k elements, merge k sorted lists, Dijkstra, median from stream — all need a **heap**.  
Python's `heapq` module implements a **min-heap** on a regular list.

---

## Theory (simple)
A **min-heap** always gives the **smallest** item first.

```text
       1
      / \
     3   2
    / \
   5   4

  heap[0] is always minimum
```

Python has **min-heap only**. For max-heap, negate numbers or use inverted keys.

---

## Syntax
```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
print(heapq.heappop(h))  # 1

heapq.heapify(lst)           # O(n) build heap from list
smallest = heapq.nsmallest(k, nums)
largest = heapq.nlargest(k, nums, key=...)
```

| Function | Purpose |
|----------|---------|
| `heappush(h, x)` | add item |
| `heappop(h)` | remove & return min |
| `heapify(h)` | turn list into heap in-place |
| `heappushpop(h, x)` | push then pop — faster |
| `nsmallest(k, it)` | k smallest without full sort |

---

## Examples

### 1) Basic min-heap
```python
import heapq

h = [5, 3, 8, 1]
heapq.heapify(h)
print(heapq.heappop(h))  # 1
heapq.heappush(h, 2)
print(h[0])              # 2 — peek min
```

### 2) Max-heap trick (negate)
```python
import heapq

nums = [3, 1, 4, 1, 5]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
print(-heapq.heappop(max_heap))  # 5
```

### 3) Top k frequent — nlargest
```python
from collections import Counter
import heapq

nums = [1,1,1,2,2,3]
top = heapq.nlargest(2, Counter(nums).items(), key=lambda x: x[1])
print(top)  # [(1, 3), (2, 2)]
```

### 4) Merge k sorted lists (concept)
```python
import heapq

def merge_k(lists):
    h = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(h, (lst[0], i, 0))
    out = []
    while h:
        val, li, idx = heapq.heappop(h)
        out.append(val)
        if idx + 1 < len(lists[li]):
            heapq.heappush(h, (lists[li][idx+1], li, idx+1))
    return out
```

---

## C++ / Java compare

**C++**
```cpp
priority_queue<int> maxHeap;  // default max
priority_queue<int, vector<int>, greater<int>> minHeap;
```

**Java**
```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
```

**Python** — min-heap only; negate for max:
```python
heapq.heappush(h, x)
heapq.heappop(h)
```

---

## DSA use cases
- Kth largest / smallest element
- Merge k sorted arrays/lists
- Dijkstra shortest path (priority queue)
- Running median (two heaps)
- Task scheduler / greedy with deadlines

---

## 3 LeetCode-style examples

### Example A — Kth largest element
```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(find_kth_largest([3,2,1,5,6,4], 2))  # 5
```

### Example B — K closest points to origin
```python
import heapq

def k_closest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)

print(k_closest([[1,3],[-2,2]], 1))
```

### Example C — Last stone weight
```python
import heapq

def last_stone_weight(stones):
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) > 1:
        a = -heapq.heappop(h)
        b = -heapq.heappop(h)
        if a != b:
            heapq.heappush(h, -(a - b))
    return -h[0] if h else 0

print(last_stone_weight([2,7,4,1,8,1]))  # 1
```

---

## 1) Summary
- `heapq` = min-heap on a list
- `heap[0]` is minimum; `heappop` removes it
- Max-heap: store `-x`, pop and negate
- `nlargest`/`nsmallest` for top-k without full sort

## 2) Common interview questions
1. Min vs max heap in Python?
2. Complexity of heappush/heappop? O(log n)
3. heapify vs sorting?
4. Tuple comparison in heap?
5. Kth largest — heap vs quickselect?

## 3) Common mistakes
- Expecting max-heap by default
- Comparing mixed types in heap (TypeError)
- Forgetting heap property after manual list edits
- Using sort O(n log n) when nsmallest O(n log k) is enough

## 4) Practice problems (Easy → Hard)
1. **Easy:** Push/pop 5 numbers; print in sorted order using heap only.
2. **Easy:** Find minimum of stream using heap (always peek h[0]).
3. **Medium:** Kth largest element in array.
4. **Medium:** Merge two sorted lists using heap (or two pointers).
5. **Harder:** Find median from data stream (two heaps pattern).

## 5) Mini quiz
1. After heapify `[3,1,2]`, heappop = ?
2. How to simulate max-heap?
3. `heappush(h, (1,'a')); heappush(h, (1,'b'))` — which pops first?
4. nsmallest(3, range(100)) complexity roughly?
5. Module name?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 26 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 27
