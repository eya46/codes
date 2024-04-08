from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        a=0
        b=len(nums)-1
        while a<b:
            mid = (a+b)//2
            if nums[mid]>nums[b]:
                a=mid+1
            else:
                b=mid
        return nums[a]

if __name__ == "__main__":
    print(Solution().findMin([4,5,6,7,0,1,2]))
