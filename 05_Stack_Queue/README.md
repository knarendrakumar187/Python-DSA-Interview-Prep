# Stack & Queue — Simple Notes

## Stack = plate stack
**Last In, First Out (LIFO)**  
Python: use `list` with `append` / `pop`

```python
st = []
st.append(3)   # push
st.pop()       # pop last
st[-1]         # peek
```

## Queue = ticket line
**First In, First Out (FIFO)**  
Python: `collections.deque`

```python
from collections import deque
q = deque()
q.append(1)     # enqueue
q.popleft()     # dequeue
```

## Must-know interview problems
1. Valid Parentheses `()` `[]` `{}`
2. Next Greater Element (monotonic stack idea)
3. Implement Queue using Stacks

## How to explain Valid Parentheses
"I push opening brackets. When I see closing, I check if stack top matches. At end stack should be empty."

## Files
- `problems.py`
- `solutions.py`
