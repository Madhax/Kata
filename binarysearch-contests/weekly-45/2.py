from collections import defaultdict

class VirtuallyCloneableStacks:
    def __init__(self):
        self.s = defaultdict(int)
        self.index = 0

    def copyPush(self, i):
        self.index += 1
        self.s[self.index] = self.s[i] + 1


    def copyPop(self, i):
        self.index += 1
        self.s[self.index] = self.s[i] - 1

    def size(self, i):
        return self.s[i]