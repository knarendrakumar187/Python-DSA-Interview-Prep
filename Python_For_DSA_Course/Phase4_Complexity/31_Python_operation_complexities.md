# Topic 31 — Python Operation Complexities
**Phase 4 · Complexity · DSA relevance: ★★★★★**

## Why this matters for DSA
Same algorithm in C++ vs Python can **TLE** (Time Limit Exceeded) if you use slow Python operations — like `list.pop(0)` or `x in list`.  
Know the **real costs** of list, dict, set, str in Python.

---

## Theory (simple)
Average-case unless noted. n = current size.

### list
| Operation | Complexity |
|-----------|------------|
| `append`, `pop()` end | O(1) amortized |
| `pop(0)`, `insert(0, x)` | O(n) |
| `x in lst` | O(n) |
| slice `lst[i:j]` | O(j-i) |
| `lst.sort()` | O(n log n) |
| index access `lst[i]` | O(1) |

### dict / set
| Operation | Complexity |
|-----------|------------|
| get/set/del, `in` | O(1) average |
| iterate all | O(n) |

### str
| Operation | Complexity |
|-----------|------------|
| `s[i]` | O(1) |
| `s + t` | O(len(s)+len(t)) — new string |
| `s in t` | O(n*m) worst |
| `"".join(parts)` | O(total chars) — preferred |

### deque
| append, pop both ends | O(1) |

### heapq
| push, pop | O(log n) |

---

## Syntax (fast patterns)
```python
# FAST
from collections import deque
q = deque(); q.append(x); q.popleft()

seen = set()
if x in seen: ...

parts = []; parts.append(ch); "".join(parts)

# SLOW for large n
q = []; q.pop(0)
if x in big_list: ...
s = ""; s += ch  # in loop
```

---

## Examples

### 1) list.pop(0) trap
```python
# O(n²) total for n pops from front
q = list(range(100000))
while q:
    q.pop(0)  # BAD

# O(n) total
from collections import deque
q = deque(range(100000))
while q:
    q.popleft()  # GOOD
```

### 2) membership — set vs list
```python
nums = list(range(10**6))
target = 999999
# x in nums  → O(n) — slow

s = set(nums)
# target in s → O(1) — fast
```

### 3) string building
```python
# BAD O(n²)
s = ""
for c in "abcdef":
    s += c

# GOOD O(n)
s = "".join(list("abcdef"))
# or
chars = []
for c in "abcdef":
    chars.append(c)
s = "".join(chars)
```

### 4) dict vs list for lookup table
```python
# index map — O(1) lookup
idx = {v: i for i, v in enumerate(arr)}
# arr.index(v)  # O(n) — avoid in loops
```

---

## C++ / Java compare
C++ `vector::pop_front` doesn't exist — use deque.  
Java `ArrayList.remove(0)` is O(n) — same as Python list.  
Python interviews punish **`in list`** and **front pops** heavily.

---

## DSA use cases
- Visited set in BFS — must be set
- Queue — must be deque
- Frequency — dict or Counter
- Sorted static array search — bisect O(log n)
- Avoid sorting inside loop — becomes O(n² log n)

---

## 3 LeetCode-style examples

### Example A — Two Sum needs dict not nested loop
```python
# O(n²) — TLE on large n
def slow(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

# O(n) — correct approach
def fast(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target-x in seen:
            return [seen[target-x], i]
        seen[x] = i
```

### Example B — Valid anagram — Counter O(n)
```python
from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
# sort(s)==sort(t) is O(n log n)
```

### Example C — Sliding window with deque not list
```python
from collections import deque
def max_window(nums, k):
    dq = deque()
    ...
    # popleft O(1) each step → O(n) total
```

---

## 1) Summary
- list front insert/pop — O(n) — use deque
- set/dict `in` — O(1) average
- list `in` — O(n)
- join strings, don't += in loops
- sort once, not every iteration

## 2) Common interview questions
1. Complexity of list.pop(0)?
2. Why set for visited in BFS?
3. dict vs list for lookup?
4. Amortized O(1) list append?
5. str concatenation in loop cost?

## 3) Common mistakes
- BFS with list.pop(0)
- Checking membership in list inside loop
- Using arr.index in loop
- Sorting inside for loop
- Building huge list when generator enough

## 4) Practice problems (Easy → Hard)
1. **Easy:** Explain why `x in my_list` is slow for 10⁶ items.
2. **Easy:** Rewrite queue using deque.
3. **Medium:** Spot O(n²) in code using nested loop + list.remove.
4. **Medium:** Choose structure for phone directory: lookup by name.
5. **Harder:** Estimate complexity of: sort + for each element bisect on another list.

## 5) Mini quiz
1. deque.popleft() = ?
2. set.add average = ?
3. list.insert(0,x) = ?
4. "".join vs += in loop?
5. heapq.heappush = ?

---

## Homework
- Memorize list vs dict vs deque table
- Fix one slow pattern in your old code
- Mark Topic 31 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 32
