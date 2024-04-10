from typing import List

MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        res = []
        path = [""] * n

        def dfs(i):
            if i == n:
                return res.append("".join(path))
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return res
