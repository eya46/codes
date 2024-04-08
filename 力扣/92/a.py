from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        raw = ListNode(next=head)
        t = raw
        for i in range(left - 1):
            t = t.next

        pre = None
        cur = t.next
        for i in range(right - left + 1):
            cur.next, pre, cur = pre, cur, cur.next
        t.next.next = cur
        t.next = pre
        return raw.next
