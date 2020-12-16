class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort(reverse=True)
        
        numLen = len(nums)
        maxVal = nums[0]
        
        def underThreshold(nums, divisor, threshold):
            total = 0
            for num in nums:
                total += int(ceil(num/divisor))
                if total > threshold:
                    return False
            
            return True
        
        currentVal = ceil(maxVal / 2)
        lowerBound = 1
        upperBound = maxVal + 1
        
        lowestFound = False
        bestVal = 0

        while lowestFound == False:
            if underThreshold(nums, currentVal, threshold) == True:
                if upperBound-lowerBound <= 1:
                    return currentVal
                
                bestVal = currentVal
                upperBound = currentVal
                currentVal -= int(ceil((upperBound-lowerBound)/2))
                
                
            else:
                if upperBound-lowerBound <= 1:
                    return bestVal
                
                lowerBound = currentVal
                currentVal += int(ceil((upperBound-lowerBound)/2))
                
                
        
        return 0
    