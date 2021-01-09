class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        sys.setrecursionlimit(20000)
        forbidden = set(forbidden)
        visited = set()
        posnScore = {}
        @lru_cache(maxsize = None)
        def recurse(posn, depth, backward):
            nonlocal visited, forbidden
            if posn > (x + (a + b + 1)*2):
                return float("inf")
            
            if posn == x:
                return depth
            
            if posn < 0:
                return float("inf")
            
            posn1 = posn+a
            posn1score = float("inf")
            if posn1 not in visited and posn1 not in forbidden:
                visited.add(posn1)
                posn1score = recurse(posn1, depth+1, False)
                visited.remove(posn1)
                
            posn2 = posn-b
            posn2score = float("inf")
            if posn2 not in visited and posn2 not in forbidden and backward == False:
                visited.add(posn2)
                posn2score = recurse(posn2, depth+1, True)
                visited.remove(posn2)
            
            return min(posn1score, posn2score)
        
        ret = recurse(0,0, False)
        if ret == float("inf"):
            return -1
        else:
            return ret
        
        