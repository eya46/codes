from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        def dfs(i, start):
            if i == n:
                res.append(path[:])
                return

            if i < n - 1:
                dfs(i + 1, start)

            t = s[start : i + 1]

            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, i + 1)
                path.pop()

        dfs(0, 0)

        return res


if __name__ == "__main__":
    print(Solution().partition("aab"))
