from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 超时555~
        n = len(nums)

        res = []
        path = []

        def dfs(i):
            if i == n:
                if sum(path) == target:
                    res.append(1)
                return

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            path.append(-nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)

        return len(res)


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(Solution().findTargetSumWays([33, 36, 38, 40, 25, 49, 1, 8, 50, 13, 41, 50, 29, 27, 18, 25, 37, 8, 0, 48], 0))
