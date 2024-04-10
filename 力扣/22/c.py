from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        res = []
        path = [""] * m

        def dfs(i, open):
            if i == m:
                return res.append("".join(path))

            if open < n:
                path[i] = "("
                dfs(i + 1, open + 1)

            if i - open < open:
                path[i] = ")"
                dfs(i + 1, open)

        dfs(0, 0)

        return res


if __name__ == "__main__":
    for i in range(1, 9):
        print(Solution().generateParenthesis(i))
