class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str, i=0, j=0) -> int:
        if len(text1) == 0 or len(text2) == 0 or i > len(text1) - 1 or j > len(text2) - 1:
            return 0
        if text1[i] == text2[j]:
            return self.longestCommonSubsequence(text1, text2, i + 1, j + 1) + 1
        else:
            return max(
                self.longestCommonSubsequence(text1, text2, i + 1, j),
                self.longestCommonSubsequence(text1, text2, i, j + 1),
            )
