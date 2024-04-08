from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(n^2),O(1)
        nums.sort()
        n = len(nums) - 1
        min_diff = 10**5
        res = 0

        for a, i in enumerate(nums[:-2]):
            # 重复则跳过
            if a > 0 and i == nums[a - 1]:
                continue

            # 这三个比target大就不用算后续了
            check = i + nums[a + 1] + nums[a + 2]
            if check > target:
                if (_ := abs(check - target)) < min_diff:
                    min_diff = _
                    res = check
                continue

            # 这三比target还小也不用比后续了
            check = i + nums[n - 1] + nums[n]
            if check < target:
                if (_ := abs(check - target)) < min_diff:
                    min_diff = _
                    res = check
                continue

            b = a + 1
            c = n

            while b < c:
                bd = nums[b]
                cd = nums[c]
                ts = i + bd + cd
                if ts == target:
                    return ts
                diff = abs(ts - target)
                if diff < min_diff:
                    min_diff = diff
                    res = ts
                if ts > target:
                    c -= 1
                else:
                    b += 1
        return res


if __name__ == "__main__":
    print(Solution().threeSumClosest([1, 1, 1, 0], -100))
