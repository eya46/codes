from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # n,n
        n = len(height)
        pre_max = [height[0]] * n
        suf_max = [height[-1]] * n
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
            suf_max[n - i - 1] = max(suf_max[n - i], height[n - i - 1])
        res = 0
        for a, b, c, in zip(height, pre_max, suf_max):
            res += min(b, c) - a
        return res


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
