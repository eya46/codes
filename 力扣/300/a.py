from math import inf
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """暴力回溯,超内存"""
        n = len(nums)
        res = []
        path = []

        def dfs(i, r):
            if i < 0:
                return res.append(len(path))

            d = nums[i]

            if d < r:
                path.append(d)
                dfs(i - 1, d)
                path.pop()

            dfs(i - 1, r)

        dfs(n - 1, inf)

        return max(res)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([7, 7, 7, 7]))
