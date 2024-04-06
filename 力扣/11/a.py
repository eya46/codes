from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n,1
        a = 0
        b = len(height) - 1
        res = 0
        while a < b:
            ad = height[a]
            bd = height[b]
            if ad > bd:
                res = max(res, bd * (b - a))
                b -= 1
            else:
                res = max(res, ad * (b - a))
                a += 1
        return res


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
