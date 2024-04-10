from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n
        use = [False] * n
        check1 = [False] * (2 * n - 1)
        check2 = [False] * (2 * n - 1)

        def dfs(r):
            if r == n:
                return res.append(["." * col + "Q" + (n - col - 1) * "." for col in path])

            for c in range(n):
                if not use[c] and not check1[r + c] and not check2[r - c]:
                    path[r] = c
                    use[c] = check1[r + c] = check2[r - c] = True
                    dfs(r + 1)
                    use[c] = check1[r + c] = check2[r - c] = False

        dfs(0)

        return res


if __name__ == "__main__":
    for i in Solution().solveNQueens(4):
        for j in i:
            print(j)

        print()
