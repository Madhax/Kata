class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0 
        
    def push(self, x: int) -> None:
        freq = self.freq[x] + 1
        self.freq[x] = freq
        if freq > self.maxFreq:
            self.maxFreq = freq
        self.group[freq].append(x)
        
    def pop(self) -> int:
        if self.maxFreq > 0:
            x = self.group[self.maxFreq].pop()
            self.freq[x] -= 1
            if not self.group[self.maxFreq]:
                self.maxFreq -=1
            return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()