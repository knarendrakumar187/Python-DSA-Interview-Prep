# Topic 15 — enumerate()
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
Many problems need **both index and value** — two pointers, prefix sums, "find first/last index", grid traversal.  
`enumerate()` gives you `(index, value)` pairs without manual `i = 0` counters.

---

## Theory (simple)
`enumerate(iterable, start=0)` returns pairs: `(0, first_item)`, `(1, second_item)`, …

```text
  ["a", "b", "c"]
     ↓ enumerate
  (0,"a"), (1,"b"), (2,"c")
```

---

## Syntax
```python
enumerate(iterable, start=0)
```

| Part | Meaning |
|------|---------|
| `iterable` | list, string, range, etc. |
| `start` | first index (default 0; use 1 for "human" numbering) |
| returns | iterator of `(index, item)` tuples |

---

## Examples

### 1) Basic loop
```python
nums = [10, 20, 30]
for i, x in enumerate(nums):
    print(i, x)
# 0 10
# 1 20
# 2 30
```

### 2) Start at 1
```python
for rank, name in enumerate(["Ali", "Bo", "Cal"], start=1):
    print(rank, name)
# 1 Ali  2 Bo  3 Cal
```

### 3) Build index map
```python
words = ["apple", "banana", "cherry"]
index_of = {w: i for i, w in enumerate(words)}
print(index_of["banana"])  # 1
```

### 4) Compare neighbors (common DSA)
```python
nums = [1, 3, 2, 4]
for i, x in enumerate(nums):
    if i > 0 and nums[i - 1] > x:
        print("drop at", i)
# drop at 2
```

---

## C++ / Java compare

**C++**
```cpp
for (int i = 0; i < v.size(); i++) {
    cout << i << " " << v[i];
}
```

**Java**
```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(i + " " + arr[i]);
}
```

**Python** — cleaner:
```python
for i, x in enumerate(arr):
    ...
```

No off-by-one if you use `enumerate` instead of `range(len(x))`.

---

## DSA use cases
- Two pointers with index: `for i, x in enumerate(nums)`
- Find first/last position of target
- Compare adjacent elements (peaks, valleys, stock prices)
- Mark visited cells in matrix with `(r, c)` loops (often nested, but same idea)
- Build `{value: index}` maps for O(1) lookup

---

## 3 LeetCode-style examples

### Example A — Two Sum (return indices)
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

### Example B — Find peak element index
```python
def find_peak(nums):
    for i, x in enumerate(nums):
        left_ok = (i == 0) or nums[i - 1] < x
        right_ok = (i == len(nums) - 1) or x > nums[i + 1]
        if left_ok and right_ok:
            return i
    return -1

print(find_peak([1, 2, 3, 1]))  # 2
```

### Example C — First unique character (string)
```python
def first_uniq_char(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    return -1

print(first_uniq_char("leetcode"))  # 0
```

---

## 1) Summary
- `enumerate(x)` → `(index, value)` pairs
- Use instead of `for i in range(len(x))`
- `start=1` when you want 1-based labels
- Great for index + value problems (Two Sum, first occurrence)

## 2) Common interview questions
1. What does `enumerate()` return?
2. Difference between `enumerate(lst)` and `range(len(lst))`?
3. How to start counting from 1?
4. Can you enumerate a string?
5. Is `enumerate` lazy (iterator)? Yes — convert with `list()` if needed.

## 3) Common mistakes
- Writing `for i in enumerate(nums)` then using `nums[i]` (i is a tuple!)
- Forgetting you can unpack: `for i, x in enumerate(...)`
- Using `enumerate` on a dict directly (iterates keys only — use `.items()`)
- Modifying list length while iterating by index

## 4) Practice problems (Easy → Hard)
1. **Easy:** Print each element with its index from a list of names.
2. **Easy:** Return list of indices where value equals target.
3. **Medium:** Given prices, return index of max profit day pair `(buy_idx, sell_idx)` if sell after buy.
4. **Medium:** Find all indices where `nums[i] == i`.
5. **Harder:** Longest consecutive sequence — use value→index map built with enumerate for O(n) approach hint.

## 5) Mini quiz
1. What is `list(enumerate("ab"))`?
2. What does `start=10` do?
3. `for i, x in enumerate([5])` — what are i and x?
4. Can enumerate work on a set? (order not guaranteed)
5. Is `enumerate` a list or iterator?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 on paper or in a `.py` file
- Mark Topic 15 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 16
