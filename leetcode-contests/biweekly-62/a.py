class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        iter = 0
        output = []
        for _ in range(m):
            output.append([])
            for _ in range(n):
                output[-1].append(original[iter])
                iter += 1
            
                
        return output
