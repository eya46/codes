from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # O(n^2),O(1)
        res = []
        n = len(nums)
        for a, i in enumerate(nums[:-2]):
            if a > 0 and i == nums[a - 1]:
                continue
            b = a + 1
            # 右边+最小都>0
            if i + nums[b] + nums[b + 1] > 0:
                break
            # 最右+最左<0
            if i + nums[-1] + nums[-2] < 0:
                continue
            c = n - 1
            while b < c:
                bd = nums[b]
                cd = nums[c]
                s = i + bd + cd
                if s == 0:
                    res.append([i, bd, cd])
                    # 跳过b右边相同
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    c -= 1
                    # 跳过c左边相同
                    while c > b and nums[c] == nums[c + 1]:
                        c -= 1
                    continue
                if s > 0:
                    c -= 1
                else:
                    b += 1
        return res


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
