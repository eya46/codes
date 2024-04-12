from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        res = 0

        for i in range(n):
            for j in range(i):
                res = max(res, prices[i] - prices[j])

        return res


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
