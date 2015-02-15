class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        flag = True
        l = len(digits)
        while l > 0 :
            if flag:
                if digits[l-1] == 9:
                    flag = True
                    digits[l-1] = 0
                else:
                    digits[l-1] += 1
                    flag = False
            l -= 1
        if flag :
            digits.insert(0, 1)
        return digits
