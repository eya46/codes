from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n

        def valid(r, c):
            for R in range(r):
                C = path[R]
                if R + C == r + c or R - C == r - c:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                return res.append(["." * col + "Q" + (n - col - 1) * "." for col in path])

            for c in s:
                if valid(r, c):
                    path[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))

        return res


if __name__ == "__main__":
    for i in Solution().solveNQueens(4):
        for j in i:
            print(j)

        print()
