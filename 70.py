class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 2 : return n
        t1, t2, t3 = 1, 2, 2
        for i in range(2, n):
            t3 = t1 + t2
            t1, t2 = t2, t3
        return t3
        
