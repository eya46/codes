from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if len(path) == k:
                return res.append(path[:])

            if i + len(path) < k:
                return

            for j in range(i, 0, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)

        return res


if __name__ == "__main__":
    print(Solution().combine(4, 2))
