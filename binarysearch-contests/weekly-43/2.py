class Solution:
    def solve(self, nums):
        
        endResult = nums.copy()
        endResult.sort()
        
        #nums.reverse()
        #if endResult == nums:
        #    return True

        #nums.reverse()

        def diffRanges(startList, endList):
            iter = 0
            ranges = 0
            minDiff = math.inf
            maxDiff = float("-inf")

            for i in range(len(startList)):
                if startList[i] != endList[i]:
                    minDiff = min(minDiff, i)
                    maxDiff = max(maxDiff, i)

            return (minDiff, maxDiff+1)

        r = diffRanges(nums, endResult)
        if r[0] is math.inf:
            return True

        part = nums[r[0]:r[1]]
        part.reverse()
        nums = nums[0:r[0]] + part + nums[r[1]:]
        #print(part, nums)
        return nums==endResult
        #return 0 <= diffRanges(nums, endResult) <= 1