# Topic 21 — any() and all()
**Phase 3 · DSA Essentials · DSA relevance: ★★★★☆**

## Why this matters for DSA
These functions check conditions across a collection in **one line** — validation, win conditions, "all visited?", "any duplicate?".  
They **short-circuit**: stop early when answer is known.

---

## Theory (simple)

| Function | True when | Short-circuit |
|----------|-----------|---------------|
| `any(iterable)` | at least one truthy | stops at first True |
| `all(iterable)` | every item truthy | stops at first False |

Empty iterable: `any([])` → False, `all([])` → True (vacuous truth).

---

## Syntax
```python
any(iterable)
all(iterable)
any(x > 0 for x in nums)   # with generator — memory efficient
all(c.isdigit() for c in s)
```

---

## Examples

### 1) Basic checks
```python
nums = [0, 0, 5, 0]
print(any(nums))   # True (5 is truthy)
print(all(nums))   # False (0 is falsy)

flags = [True, True, True]
print(all(flags))  # True
```

### 2) Condition on elements
```python
nums = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in nums))  # all even

nums = [1, 3, 5]
print(any(x > 10 for x in nums))      # False
```

### 3) Validate input
```python
def valid_password(s):
    return (len(s) >= 8 and
            any(c.isupper() for c in s) and
            any(c.isdigit() for c in s))

print(valid_password("Hello123"))  # True
```

### 4) Compare with loops
```python
# instead of:
found = False
for x in nums:
    if x == target:
        found = True
        break
# use:
found = any(x == target for x in nums)
```

---

## C++ / Java compare

**C++** — `std::any_of`, `std::all_of`:
```cpp
any_of(v.begin(), v.end(), [](int x){ return x > 0; });
```

**Java**
```java
nums.stream().anyMatch(x -> x > 0);
nums.stream().allMatch(x -> x % 2 == 0);
```

**Python** — built-in, no import:
```python
any(x > 0 for x in nums)
```

---

## DSA use cases
- Check if array has duplicate: `len(nums) != len(set(nums))`
- All characters unique: `len(s) == len(set(s))`
- Any negative? `any(x < 0 for x in nums)`
- Sudoku / valid board row checks with `all`
- Early exit validation before heavy algorithm

---

## 3 LeetCode-style examples

### Example A — Contains duplicate
```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
# or: any(nums.count(x) > 1 for x in set(nums)) — slower
```

### Example B — Valid sudoku row (one row)
```python
def valid_row(row):
    cells = [x for x in row if x != "."]
    return len(cells) == len(set(cells))

print(valid_row(["1","2","3","4","5","6","7","8","9"]))  # True
```

### Example C — Jump game — can reach end?
```python
def can_jump(nums):
    reach = 0
    for i, jump in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + jump)
    return True

print(can_jump([2,3,1,1,4]))  # True
# any/all less direct here — loop with reach is standard
```

### Example D — All required chars present
```python
def has_all_chars(s, required):
    return all(c in s for c in required)

print(has_all_chars("hello", "hel"))  # True
```

---

## 1) Summary
- `any` = at least one truthy; `all` = all truthy
- Use generator expressions for efficiency
- Short-circuit saves time on big data
- `all([])` is True; `any([])` is False

## 2) Common interview questions
1. What is short-circuit evaluation?
2. Result of `all([0, 1, 2])`?
3. Result of `any("")`?
4. any vs OR across fixed variables?
5. Write "all elements distinct" without set?

## 3) Common mistakes
- `all(x > 0 for x in nums)` vs `all([x > 0 for x in nums])` — latter builds full list (wasteful)
- Confusing `any` with `max`
- Using `all(nums)` on numbers — 0 makes False
- Forgetting empty `all([])` is True

## 4) Practice problems (Easy → Hard)
1. **Easy:** Check if list has any negative number.
2. **Easy:** Check if all strings in list are non-empty.
3. **Medium:** Valid parentheses — use stack, not any/all directly (know when each fits).
4. **Medium:** All numbers in range [1,n] present exactly once — use set + length.
5. **Harder:** Matrix search — any row sorted? combine any with all per row.

## 5) Mini quiz
1. `all([True, True, False])` = ?
2. `any([])` = ?
3. `all([])` = ?
4. `any(x == 0 for x in [1,2,3])` = ?
5. Faster: generator or list inside any?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5
- Mark Topic 21 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 22
