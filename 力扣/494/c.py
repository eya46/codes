from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)

        if target < 0 or target % 2:
            return 0

        target //= 2

        n = len(nums)

        f = [[0] * (target + 1) for i in range(n + 1)]

        # 都为1的时候当然就一种解法
        f[0][0] = 1

        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]

        return f[n][target]
