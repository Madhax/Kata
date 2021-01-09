
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        leftodds = 0
        leftevens = 0
        rightodds = sum(nums[1::2])
        rightevens = sum(nums[::2])
        
        ans = 0
        
        for index,el in enumerate(nums):
            remodds = leftodds + rightevens
            remevens = leftevens + rightodds
            if index%2 == 0:
                remodds-=el
                rightevens-=el
                leftevens+=el
            else:
                remevens-=el
                rightodds-=el
                leftodds+=el
            if remodds == remevens:
                ans+=1
        