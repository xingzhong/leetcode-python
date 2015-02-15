class Solution:
    # @return an integer
    # python not make any sense here
    def reverse(self, x):
        if x >= 0 :
            t = int(str(x)[::-1])
            return 0 if t > 2**31 else t
        else:
            t = -int(str(x)[:0:-1])
            return 0 if t < -2**31 else t
