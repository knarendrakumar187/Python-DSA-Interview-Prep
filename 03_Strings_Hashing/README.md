# Hashing + Strings — Simple Notes

## Hashing in one line
Use a **dict** / **set** to remember things fast (almost O(1)).

## When to use hashing
- frequency count
- "have I seen this before?"
- anagram checks
- Two Sum style lookup

## Must know code
```python
from collections import Counter

freq = Counter("hello")   # {'h':1,'e':1,'l':2,'o':1}
seen = set()
if x in seen: ...
seen.add(x)
```

## Anagram idea
Two strings are anagrams if they have **same letter counts**.
Example: `listen` and `silent`.

## Interview tip
Say: "I will use a hash map for O(1) average lookup."

## Files
- `day3_problems.py` — hashing
- `strings_problems.py` — string practice
- `solutions.py` — answers
