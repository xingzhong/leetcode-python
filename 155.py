class MinStack:
    # @param x, an integer
    # @return an integer
    stack = []
    smin = None
    def push(self, x):
        if (self.smin is None) or x <= self.smin:
            self.stack.append(self.smin)
            self.smin = x
        self.stack.append(x)
        
    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.smin:
            self.smin = self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.smin
