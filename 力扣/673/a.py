from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        f = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    nums[i] = max(nums[i], nums[j])

            f[i] += 1
            if nums[i] > 0:
                res += 1

        return res


if __name__ == "__main__":
    print(Solution().findNumberOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().findNumberOfLIS([7, 7, 7, 7]))
    print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]))
