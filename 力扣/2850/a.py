from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        left = []
        lack = []

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    lack.append((i, j))
                elif grid[i][j] > 1:
                    left.append((i, j, grid[i][j]))

        del i, j

        n = len(left)

        res = []
        path = []

        def dis(x0, y0, x1, y1):
            return abs(x0 - x1) + abs(y0 - y1)

        def dfs(i):
            if i == n:
                return res.append(min(path))
