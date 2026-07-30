# DAY 1 — Python Basics for DSA

**Goal:** type Python fast in interviews (only what DSA needs)  
**Time:** 60–90 min  
**Next:** `../Day01_02_Arrays/Day01_problems.py`

---

## Study order today
1. Read this README (10 min)
2. Run and play: `Day01_python_cheatsheet.py` (15 min)
3. Solve: `Day01_warmup.py` (20 min)
4. Solve: `Day01_drills.py` (30–40 min)
5. Check solutions only after trying

---

## 1) Structures you must know

| Tool | Use in DSA | Example |
|------|------------|---------|
| `list` | array | `a = [1, 2, 3]` |
| `dict` | hash map | `freq[x] = freq.get(x, 0) + 1` |
| `set` | unique / seen | `if x in seen:` |
| `str` | text problems | `s.lower()`, `s[i]` |
| `tuple` | dict key / pair | `key = (a, b)` |
| `deque` | queue / popleft | `from collections import deque` |

---

## 2) Complexity (say in interview)

| Action | Time |
|--------|------|
| `list[i]` access | O(1) |
| scan whole list | O(n) |
| `dict` / `set` add/check (avg) | O(1) |
| `arr.sort()` / `sorted(arr)` | O(n log n) |
| string concat in loop (`s += ch`) | avoid (slow) → use list then `"".join` |

**Space words**
- O(1) = few variables only  
- O(n) = dict/set/list of size n  

---

## 3) Code patterns you will type every day

### Loop with index
```python
for i, x in enumerate(arr):
    ...
```

### Frequency map
```python
from collections import Counter
freq = Counter(arr)
# or
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

### Seen set
```python
seen = set()
if x in seen: ...
seen.add(x)
```

### Two pointers
```python
l, r = 0, len(arr) - 1
while l < r:
    ...
    l += 1
    r -= 1
```

### Build answer string safely
```python
parts = []
parts.append("a")
return "".join(parts)
```

### Sort
```python
arr.sort()                 # in-place
b = sorted(arr)            # new list
b = sorted(arr, reverse=True)
```

### Useful builtins
```python
len(arr), min(arr), max(arr), sum(arr)
abs(x), float("inf"), float("-inf")
```

---

## 4) Interview speaking habit
1. Clarify input/output  
2. One example  
3. Approach  
4. Code  
5. **Time + Space**  
6. Edge cases (empty, 1 element, duplicates, negatives)

---

## Files
| File | Purpose |
|------|---------|
| `Day01_python_cheatsheet.py` | run & learn patterns |
| `Day01_warmup.py` | first practice |
| `Day01_warmup_solutions.py` | answers |
| `Day01_drills.py` | DSA Python muscle |
| `Day01_drills_solutions.py` | answers |
