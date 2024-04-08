from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        if b == -1:
            return -1
        while a <= b:
            mid = (a + b) // 2
            md = nums[mid]
            if md == target:
                return mid
            s = nums[0]
            if s <= md:
                if s <= target < md:
                    b = mid - 1
                else:
                    a = mid + 1
            else:
                if md < target <= nums[-1]:
                    a = mid + 1
                else:
                    b = mid - 1
        return -1
