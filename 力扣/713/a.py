from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        a = 0
        s = 1
        for b, i in enumerate(nums):
            s *= i
            while s >= k:
                s /= nums[a]
                a += 1
            res += b - a + 1
        return res


if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))
