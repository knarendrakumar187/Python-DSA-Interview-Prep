# Topic 33 — Fast Input / Output
**Phase 5 · Coding Style · DSA relevance: ★★★★☆**

## Why this matters for DSA
Competitive programming and some online judges need **fast I/O** for large input (10⁵–10⁶ lines).  
Default `input()` works for learning; `sys.stdin` is faster at scale.

---

## Theory (simple)
Reading many lines with `input()` in a loop is slow in Python.  
Reading **all at once** or using **`sys.stdin.readline`** is faster.

For output, many `print()` calls can be slow — collect lines and one big print, or use `sys.stdout.write`.

---

## Syntax
```python
import sys

data = sys.stdin.read().split()    # all tokens
# or
line = sys.stdin.readline().strip()

# fast print
sys.stdout.write(" ".join(map(str, ans)) + "\n")

# competitive template
input = sys.stdin.readline
```

---

## Examples

### 1) Read n integers
```python
n = int(input())
nums = list(map(int, input().split()))
```

### 2) Fast token read (competitive)
```python
import sys
data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
nums = [int(next(it)) for _ in range(n)]
```

### 3) readline template
```python
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # solve...
    print(ans)
```

### 4) Output many integers
```python
# slower
for x in ans:
    print(x)

# faster
print("\n".join(map(str, ans)))
# or one line
print(*ans)
```

### 5) LeetCode style (no fast I/O needed)
```python
class Solution:
    def twoSum(self, nums, target):
        ...
# LeetCode calls methods directly — use normal code
```

---

## C++ / Java compare

**C++**
```cpp
ios::sync_with_stdio(false);
cin.tie(nullptr);
```

**Java**
```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```

**Python**
```python
import sys
input = sys.stdin.readline
```

---

## DSA use cases
- Codeforces / HackerRank large input
- Graph with 10⁵ edges — read edges in loop with readline
- Multiple test cases T
- Print matrix row by row with join

---

## 3 LeetCode-style examples

### Example A — Read graph edges
```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
```

### Example B — Multiple test cases
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))
```

### Example C — 2D grid input
```python
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]
# or ints:
grid = [list(map(int, input().split())) for _ in range(r)]
```

---

## 1) Summary
- LeetCode: normal I/O; judges: consider fast I/O
- `sys.stdin.read().split()` for all tokens
- `input = sys.stdin.readline` for line-by-line speed
- `print(*arr)` or join for bulk output

## 2) Common interview questions
1. When need fast I/O in Python?
2. readline vs input()?
3. How read unknown number of lines until EOF?
4. Print list without spaces between brackets?
5. LeetCode vs Codeforces I/O difference?

## 3) Common mistakes
- Forgetting `.strip()` on readline (newline in string)
- map(int, input().split()) on empty line
- Using fast I/O on LeetCode unnecessarily
- print in tight loop on 10⁶ lines

## 4) Practice problems (Easy → Hard)
1. **Easy:** Read n and sum n integers from one line.
2. **Easy:** Read matrix r×c of integers.
3. **Medium:** T test cases, each with n and array — output max each.
4. **Medium:** Read graph n,m and print adjacency list.
5. **Harder:** Simulate fast I/O template on sample Codeforces problem.

## 5) Mini quiz
1. Module for readline?
2. `print(*[1,2,3])` output?
3. read().split() splits on?
4. Need fast I/O on LeetCode?
5. strip() removes?

---

## Homework
- Practice competitive template once
- Mark Topic 33 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 34
