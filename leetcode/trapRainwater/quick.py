class Solution:
    def trap(self, height: List[int]) -> int:
        
        output = 0
        left = left_max = right_max = 0        
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    output += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    output += (right_max - height[right])
                right -= 1
                
        return output