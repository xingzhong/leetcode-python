class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        ls = len(strs)
        if ls == 0 : return ''
        lls = len(strs[0])
        if lls == 0 : return ''
        for i in range(lls):
            for j in range(1, ls):
                try:
                    if strs[0][:i+1] != strs[j][:i+1]:
                        return strs[0][:i]
                except:
                    return strs[0][:i]
                    
        return strs[0][:i+1]
