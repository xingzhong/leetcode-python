class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        m = len(triangle)
        if m == 0 :
            return 0
        
        for i in range(m-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j:j+2])
        
        return triangle[0][0]
            
