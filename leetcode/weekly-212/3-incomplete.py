import functools
class Solution:
    minDiffs = [0]
    widthLen = 0
    heightLen = 0
   
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.minDiffs = x = [[10**7 for i in range(len(heights[0]))] for j in range(len(heights))]
        self.widthLen = len(heights[0])
        self.heightLen = len(heights)
        #print(self.maxDiffs)
        def dfs(heights, y, x, minDiff):
            if self.minDiffs[y][x] > minDiff:
                self.minDiffs[y][x] = minDiff
            else:
                return
           
            currentHeight = heights[y][x]
            paths = []
            #down
            if y < (self.heightLen - 1):
                newHeight = heights[y+1][x]
                if newHeight > 0:
                    newDiff = max(minDiff, abs(currentHeight-newHeight))
                    if self.minDiffs[y+1][x] > newDiff:
                        #heights[y][x] = 0
                        #dfs(heights, y+1, x, newDiff)
                        paths.append([newDiff, y+1, x])
                        #heights[y][x] = currentHeight
                       
            #right
            if x < (self.widthLen - 1):
                newHeight = heights[y][x+1]
                if newHeight > 0:
                    newDiff = max(minDiff, abs(currentHeight-newHeight))
                    if self.minDiffs[y][x+1] > newDiff:
                        #heights[y][x] = 0
                        #dfs(heights, y, x+1, newDiff)
                        paths.append([newDiff, y, x+1])
                        #heights[y][x] = currentHeight
                       
            #up
            if y > 0:
                newHeight = heights[y-1][x]
                if newHeight > 0:
                    newDiff = max(minDiff, abs(currentHeight-newHeight))
                    if self.minDiffs[y-1][x] > newDiff:
                        #heights[y][x] = 0
                        #dfs(heights, y-1, x, newDiff)
                        paths.append([newDiff, y-1, x])
                        #heights[y][x] = currentHeight
            #left  
            if x > 0:
                newHeight = heights[y][x-1]
                if newHeight > 0:
                    newDiff = max(minDiff, abs(currentHeight-newHeight))
                    if self.minDiffs[y][x-1] > newDiff:
                        ##heights[y][x] = 0
                        #dfs(heights, y, x-1, newDiff)
                        paths.append([newDiff, y, x-1])
                        #heights[y][x] = currentHeight
           
            paths.sort()
            heights[y][x] = 0
            for path in paths:
                dfs(heights, path[1], path[2], path[0])
            heights[y][x] = currentHeight
           
        dfs(heights, 0, 0, 0)
        return self.minDiffs[-1][-1]
