class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
       
        output = []
       
        start = 0
        end = 0
        numLen = len(nums)
        while start < numLen:
            end = start + 1
            while end < numLen:
                if nums[end] - nums[end-1] > 1:
                    break
                end += 1

            if end - start == 1:
                output.append("%d" % (nums[start]))
            else:
                output.append("%d->%d" % (nums[start], nums[end-1]))
            start = end
           
        return output