class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        t = {}
        for idx, n in enumerate(num,start=1):
            if n in t :
                return (t[n], idx)
            t[target-n] = idx
            
