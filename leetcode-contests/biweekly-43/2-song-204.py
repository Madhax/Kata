class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y: # ab
            r = 0
            d = []
            for si in s:
                d.append(si)
                while len(d) > 1 and d[-1] == 'b' and d[-2] == 'a':
                    d.pop()
                    d.pop()
                    r += x
            s = "".join(d)
            d = []
            for si in s:
                d.append(si)
                while len(d) > 1 and d[-1] == 'a' and d[-2] == 'b':
                    d.pop()
                    d.pop()
                    r += y
            return r
        else:
            r = 0
            d = []
            for si in s:
                d.append(si)
                while len(d) > 1 and d[-1] == 'a' and d[-2] == 'b':
                    d.pop()
                    d.pop()
                    r += y
            s = "".join(d)
            d = []
            for si in s:
                d.append(si)
                while len(d) > 1 and d[-1] == 'b' and d[-2] == 'a':
                    d.pop()
                    d.pop()
                    r += x
            return r
        
