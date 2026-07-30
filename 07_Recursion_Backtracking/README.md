# Recursion — Simple Notes

## Recursion in one line
A function that calls itself to solve a smaller problem.

## 3 things every recursion needs
1. **Base case** (when to stop)
2. **Smaller call**
3. **Combine result**

## Simple example
```python
def fact(n):
    if n <= 1:          # base
        return 1
    return n * fact(n-1) # smaller problem
```

## Interview tip
Say the base case first. Then explain one recursive step.

## Backtracking (simple)
Try a choice → go deeper → undo choice → try next.
Used in: subsets, parentheses generation.

## Files
- `problems.py`
- `solutions.py`
