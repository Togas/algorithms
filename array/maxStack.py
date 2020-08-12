#max stack, implemented with tupel which holds maxValue and current value
class MaxStack:
    def __init__(self):
        #contains tupel 0=value, 1=maxValue
        self.stack=[]

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, max(x, self.stack[-1][1])))
        else:
            self.stack.append((x,x))
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()[0]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def peekMax(self) -> int:
        if self.stack:
            return self.stack[-1][1]
            

    def popMax(self) -> int:
        if self.stack:
            temp=[]
            maxElement=self.stack[-1][1]
            while self.stack[-1][0]!=maxElement:
                temp.append((self.stack.pop()))
            self.stack.pop()
            for i in reversed(range(len(temp))):
                if self.stack:
                    self.stack.append((temp[i][0], max(temp[i][0], self.stack[-1][1])))
                else:
                    self.stack.append((temp[i][0], temp[i][0]))
            return maxElement