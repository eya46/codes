from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n,1
        if sum(nums) < target:
            return 0
        n = len(nums)
        res = n + 1
        s = 0
        a = 0
        for b, i in enumerate(nums):
            s += i
            while s >= target:
                res = min(res, b - a + 1)
                s -= nums[a]
                a += 1
        return res if res <= n else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(4, [1, 4, 4]))
