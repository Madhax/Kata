class Solution:
    def maxArea(self, height: List[int]) -> int:
       
        i = 0
        j = len(height) - 1
       
        best = 0
       
        while j > i:
            area = min(height[i], height[j]) * (j-i)
            if area > best:
                best = area
               
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
               
        return best