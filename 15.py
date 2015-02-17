class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3 : return []
        num.sort()
        res, i, l = [], 0, len(num)
        while i < l - 2:
            a = num[i]
            start = i + 1
            end = l - 1
            while start < end :
                b, c = num[start], num[end]
                if a + b + c < 0 :
                    start += 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    res.append([a, b, c])
                    start += 1
                    end -= 1
                    while start < end and num[start] == num[start-1]:
                        start += 1
                    while start < end and num[end] == num[end+1]:
                        end -= 1
            i += 1
            while i < l-2 and num[i] == num[i-1]:
                i += 1
                
        return res
        
                
