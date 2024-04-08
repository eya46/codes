from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], top: int):
            if node is None:
                return None

            top += node.val

            # 叶子节点
            if node.left == node.right:
                return None if top < limit else node

            node.left = dfs(node.left, top)
            node.right = dfs(node.right, top)

            # 变成叶子节点, 加上子节点都达不到limit肯定要删, 存在叶子节点说明还行
            return None if node.left == node.right else node

        return dfs(root, 0)
