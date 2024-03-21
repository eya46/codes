from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        even, odd = 0, 0
        for i in c.values():
            _, __ = divmod(i, 2)
            even += _ * 2
            if __:
                odd = 1
        return even + odd
