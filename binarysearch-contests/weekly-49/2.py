from collections import deque
class Solution:
    def solve(self, a, b):
        
        output = 0
        aiter = 0
        biter = 0
        repA = 0
        repB = 0
        while aiter < len(a) or biter < len(b):
            
            if repA == 0:
                repA = a[aiter]
                ctrA = a[aiter+1]
                aiter += 2

            if repB == 0:
                repB = b[biter]
                ctrB = b[biter+1]
                biter += 2

            while repA > 0 and repB > 0:
                sub = min(repA, repB)
                output += (ctrB * ctrA) * min(repA, repB)
                repB -= sub
                repA -= sub

            
            """
            if aiter < len(a):
                A.extend([a[aiter+1]] * a[aiter])

            if biter < len(b):
                B.extend([b[biter+1]] * b[biter])

            while len(A) > 0 and len(B) > 0:
                output += A.popleft() * B.popleft()
            """
            #aiter += 2
            #biter += 2
            
        return output
