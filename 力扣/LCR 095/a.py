from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(a, b):
            if a < 0 or b < 0:
                return 0
            if text1[a] == text2[b]:
                return dfs(a - 1, b - 1) + 1
            return max(dfs(a - 1, b), dfs(a, b - 1))

        return dfs(len(text1) - 1, len(text2) - 1)
