from sortedcontainers import SortedList
from bisect import *
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        sortedNums = nums.copy()
        sortedNums.sort()
        
        rsortedNums = nums.copy()
        sortedNums.sort(reverse=True)
        
        if nums == rsortedNums:
            return sortedNums
        
        def
        """
        prev = -inf
        s = SortedList()
        found = False 
        for x in range(len(nums)-1, -1, -1):
            if nums[x] >= prev:
                prev = nums[x]
                s.add(nums[x])
                
            else:
                #print(s)
                found = True
                tmp = nums[x]
                #print(tmp)
                y = bisect(s, tmp)
                if y == len(s):
                    y -= 1
                    
                #print(y)
                nums[x] = s[y]
                s.pop(y)
                s.add(tmp)
                nums[x+1:] = list(s)
                break
                

        if found == False:
            nums.sort()
            
        return nums