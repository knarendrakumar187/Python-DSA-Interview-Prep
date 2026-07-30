# Arrays — Simple Notes (Interview)

## What is an array?
A list of items in a line: `[10, 20, 30, 40]`  
Index starts at **0**.

## What interviewers want
- Can you scan left → right?
- Can you use a **hash map** (dict)?
- Do you know **Time** and **Space**?

## Important ideas (simple)

### 1) One pass scan
Look at each element once.  
Example: find max.

### 2) Hash map (dict)
Remember what you saw.  
Example: Two Sum — store `value -> index`.

### 3) Prefix sum
`prefix[i] = sum of first i elements`  
Helps answer range-sum fast.

### 4) In-place
Change the same array (no new big array).  
Example: Move Zeroes.

## Complexity words (say these)
- **O(n)** = one loop over n items
- **O(1)** extra space = only few variables
- **O(n)** space = dict/set/list of size n

## How to answer in interview
1. Example on paper  
2. Brute force  
3. Better way  
4. Code  
5. Time / Space  
6. Edge cases (empty, 1 element, duplicates)

## Files
- `day1_problems.py` — first 5 must-do
- `day2_problems.py` — prefix + more practice
- `*_solutions.py` — check after trying
