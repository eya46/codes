from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        cur = deque([root])
        while cur:
            floor = []
            for i in range(len(cur)):
                i = cur.popleft()
                floor.append(i.val)
                if i.left:
                    cur.append(i.left)
                if i.right:
                    cur.append(i.right)
            res.append(floor)
        return res
