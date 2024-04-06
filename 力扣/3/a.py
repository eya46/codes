class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        buffer = ""
        for t in s:
            if t in buffer:
                temp = buffer.split(t)
                # 从重复的字符分割, 非末尾就切割继续+
                if len(temp) == 2:
                    buffer = temp[1] + t
                else:
                    buffer = t
            else:
                buffer += t
                max_length = max(max_length, len(buffer))

        return max_length
