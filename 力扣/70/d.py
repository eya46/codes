class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        f0 = 1
        f1 = 2

        for i in range(2, n):
            # f3 = f0 + f1
            # f0 = f1
            # f1 = f3
            f0, f1 = f1, f0 + f1

        return f1


if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(44))
