from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        f = [0] * (n + 2)
        for idx, i in enumerate(nums):
            f[idx + 2] = max(f[idx + 1], f[idx] + i)

        return f[n + 1]
