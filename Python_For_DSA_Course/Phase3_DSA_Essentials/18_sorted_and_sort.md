# Topic 18 — sorted() and sort()
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
Sorting is everywhere — intervals, greedy, binary search prep, top-k, anagrams.  
Python gives two tools: **`sorted()`** (new list) and **`.sort()`** (in-place).

---

## Theory (simple)

| Method | Returns | Modifies original? |
|--------|---------|-------------------|
| `sorted(lst)` | new sorted list | No |
| `lst.sort()` | `None` | Yes, in-place |

Both accept `key=` and `reverse=`.

Default sort is **stable** — equal keys keep original order.

---

## Syntax
```python
sorted(iterable, key=None, reverse=False)
lst.sort(key=None, reverse=False)
```

```python
sorted([3, 1, 2])              # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)         # by length
```

---

## Examples

### 1) Basic sort
```python
nums = [3, 1, 4, 1, 5]
print(sorted(nums))   # [1, 1, 3, 4, 5]
print(nums)           # [3, 1, 4, 1, 5] unchanged

nums.sort()
print(nums)           # [1, 1, 3, 4, 5]
```

### 2) Sort strings
```python
print(sorted("python"))  # ['h', 'n', 'o', 'p', 't', 'y']
print("".join(sorted("cba")))  # "abc" — anagram check
```

### 3) Sort with key
```python
pairs = [(1, 3), (2, 1), (3, 2)]
print(sorted(pairs, key=lambda p: p[1]))
```

### 4) Sort multiple keys (tuple trick)
```python
# sort by age asc, then name asc
people = [("Bob", 30), ("Ann", 30), ("Cal", 25)]
people.sort(key=lambda p: (p[1], p[0]))
print(people)
```

---

## C++ / Java compare

**C++**
```cpp
sort(v.begin(), v.end());                    // ascending
sort(v.begin(), v.end(), greater<int>());    // descending
```

**Java**
```java
Arrays.sort(arr);
Collections.sort(list, Comparator.comparingInt(x -> x));
```

**Python** — no separate comparator class needed:
```python
sorted(arr, key=lambda x: x, reverse=True)
```

---

## DSA use cases
- Sort intervals before merging
- Sort by frequency (with Counter)
- Sort coordinates for sweep line
- Anagram: `sorted(s) == sorted(t)`
- Greedy: sort by end time, ratio, distance

---

## 3 LeetCode-style examples

### Example A — Valid anagram
```python
def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram"))  # True
```

### Example B — Merge intervals
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s, e])
    return res
```

### Example C — Largest number (custom sort)
```python
def largest_number(nums):
    strs = list(map(str, nums))
    strs.sort(key=lambda x: x * 10, reverse=True)
    return "".join(strs).lstrip("0") or "0"

print(largest_number([10, 2]))  # "210"
```

---

## 1) Summary
- `sorted()` → new list; `.sort()` → in-place, returns None
- Use `key=` for custom order; `reverse=True` for descending
- Python sort is Timsort: O(n log n), stable
- Strings sort lexicographically; use `key=int` for numeric strings

## 2) Common interview questions
1. Difference between `sort()` and `sorted()`?
2. What does `lst.sort()` return?
3. How to sort dict by values?
4. Is Python sort stable?
5. Time complexity of sorting in Python?

## 3) Common mistakes
- `x = lst.sort()` then using x (x is None!)
- Sorting list of lists without key — wrong order
- Forgetting strings sort as chars: `sorted("10")` → `['0','1']`
- Mutating list while sorting (avoid)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Sort a list of integers ascending and descending.
2. **Easy:** Check if two strings are anagrams using sorted.
3. **Medium:** Sort list of `[name, score]` by score descending.
4. **Medium:** Given intervals, merge after sorting by start.
5. **Harder:** Sort colors (Dutch flag) — know when sort vs two pointers.

## 5) Mini quiz
1. What does `[3,1,2].sort()` return?
2. `sorted("321")` = ?
3. How to sort by second element of tuples?
4. Stable sort means?
5. Complexity of `sorted(n items)`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 18 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 19
