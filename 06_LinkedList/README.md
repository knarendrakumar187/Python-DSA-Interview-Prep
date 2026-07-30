# Linked List — Simple Notes

## What is Linked List?
Boxes connected by arrows (pointers).

```
[1] -> [2] -> [3] -> None
```

Each box has:
- `val` = value
- `next` = address of next box

## Why interviews love it
Shows you understand pointers / references.

## Must-know tricks

### 1) Reverse a list
Change arrows one by one:
`prev`, `curr`, `nxt`

### 2) Slow & Fast pointers
- Middle of list: slow +1, fast +2
- Detect cycle: if fast meets slow → cycle

### 3) Dummy node
Extra fake node at start to make insert/delete easy.

## How to draw in interview
Always draw 3–4 nodes on paper. Talk while pointing.

## Files
- `problems.py`
- `solutions.py`
