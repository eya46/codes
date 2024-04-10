from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)

        if target < 0 or target % 2:
            return 0

        target //= 2

        n = len(nums)

        @cache
        def dfs(i, left):
            if i < 0:
                return 1 if left == 0 else 0

            if left < nums[i]:
                return dfs(i - 1, left)
            return dfs(i - 1, left) + dfs(i - 1, left - nums[i])

        return dfs(n - 1, target)
