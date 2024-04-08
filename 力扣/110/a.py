from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        l = self.check(node.left)
        if l < 0:
            return -1
        r = self.check(node.right)
        if r < 0:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check(root) != -1
