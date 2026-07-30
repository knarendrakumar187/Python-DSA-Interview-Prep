# Sorting & Binary Search — Simple Notes

## Sorting (what to say)
- **Bubble / Selection:** easy but slow O(n^2) — know idea only
- **Merge Sort:** O(n log n), stable, needs extra space
- **Quick Sort:** average O(n log n), in-place-ish

In Python interviews, `sorted(arr)` / `arr.sort()` is fine after explaining idea.

## Binary Search (must master)
Works on **sorted** array.
Each step cut half.

```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

**Time:** O(log n)

## Interview tip
Before coding binary search, say: "Array is sorted, so binary search applies."

## Files
- `problems.py`
- `solutions.py`
