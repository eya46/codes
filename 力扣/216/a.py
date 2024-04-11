from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path[:])

                return

            # 剪枝
            d = k - len(path)
            if sum(path) + (i * 2 - d + 1) * d // 2 < n:
                return

            for j in range(i, 0, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(9)

        return res


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))
    print(Solution().combinationSum3(9, 45))
