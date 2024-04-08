from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a = 0
        b = len(nums) - 1
        while a < b:
            mid = (a + b) // 2
            if nums[mid] > nums[mid + 1]:
                b = mid
            else:
                a = mid + 1
        return a


if __name__ == "__main__":
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
