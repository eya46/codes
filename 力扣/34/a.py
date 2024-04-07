from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = 0
        b = len(nums) - 1

        while a <= b:
            ad = nums[a]
            bd = nums[b]
            if ad == bd == target:
                return [a, b]
            if ad != target:
                a += 1
            if bd != target:
                b -= 1

        return [-1, -1]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 0))
    print(Solution().searchRange([], 8))
    print(Solution().searchRange([1], 1))
