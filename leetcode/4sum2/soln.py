class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        #precompute values
        row1 = []
        row2 = {}
        
        for c in C:
            for d in D:
                val = c+d
                if val not in row2:
                    row2[val] = 1
                else:
                    row2[val] += 1
        output = 0
        for a in A:
            for b in B:
                val = a+b
                if -val in row2:
                    output += row2[-val]
                
        return output
    
        #def countSums(value, level)