class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * n

        # f[i] = f[i-1] + f[i-2]

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(44))
