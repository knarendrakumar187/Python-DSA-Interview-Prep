# Topic 09 — Strings
**Phase 2 · Collections · DSA relevance: ★★★★★**

## Why this matters for DSA
Many problems are string-only: palindrome, anagram, substring, parsing.  
Python strings are **immutable** — know slicing and methods cold.

---

## Theory (simple)
A **string** is a sequence of characters. Index starts at 0.

```python
s = "hello"
s[0]    # 'h'
s[-1]   # 'o'  last char
len(s)  # 5
```

Strings cannot change in place — operations create new strings.

---

## Syntax

```python
s = "abc"
s + "d"           # concat
s * 3             # repeat
s[i:j]            # slice [i, j)
s[::-1]           # reverse
s.lower(), s.upper()
s.strip()         # trim whitespace
s.split(",")      # list of parts
",".join(lst)     # join list → string
s.find("x")       # index or -1
"x" in s          # membership
ord('a'), chr(97) # char ↔ ASCII
```

### Useful for interviews
```python
for ch in s:
    ...
for i in range(len(s)):
    ...
```

---

## Compare with C++/Java

| Feature | C++ `string` | Java `String` | Python `str` |
|---------|--------------|---------------|--------------|
| Mutable? | Yes | No | No |
| Reverse | loop / reverse | `StringBuilder` | `s[::-1]` |
| Compare | `==` | `.equals()` | `==` |
| Char at i | `s[i]` | `charAt(i)` | `s[i]` |

Python `==` compares value (good for interviews).

---

## Examples

### 1) Palindrome check
```python
s = "racecar"
print(s == s[::-1])   # True
```

### 2) Count characters
```python
s = "aabbc"
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
print(count)   # {'a':2, 'b':2, 'c':1}
```

### 3) Split and join
```python
line = "1,2,3,4"
nums = [int(x) for x in line.split(",")]
print(nums)   # [1,2,3,4]
print("-".join(map(str, nums)))   # 1-2-3-4
```

### 4) Sliding window on string
```python
s = "abcabcbb"
best = 0
seen = set()
left = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    best = max(best, right - left + 1)
print(best)   # 3 ("abc")
```

---

## DSA use cases
- Two pointers on string (palindrome, valid palindrome II)
- Frequency map for anagrams
- Substring window (longest without repeat)
- Parse input: `split`, digit checks `ch.isdigit()`

---

## 3 LeetCode-style examples

### Example A — Valid anagram
```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

print(is_anagram("listen", "silent"))   # True
```

### Example B — First unique character
```python
def first_uniq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

print(first_uniq("leetcode"))   # 0
```

### Example C — Reverse words in string
```python
def reverse_words(s):
    words = s.split()
    return " ".join(reversed(words))

print(reverse_words("the sky is blue"))   # blue is sky the
```

---

## 1) Summary
- Strings immutable; use slicing `s[i:j]`, `s[::-1]`
- Loop `for ch in s` or index with `range(len(s))`
- `split` / `join` for tokenizing and building
- Frequency dict pattern: `.get(ch, 0) + 1`

## 2) Common interview questions
1. Are Python strings mutable?
2. How reverse a string?
3. Difference between `find` and `index`?
4. How check if two strings are anagrams?
5. What is `s[::-1]`?

## 3) Common mistakes
- Trying `s[0] = 'x'` (TypeError)
- Off-by-one in slices (stop exclusive)
- Comparing strings with `is` instead of `==`
- Forgetting case: use `.lower()` for anagram checks

## 4) Practice problems (Easy → Hard)
1. **Easy:** Check if string is palindrome.
2. **Easy:** Count vowels in string.
3. **Medium:** Check valid anagram (two strings).
4. **Medium:** Longest common prefix of string array.
5. **Harder:** Minimum window substring containing all chars of `t` (basic version).

## 5) Mini quiz
1. What is `"abc"[1:3]`?
2. Is `"a" * 3` valid? Result?
3. What does `"  hi  ".strip()` return?
4. `ord('A')` vs `ord('a')` — same?
5. Can list be dict key? Can string?

---

## Homework
- Type all examples in this file yourself
- Solve practice 1–5 in `Practice/09_strings_practice.py` (create file)
- Mark Topic 09 done in `PROGRESS.md`
- When ready, say **`Next`** in chat for Topic 10
