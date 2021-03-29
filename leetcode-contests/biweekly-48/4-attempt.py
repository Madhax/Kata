class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)/2
        divisorsList = []
        numsCounter = Counter() 
        nums.sort()
        
        for num in nums:
            numsCounter[num] += 1
            
        x  = 0
        while x < len(nums):
            y = x + 1
            while y < len(nums):
                divisor = gcd(nums[x], nums[y])
                if divisor > 1:
                    divisorsList.append((divisor, nums[x], nums[y]))
                    
                y += 1
            
            x += 1
        
        divisorsList.sort(key= lambda x: x[0])
        
        output = 0
        while n > 0 and len(divisorsList) > 0:
            (val, x, y) = divisorsList.pop()
            
            if numsCounter[x] > 0 and numsCounter[y] > 0:
                #print(n, val)
                output += n * val
                numsCounter[x] -= 1
                numsCounter[y] -= 1
                n -= 1
            
        while n > 0:
            output += n
            n -= 1
        
        return int(output)