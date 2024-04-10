from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n

        def dfs(r, s):
            if r == n:
                return res.append(["." * col + "Q" + (n - col - 1) * "." for col in path])

            for c in s:
                if all(R + path[R] != r + c and R - path[R] != r - c for R in range(r)):
                    path[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))

        return res


if __name__ == "__main__":
    for i in Solution().solveNQueens(4):
        for j in i:
            print(j)

        print()
