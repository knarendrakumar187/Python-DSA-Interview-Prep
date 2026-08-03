# Top 100 Python DSA Interview Q&A
**Short answers — review aloud**

---

## Python basics (1–15)
1. **Mutable vs immutable?** — list/dict/set mutable; int/str/tuple immutable.
2. **Dynamic typing?** — variable type decided at runtime by value.
3. **Swap two variables?** — `a, b = b, a`
4. **Truthy values?** — empty/zero/None False; non-empty True.
5. **`is` vs `==`?** — `is` same object; `==` equal value.
6. **`None` meaning?** — no value / null.
7. **List vs tuple?** — list mutable; tuple immutable, hashable if all items hashable.
8. **Set properties?** — unique, unordered, O(1) membership.
9. **Dict key rules?** — hashable keys only (no list keys).
10. **`*args` / `**kwargs`?** — variable positional / keyword args.
11. **Default arg trap?** — never `def f(x=[])` — shared mutable default.
12. **Scope LEGB?** — Local, Enclosing, Global, Built-in.
13. **Recursion limit?** — ~1000 default; deep graphs use iterative BFS/stack.
14. **`pass` vs `continue`?** — pass noop; continue next loop iteration.
15. **`range` inclusive?** — start inclusive, stop exclusive.

## Strings & lists (16–30)
16. **Reverse string?** — `s[::-1]`
17. **Split/join?** — `s.split()`, `"".join(parts)`
18. **String immutable?** — yes; use list of chars + join to build.
19. **List slice copy?** — `lst[:]` or `list(lst)` — shallow copy.
20. **Shallow vs deep copy?** — shallow copies refs; deepcopy nested objects.
21. **List comp vs loop?** — comp faster/cleaner for map-filter style.
22. **`append` vs `extend`?** — append one item; extend many.
23. **`remove` vs `pop`?** — remove by value; pop by index.
24. **Sort strings in list?** — `sorted(words)` lexicographic.
25. **Sort nums as strings trap?** — `sorted(["10","2"])` wrong order — use `key=int`.
26. **2D list init trap?** — `[[0]*n]*m` shares rows — use comp.
27. **Index out of range?** — valid 0..len-1.
28. **Negative index?** — -1 last element.
29. **Enumerate purpose?** — index + value pairs.
30. **Zip stops when?** — shortest iterable ends.

## Functions & lambda (31–40)
31. **Lambda limits?** — single expression, no statements.
32. **When use lambda?** — short `key=` for sort/min/max.
33. **`sorted` vs `sort`?** — sorted new list; sort in-place returns None.
34. **Stable sort?** — Python yes (Timsort).
35. **`key=` meaning?** — compare key(item) not whole item.
36. **map/filter lazy?** — yes iterators in Python 3.
37. **`any` / `all` empty?** — any False, all True.
38. **`min` empty list?** — ValueError unless default=.
39. **`sum` start param?** — `sum(nums, 10)` adds 10 + total.
40. **First-class functions?** — functions are objects, pass as args.

## collections (41–55)
41. **Counter missing key?** — returns 0.
42. **most_common(k)?** — k highest (item, count) pairs.
43. **defaultdict list use?** — graph adjacency append without KeyError.
44. **defaultdict int use?** — frequency `freq[x]+=1`.
45. **deque vs list queue?** — deque O(1) popleft; list O(n).
46. **deque maxlen?** — auto drops oldest when full.
47. **OrderedDict today?** — mainly LRU move_to_end; dict ordered 3.7+.
48. **namedtuple?** — lightweight fixed-field record.
49. **ChainMap?** — stacked dicts, first hit wins.
50. **Counter anagram check?** — `Counter(s)==Counter(t)`.
51. **Group anagrams key?** — sorted tuple or count tuple.
52. **BFS container?** — deque.
53. **DFS container?** — recursion stack or explicit stack.
54. **When Counter vs dict?** — Counter for frequency APIs.
55. **Convert defaultdict to dict?** — `dict(dd)`.

## heapq & bisect (56–65)
56. **Python heap type?** — min-heap only.
57. **Max heap trick?** — store `-x`.
58. **heappush complexity?** — O(log n).
59. **heapify complexity?** — O(n).
60. **nlargest vs sort?** — nlargest O(n log k) better for small k.
61. **bisect requires?** — sorted list.
62. **bisect_left vs right?** — left first ≥ x; right first > x.
63. **Count x in sorted arr?** — right-left with bisect.
64. **insort cost?** — O(n) shift + O(log n) find.
65. **Tuple in heap?** — compares lexicographically.

## itertools & modules (66–72)
66. **combinations vs permutations?** — order ignored vs order matters.
67. **accumulate?** — prefix sums / running reduce.
68. **product use?** — Cartesian product, binary strings.
69. **pairwise?** — adjacent pairs (3.10+).
70. **When brute itertools OK?** — small n (~≤20).
71. **Import bisect?** — `import bisect`.
72. **Import heapq?** — `import heapq`.

## Big O (73–85)
73. **O(1)?** — constant time.
74. **O(log n) example?** — binary search.
75. **O(n) example?** — single scan.
76. **O(n log n) example?** — efficient sort.
77. **O(n²) example?** — nested loops on n.
78. **Drop constants?** — O(2n)→O(n).
79. **Space complexity?** — extra memory vs input.
80. **Two Sum optimal?** — O(n) hash map.
81. **BFS complexity?** — O(V+E).
82. **DFS complexity?** — O(V+E).
83. **Sort then two pointers?** — O(n log n).
84. **list.pop(0) total n times?** — O(n²).
85. **Amortized append?** — O(1) average.

## Patterns (86–95)
86. **Two pointers when?** — sorted array pair sum, palindrome.
87. **Sliding window when?** — contiguous subarray/substring constraints.
88. **Prefix sum when?** — range sum many queries.
89. **Monotonic stack when?** — next greater/smaller element.
90. **Union-Find when?** — dynamic connectivity, Kruskal.
91. **Dijkstra needs?** — non-negative weights + priority queue.
92. **Topological sort?** — DAG ordering, course schedule.
93. **Kadane algorithm?** — max subarray sum O(n).
94. **Floyd cycle?** — linked list cycle detection.
95. **Backtracking template?** — choose, explore, unchoose.

## Interview meta (96–100)
96. **First 2 minutes?** — clarify constraints + examples.
97. **Stuck what do?** — brute force, then optimize.
98. **After coding?** — walk through example + edge cases.
99. **TLE in Python?** — check pop(0), nested loops, wrong structure.
100. **LeetCode I/O?** — method on class; no fast I/O needed.

---
*Say answers aloud. Mark weak numbers and re-read those topics.*
