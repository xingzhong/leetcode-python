class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        t1 = [1] * (rowIndex+1)
        t2 = [1] * (rowIndex+1)
        for i in range(1, rowIndex+1):
            for j in range(i+1):
                if j == 0 or j == i :
                    t2[j] = 1
                else:
                    t2[j] = t1[j-1] + t1[j]
            t1 = t2[:]
        return t1
