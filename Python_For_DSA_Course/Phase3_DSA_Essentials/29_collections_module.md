# Topic 29 — collections Module Overview
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
The **`collections`** module bundles the data structures interviews expect — beyond plain dict/list.  
You already learned Counter, defaultdict, deque; this topic ties them together plus **OrderedDict**, **namedtuple**, and when to use each.

---

## Theory (simple)
| Type | One-line purpose |
|------|------------------|
| `Counter` | count frequencies |
| `defaultdict` | dict with auto default |
| `deque` | double-ended queue |
| `OrderedDict` | dict + move-to-end (LRU ideas) |
| `namedtuple` | lightweight struct with fields |
| `ChainMap` | stack of dicts (scopes) |

For modern Python (3.7+), regular `dict` keeps insertion order — OrderedDict is mainly for **move_to_end** LRU patterns.

---

## Syntax
```python
from collections import (
    Counter, defaultdict, deque,
    OrderedDict, namedtuple, ChainMap
)

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)

od = OrderedDict()
od["a"] = 1
od.move_to_end("a")  # LRU touch
```

---

## Examples

### 1) Counter — recap
```python
from collections import Counter
c = Counter("aabbc")
print(c.most_common(1))  # [('a', 2)]
```

### 2) defaultdict — recap
```python
from collections import defaultdict
g = defaultdict(list)
g[1].append(2)
```

### 3) deque — recap
```python
from collections import deque
q = deque([1, 2])
q.appendleft(0)
```

### 4) namedtuple — clean node/edge records
```python
from collections import namedtuple

Edge = namedtuple("Edge", ["u", "v", "w"])
edges = [Edge(1, 2, 10), Edge(2, 3, 5)]
for e in edges:
    print(e.u, e.v, e.w)
```

### 5) OrderedDict — LRU cache sketch
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)  # evict oldest
```

---

## C++ / Java compare

**C++** — separate containers: `unordered_map`, `queue`, `deque`, struct

**Java** — `HashMap`, `ArrayDeque`, `LinkedHashMap` (LRU)

**Python collections** — one import hub for DSA patterns

---

## DSA use cases
- **Counter** — frequency, anagram
- **defaultdict** — graph, grouping
- **deque** — BFS, sliding window
- **namedtuple** — readable tuples in priority queues
- **OrderedDict** — LRU cache design question

---

## 3 LeetCode-style examples

### Example A — Group shifted strings (defaultdict)
```python
from collections import defaultdict

def group_strings(strings):
    groups = defaultdict(list)
    for s in strings:
        key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
        groups[key].append(s)
    return list(groups.values())
```

### Example B — Top K frequent (Counter + heap or bucket)
```python
from collections import Counter
import heapq

def top_k(nums, k):
    return heapq.nlargest(k, Counter(nums).items(), key=lambda x: x[1])
```

### Example C — Design hit counter (deque of timestamps)
```python
from collections import deque

class HitCounter:
    def __init__(self):
        self.q = deque()

    def hit(self, t):
        self.q.append(t)

    def getHits(self, t):
        while self.q and self.q[0] <= t - 300:
            self.q.popleft()
        return len(self.q)
```

---

## 1) Summary
- `collections` = interview toolbox beyond builtins
- Pick structure by operation: count → Counter, graph → defaultdict(list), queue → deque
- namedtuple for readable fixed fields
- OrderedDict when you need move_to_end (LRU)

## 2) Common interview questions
1. When Counter vs defaultdict(int)?
2. deque vs list for BFS?
3. dict vs OrderedDict in Python 3.7+?
4. namedtuple vs dataclass vs tuple?
5. Implement LRU — which collection helps?

## 3) Common mistakes
- Importing whole collections without names
- Using OrderedDict when plain dict enough
- defaultdict without correct factory type
- namedtuple field names as keywords (syntax error)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Use Counter to find mode (most common element).
2. **Easy:** Build adjacency list with defaultdict(list) from 5 edges.
3. **Medium:** LRU cache with OrderedDict (capacity 2).
4. **Medium:** namedtuple for Point — sort points by distance from origin.
5. **Harder:** Combine Counter + deque for sliding window anagram match.

## 5) Mini quiz
1. Three structures from collections for graph BFS?
2. Counter missing key returns?
3. deque popleft complexity?
4. namedtuple immutable?
5. OrderedDict popitem(last=False) removes?

---

## Homework
- Type all examples in this file yourself
- Review topics 23–28 and map each to one LeetCode pattern
- Solve practice 1–5
- Mark Topic 29 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 30 (Big O)
