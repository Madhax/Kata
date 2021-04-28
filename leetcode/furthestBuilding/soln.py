class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
       
        """
        @functools.cache
        def dp(index, bricks, ladders):
           
            if index == len(heights) - 1:
                return 0
           
            best = 0
            if heights[index] >= heights[index+1]:
                best = max(best, 1 + dp(index+1, bricks, ladders))
                           
            else:
                if ladders > 0:
                    best = max(best, 1 + dp(index + 1, bricks, ladders-1))
               
                if bricks >= heights[index+1] - heights[index]:
                    best = max(best, 1+dp(index + 1, bricks - (heights[index+1] - heights[index]), ladders))
                           
            return best
           
        return dp(0, bricks, ladders)
        """
       
        jumps = []
        for x in range(1, len(heights)):
            jumps.append(heights[x] - heights[x-1])
       
        def canReach(index, ladders, bricks):
            testHeights = jumps[:index]
            testHeights.sort(reverse=True)
            iter = 0
            while ladders > 0 and iter < index:
                if testHeights[iter] > 0:
                    ladders -= 1
                iter += 1
               
            if iter == index:
                return True
           
            while iter < index:
                if testHeights[iter] > 0:
                    if bricks >= testHeights[iter]:
                        bricks -= testHeights[iter]
                    else:
                        return False
                   
                iter += 1
               
            return True
               
        high = len(heights)-1
        low = 0
       
        while high >= low:
            mid = (high + low) // 2
           
            if canReach(mid, ladders, bricks):
                low = mid + 1
            else:
                high = mid - 1
               
        return low - 1