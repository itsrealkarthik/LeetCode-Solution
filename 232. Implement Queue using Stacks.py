class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x):
        self.stack1.append(x)
        
    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        element=self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return element
        
    def peek(self):
        return self.stack1[0]
        
    def empty(self):
        return bool(not(len(self.stack1)))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()