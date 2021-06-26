from sortedcontainers import SortedList
from bisect import *
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ret = []
        work = []
        #num = 
        for num in nums[::-1]:
            posn = bisect_left(work, num)
            ret.append(posn)
            work.insert(posn, num)
            #work.add(num)
            
        return ret[::-1]
        