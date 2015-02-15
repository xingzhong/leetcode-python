class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            r = []
            for j in range(i+1):
                if j == 0 or j==i :
                    r.append(1)
                else:
                    r.append(res[-1][j-1] + res[-1][j])
            res.append(r)
        return res
