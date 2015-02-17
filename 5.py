class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s is None or len(s) == 0 : 
            return 0
        table = [[False] * len(s) for _ in range(len(s))]
        maxLen, start = 1, 0
        for step in range(len(s)):
            for i in range(len(s) - step):
                if step - 2 > maxLen:
                    break
                if step == 0 :
                    table[i][i] = True
                elif step == 1 : 
                    table[i][i+1] = s[i] == s[i+1]
                else:
                    table[i][i+step] = table[i+1][i+step-1] and s[i] == s[i+step]
                    if table[i][i+step]:
                        maxLen, start = step, i
        return s[start:start+maxLen+1]
