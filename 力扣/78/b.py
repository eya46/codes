from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []

        def dfs(i):
            if i == n:
                return res.append(path[:])

            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)

        dfs(0)
        return res
