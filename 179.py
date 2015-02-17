class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def cmp(x, y):
            a, b = int(str(x) + str(y)), int(str(y) + str(x))
            if a > b : 
                return -1
            elif a < b : 
                return 1
            else:
                return 0
        num.sort(cmp)
        return str(int("".join(map(str, num))))
