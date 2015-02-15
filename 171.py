class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        total = 0
        start = ord('A') - 1
        for idx, ss in enumerate(s[::-1]):
            total += 26**idx * (ord(ss) - start )
        return total
	# return sum(map( lambda x: 26**x[0] * (ord(x[1])-ord('A')+1), enumerate(s[::-1]) ))

