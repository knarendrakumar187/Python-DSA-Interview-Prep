# Topic 01 — Variables and Data Types
**Phase 1 · Python Basics · DSA relevance: ★★★★★**

## Why this matters for DSA
Every problem stores values (numbers, text, flags).  
If you confuse `int` vs `str`, or mutate a list by mistake, you lose easy marks.

---

## Theory (simple)
A **variable** is a name that points to a value in memory.

```text
  x  ----->  10
 name -----> "Ram"
```

In C++/Java you often declare type:
```cpp
int x = 10;
string name = "Ram";
```

In Python, type is decided by the value:
```python
x = 10          # int
name = "Ram"    # str
```

You can reassign freely:
```python
x = 10
x = "hello"   # now str (allowed in Python)
```

---

## Main data types for DSA

| Type | Example | Use in DSA |
|------|---------|------------|
| `int` | `5`, `-2` | counts, indices, answers |
| `float` | `3.14` | rare in DSA (sometimes averages) |
| `bool` | `True`, `False` | flags, visited |
| `str` | `"abc"` | string problems |
| `list` | `[1,2,3]` | arrays |
| `tuple` | `(1,2)` | fixed pairs, dict keys |
| `set` | `{1,2}` | unique / seen |
| `dict` | `{"a":1}` | hash maps |
| `None` | `None` | empty / null |

Check type:
```python
x = 10
print(type(x))   # <class 'int'>
```

---

## Examples

### 1) Basic assignment
```python
a = 5
b = 7
s = a + b
print(s)   # 12
```

### 2) Multiple assignment
```python
a, b = 1, 2
a, b = b, a   # swap (very useful in DSA)
print(a, b)   # 2 1
```

C++ swap needs temp or `swap(a,b)`.  
Python swap is elegant: `a, b = b, a`

### 3) Truthy / falsy (important)
```python
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False
print(bool(1))      # True
print(bool([0]))    # True (list not empty)
```

### 4) Immutability idea
```python
x = 5
y = x
x = 6
print(y)  # 5  (ints are immutable; y still points to 5)
```

Lists are mutable (later topic):
```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1,2,3]  same object!
```

---

## DSA use cases
- Counters: `count = 0`
- Flags: `found = False`
- Answers: `ans = float("inf")` or `ans = 0`
- Swap in sorting / two pointers: `a, b = b, a`

---

## 3 LeetCode-style examples

### Example A — Running sum variable
```python
nums = [1, 2, 3, 4]
total = 0
for x in nums:
    total += x
print(total)  # 10
```

### Example B — Track minimum
```python
prices = [7, 1, 5, 3, 6]
mini = float("inf")
for p in prices:
    if p < mini:
        mini = p
print(mini)  # 1
```

### Example C — Boolean flag
```python
nums = [1, 2, 3, 1]
seen = set()
has_duplicate = False
for x in nums:
    if x in seen:
        has_duplicate = True
        break
    seen.add(x)
print(has_duplicate)  # True
```

---

## 1) Summary
- Variables store values; Python types are automatic
- DSA mostly uses: `int`, `bool`, `str`, `list`, `set`, `dict`
- `a, b = b, a` swap is interview gold
- Empty values are falsy: `0`, `""`, `[]`, `None`

## 2) Common interview questions
1. Difference between mutable and immutable types?
2. How does Python swap two variables?
3. What is `None`?
4. What is dynamic typing?
5. Why can dict keys not be lists?

## 3) Common mistakes
- Using string `"5"` instead of int `5` after input
- Expecting `bool([0])` to be False (it is True)
- Copying lists with `b = a` then mutating both
- Forgetting `float("inf")` spelling

## 4) Practice problems (Easy → Hard)
1. **Easy:** Create variables for your name (str), age (int), is_student (bool). Print types.
2. **Easy:** Swap three values `a,b,c` so they rotate left.
3. **Medium:** Given list of ints, find max without using `max()`.
4. **Medium:** Count how many values are falsy in a list.
5. **Harder:** Simulate score tracker: start 0, apply operations `["+5","-2","+10"]` (as strings), return final int score.

## 5) Mini quiz
1. What is `type(3.0)`?
2. After `a = b = [1]`, `b.append(2)`, what is `a`?
3. Is `bool("False")` True or False?
4. How do you write infinity in Python for DSA mins?
5. Are strings mutable?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/01_variables_practice.py` (create file)
- Mark Topic 01 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 02
