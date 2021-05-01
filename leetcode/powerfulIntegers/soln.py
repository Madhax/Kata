#sys.setrecursionlimit(10000000)
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        output = set()
        seen = set()
        #@functools.cache
        def recurse(i, j):
            nonlocal output
            #print(i,j, x**i + y**j, bound, (x**i + y**j) <= bound)
            lval = x**i
            rval = y**j
            
            val = (x**i + y**j)
            if val <= bound and (lval,rval) not in seen:
                seen.add((lval,rval))
                output.add(x**i + y**j)
                recurse(i+1, j)
                recurse(i, j+1)
                recurse(i+1, j+1)
            return 0
        
        recurse(0,0)
        #output.sort()
        return list(output)