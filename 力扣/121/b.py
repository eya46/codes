from typing import List
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, md):
            if i == 0:
                return md

            local = prices[i]
            for j in range(i):
                md = max(md, local - prices[j])

            return dfs(i - 1, md)

        return dfs(len(prices) - 1, 0)


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
