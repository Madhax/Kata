class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 123
        # 132
        
        
        # 213
        # 231
        # 312
        #321 
        
        #1432
        n = len(nums)
        target_idx = -1
        target_num = 0
        
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                target_idx = i
                target_num = nums[i]
                break
                
        if target_idx == -1:
            nums.sort()
            return
        
        for i in range(len(nums)-1,target_idx,-1):
            if target_num < nums[i]:
                nxt_smallest, nxt_smallest_idx  = nums[i], i
                break
                
        nums[target_idx], nums[nxt_smallest_idx] = nums[nxt_smallest_idx], nums[target_idx]
      
        first, second = target_idx+1, n-1
        while first < second:
            nums[first], nums[second] = nums[second], nums[first]
            first += 1