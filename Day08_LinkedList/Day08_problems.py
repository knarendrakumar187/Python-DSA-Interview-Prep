"""DAY 8 — Linked List problems. Folder: Day08_LinkedList"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """LeetCode 206. Reverse Linked List."""
    # TODO
    pass


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """LeetCode 876. Middle node (second middle if even)."""
    # TODO
    pass


def has_cycle(head: Optional[ListNode]) -> bool:
    """LeetCode 141. Detect cycle."""
    # TODO
    pass


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """LeetCode 21. Merge two sorted lists."""
    # TODO
    pass


if __name__ == "__main__":
    print("rev", "PASS" if to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1] else "FAIL")
    mid = middle_node(build([1, 2, 3, 4, 5]))
    print("mid", "PASS" if mid and mid.val == 3 else "FAIL")

    # cycle test: 1->2->3->2...
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next, b.next, c.next = b, c, b
    print("cycle_yes", "PASS" if has_cycle(a) is True else "FAIL")
    print("cycle_no", "PASS" if has_cycle(build([1, 2, 3])) is False else "FAIL")

    merged = merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))
    print("merge", "PASS" if to_list(merged) == [1, 1, 2, 3, 4, 4] else "FAIL")
