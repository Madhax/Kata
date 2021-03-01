import operator
class FreqStack:

    def __init__(self):
        self.s = []
        self.f = {}
        
    def push(self, x: int) -> None:
        self.s.append(x)
        if x in self.f:
            self.f[x] += 1
        else:
            self.f[x] = 1

    def pop(self) -> int:
        #key = max(self.f.items(), key=operator.itemgetter(1))[0]
        
        maxVal = max(self.f.values())
        #print(maxVal)
        key = self.s.pop(self.PositionLast(maxVal, self.s))
        self.f[key] -= 1
        return key
    
    def PositionLast(self, maxVal, s):
        for i, v in enumerate(reversed(s)):
            if self.f[v] == maxVal:
                return len(s) - i - 1  # return the index in the original list
        return None
    

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()