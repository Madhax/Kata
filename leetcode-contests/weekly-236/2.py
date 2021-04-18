class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = [x for x in range(1, n+1)]
        
        curIndex = 0
        
        while len(d) > 1:
            popitem = (curIndex + k - 1) % len(d)
            #print(popitem, d[popitem], " popped")
            d.pop(popitem)
            curIndex = popitem
            
        return d[0]