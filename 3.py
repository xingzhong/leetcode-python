class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2 : return len(s)
        pos = {}
        i, j, maxLen = 0, 0, 1
        for i in range(len(s)):
            if s[i] in pos and pos[s[i]] >= j:
                j = pos[s[i]] + 1
            maxLen = max(maxLen, i - j + 1 )
            pos[s[i]] = i
        return maxLen
