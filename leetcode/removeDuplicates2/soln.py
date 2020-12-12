class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = float("-inf")
        prevCtr = 0
        assignmentIterator = 0
        traverseIterator = 0
        while traverseIterator < len(nums):
            #print(nums[traverseIterator], nums[traverseIterator] != prev, prev, prevCtr)
            
            if nums[traverseIterator] != prev:
                nums[assignmentIterator] = nums[traverseIterator]
                prevCtr = 1
                prev = nums[traverseIterator]
                
                assignmentIterator += 1
                traverseIterator += 1
                
            elif nums[traverseIterator] == prev and prevCtr < 2:
                nums[assignmentIterator] = nums[traverseIterator]
                prevCtr += 1
                
                assignmentIterator += 1
                traverseIterator += 1
                
            else:
                traverseIterator += 1

            
        return assignmentIterator