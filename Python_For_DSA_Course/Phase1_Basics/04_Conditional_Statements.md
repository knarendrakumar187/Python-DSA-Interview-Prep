# Topic 04 — Conditional Statements
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Every algorithm branches: binary search (`if mid`), tree walks, greedy choices.  
Clean `if/elif/else` keeps logic readable under interview pressure.

---

## Theory (simple)
Run code **only when a condition is True**.

```text
if condition:
    do A
elif other:
    do B
else:
    do C
```

**Indentation matters** — Python uses spaces (4 is standard), not `{ }`.

---

## Syntax

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary (one-liner)
msg = "big" if n > 10 else "small"

# No switch until Python 3.10+ match (interviews: if/elif chain is fine)
```

### Truthy checks (common pattern)
```python
if lst:          # not empty
    ...
if not visited:  # False or empty
    ...
```

---

## Compare with C++/Java

| C++/Java | Python |
|----------|--------|
| `if (x > 0) { }` | `if x > 0:` |
| `else if` | `elif` |
| `? :` ternary | `a if cond else b` |
| `(x > 0)` parens optional | no parens needed |

---

## Examples

### 1) Find max of three
```python
a, b, c = 3, 7, 5
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
```

### 2) Valid triangle
```python
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    print("valid")
else:
    print("invalid")
```

### 3) Grade bucket
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

### 4) Guard clause (interview style)
```python
def solve(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    # main logic here
```

---

## DSA use cases
- Binary search: `if arr[mid] == target`
- Graph BFS: `if neighbor not in visited`
- Two pointers: `if sum < target: left++ else: right--`
- Early exit: `if found: return`

---

## 3 LeetCode-style examples

### Example A — Valid Parentheses (single type check)
```python
def is_open(c):
    return c in "([{"

def is_match(a, b):
    return (a == "(" and b == ")") or (a == "[" and b == "]") or (a == "{" and b == "}")

s = "()[]{}"
stack = []
ok = True
for ch in s:
    if is_open(ch):
        stack.append(ch)
    elif not stack or not is_match(stack.pop(), ch):
        ok = False
        break
if ok and not stack:
    print("valid")
```

### Example B — Number sign (LC easy pattern)
```python
x = -42
if x > 0:
    sign = 1
elif x < 0:
    sign = -1
else:
    sign = 0
print(sign)
```

### Example C — Search insert position (binary search branch)
```python
nums = [1, 3, 5, 6]
target = 2
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
else:
    print(lo)   # insert position
```

---

## 1) Summary
- `if` / `elif` / `else` + **indentation**
- Ternary: `x if cond else y`
- Use guard clauses for empty/single-element edge cases
- Combine conditions with `and`, `or`, `not`

## 2) Common interview questions
1. Difference between `elif` and multiple `if`?
2. What happens if you forget indentation?
3. How write ternary in Python?
4. When use `if not lst` vs `if len(lst) == 0`?
5. How does binary search use if/else?

## 3) Common mistakes
- Missing colon after `if`
- Wrong indent level (mixing tabs/spaces)
- Using `=` instead of `==` in condition
- `elif` after `else` (syntax error)
- Not handling empty input first

## 4) Practice problems (Easy → Hard)
1. **Easy:** Read int; print positive/negative/zero.
2. **Easy:** Read year; print leap or not.
3. **Medium:** Read three sides; classify triangle: equilateral, isosceles, scalene, or invalid.
4. **Medium:** Given sorted array and target, print index or -1 (linear search).
5. **Harder:** Given `n` and list, print second largest (handle duplicates, n<2).

## 5) Mini quiz
1. Keyword for "else if" in Python?
2. Is `if []:` True or False?
3. Write ternary: max of `a` and `b` in one line.
4. Must `elif` come before or after `else`?
5. What prints: `print("A" if 5 > 3 else "B")`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/04_conditionals_practice.py` (create file)
- Mark Topic 04 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 05
