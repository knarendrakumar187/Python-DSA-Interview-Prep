# Topic 27 — bisect (binary search on sorted data)
**Phase 3 · DSA Essentials · DSA relevance: ★★★★★**

## Why this matters for DSA
Binary search is O(log n). Python's **`bisect`** module finds insertion points in **sorted** lists — lower bound, upper bound, insert while keeping order.

---

## Theory (simple)
On sorted array, `bisect_left` finds first index where `x` can go to keep order.

```text
  arr = [1, 3, 3, 5]
  bisect_left(arr, 3)  → 1
  bisect_right(arr, 3) → 3  (after existing 3s)
```

---

## Syntax
```python
import bisect

bisect.bisect_left(a, x)    # first position for x
bisect.bisect_right(a, x)   # last position for x (alias bisect)
bisect.bisect(a, x)         # same as bisect_right

bisect.insort_left(a, x)    # insert keeping sort
bisect.insort(a, x)         # insort_right
```

| Function | Use |
|----------|-----|
| `bisect_left` | first index ≥ x (lower bound) |
| `bisect_right` | first index > x (upper bound) |
| `insort` | insert x in sorted order |

---

## Examples

### 1) Find insertion point
```python
import bisect

a = [1, 3, 5, 7]
print(bisect.bisect_left(a, 5))   # 2
print(bisect.bisect_left(a, 4))   # 2 (would insert before 5)
print(bisect.bisect_right(a, 5))  # 3
```

### 2) Count occurrences of x
```python
import bisect

def count(a, x):
    return bisect.bisect_right(a, x) - bisect.bisect_left(a, x)

a = [1, 2, 2, 2, 3]
print(count(a, 2))  # 3
```

### 3) Insert in sorted order
```python
import bisect

a = [1, 3, 7]
bisect.insort(a, 5)
print(a)  # [1, 3, 5, 7]
```

### 4) Manual binary search (interview fallback)
```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## C++ / Java compare

**C++**
```cpp
lower_bound(v.begin(), v.end(), x);
upper_bound(v.begin(), v.end(), x);
```

**Java**
```java
Collections.binarySearch(list, key);
Arrays.binarySearch(arr, key);
```

**Python**
```python
import bisect
i = bisect.bisect_left(sorted_list, x)
```

---

## DSA use cases
- Search in rotated array (with manual BS)
- Find first/last position of element
- Insert into sorted structure
- Count smaller elements (bisect on sorted copy)
- Time-based key-value series (LeetCode RecentCounter style)

---

## 3 LeetCode-style examples

### Example A — Search insert position
```python
import bisect

def search_insert(nums, target):
    return bisect.bisect_left(nums, target)

print(search_insert([1,3,5,6], 5))  # 2
print(search_insert([1,3,5,6], 2))  # 1
```

### Example B — First and last position
```python
import bisect

def search_range(nums, target):
    if target not in nums:  # optional early exit
        pass
    lo = bisect.bisect_left(nums, target)
    if lo == len(nums) or nums[lo] != target:
        return [-1, -1]
    hi = bisect.bisect_right(nums, target) - 1
    return [lo, hi]

print(search_range([5,7,7,8,8,10], 8))  # [3, 4]
```

### Example C — Length of LIS using bisect on tails (advanced)
```python
import bisect

def length_of_lis(nums):
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

print(length_of_lis([10,9,2,5,3,7,101,18]))  # 4
```

---

## 1) Summary
- List must be **sorted** before bisect
- `bisect_left` = lower bound; `bisect_right` = upper bound
- `insort` maintains sorted order — O(n) insert shift
- For pure search, manual binary search also fine in interviews

## 2) Common interview questions
1. bisect_left vs bisect_right?
2. Can bisect work on unsorted list? No — wrong answer.
3. Complexity of bisect? O(log n) search; insort O(n) due to shift
4. Find first bad version — binary search template?
5. Rotated sorted array — bisect module enough? Usually manual.

## 3) Common mistakes
- Using bisect on unsorted data
- Confusing return value with "found index" when x absent
- Forgetting `import bisect`
- Using insort in tight loop — O(n²) total

## 4) Practice problems (Easy → Hard)
1. **Easy:** Insert target into sorted list at correct position (insort).
2. **Easy:** Count how many elements are strictly less than x.
3. **Medium:** Search insert position (LeetCode 35).
4. **Medium:** First and last position of target.
5. **Harder:** Find peak element or minimum in rotated sorted array (manual BS).

## 5) Mini quiz
1. `[1,2,4]. bisect_left(3)` = ?
2. Difference left vs right for `[1,2,2,2,3]` and x=2?
3. Must list be sorted ascending?
4. insort time complexity?
5. bisect on empty list returns?

---

## Homework
- Type all examples in this file yourself
- Write manual binary search from memory
- Solve practice 1–5
- Mark Topic 27 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 28
