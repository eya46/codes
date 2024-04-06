from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # n,1

        f0 = f1 = 0

        for i in nums:
            f0, f1 = f1, max(f1, f0 + i)

        return f1
