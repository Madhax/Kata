class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        boundingRanges = defaultdict(list)
        
        def boundingRange(col,row):
            nonlocal boundingRanges
            start = None
            iter = 0
            while iter < len(row):
                if row[iter] == 1:
                    if start == None:
                        start = iter
                else:
                    if start is not None:
                        boundingRanges[col].append([start, iter])
                        start = None  
                iter += 1
                
            if start is not None:
                boundingRanges[col].append([start, iter])
                
            
        
        #colMatrix = [] * len(matrix)
        colMatrix = []
        
        for x in range(len(matrix[0])):
            newrow = []
            for y in range(len(matrix)):
                newrow.append(matrix[y][x])
            
            colMatrix.append(newrow.copy())
            
        #for y in range(len(matrix)):
        #    for x in range(len(matrix[0])):
        #        colMatrix[y][x] = matrix[x][y]
                
        def isSubset(range1, range2):
            return range1[0] >= range2[0] and range1[1] <= range2[1]
        
        
        #colMatrix.sort(key=lambda x: -longestSequence(x))
        
        #startCol = colMatrix[0]
        #startVol = longestSequence(startCol)
        #print(colMatrix)
        for r in range(len(colMatrix)):
            boundingRange(r, colMatrix[r])
        
        maxVol = 0
        
        for r in range(len(colMatrix)):
            for r1 in boundingRanges[r]:
                ctr = 1
                
                for nextcol in range(len(colMatrix)):
                    if r == nextcol:
                        continue
                    for r2 in boundingRanges[nextcol]:
                        if isSubset(r1, r2):
                            print(r1, r2)
                            ctr += 1
                            
                curVol = (r1[1]-r1[0]) * ctr
                if curVol > maxVol:
                    print(r1, ctr)
                    maxVol = curVol
                
        
        
        #print(maxVol)
        return maxVol