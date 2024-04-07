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

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print("左")
        a = self.search(nums, target)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        print("右")
        return [a, self.search(nums, target + 1) - 1]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    # print(Solution().searchRange([5, 7, 7, 8, 8, 10], 0))
    # print(Solution().searchRange([], 8))
    # print(Solution().searchRange([1], 1))
    # print(Solution().searchRange([2, 2], 2))
    # print(Solution().searchRange([1, 3], 1))
