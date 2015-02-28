class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def cmp(x, y):
            return -1 if str(x) + str(y) > str(y) + str(x) else 1
        num = map(str, num)
        num.sort(cmp)
        return "".join(num).lstrip('0') or '0'
