from typing import List
from functools import cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """暴力回溯,超内存"""
        """但可以加cache,因为不用处理path"""
        n = len(nums)

        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))

            return res + 1

        return max(dfs(i) for i in range(n))


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([7, 7, 7, 7]))
