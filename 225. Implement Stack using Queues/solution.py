class MyStack:

    def __init__(self):
        self.left_q = []        
        # self.right_q = []        

    def push(self, x: int) -> None:
        self.left_q.append(x)

    def pop(self) -> int:
        return self.left_q.pop()
        

    def top(self) -> int:
        return self.left_q[-1]

    def empty(self) -> bool:
        return not self.left_q



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()