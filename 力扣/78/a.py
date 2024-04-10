from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []

        def dfs(i):
            # 每个元素都选过
            if i == n:
                return res.append(path[:])

            # 不选i位元素
            dfs(i + 1)

            # 选i位元素
            path.append(nums[i])
            dfs(i + 1)

            # 清扫
            path.pop()

        dfs(0)
        return res
