class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)
        
        if n == 1:
            return heights[0]
        
        stack = [(heights[0], 0)]
        
        max_area = 0
        
        for i, height in enumerate(heights):
            #print(stack)
            
            if height < stack[-1][0]:
                while stack and height < stack[-1][0]:
                    height2, i2 = stack.pop()
                    area = height2 * (i - i2)
                    max_area = max(max_area, area)
                stack.append((height, i2))
                
                
            if not stack or height > stack[-1][0]:
                stack.append((height, i))
            
            #for height2, i2 in stack:
             #   area = min(height, height2) * (i - i2 + 1)
              #  max_area = max(max_area, area)
        
        while stack:
            height, i = stack.pop()
            area = height * (n - i)
            max_area = max(max_area, area)
            
                
            #print(area, stack)
            #print("")
                
        return max_area