class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        a = 0
        for b, t in enumerate(s):
            if t in s[a:b]:
                a = s.index(t, a) + 1
            else:
                max_length = max(max_length, b - a + 1)
        return max_length


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
