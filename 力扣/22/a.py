from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(i):
            l_count = path.count("(")
            r_count = path.count(")")

            if l_count == r_count == n:
                return res.append("".join(path))

            if l_count > n or r_count > n:
                return

            p = 0
            if l_count < n:
                path.append("(")
                dfs(i - 1)
                p += 1

            if r_count < n and r_count < l_count:
                path.append(")")
                dfs(i - 1)
                p += 1
            for _ in range(p):
                path.pop()

            p = 0
            if r_count < n and r_count < l_count:
                path.append(")")
                dfs(i - 1)
                p += 1
            if l_count < n:
                path.append("(")
                dfs(i - 1)
                p += 1

            for _ in range(p):
                path.pop()

        dfs(n)
        return list(set(res))


if __name__ == "__main__":
    for i in range(1, 9):
        print(Solution().generateParenthesis(i))
