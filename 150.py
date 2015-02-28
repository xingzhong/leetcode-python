class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        def cal(x, y, t):
            x = int(x)
            y = int(y)
            if t=='/' and x * y < 0 :
                return eval("-(%s%s%s)"%(abs(x), t, abs(y)))
            else:
                return eval("%s%s%s"%(x, t, y))
                
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                stack.append(cal(a,b,t))
            else:
                stack.append(t)
        return int(stack[0])
