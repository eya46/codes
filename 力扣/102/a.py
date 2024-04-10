from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def qfs(node: Optional[TreeNode], depth: int):
            if node is None:
                return
            qfs(node.left, depth + 1)
            qfs(node.right, depth + 1)
            res[depth].append(node.val)

        qfs(root, 0)
        return [i[1] for i in sorted(res.items(), key=lambda x: x[0])]
