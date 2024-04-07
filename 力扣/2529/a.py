from typing import List


class Solution:
    def search(self, nums: List[int], target):
        a = 0
        b = len(nums) - 1
        while a <= b:
            mid = (a + b) // 2
            if nums[mid] < target:
                a = mid + 1
            else:
                b = mid - 1
        return a

    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] >= 0 or nums[-1] <= 0:
            return len(nums) - nums.count(0)
        n = len(nums)

        return max(self.search(nums, 0), n - self.search(nums, 1))


if __name__ == "__main__":
    print(Solution().maximumCount([-2, -1, -1, 1, 2, 3]))
    print(Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2]))
    print(Solution().maximumCount([5, 20, 66, 1314]))
