class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
       
        #how to compare old posn to new posn?
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        s1 = list(s1)
       
        @functools.cache
        #can be converted to s1start, s1end, s2start
        def recurse(s1start, s1end, s2start):
           
            #print(s1start, s1end, s2start)
           
            if s1end-s1start == 1:
                return s1[s1start] == s2[s2start]
           
            ret = False
            for x in range(s1start+1, s1end):
               
                #ret = (recurse(l1[:x], start) & recurse(l1[x:], start+x))
               
                ret = recurse(s1start, x, s2start) & recurse(x, s1end, s2start+(x-s1start))
               
                if ret:
                    return True
               
                #this is incorrect
                #ret = recurse(l1[:x], len(l1) - x) & recurse(l1[x:], start)
               
                #abc => bca
               
                ret = recurse(s1start, x, s2start + (s1end-s1start) - (x-s1start)) & recurse(x, s1end, s2start)
               
                if ret:
                    return True
               
            return False
       
        def recurse2(l1, start):
           
            if len(l1) == 1:
                return l1[0] == s2[start]
           
            ret = False
            for x in range(1, len(l1)):
               
                ret = (recurse2(l1[:x], start) & recurse2(l1[x:], start+x))

                if ret:
                    return True
               
                ret = recurse2(l1[:x], start + len(l1) - x) & recurse2(l1[x:], start)
 
                if ret:
                    return True
               
            return False
        return recurse(0, len(s1), 0)
        #return recurse2(s1, 0)