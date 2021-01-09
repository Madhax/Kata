class Solution:
    d = {}
    smallest = ""
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        self.d = {}
        self.smallest = s
        def opA(s, a, b):
            s = list(s)
            for x in range(1, len(s), 2):
                s[x] = str((int(s[x]) + a) % 10)
                
            s = "".join(s)
            if s < self.smallest:
                self.smallest = s
                
            if s in self.d:
                return
            else:
                self.d[s] = True
                opB(s, a, b)
                opA(s, a, b)
        
        def opB(s, a, b):
            s = list(s)
            newS = s[len(s)-b:]
            newS += s[0: len(s) - b]
            s[:] = newS
            s = "".join(s)
            if s < self.smallest:
                self.smallest = s
                
            if s in self.d:
                return
            else:
                self.d[s] = True
                opA(s, a, b)
                opB(s, a, b)
                
        opA(s,a,b)
        opB(s,a,b)
        return self.smallest