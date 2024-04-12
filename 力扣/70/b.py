from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(left):
            if left < 2:
                return 1

            return dfs(left - 1) + dfs(left - 2)

        return dfs(n)


if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(44))
