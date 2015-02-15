class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    # python do not make any sense
    def strStr(self, haystack, needle):
        lh, ln = len(haystack), len(needle)
        if lh == 0 and ln == 0: return 0
        if lh < ln : return -1
        for i in range(lh):
            if haystack[i:i+ln] == needle:
                return i
        return -1
