class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        ret = [ prices[i+1] - prices[i] for i in range(len(prices)-1)]
        sumRet = ret[0]
        maxRet = max(ret[0], 0)
        minRet = min(ret[0], 0)
        for i in xrange(1, len(ret)):
            sumRet += ret[i]
            maxRet = max(maxRet, sumRet-minRet)
            minRet = min(minRet, sumRet)
        return maxRet
