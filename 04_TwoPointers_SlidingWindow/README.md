# Two Pointers + Sliding Window — Simple Notes

## Two Pointers (simple idea)
Use two indices (`left`, `right`) and move them smartly.

### Common cases
1. Array is **sorted** → left start, right end  
2. Remove duplicates / move zeroes style  
3. Palindrome check from both ends  

### Example talk
"I put one pointer at start and one at end. If sum is too big, move right left. If too small, move left right."

## Sliding Window (simple idea)
Look at a **continuous part** of array/string, then slide it.

### Fixed window
Size is fixed (example: max sum of k elements)

### Variable window
Grow/shrink until condition is valid  
(example: longest substring without repeating chars)

## When to choose what?
| Pattern | Use when |
|---------|----------|
| Two pointers | sorted array, pair sum, palindrome |
| Sliding window | subarray/substring continuous problem |
| Hash map | count / seen before |

## Files
- `two_pointers_problems.py`
- `sliding_window_problems.py`
- `solutions.py`
