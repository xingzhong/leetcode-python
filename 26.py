class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0 : return 0
        j = 1
        pilot = A[0]
        for i in range(1, len(A)):
            if A[i] != pilot:
                A[j] = A[i]
                pilot = A[j]
                j += 1
        return j
