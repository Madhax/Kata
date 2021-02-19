class Solution:
    def numTrees(self, n: int) -> int:
        l = []
        for i in range(n+1):
            if i == 0:
                l.append(1)
            elif i == 1:
                l.append(1)
            elif i == 2:
                l.append(2)
            else:
                s = 0
                for j in range(1,i+1):
                    s += (l[j-1]*l[i-j])
                l.append(s)
        return l[-1]