# Topic 05 — Loops
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Almost every solution visits data: arrays, graphs, strings.  
`for` and `while` are your main tools for O(n) scans and two-pointer moves.

---

## Theory (simple)
**Loop** = repeat code until a condition fails or collection ends.

Two types:
- **`for`** — iterate over a sequence or range (most common in DSA)
- **`while`** — repeat while condition is True (binary search, queues)

Control:
- `break` — exit loop now
- `continue` — skip to next iteration

---

## Syntax

```python
# for over list
for x in nums:
    print(x)

# for with index (prefer enumerate later)
for i in range(len(nums)):
    print(i, nums[i])

# while
while lo <= hi:
    lo += 1

# else on loop (runs if no break — rare but good to know)
for x in nums:
    if x == target:
        break
else:
    print("not found")
```

---

## Compare with C++/Java

| C++/Java | Python |
|----------|--------|
| `for (int i=0; i<n; i++)` | `for i in range(n):` |
| `while (cond)` | `while cond:` |
| `break`, `continue` | same idea |
| `for (int x : arr)` | `for x in arr:` |

Python has no `i++`; use `i += 1`.

---

## Examples

### 1) Sum array
```python
nums = [1, 2, 3, 4]
total = 0
for x in nums:
    total += x
print(total)   # 10
```

### 2) Two-pointer (sorted pair)
```python
nums = [1, 2, 3, 4, 6]
target = 6
lo, hi = 0, len(nums) - 1
while lo < hi:
    s = nums[lo] + nums[hi]
    if s == target:
        print(lo, hi)
        break
    elif s < target:
        lo += 1
    else:
        hi -= 1
```

### 3) Nested loops (2D matrix)
```python
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```

### 4) Count with continue
```python
count = 0
for x in range(1, 11):
    if x % 2 == 0:
        continue
    count += 1
print(count)   # 5 odd numbers
```

---

## DSA use cases
- Linear scan: find max, count frequency
- Nested loops: brute force pairs O(n²)
- While: binary search, BFS queue processing
- Break early when answer found

---

## 3 LeetCode-style examples

### Example A — Two Sum (brute force)
```python
nums = [2, 7, 11, 15]
target = 9
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break
```

### Example B — Remove element (in-place style)
```python
nums = [3, 2, 2, 3]
val = 3
k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
print(k, nums[:k])   # 2, [2, 2]
```

### Example C — Climbing stairs (loop DP)
```python
n = 5
if n <= 2:
    print(n)
else:
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)   # 8 ways for n=5
```

---

## 1) Summary
- `for x in collection` is the default DSA loop
- `while` for pointer movement until condition fails
- `break` / `continue` control flow
- Nested loops → often O(n²) — know when to optimize

## 2) Common interview questions
1. `for` vs `while` — when to use each?
2. What does `break` vs `continue` do?
3. How to loop with index without `range(len)`? (enumerate — Topic 15)
4. Time complexity of nested loops over n?
5. What is infinite loop risk with `while`?

## 3) Common mistakes
- Off-by-one: `range(n)` vs `range(n+1)`
- Modifying list while iterating over it
- Forgetting to update loop variable in `while` → infinite loop
- Using nested loops when hash map gives O(n)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Print 1 to n.
2. **Easy:** Print sum of 1 to n.
3. **Medium:** Print all pairs (i,j) with i<j in array.
4. **Medium:** Given array, move all zeros to end (order of non-zeros kept).
5. **Harder:** Given matrix, print spiral order (simulate with directions).

## 5) Mini quiz
1. How many times: `for i in range(5):`?
2. What stops `while True` safely?
3. Does `for` need index variable?
4. Complexity of double loop 0..n-1?
5. After `break`, does loop `else` run?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/05_loops_practice.py` (create file)
- Mark Topic 05 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 06
