from typing import List, Optional


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
        cur = [root]
        while cur:
            floor = []
            res.append(floor)
            pre = cur
            cur = []
            for i in pre:
                floor.append(i.val)
                if i.left:
                    cur.append(i.left)
                if i.right:
                    cur.append(i.right)
        return res
