from collections import Counter


# 时间空间都比b差
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        a = 0
        ct = Counter()
        for b, t in enumerate(s):
            ct[t] += 1
            while ct[t] > 1:
                ct[s[a]] -= 1
                a += 1
            max_length = max(max_length, b - a + 1)
        return max_length


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
