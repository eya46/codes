from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def run(self, root, res):
        if root is None:
            return res
        self.run(root.left, res)
        if root.val is not None:
            res.append(root.val)
        return self.run(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.run(root, [])
