from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dfs(i) = i-min(prices[:i])
        """

        res = 0
        mip = prices[0]

        for i in prices[1:]:
            res = max(res, i - mip)
            mip = min(mip, i)

        return res


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
