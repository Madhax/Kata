class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        preSum = defaultdict(lambda: defaultdict(int))
        
        for y in range(len(matrix)):
            preSum[y][0] = matrix[y][0]
            for x in range(1, len(matrix[0])):
                preSum[y][x] = matrix[y][x] + preSum[y][x-1]
                
        best = -math.inf
        
        for startx in range(-1, len(matrix[0])):
            for endx in range(startx+1, len(matrix[0])):
                
                for starty in range(len(matrix)):
                    val = 0
                    for endy in range(starty, len(matrix)):
                        if startx >= 0:
                            val += preSum[endy][endx] - preSum[endy][startx]
                        else:
                            val += preSum[endy][endx]
                        if val > best and val <= k:
                            #print("here", val, startx, endx, starty, endy)
                            best = val
                            if val == k:
                                return k
                            
        #print(preSum[0][0], preSum[0][1], preSum[0][2])
        #print(preSum[1][2] + preSum[2][2])
        return best
                