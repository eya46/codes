from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        if root.left == root.right:

            if root.val == targetSum:
                return [[targetSum]]
            else:
                return []

        targetSum -= root.val
        res = self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        for i in res:
            i.insert(0, root.val)

        return res
