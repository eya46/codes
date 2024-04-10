from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """回溯-子集"""
        # 不合适
        n = len(s)
        res = []
        path = []

        def dfs(i):
            if i == n:
                if len(path) == n:
                    res.append("".join(path))
                return

            for j in range(i, n):
                c = s[j]

                if c.isalpha():
                    path.append(c.lower() if c.isupper() else c.upper())
                    dfs(j + 1)
                    path.pop()

                path.append(c)
                dfs(j + 1)
                path.pop()

        dfs(0)

        return res


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))
