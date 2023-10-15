class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1
        if len(set(s)) == len(s):
            return len(s)
        substring = ''
        for i in s:
            if i not in substring:
                substring += i
                max_length = max(max_length, len(substring))
            else:
                substring = substring.split(i)[1] + i
        return max_length