# Topic 13 — Dictionaries
**Phase 2 · Collections · DSA relevance: ★★★★★**

## Why this matters for DSA
Dicts are **hash maps** — O(1) average get/set.  
Two Sum, frequency count, graph adjacency lists, memoization — all dicts.

---

## Theory (simple)
A **dictionary** maps **keys** to **values**.

```python
d = {"a": 1, "b": 2}
d = dict()
d[key] = value
x = d.get(key, default)
```

Keys must be **hashable** (str, int, tuple of hashables — not list).

---

## Syntax

```python
d = {}
d = {"name": "Ali", "score": 90}
d["name"]           # KeyError if missing
d.get("name")       # None if missing
d.get("x", 0)       # default 0
d["new"] = 5
del d["new"]
key in d            # membership on keys
d.keys(), d.values(), d.items()

for k in d:
    ...
for k, v in d.items():
    ...
```

### Frequency pattern (memorize)
```python
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

---

## Compare with C++/Java

| Python | C++ | Java |
|--------|-----|------|
| `dict` | `unordered_map` | `HashMap` |
| `d[key]` | `m[key]` | `map.get(key)` |
| `.get(k, default)` | `m.count(k)? m[k]: def` | `getOrDefault` |

---

## Examples

### 1) Character frequency
```python
s = "hello"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)   # {'h':1, 'e':1, 'l':2, 'o':1}
```

### 2) Graph as adjacency list
```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
for nei in graph[2]:
    print(nei)
```

### 3) Memoization skeleton
```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(30))
```

### 4) Group by key
```python
pairs = [("a", 1), ("b", 2), ("a", 3)]
groups = {}
for k, v in pairs:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)
print(groups)   # {'a': [1,3], 'b': [2]}
```

---

## DSA use cases
- Two sum: `{value: index}`
- Frequency / anagram maps
- Graph: `node -> neighbors`
- DP memo: `(i, j) -> result` or string key
- Prefix sum + hash map for subarray sum

---

## 3 LeetCode-style examples

### Example A — Two Sum (classic dict)
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
```

### Example B — First character not repeating
```python
def first_unique(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

print(first_unique("loveleetcode"))   # 2
```

### Example C — Subarray sum equals K (prefix + dict)
```python
def subarray_sum(nums, k):
    count = 0
    prefix = 0
    freq = {0: 1}
    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count

print(subarray_sum([1, 1, 1], 2))   # 2
```

---

## 1) Summary
- Dict = key → value hash map; O(1) average ops
- Safe read: `.get(key, default)`; write: `d[k] = v`
- Frequency: `freq[x] = freq.get(x, 0) + 1`
- Loop pairs: `for k, v in d.items()`

## 2) Common interview questions
1. What can be dict keys?
2. `d[k]` vs `d.get(k)`?
3. How implement Two Sum with dict?
4. Dict time complexity for insert/lookup?
5. How represent graph with dict?

## 3) Common mistakes
- Using list as key (unhashable)
- `d[k]` when key might missing → KeyError
- Forgetting default in `.get` for counting
- Modifying dict size while iterating (use list copy of keys)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Count frequency of each element in list.
2. **Easy:** Two sum return indices (dict).
3. **Medium:** Group anagrams (sorted string or freq as key).
4. **Medium:** Longest substring without repeating (set + dict last index).
5. **Harder:** Subarray sum equals k (prefix hash map).

## 5) Mini quiz
1. What does `{}` create — set or dict?
2. Return value of `d.get("missing")`?
3. Are dict keys ordered (Python 3.7+)?
4. Can tuple `(1,2)` be a key?
5. Pattern to increment count for key `x`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/13_dicts_practice.py` (create file)
- Mark Topic 13 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 14
