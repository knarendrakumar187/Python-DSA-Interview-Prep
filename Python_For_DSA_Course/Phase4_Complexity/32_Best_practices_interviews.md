# Topic 32 — Best Practices for Interviews
**Phase 4 · Complexity · DSA relevance: ★★★★★**

## Why this matters for DSA
Correct code that **TLEs** or is unreadable still fails.  
Interview best practices = clear thinking, right Python tools, edge cases, and communication.

---

## Theory (simple)
Interview flow:
1. **Clarify** — input size, duplicates, negative numbers, empty?
2. **Brute force** — state complexity
3. **Optimize** — hash map, two pointers, etc.
4. **Code** — clean Python, name variables well
5. **Test** — empty, single element, duplicates
6. **Analyze** — time/space Big O

---

## Syntax (interview-ready habits)
```python
def solve(nums: list[int]) -> int:
    if not nums:
        return 0
    # main logic
    return ans

# Edge cases first
# Use descriptive names: seen, left, prefix
# Avoid magic numbers — use constants
INF = float("inf")
```

---

## Examples

### 1) Clarifying questions template
```text
- Can nums be empty?
- Are values sorted?
- Can there be duplicates?
- Return index or value?
- Fit in memory? (n up to 10^5?)
```

### 2) Start with brute force, then improve
```python
# Brute O(n²) — say it aloud
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimal O(n)
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
```

### 3) Edge case checklist
```python
def test_thoughts():
    # [], [1], all same, negative, large n
    pass
```

### 4) Python idioms interviewers like
```python
from collections import Counter, defaultdict, deque
import heapq, bisect

# swap
a, b = b, a

# infinity
best = float("-inf")

# iterate with index
for i, x in enumerate(nums):

# frequency
freq = Counter(nums)
```

---

## C++ / Java compare
Python interviews allow **shorter code** — use it, but know complexity.  
Don't mimic C++ index loops when `enumerate` / `for x in nums` is clearer.

---

## DSA use cases
- Always state pattern name: "two pointers", "prefix sum", "monotonic stack"
- Pick collection before coding
- For n ≤ 10⁵: aim O(n) or O(n log n)
- For n ≤ 20: bitmask / itertools OK
- Recursion depth ~1000 default — sys.setrecursionlimit risky

---

## 3 LeetCode-style examples

### Example A — Communicate approach (Contains Duplicate)
```python
def contains_duplicate(nums):
    # O(n) time, O(n) space — set of seen
    return len(nums) != len(set(nums))
```

### Example B — Edge cases (Max subarray)
```python
def max_subarray(nums):
    if not nums:
        return 0
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
# all negative → returns max single element
```

### Example C — Don't over-engineer
```python
# Good enough for interview
def reverse_string(s):
    return s[::-1]
# Two-pointer swap also fine if asked in-place on list
```

---

## 1) Summary
- Clarify → brute → optimize → code → test → complexity
- Use sets/dicts/deques/heaps intentionally
- Handle empty/single/duplicate cases
- Talk while coding; keep names clear

## 2) Common interview questions
1. How do you approach a new problem?
2. What if you get stuck?
3. Tradeoff time vs space?
4. How test your code?
5. Python vs Java for interviews?

## 3) Common mistakes
- Coding before clarifying
- Silent for 10 minutes
- No edge case testing
- Over-complicated class design for simple problem
- Ignoring TLE — wrong data structure

## 4) Practice problems (Easy → Hard)
1. **Easy:** Practice explaining Two Sum aloud in 2 minutes.
2. **Easy:** List 5 edge cases for binary search.
3. **Medium:** Mock interview: valid parentheses — full flow.
4. **Medium:** Rewrite messy nested loops into hash map solution.
5. **Harder:** Timed 25 min: solve + explain 1 medium LeetCode.

## 5) Mini quiz
1. First step when you see a problem?
2. n=10⁵, O(n²) OK?
3. Default Python recursion limit ~?
4. When use set over list?
5. After coding you should say?

---

## Homework
- Do one mock interview with timer
- Review Phase 3 tools cheat list
- Mark Topic 32 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 33
