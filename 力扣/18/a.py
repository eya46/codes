from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n - 3):
            ad = nums[a]
            b = a + 1
            while b < n - 2:
                bd = nums[b]
                c = b + 1
                d = n - 1
                while c < d:
                    cd = nums[c]
                    dd = nums[d]

                    ts = ad + bd + cd + dd
                    if ts == target and [ad, bd, cd, dd] not in res:
                        res.append([ad, bd, cd, dd])
                    if ts < target:
                        c += 1
                    else:
                        d -= 1
                b += 1
        return res


if __name__ == "__main__":
    # print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([0, 0, 0, 0], 0))
