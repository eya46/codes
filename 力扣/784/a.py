from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """回溯"""
        n = len(s)
        res = []
        path = []

        def dfs(i):
            if i == n:
                return res.append("".join(path))

            c = s[i]

            # c是字母的时候才考虑选不选
            if c.isalpha():
                path.append(c.lower() if c.isupper() else c.upper())
                dfs(i + 1)
                path.pop()

            path.append(c)
            dfs(i + 1)
            path.pop()

        dfs(0)

        return res


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))
