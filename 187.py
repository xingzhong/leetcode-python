class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        d = {}
        res = []
        if len(s) < 10 : 
            return []
        for i in xrange(len(s)-9):
            if s[i:i+10] in d :
                if d[s[i:i+10]] < 2:
                    res.append(s[i:i+10])
                d[s[i:i+10]] += 1
            else:
                d[s[i:i+10]] = 1
        return res
