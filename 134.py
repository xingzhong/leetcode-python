class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        i, j, sum, sumTotal = 0, 0, 0, 0
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            sumTotal += gas[i] - cost[i]
            if sum < 0 :
                sum = 0
                j = i + 1
        if sumTotal>=0 and j < len(gas) :
            return j
        else:
            return -1
