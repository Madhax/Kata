class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = set(nums)
        addedNumbers = set()
        d = dict()
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
                
        counter = 0
        for x in s:
            complement = x - k * -1
            if complement in s and x not in addedNumbers:
                if k == 0 and d[complement] >= 2:
                    addedNumbers.add(x)
                    #addedNumbers.add(complement)
                    counter += 1
                elif k != 0:
                    addedNumbers.add(x)
                    #addedNumbers.add(complement)
                    counter += 1
                    
                
        return counter