from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        # n,n
        n = len(nums)

        @cache
        def dfs(i):
            if i < 0:
                return 0
            # 下一个, 当前的和下下个
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(n - 1)
