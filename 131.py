class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0 : return []
        _isP = [[-1] * len(s) for _ in range(len(s)) ]
        def isP(i, j):
            if _isP[i][j] != -1 :
                return _isP[i][j]
            if i >= j :
                _isP[i][j] = True
                return True
            _isP[i][j] = s[i] == s[j] and isP(i+1, j-1)
            return _isP[i][j]
        
        def part(i, j) :
            if i > j : return [[]]
            if i == j :  return [[s[i]]]
            res = []
            for k in range(i, j+1):
                if isP(i, k):
                    for p in part(k+1, j):
                        res.append([s[i:k+1]] + p)
            return res
        
        return part(0, len(s)-1)
