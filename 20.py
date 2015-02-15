class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        table = {'(':')', "{":"}", "[":']'}
        for ss in s:
            if ss in ['(', '{', '[']:
                stack.append(table[ss])
            elif len(stack) == 0 or stack.pop() != ss:
                return False
        return len(stack)==0
