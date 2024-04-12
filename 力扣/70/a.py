class Solution:
    def climbStairs(self, n: int) -> int:
        # 超时
        res = 0

        def dfs(left):
            if left < 2:
                nonlocal res
                res += 1
                return

            dfs(left - 1)
            dfs(left - 2)

        dfs(n)

        return res


if __name__ == "__main__":
    print(Solution().climbStairs(2))
