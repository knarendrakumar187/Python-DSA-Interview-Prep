# Topic 08 — Recursion Basics
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Trees, graphs, backtracking, and divide-and-conquer are recursion.  
If you can't write base case + recursive step, hard LC problems stay locked.

---

## Theory (simple)
**Recursion** = function calls itself on a **smaller** subproblem.

Every recursive function needs:
1. **Base case** — stop (no more calls)
2. **Recursive case** — call self with smaller input

```text
factorial(5)
  → 5 * factorial(4)
  → 5 * 4 * factorial(3)
  → …
  → 5 * 4 * 3 * 2 * 1
```

---

## Syntax

```python
def factorial(n):
    if n <= 1:           # base case
        return 1
    return n * factorial(n - 1)   # recursive case

def sum_list(nums, i=0):
    if i == len(nums):   # base
        return 0
    return nums[i] + sum_list(nums, i + 1)
```

### Recursion limits
Python default recursion depth ~1000. Deep trees may need iterative DFS or increase limit (careful in interviews).

---

## Compare with C++/Java
Same idea: base + recursive call.  
C++/Java often use recursion for trees same as Python.  
Tail recursion is **not** optimized in Python (unlike some functional langs).

```java
int fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}
```

---

## Examples

### 1) Factorial
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(5))   # 120
```

### 2) Fibonacci (slow — teaching only)
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))   # 8
# Use loop or memo for big n
```

### 3) Print 1 to n
```python
def print_upto(n):
    if n == 0:
        return
    print_upto(n - 1)
    print(n)

print_upto(5)   # 1 2 3 4 5
```

### 4) Reverse string
```python
def rev(s):
    if len(s) <= 1:
        return s
    return rev(s[1:]) + s[0]

print(rev("abc"))   # cba
```

---

## DSA use cases
- Tree traversals: preorder, inorder, postorder
- Graph DFS
- Backtracking: subsets, permutations, N-Queens
- Divide & conquer: merge sort, quick sort

---

## 3 LeetCode-style examples

### Example A — Maximum depth of binary tree (concept)
```python
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# leaf only → depth 1
```

### Example B — Pow(x, n) recursive
```python
def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    half = my_pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x

print(my_pow(2, 10))   # 1024.0
```

### Example C — Subsets (backtracking skeleton)
```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])   # copy current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()             # undo choice

    backtrack(0, [])
    return result

print(subsets([1, 2]))   # [[], [1], [1,2], [2]]
```

---

## 1) Summary
- Base case stops recursion; recursive case shrinks problem
- Trust the recursion — assume subcall is correct
- Copy lists when saving state: `path[:]` not `path`
- Backtrack: choose → explore → undo (`pop`)

## 2) Common interview questions
1. What are base case and recursive case?
2. Why stack overflow happens?
3. Recursion vs iteration — tradeoffs?
4. What is backtracking?
5. How draw recursion tree for `fib(5)`?

## 3) Common mistakes
- Missing base case → infinite recursion
- Not returning recursive result: `fact(n-1)` vs `return n * fact(n-1)`
- Mutating shared list without backtracking
- O(2^n) fib without memoization

## 4) Practice problems (Easy → Hard)
1. **Easy:** Recursive sum 1..n.
2. **Easy:** Recursive count digits in positive int.
3. **Medium:** Recursive binary search on sorted array.
4. **Medium:** Generate all subsets of a list (backtracking).
5. **Harder:** Generate all permutations of distinct nums.

## 5) Mini quiz
1. What does `factorial(0)` return in standard definition?
2. Two parts every recursive function needs?
3. Why `result.append(path)` is wrong in subsets?
4. Is Python tail-recursion optimized?
5. Base case for `max_depth(None)`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/08_recursion_practice.py` (create file)
- Mark Topic 08 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 09
