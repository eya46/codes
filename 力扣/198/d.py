from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 超时+爆内存
        n = len(nums)
        res = []
        path = []

        def dfs(i):
            # print(path)
            if i > n - 1:
                return res.append(sum(path))

            path.append(nums[i])
            dfs(i + 2)
            path.pop()

            dfs(i + 1)

        dfs(0)

        return max(res)


if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))
    print(
        Solution().rob(
            [
                183,
                219,
                57,
                193,
                94,
                233,
                202,
                154,
                65,
                240,
                97,
                234,
                100,
                249,
                186,
                66,
                90,
                238,
                168,
                128,
                177,
                235,
                50,
                81,
                185,
                165,
                217,
                207,
                88,
                80,
                112,
                78,
                135,
                62,
                228,
                247,
                211,
            ]
        )
    )
