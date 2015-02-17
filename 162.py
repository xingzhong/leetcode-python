class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if num is None or len(num) == 0 :
            return None
        l = len(num)
        def get(i):
            if i == -1 or i == l :
                return -1e10
            else:
                return num[i]
                
        def peak(start, end):
            mid = ( start + end ) / 2 
            l, m, r = get(mid-1), get(mid), get(mid+1)
            if m > l and m > r:
                return mid
            elif m > l and m < r:
                return peak(mid+1, end)
            else :
                return peak(start, mid)
        return peak(0, l-1)
            
