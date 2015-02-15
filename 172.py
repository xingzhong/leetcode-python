class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        i = 5 
        num = 0
        while i <= n :
            num += n / i
            i *= 5
        return num
