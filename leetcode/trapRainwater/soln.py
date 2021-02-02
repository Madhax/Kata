class Solution:
    def trap(self, height: List[int]) -> int:
       
        @functools.cache
        def maxLeftHeight(i):
            nonlocal height
           
            if i == -1:
                return 0
           
            return max(height[i], maxLeftHeight(i-1))
       
        @functools.cache
        def maxRightHeight(i):
            nonlocal height
           
            if i == len(height):
                return 0
               
            return max(height[i], maxRightHeight(i+1))
        """
        rain = 0
        for (i, h) in enumerate(height):
            rain += max(0, min(maxLeftHeight(i-1), maxRightHeight(i+1)) - h)
            print(i,h)
            print(h, maxLeftHeight(i-1), maxRightHeight(i+1), rain)
            #rain += h-min(maxLeftHeight(i-1), maxRightHeight(i+1))
   
        return rain"""
        #print(maxLeftHeight(2), maxRightHeight(3))
        #return 0
        return sum([(max(0, min(maxLeftHeight(i-1), maxRightHeight(i+1)) - h)) for (i, h) in enumerate(height)])
