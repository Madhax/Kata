class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        memo = {}
        
        
        lowerSum = 0
        upperSum = sum(nums)
        for y in range(len(nums)):
            
            digit = nums[y]
            
            
            total = (y*digit) - lowerSum + (abs((len(nums)-y)*digit  - upperSum))
            upperSum -= digit
            lowerSum += digit
            output[y] = total
            """
            if digit in memo:
                output[y] = memo[digit]
                
            else:
                for x in range(y, len(nums)):
                    total += abs(digit - nums[x])
                
                memo[digit] = total
                output[y] = total
            """
            #currentSum += digit
        
        return output