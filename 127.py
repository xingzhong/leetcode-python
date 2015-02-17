class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, d):
        def diff(x, y):
            cnt = 0
            for i in xrange(len(x)):
                if x[i] != y[i]:
                    cnt += 1
                if cnt > 1 :
                    return False
            return True
            
        def nextLayer(word):
            res = set()
            for i in range(len(word)):
                for j in range(26):
                    w = "%s%c%s"%(word[:i], ord('a') + j, word[i+1:])
                    if w in d:
                        res.add(w)
            res.remove(word)
            return res
        
        s1, s2 = set([start]), set([end])
        cnt = 1
        while len(s1) > 0 and len(s2) > 0 :
            s = s1 if len(s1) <= len(s2) else s2
            t = set()
            for word in s :
                t |= nextLayer(word)
            s.clear()
            s.update(t)
            cnt += 1
            if len(s1 & s2) > 0 :
                return cnt
        
        return 0
            
