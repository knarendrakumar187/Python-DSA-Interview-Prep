# Topic 03 — Operators
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Operators drive comparisons in binary search, modulo in hashing, and `//` vs `/` in index math.  
Wrong operator = wrong answer on edge cases.

---

## Theory (simple)
Operators are symbols that combine values.

**Categories:** arithmetic, comparison, logical, assignment, membership, identity.

---

## Syntax

### Arithmetic
```python
a + b    # add
a - b    # subtract
a * b    # multiply
a / b    # float division: 7/2 → 3.5
a // b   # floor division: 7//2 → 3
a % b    # remainder: 7%2 → 1
a ** b   # power: 2**3 → 8
```

### Comparison (return bool)
```python
a == b   a != b   a < b   a <= b   a > b   a >= b
```

### Logical
```python
x and y    # both True → True
x or y     # either True → True
not x      # flip bool
```

### Assignment shortcuts
```python
x += 1    # x = x + 1
x -= 2    x *= 3    x //= 2
```

### Membership & identity
```python
x in lst       # x in [1,2,3]
x not in s
a is b         # same object (rare in DSA)
a is not b
```

---

## Compare with C++/Java

| Feature | C++/Java | Python |
|---------|----------|--------|
| Integer division | `7/2 → 3` (ints) | `7/2 → 3.5` (use `//`) |
| Power | `pow(a,b)` or `a^b` (C++ bitwise!) | `a ** b` |
| Logical AND/OR | `&&`, `\|\|` | `and`, `or` |
| Not | `!` | `not` |

**Trap:** Python `/` always gives float. Use `//` for index math.

---

## Examples

### 1) Modulo for even/odd and cycles
```python
n = 17
print(n % 2)        # 1 (odd)
print(n % 10)       # 7 (last digit)
print((i + 1) % n)  # wrap index in circular array
```

### 2) Floor vs float division
```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3  ← use for middle index, page count
print(-7 // 2)  # -4  (floors toward negative infinity)
```

### 3) Chained comparisons (Python bonus)
```python
x = 5
print(1 < x < 10)   # True  (like 1 < x and x < 10)
```

### 4) Short-circuit
```python
# and stops at first False; or stops at first True
if lst and lst[0] > 0:   # safe: won't index if lst empty
    print("ok")
```

---

## DSA use cases
- `% n` — hash index, circular queue, even/odd
- `// 2` — binary search mid, split array
- `==`, `<`, `>` — sorting conditions, binary search
- `in` — O(1) set/dict lookup vs O(n) list scan
- `+=` — accumulate sum, count

---

## 3 LeetCode-style examples

### Example A — Check palindrome number (modulo)
```python
x = 121
orig = x
rev = 0
while x > 0:
    rev = rev * 10 + x % 10
    x //= 10
print(rev == orig)   # True
```

### Example B — FizzBuzz logic
```python
n = 15
for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Example C — Power of two (bit trick preview)
```python
n = 16
print(n > 0 and (n & (n - 1)) == 0)   # True
# Also: n > 0 and n % (n - 1) == 0 works only for powers of 2
```

---

## 1) Summary
- Use `//` and `%` for indices and remainders; `/` gives float
- `and`, `or`, `not` replace `&&`, `||`, `!`
- `in` checks membership (fast for set/dict)
- Chained comparisons: `lo <= x <= hi`

## 2) Common interview questions
1. Difference between `/` and `//` in Python?
2. What does `n % 2 == 0` check?
3. What is short-circuit evaluation?
4. Difference between `==` and `is`?
5. How do you check if `x` is in range `[a, b]` inclusive?

## 3) Common mistakes
- Using `/` when integer result needed → `3.0` breaks indexing
- `if x = 5` (assignment) instead of `if x == 5`
- Confusing `and`/`or` priority — use parentheses
- Negative `%` behavior differs from some languages (Python result sign follows divisor)

## 4) Practice problems (Easy → Hard)
1. **Easy:** Given int `n`, print if even or odd.
2. **Easy:** Given `a, b`, print quotient and remainder using `//` and `%`.
3. **Medium:** Given year, check leap year (div by 4, except 100 unless 400).
4. **Medium:** Given digit string, sum digits using `%` and `//`.
5. **Harder:** Given `n`, count numbers 1..n divisible by 3 or 5 but not both.

## 5) Mini quiz
1. What is `10 // 3`?
2. What is `10 % 3`?
3. What is `True and False`?
4. Is `5 in [1,2,3]` True or False?
5. What is `2 ** 4`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/03_operators_practice.py` (create file)
- Mark Topic 03 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 04
