# Top 50 Builtins & Functions for Python DSA
**One-line use for each**

| # | Name | One-line DSA use |
|---|------|------------------|
| 1 | `len(x)` | Get size of list/string/graph bounds |
| 2 | `range(n)` | Loop indices 0..n-1 |
| 3 | `enumerate(it)` | Index + value in one loop |
| 4 | `zip(a, b)` | Pair elements from two iterables |
| 5 | `sorted(x)` | New sorted list without mutating |
| 6 | `list.sort()` | Sort list in-place |
| 7 | `reversed(x)` | Iterate backwards |
| 8 | `min(x)` | Smallest element or min with key= |
| 9 | `max(x)` | Largest element or max with key= |
| 10 | `sum(x)` | Total of numbers / prefix helper |
| 11 | `any(it)` | True if at least one truthy |
| 12 | `all(it)` | True if all truthy |
| 13 | `map(f, it)` | Apply f to each (parse ints from input) |
| 14 | `filter(f, it)` | Keep items passing test |
| 15 | `list(x)` | Convert iterator to list |
| 16 | `set(x)` | Unique elements / O(1) membership |
| 17 | `dict(x)` | Build hash map |
| 18 | `tuple(x)` | Immutable key for Counter/grouping |
| 19 | `str(x)` | Convert to string for join/compare |
| 20 | `int(x)` | Parse integer from input |
| 21 | `float(x)` | Infinity: float("inf") for DP min |
| 22 | `bool(x)` | Cast to True/False |
| 23 | `type(x)` | Debug variable type |
| 24 | `isinstance(x, t)` | Type check |
| 25 | `abs(x)` | Absolute value / distance |
| 26 | `divmod(a,b)` | Quotient and remainder together |
| 27 | `pow(a,b,m)` | Fast modular exponentiation |
| 28 | `print()` | Output (LeetCode less needed) |
| 29 | `input()` | Read line in practice scripts |
| 30 | `open()` | Read file lines in contests |
| 31 | `ord(c)` | Char to ASCII code |
| 32 | `chr(n)` | ASCII to char |
| 33 | `slice` / `[i:j]` | Subarray substring extraction |
| 34 | `"".join(lst)` | Build string O(n) |
| 35 | `s.split()` | Tokenize input line |
| 36 | `x in s` | Membership test |
| 37 | `x not in s` | Negative membership |
| 38 | `lambda` | Anonymous key for sort |
| 39 | `Counter` | Frequency map (collections) |
| 40 | `defaultdict` | Auto-init dict values |
| 41 | `deque` | BFS queue O(1) both ends |
| 42 | `heapq.heappush` | Add to min-heap |
| 43 | `heapq.heappop` | Pop smallest from heap |
| 44 | `heapq.heapify` | Build heap in O(n) |
| 45 | `heapq.nlargest` | Top k without full sort |
| 46 | `bisect.bisect_left` | Lower bound in sorted list |
| 47 | `bisect.insort` | Insert keeping sorted order |
| 48 | `combinations` | Choose k items (subsets) |
| 49 | `accumulate` | Prefix sums running total |
| 50 | `sys.stdin.readline` | Fast input in judges |

### Bonus quick refs
- `float("inf")` / `float("-inf")` — init min/max in loops
- `collections.OrderedDict` — LRU move_to_end
- `itertools.permutations` — arrange k items
- `itertools.product` — Cartesian product
- `math.gcd(a,b)` — GCD for number theory

---
*Print and highlight the 15 you forget most often.*
