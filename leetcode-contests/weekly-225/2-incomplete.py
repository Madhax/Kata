from collections import Counter
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        CounterA = Counter()
        CounterB = Counter()
        
        for c in a:
            CounterA[c] += 1
        
        for c in b:
            CounterB[c] += 1
            
        @functools.cache
        def hasLessThanA(check):
            nonlocal CounterA, CounterB
            charset = "bcdefghijklmnopqrstuvwxyz"

            iter = 0
            for c in charset:
                if CounterA[c] > 0:
                    if check == "z":
                        return CounterB[check]
                    else:
                        return min(CounterA[c], CounterB[check])
                if check == c:
                    break
            return 0
        
        @functools.cache
        def hasMoreThanA(check):
            nonlocal CounterA, CounterB
            charset = "abcdefghijklmnopqrstuvwxy"
            charset = charset[::-1]
            iter = 0
            for c in charset:
                if CounterA[c] > 0:
                    if check == "a":
                        return CounterB[check]
                    else:
                        return min(CounterA[c], CounterB[check])
                if check == c:
                    break
            return 0
        
        @functools.cache
        def hasLessThanB(check):
            nonlocal CounterB, CounterA
            charset = "bcdefghijklmnopqrstuvwxyz"

            iter = 0
            for c in charset:
                if CounterB[c] > 0:
                    if check == "z":
                        return CounterA[check]
                    else:
                        return min(CounterB[c], CounterA[check])
                if check == c:
                    break
            return 0
        
        @functools.cache
        def hasMoreThanB(check):
            nonlocal CounterB
            charset = "abcdefghijklmnopqrstuvwxy"
            charset = charset[::-1]
            iter = 0
            for c in charset:
                if CounterB[c] > 0:
                    if check == "a":
                        return CounterA[check]
                    else:
                        return min(CounterB[c], CounterA[check])
                if check == c:
                    break
            return 0
        
        #print(CounterA, CounterB)
        
        #most common A -> B
        #most common B -> A
        
        ops = math.inf
        #print(CounterA.most_common(1)[0][0])
        ops = min(ops, (len(b) - CounterB[CounterA.most_common(1)[0][0]] )+( len(a) - CounterA[CounterB.most_common(1)[0][0]]))
        print(ops)
        #make a less than b
        totalOps = 0
        for c in a:
            if c != "a":
                totalOps += hasLessThanB(c)
                
        totalOps += CounterB['a']
        
        ops = min(ops, totalOps)
        print(ops)
        #make b less than a
        totalOps = 0
        for c in set(b):
            if c != "a":
                totalOps += hasLessThanA(c)
                
        totalOps += CounterA['a']
        
        ops = min(ops, totalOps)
        print(ops)
        
        #make a greater than b
        totalOps = 0
        for c in set(a):
            if c != "z":
                #print(c)
                totalOps += hasMoreThanB(c)
                
        #print(totalOps)
        totalOps += CounterB['z']
        
        ops = min(ops, totalOps)
        print(ops)
        #make b greater than a
        totalOps = 0
        for c in set(b):
            if c != "z":
                totalOps += hasMoreThanA(c)
                print(c, hasMoreThanA(c))
                
        totalOps += CounterA['z']
        
        ops = min(ops, totalOps)
        print(ops)
        return ops
        