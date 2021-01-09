import functools
class Solution:
    heights = []
    bestPath = []
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        self.heights = heights
        self.bestPath = [0] * len(heights)
        @lru_cache(maxsize=None)
        def dp(index, bricks, ladders):
            if index >= len(self.heights) - 1:
                return len(self.heights) - 1
           
            if self.bestPath[index] == 0:
                self.bestPath[index] = [ladders, bricks]
               
            elif self.bestPath[index] > [ladders,bricks]:
                return 0
           
            jumpValue = self.heights[index+1] - self.heights[index]
           
            #print(index, bricks, ladders, jumpValue)
           
            if jumpValue < 0:
                return dp(index+1, bricks, ladders)
               
            else:
                l = 0
                r = 0
                if jumpValue <= bricks:
                    l = dp(index+1, bricks-jumpValue, ladders)
                if ladders > 0:
                    r = dp(index+1, bricks, ladders-1)
                   
                return max(l,r, index)
           
            return index
               
        return dp(0, bricks, ladders)