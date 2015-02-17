class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2 : return 0
        return sum([prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i+1] > prices[i]])
