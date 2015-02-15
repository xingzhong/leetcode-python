class Solution:
    # @return a string
    def countAndSay(self, n):
        def say(x):
            p, c, res = x[0], 1, []
            for i in xrange(1, len(x)):
                if x[i] != p:
                    res.append(c)
                    res.append(p)
                    p, c = x[i], 1
                else:
                    c += 1
            res.append(c)
            res.append(p)
            return "".join(map(str, res))
        init = '1'
        for i in range(1, n):
            init = say(init)
        return init
