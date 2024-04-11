from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


inf = float("inf")


class Solution:
    pre = -(2**32)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(node: Optional[TreeNode]):
            if node is None:
                return inf, -inf
            x = node.val
            lmin, lmax = f(node.left)
            if x <= lmax:
                return -inf, inf

            rmin, rmax = f(node.right)

            if x >= rmin:
                return -inf, inf

            return min(lmin, x), max(rmax, x)

        return f(root)[1] != inf
