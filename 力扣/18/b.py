from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n - 3):
            ad = nums[a]
            b = a + 1

            if a and ad == nums[a - 1]:  # 1判重
                continue
            if ad + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                continue
            if ad + nums[-3] + nums[-2] + nums[-1] < target < target:
                continue

            while b < n - 2:
                bd = nums[b]
                c = b + 1
                d = n - 1

                if b > a + 1 and bd == nums[b - 1]:  # 2判重
                    b += 1
                    continue
                if ad + bd + nums[b + 1] + nums[b + 2] > target:
                    break
                if ad + bd + nums[-2] + nums[-1] < target:
                    b += 1
                    continue
                while c < d:
                    cd = nums[c]
                    dd = nums[d]

                    ts = ad + bd + cd + dd
                    if ts < target:
                        c += 1
                    elif ts > target:
                        d -= 1
                    else:
                        res.append([ad, bd, cd, dd])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 3判重
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:  # 4判重
                            d -= 1
                b += 1
        return res


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([0, 0, 0, 0], 0))
