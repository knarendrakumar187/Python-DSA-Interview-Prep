# Topic 23 — Counter (collections)
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
**Frequency counting** is core — anagrams, top-k frequent, sliding window character counts, majority element.  
`Counter` is a dict subclass built for counting fast.

---

## Theory (simple)
`Counter(iterable)` counts how many times each item appears.

```text
  "aab"  →  Counter({'a': 2, 'b': 1})
```

Missing keys return **0** (not KeyError).

---

## Syntax
```python
from collections import Counter

c = Counter("hello")
c = Counter([1, 1, 2, 3])
c["z"]          # 0 if missing
c.most_common(2)  # top 2 [(item, count), ...]
c.update("ll")    # add more
```

| Method | Purpose |
|--------|---------|
| `most_common(n)` | n highest counts |
| `elements()` | iterator repeating items |
| `subtract()` | decrease counts |
| `+`, `-` | combine counters (min 0) |

---

## Examples

### 1) Basic count
```python
from collections import Counter

c = Counter("banana")
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})
print(c["a"], c["x"])  # 3 0
```

### 2) most_common
```python
nums = [1, 1, 1, 2, 2, 3]
c = Counter(nums)
print(c.most_common(2))  # [(1, 3), (2, 2)]
```

### 3) Anagram check
```python
def is_anagram(s, t):
    return Counter(s) == Counter(t)

print(is_anagram("listen", "silent"))  # True
```

### 4) Manual vs Counter
```python
# manual
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Counter — one line
freq = Counter(s)
```

---

## C++ / Java compare

**C++** — `unordered_map` manual:
```cpp
map<char,int> freq;
freq[c]++;
```

**Java**
```java
Map<Character, Integer> freq = new HashMap<>();
freq.merge(c, 1, Integer::sum);
```

**Python**
```python
from collections import Counter
freq = Counter(s)
```

---

## DSA use cases
- Anagram / permutation problems
- Top k frequent elements
- Sliding window fixed size — Counter on window
- Ransom note / magazine characters
- Majority element (> n/2) via most_common

---

## 3 LeetCode-style examples

### Example A — Valid anagram
```python
from collections import Counter

def is_anagram(s, t):
    return len(s) == len(t) and Counter(s) == Counter(t)
```

### Example B — Top K frequent
```python
def top_k_frequent(nums, k):
    return [x for x, _ in Counter(nums).most_common(k)]

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]
```

### Example C — Ransom note
```python
def can_construct(ransom, magazine):
    need = Counter(ransom)
    have = Counter(magazine)
    for ch, cnt in need.items():
        if have[ch] < cnt:
            return False
    return True

print(can_construct("aa", "aab"))  # True
```

---

## 1) Summary
- `Counter(it)` builds frequency map
- Missing key → 0
- `most_common(k)` for top-k frequent
- Compare two Counters for anagrams

## 2) Common interview questions
1. Counter vs dict with manual count?
2. Time to build Counter of n items? O(n)
3. How to get all chars with count 1?
4. Can Counter count lists? Yes if hashable items.
5. Counter subtract use case?

## 3) Common mistakes
- Forgetting import: `from collections import Counter`
- Using Counter when you need insertion order only — use dict
- `c["missing"]` returns 0 — can hide bugs (check membership if needed)
- Comparing anagrams with sort only — Counter is O(n)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Count letters in a word; print most common letter.
2. **Easy:** Check if two strings are anagrams.
3. **Medium:** First unique character in string using Counter.
4. **Medium:** Find all duplicates in array (count > 1).
5. **Harder:** Minimum window substring — Counter for window vs need.

## 5) Mini quiz
1. `Counter("aaa")["a"]` = ?
2. `Counter("aaa")["b"]` = ?
3. `most_common(1)` returns type?
4. Are Counter keys ordered (3.7+)? insertion order of first seen
5. `Counter("ab") + Counter("bc")` gives?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 23 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 24
