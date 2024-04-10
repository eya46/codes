from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            path.append(str(node.val))

            if node.left == node.right:
                res.append("->".join(path))
                return path.pop()

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            path.pop()

        dfs(root)

        return res
