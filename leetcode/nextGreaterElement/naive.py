class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        lowerbound = n
        strn = str(n)
        def helper(iterable, r=None):
            nonlocal lowerbound
            upperbound = float("inf")
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n-r, -1))
            permutation =  int("".join(tuple(pool[i] for i in indices[:r])))
            if lowerbound < permutation < upperbound:
                upperbound = permutation
                    
            while n:
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        permutation = int("".join(tuple(pool[i] for i in indices[:r])))
                        if lowerbound < permutation < upperbound:
                            upperbound = permutation
                        
                        break
                else:
                    return upperbound
                
            return upperbound
                
        output = helper(strn)
        return output if output < 2147483647 else -1
        