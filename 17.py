class Solution:
    # @return a list of strings, [s1, s2]
    d = {'2':['a','b', 'c'] , '3': ['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], 
            '8': ['t', 'u', 'v'], '9': ['w','x','y','z']}
    def letterCombinations(self, digits):
        if digits is None or len(digits) == 0 :
            return [""]
        res = []
        for c in self.letterCombinations(digits[1:]):
            for cc in self.d[digits[0]]:
                res.append(cc + c)
        return res
