"""Day 11 — Trees."""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_level(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """Build tree from level-order list like [1,2,3,None,4]."""
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root


def max_depth(root: Optional[TreeNode]) -> int:
    """LeetCode 104."""
    # TODO
    pass


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """LeetCode 100."""
    # TODO
    pass


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """LeetCode 226."""
    # TODO
    pass


def inorder(root: Optional[TreeNode]) -> List[int]:
    """Return inorder values."""
    # TODO
    pass


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """LeetCode 102."""
    # TODO
    pass


if __name__ == "__main__":
    t = build_level([3, 9, 20, None, None, 15, 7])
    print("depth", "PASS" if max_depth(t) == 3 else "FAIL")
    print("same", "PASS" if is_same_tree(build_level([1, 2, 3]), build_level([1, 2, 3])) is True else "FAIL")
    inv = invert_tree(build_level([4, 2, 7, 1, 3, 6, 9]))
    print("invert", "PASS" if inorder(inv) == [9, 7, 6, 4, 3, 2, 1] else "FAIL")
    print("inorder", "PASS" if inorder(build_level([1, None, 2, 3])) == [1, 3, 2] else "FAIL")
    print("level", "PASS" if level_order(t) == [[3], [9, 20], [15, 7]] else "FAIL")
