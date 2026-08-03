# Topic 02 — Input and Output
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Every coding test reads input and prints answers.  
Wrong parsing (`"5"` vs `5`) or slow I/O can fail hidden tests.

---

## Theory (simple)
**Output** sends data to the screen. **Input** reads data from the user (or test file).

In interviews you often:
- Read `n`, then read `n` numbers
- Print one answer per line
- Use fast I/O for large inputs (Topic 33)

---

## Syntax

### Output
```python
print("Hello")           # Hello
print(10, 20)            # 10 20  (space between)
print(10, 20, sep=",")   # 10,20
print("done", end="")    # no newline at end
```

### Input (always returns string)
```python
name = input("Enter name: ")   # prompt is optional
x = int(input())               # read one integer
a, b = map(int, input().split())   # read two ints on one line
```

### Common patterns for DSA
```python
n = int(input())
arr = list(map(int, input().split()))
arr = [int(input()) for _ in range(n)]   # n lines, one int each
```

---

## Compare with C++/Java

| Task | C++ | Java | Python |
|------|-----|------|--------|
| Read int | `cin >> n` | `Scanner.nextInt()` | `int(input())` |
| Read line | `getline(cin, s)` | `nextLine()` | `input()` |
| Print | `cout << x` | `System.out.println(x)` | `print(x)` |

Python `input()` always gives **str** — you must convert.

---

## Examples

### 1) Basic read and print
```python
n = int(input())
print(n * 2)
# Input: 7  →  Output: 14
```

### 2) Read array in one line
```python
nums = list(map(int, input().split()))
print(sum(nums))
# Input: 1 2 3 4  →  Output: 10
```

### 3) Read n lines
```python
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
print(lines)
```

### 4) Formatted output (f-strings)
```python
a, b = 3, 5
print(f"Sum = {a + b}")   # Sum = 8
print(f"{a:03d}")         # 003  (pad to 3 digits)
```

---

## DSA use cases
- Read `n`, then `n` elements → arrays, graphs
- Print `Yes` / `No` for boolean answers
- Print multiple values: `print(i, j)` for coordinates
- Competitive: `sys.stdin.readline` (later topic)

---

## 3 LeetCode-style examples

### Example A — Two Sum style (read + check)
```python
# Given n, array, target — print indices (0-based) if pair exists
n = int(input())
nums = list(map(int, input().split()))
target = int(input())
seen = {}
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        print(seen[need], i)
        break
    seen[x] = i
```

### Example B — Count positives
```python
n = int(input())
arr = list(map(int, input().split()))
count = sum(1 for x in arr if x > 0)
print(count)
```

### Example C — Print matrix row by row
```python
r, c = map(int, input().split())
matrix = []
for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
for row in matrix:
    print(*row)   # unpack: print 1 2 3 not [1,2,3]
```

---

## 1) Summary
- `print()` for output; `input()` returns **string**
- Use `int()`, `map()`, `split()` to parse numbers
- Pattern: `n = int(input())` then read `n` items
- `print(*arr)` prints list elements separated by spaces

## 2) Common interview questions
1. What type does `input()` return?
2. How do you read two integers from one line?
3. How do you read an unknown-length list from one line?
4. Difference between `print(x)` and `print(*x)` when `x` is a list?
5. Why convert input to `int` before math?

## 3) Common mistakes
- Forgetting `int()`: `"5" + "3"` → `"53"`, not `8`
- Using `input().split()` without `map(int, ...)` → strings stay strings
- Extra spaces in output failing judge (match format exactly)
- Reading `n` lines when problem gives one line of `n` numbers

## 4) Practice problems (Easy → Hard)
1. **Easy:** Read name and age, print `Hello, {name}. You are {age}.`
2. **Easy:** Read three ints, print their sum and product.
3. **Medium:** Read `n` and `n` ints; print max and min on one line.
4. **Medium:** Read a string; print each word on its own line.
5. **Harder:** Read matrix `r×c`; print sum of each row, then sum of each column.

## 5) Mini quiz
1. What is `type(input())`?
2. How do you read `a b c` as three ints in one line?
3. What does `print(1, 2, 3, sep="-")` print?
4. Input `"10"`, you write `x = input()`. Is `x + 1` valid?
5. How do you print list `[1,2,3]` as `1 2 3`?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/02_io_practice.py` (create file)
- Mark Topic 02 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 03
