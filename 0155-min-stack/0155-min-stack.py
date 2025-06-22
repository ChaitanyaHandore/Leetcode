class MinStack(object):

    def __init__(self):
        self.st = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        minval=self.getMin()
        if minval==None or val<minval:
            minval=val
        self.st.append([val,minval])

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1] if self.st else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()