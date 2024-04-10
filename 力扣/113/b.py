from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """回溯"""
        res = []
        path = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return

            path.append(node.val)

            if node.left == node.right:
                if sum(path) == targetSum:
                    res.append(path[:])

            dfs(node.left)
            dfs(node.right)

            path.pop()

        dfs(root)

        return res
