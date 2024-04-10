from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """回溯"""
        n = len(s)
        res = []

        def dfs(i, d):
            if i == n:
                return res.append(d)

            c = s[i]

            # c是字母的时候才考虑选不选
            if c.isalpha():
                dfs(i + 1, d + (c.lower() if c.isupper() else c.upper()))

            dfs(i + 1, d + c)

        dfs(0, "")

        return res


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))
