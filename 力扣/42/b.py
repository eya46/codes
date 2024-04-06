from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # n,1
        a = 0
        b = len(height) - 1
        res = 0
        pre_max = suf_max = 0
        while a <= b:
            ah = height[a]
            bh = height[b]
            pre_max = max(pre_max, ah)
            suf_max = max(suf_max, bh)
            if pre_max < suf_max:
                res += pre_max - ah
                a += 1
            else:
                res += suf_max - bh
                b -= 1
        return res


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
