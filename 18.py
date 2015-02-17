class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if num is None or len(num) < 4 :
            return []
        m = {}
        num.sort()
        for i1 in range(len(num)-1):
            for i2 in range(i1+1, len(num)):
                t = target-num[i1]-num[i2]
                if t in m :
                    m[t].append([i1, i2])
                else:
                    m[t] = [[i1, i2]]
        res = set()
        for k, v in m.iteritems():
            for v1 in v:
                t = num[v1[0]] + num[v1[1]]
                if t in m:
                    for v2 in m[t]:
                        if v2[0] > v1[1]:
                            res.add(tuple([num[v1[0]], num[v1[1]], num[v2[0]], num[v2[1]]]))
        return map(list, res)
        
