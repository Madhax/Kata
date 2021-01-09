class OrderedStream:
    ptr = 1
    d = {}
        
    def __init__(self, n: int):
        self.ptr = 1
        self.d = {}

    def insert(self, id: int, value: str) -> List[str]:
        self.d[id] = value
        ret = []
        while self.ptr in self.d:
            ret.append(self.d[self.ptr])
            self.ptr += 1
            
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)