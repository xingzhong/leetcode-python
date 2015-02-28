class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0 : return ['']
        res = set()
        for p in self.generateParenthesis(n-1):
            for j in range(len(p)+1):
                res.add( p[:j] + '()' + p[j:])
        return list(res)
