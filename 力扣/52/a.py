class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        path = []

        def check(i, j):
            for x in range(i):
                y = path[x]
                if i + j == x + y or i - j == x - y:
                    return False
            return True

        def dfs(i, left):
            if i == n:
                nonlocal res
                res += 1
                return

            for j in left:
                if check(i, j):
                    path.append(j)
                    dfs(i + 1, left - {j})
                    path.pop()

        dfs(0, set(range(n)))

        return res


if __name__ == "__main__":
    print(Solution().totalNQueens(4))
