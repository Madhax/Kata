class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicateVal = None
        missingVal = None
       
        properSet = set([x for x in range(1, len(nums)+1)])
        #nums.sort()
        numSet = set()
        for x in nums:
            if x in numSet:
                duplicateVal = x
            else:
                numSet.add(x)
               
        missingVal = next(iter(properSet - numSet))
        return [duplicateVal, missingVal]