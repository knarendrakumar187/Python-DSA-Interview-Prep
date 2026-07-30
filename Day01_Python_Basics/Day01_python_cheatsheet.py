"""
DAY 1 — Python Cheatsheet for DSA
Run: python Day01_python_cheatsheet.py

Read output. Edit numbers. Re-run.
This is not a test — it is muscle memory.
"""

from collections import Counter, defaultdict, deque

print("=" * 50)
print("1) LIST = array")
print("=" * 50)
arr = [10, 20, 30, 40]
print("arr:", arr)
print("arr[0]:", arr[0], "| arr[-1]:", arr[-1])
print("slice arr[1:3]:", arr[1:3])
arr.append(50)          # add at end
print("after append:", arr)
last = arr.pop()        # remove end
print("popped:", last, "| now:", arr)

print("\nloop with index:")
for i, x in enumerate(arr):
    print(f"  i={i}, x={x}")

print("\n" + "=" * 50)
print("2) DICT = hash map (most important for DSA)")
print("=" * 50)
freq = {}
for x in [1, 1, 2, 3, 1]:
    freq[x] = freq.get(x, 0) + 1
print("freq with .get:", freq)
print("Counter:", Counter([1, 1, 2, 3, 1]))

# defaultdict auto-creates missing keys
groups = defaultdict(list)
for word in ["eat", "tea", "bat"]:
    groups["".join(sorted(word))].append(word)
print("group by sorted letters:", dict(groups))

print("\n" + "=" * 50)
print("3) SET = unique + fast 'have I seen?'")
print("=" * 50)
seen = set()
for x in [4, 1, 4, 2, 1]:
    if x in seen:
        print("  duplicate found:", x)
    seen.add(x)
print("unique values:", seen)

print("\n" + "=" * 50)
print("4) STRING basics")
print("=" * 50)
s = "Hello"
print("lower:", s.lower(), "| isalnum H:", "H".isalnum())
print("join:", "".join(["a", "b", "c"]))
print("split words:", "hello world".split())

print("\n" + "=" * 50)
print("5) TWO POINTERS pattern")
print("=" * 50)
a = [1, 2, 3, 4, 5]
l, r = 0, len(a) - 1
pairs = []
while l < r:
    pairs.append((a[l], a[r]))
    l += 1
    r -= 1
print("pairs from ends:", pairs)

print("\n" + "=" * 50)
print("6) DEQUE = queue (pop from left is O(1))")
print("=" * 50)
q = deque([1, 2, 3])
q.append(4)       # right
q.appendleft(0)   # left
print("deque:", q)
print("popleft:", q.popleft(), "| now:", q)

print("\n" + "=" * 50)
print("7) SORT + INF")
print("=" * 50)
nums = [3, 1, 4, 1, 5]
print("sorted:", sorted(nums))
print("max/min/sum:", max(nums), min(nums), sum(nums))
print("inf examples:", float("inf"), float("-inf"))

print("\n" + "=" * 50)
print("8) Complexity reminder")
print("=" * 50)
print("dict/set check ~ O(1) average")
print("one loop over n       O(n)")
print("sort                  O(n log n)")
print("Done. Now solve Day01_warmup.py")
