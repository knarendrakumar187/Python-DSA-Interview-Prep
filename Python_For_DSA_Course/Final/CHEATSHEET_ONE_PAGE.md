# Python DSA — One-Page Cheat Sheet

## Imports (copy-paste block)
```python
from collections import Counter, defaultdict, deque
import heapq, bisect
from itertools import combinations, permutations, accumulate
INF = float("inf")
```

## Data structures — pick fast
| Need | Use | Avoid |
|------|-----|-------|
| Queue / BFS | `deque` | `list.pop(0)` |
| Frequency | `Counter` / `dict` | scan list each time |
| Graph neighbors | `defaultdict(list)` | — |
| Lookup / visited | `set`, `dict` | `x in big_list` |
| Min / top-k | `heapq` | sort whole list repeatedly |
| Sorted search | `bisect` | linear scan on static data |

## Complexities (Python)
| Op | Time |
|----|------|
| `list[i]`, append, pop() | O(1)* |
| `list.pop(0)`, insert(0) | O(n) |
| `x in list` | O(n) |
| `x in set/dict` | O(1) avg |
| `sort(n)` | O(n log n) |
| `heappush/pop` | O(log n) |
| `bisect` | O(log n) |

## Core patterns
**Two pointers:** `left, right = 0, len-1` — sorted arrays, palindrome  
**Sliding window:** expand `right`, shrink `left` until valid  
**Prefix sum:** `pref[i+1]-pref[j]` = sum j..i  
**Hash map:** `seen[x]=i`, `Counter`, complement `target-x`  
**BFS:** `deque`, `popleft`, visited set  
**DFS:** recursion or stack, mark visited  
**Heap:** min-heap; max = negate; `nlargest(k,...)`  
**Binary search:** `lo, hi`, `mid`, update lo/hi  
**DP 1D:** `prev2, prev1, cur` rolling  

## Must-know one-liners
```python
a, b = b, a                                    # swap
"".join(chars)                                 # build string
sorted(s) == sorted(t)                         # anagram
len(nums) != len(set(nums))                    # duplicate
max(nums, key=len)                             # custom max
sorted(items, key=lambda x: x[1])               # sort by field
heapq.nlargest(k, nums)                        # top k
bisect.bisect_left(arr, x)                     # lower bound
for i, x in enumerate(nums): ...               # index+value
for a, b in zip(a, b): ...                     # parallel walk
any(...), all(...)                             # boolean checks
```

## Interview flow
1. Clarify → 2. Brute force + Big O → 3. Optimize → 4. Code → 5. Test edges → 6. State time/space

## Edge cases checklist
`[]`, `[x]`, all same, negatives, duplicates, sorted?, overflow (use `INF`)

## Fast I/O (judges only)
```python
import sys
input = sys.stdin.readline
print(*ans)
```

---
*Print this page. Review before every mock interview.*
