class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.strip().lower()
        start, end = 0, len(s)-1
        while start < end :
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

