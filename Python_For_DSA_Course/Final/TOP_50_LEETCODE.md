# Top 50 LeetCode Problems for Python DSA
**Easy → Hard · Pattern tags · Python-focused tips**

| # | Problem | Diff | Pattern | Python tip |
|---|---------|------|---------|------------|
| 1 | Two Sum | E | Hash map | `seen[x]=i`, complement lookup |
| 2 | Valid Parentheses | E | Stack | `d = {')':'('}` match stack top |
| 3 | Merge Two Sorted Lists | E | Two pointers | Dummy node simplifies head |
| 4 | Best Time to Buy/Sell Stock | E | One pass | `min_price`, `max_profit` |
| 5 | Valid Palindrome | E | Two pointers | `s = ''.join(c.lower() for c in s if c.isalnum())` |
| 6 | Invert Binary Tree | E | DFS/BFS | Swap children recursively |
| 7 | Maximum Depth of BT | E | DFS | `1+max(left,right)` |
| 8 | Same Tree | E | DFS | Compare nodes recursively |
| 9 | Subtree of Another Tree | E | DFS | Same as same tree helper |
| 10 | Lowest Common Ancestor BST | E | BST | Go left/right by value |
| 11 | Reverse Linked List | E | Iterative | `prev, curr = None, head` |
| 12 | Linked List Cycle | E | Floyd | slow/fast pointers |
| 13 | Contains Duplicate | E | Set | `len(nums)!=len(set(nums))` |
| 14 | Valid Anagram | E | Counter | `Counter(s)==Counter(t)` |
| 15 | Group Anagrams | M | Hash + sort key | `tuple(sorted(s))` key |
| 16 | Top K Frequent Elements | M | Counter + heap | `Counter.most_common(k)` or nlargest |
| 17 | Product of Array Except Self | M | Prefix/suffix | Two passes, O(1) extra |
| 18 | Longest Consecutive Sequence | M | Set | O(n) with `num-1 not in set` start |
| 19 | Encode and Decode Strings | M | Delimiter | Length prefix `#` trick |
| 20 | Longest Substring Without Repeat | M | Sliding window | `seen` + shrink left |
| 21 | Longest Repeating Char Replacement | M | Sliding window | `len - max_freq <= k` |
| 22 | Minimum Window Substring | H | Sliding window | Expand/shrink with need/have Counter |
| 23 | Valid Sudoku | M | Set per unit | Row/col/box sets |
| 24 | Search in Rotated Sorted Array | M | Binary search | Which half sorted check |
| 25 | Find Minimum in Rotated Array | M | Binary search | Compare mid with right |
| 26 | Time Based Key-Value Store | M | Binary search | bisect on timestamps |
| 27 | Median of Two Sorted Arrays | H | Binary search | Partition smaller array |
| 28 | Reverse Linked List II | M | Linked list | Save connections carefully |
| 29 | Reorder List | M | LL + stack | Find mid, reverse second half |
| 30 | Remove Nth Node From End | M | Two pointers | Fast ahead n steps |
| 31 | Merge K Sorted Lists | H | Heap | Push (val, i, idx) tuples |
| 32 | Binary Tree Level Order | M | BFS | `for _ in range(len(q))` levels |
| 33 | Validate BST | M | DFS | Pass min/max bounds |
| 34 | Kth Smallest in BST | M | Inorder | Iterative stack or recurse |
| 35 | Construct BT from Preorder+Inorder | M | Recursion | `root_val` split inorder |
| 36 | Number of Islands | M | BFS/DFS | `deque`, mark visited |
| 37 | Clone Graph | M | BFS + hash | `old→new` node map |
| 38 | Pacific Atlantic Water Flow | M | DFS multi-source | From oceans inward |
| 39 | Course Schedule | M | Topo sort | Kahn BFS indegree |
| 40 | Course Schedule II | M | Topo sort | Return order list |
| 41 | Number of Connected Components | M | Union-Find / DFS | — |
| 42 | Graph Valid Tree | M | Union-Find | n-1 edges + connected |
| 43 | Redundant Connection | M | Union-Find | First edge forming cycle |
| 44 | Word Search | M | Backtracking | Mark cell, undo |
| 45 | House Robber | M | DP 1D | `prev2, prev1, cur` |
| 46 | House Robber II | M | DP | Rob line 0..n-2 vs 1..n-1 |
| 47 | Longest Palindromic Substring | M | Expand center | Or DP table |
| 48 | Palindromic Substrings | M | Expand center | Count expansions |
| 49 | Decode Ways | M | DP | `dp[i]+=dp[i-1]+dp[i-2]` |
| 50 | Coin Change | M | DP | Unbounded knapsack `dp[amt]` |

---

## Study order (Python learner)
**Week 1 (Easy 1–14):** hash map, stack, two pointers, basic tree/LL  
**Week 2 (Medium 15–25):** sliding window, binary search, Counter  
**Week 3 (Medium 26–40):** BFS, topo, graphs, heaps  
**Week 4 (Medium/Hard 41–50):** Union-Find, DP, backtracking  

## Pattern frequency (interview)
1. Hash map — 15+ problems  
2. Two pointers / sliding window — 10+  
3. BFS/DFS — 10+  
4. Binary search — 8+  
5. DP — 8+  
6. Heap — 5+  

## Python shortcuts per pattern
- **Anagram/group:** `Counter`, `defaultdict(list)`, sorted tuple keys  
- **Top K:** `heapq.nlargest`, `Counter.most_common`  
- **Grid BFS:** `deque`, directions tuple `((1,0),(-1,0),(0,1),(0,-1))`  
- **Sorted search:** `bisect` on static array; manual BS on rotated  
- **Intervals:** sort by start `key=lambda x:x[0]`  

---
*Do each problem twice: once with help, once timed from scratch.*
