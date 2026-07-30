# Python Basics for Interviews (Simple)

## Must-know structures
| Tool | Use |
|------|-----|
| `list` | ordered values |
| `dict` | key → value (hash map) |
| `set` | unique values, fast check |
| `str` | text (immutable) |

## Complexity (memorize)
- dict/set average lookup: **O(1)**
- list scan/search: **O(n)**
- sorting: **O(n log n)**

## Code you will type often
```python
from collections import Counter, defaultdict, deque

for i, x in enumerate(arr):
    ...

freq = Counter(arr)
seen = set()
```

## Interview habit
Always say Time and Space after coding.

## Do now
1. Fill `warmup.py`
2. Run it until all PASS
3. Then go to `../02_Arrays/day1_problems.py`
