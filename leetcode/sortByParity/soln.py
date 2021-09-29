class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for x in range(len(nums)):
            if nums[x] & 1:
                odds.append(nums[x])
            else:
                evens.append(nums[x])
                
        output = []
        while odds:
            output.append(evens.pop())
            output.append(odds.pop())
            
        return output