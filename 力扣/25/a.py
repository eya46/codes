from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        index = 0
        cur = head

        while cur:
            index += 1
            cur = cur.next

        raw = ListNode(next=head)
        t = raw
        pre = None
        cur = t.next
        while index >= k:
            index -= k

            for i in range(k):  # 反转k区间的
                cur.next, pre, cur = pre, cur, cur.next

            # 重置头结点
            t.next.next, t.next, t = cur, pre, t.next
        return raw.next
