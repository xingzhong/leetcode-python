class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = []
        while num > 0 :
            res.append( chr(ord('A') +  (num-1) % 26 ) )
            num = (num-1) / 26
        return "".join(res[::-1])
