# Topic 24 — defaultdict (collections)
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
Graph adjacency lists, grouping items, nested maps — you often need `dict[key].append(x)` without checking if key exists.  
**`defaultdict`** auto-creates missing keys with a default factory.

---

## Theory (simple)
Normal dict:
```python
d = {}
d["a"].append(1)  # KeyError!
```

`defaultdict(list)`:
```python
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)  # works — "a" starts as []
```

---

## Syntax
```python
from collections import defaultdict

dd = defaultdict(list)      # default []
dd = defaultdict(int)       # default 0
dd = defaultdict(set)       # default set()
dd = defaultdict(dict)        # default {}
```

Common factories: `list`, `int`, `set`, `bool`.

---

## Examples

### 1) Group by key
```python
from collections import defaultdict

pairs = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
groups = defaultdict(list)
for k, v in pairs:
    groups[k].append(v)
print(dict(groups))
# {'fruit': ['apple', 'banana'], 'veg': ['carrot']}
```

### 2) Count without .get
```python
freq = defaultdict(int)
for ch in "hello":
    freq[ch] += 1
print(dict(freq))
```

### 3) Graph adjacency list
```python
graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected
print(dict(graph))
```

### 4) defaultdict vs dict.get
```python
# dict
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

# defaultdict
freq = defaultdict(int)
for x in nums:
    freq[x] += 1
```

---

## C++ / Java compare

**C++**
```cpp
map<int, vector<int>> graph;
graph[u].push_back(v);  // creates empty vector if missing
```

**Java**
```java
Map<Integer, List<Integer>> graph = new HashMap<>();
graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
```

**Python**
```python
graph = defaultdict(list)
graph[u].append(v)
```

---

## DSA use cases
- Graph BFS/DFS adjacency list
- Group anagrams by sorted string key
- Trie-like nested defaultdict for prefix trees
- Union-find alternative structures sometimes
- Multi-map: key → list of indices

---

## 3 LeetCode-style examples

### Example A — Group anagrams
```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
```

### Example B — Build graph for course schedule
```python
def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1
    # BFS topological sort follows...
    return True  # simplified stub
```

### Example C — Nested map for path prefix
```python
def insert_word(root, word):
    for ch in word:
        root = root[ch]  # defaultdict creates next level
    root["#"] = True

root = defaultdict(lambda: defaultdict(dict))
# Often use nested defaultdict(lambda: defaultdict(...)) for trie
```

---

## 1) Summary
- `defaultdict(factory)` auto-inits missing keys
- `defaultdict(list)` + `.append` — graph/group pattern
- `defaultdict(int)` — frequency counting
- Convert to normal dict: `dict(dd)` when done

## 2) Common interview questions
1. defaultdict vs dict with get?
2. What factory for counting? `int`
3. Can default be custom function? Yes: `defaultdict(lambda: -1)`
4. KeyError on defaultdict? Only if you read missing key without factory applying — rare
5. Memory vs regular dict?

## 3) Common mistakes
- Using `defaultdict(list)` then assigning `d[k] = x` overwriting list
- Forgetting `from collections import defaultdict`
- Nested defaultdict lambda recursion for trie — syntax tricky
- Expecting defaultdict to delete key when list becomes empty

## 4) Practice problems (Easy → Hard)
1. **Easy:** Count word frequencies in a sentence with defaultdict(int).
2. **Easy:** Group numbers by even/odd using defaultdict(list).
3. **Medium:** Build undirected graph from edge list; print neighbors of node 1.
4. **Medium:** Group strings that are anagrams.
5. **Harder:** Implement trie insert/search with nested defaultdict.

## 5) Mini quiz
1. `defaultdict(int)["x"]` after access = ?
2. Factory for set of neighbors?
3. Does defaultdict(list) share one list for all keys? No — new list each time
4. Convert to plain dict?
5. `defaultdict(list)` vs `dict` of lists — main benefit?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 24 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 25
