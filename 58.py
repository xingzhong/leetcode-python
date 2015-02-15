class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        if len(s) < 1 : return 0
        return len(s.split()[-1])
