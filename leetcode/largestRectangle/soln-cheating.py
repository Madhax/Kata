class Solution:
    def largestRectangleArea(self, heights):

        if not heights: 
          return 0
        n = len(heights)
        lessFromLeft = [-1] * n
        lessFromRight = [n] * n        
        stack = []    
        for i,v in enumerate(heights):
            while stack and heights[stack[-1]] >= v: # right is from the popping out
                lessFromRight[stack.pop()] = i
            if stack:  #left is from the pushing in
                lessFromLeft[i] = stack[-1]
            stack.append(i)  
 
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, heights[i]*(lessFromRight[i]-lessFromLeft[i]-1))           
        return maxArea