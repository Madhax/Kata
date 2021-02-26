class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        # 2 6 | 4 8 | 7, 9, 15
        # 2, 6, | 4, 9, 15
        # 2 4 6 9 15
        
        a, b = 0, len(nums) - 1
        while a < b and nums[a + 1] >= nums[a]: a += 1
        while a < b and nums[b - 1] <= nums[b]: b -= 1
        if a == b: return 0
        
        #print(a, b)
        if a < b: 
            minv = min(nums[a+1:b+1])
            maxv = max(nums[a:b])
        while b < len(nums) and nums[b] < maxv: b += 1
        while a > -1 and nums[a] > minv: a -= 1
        #print(a, b)
        return b -1 - a
        