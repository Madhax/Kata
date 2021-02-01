from collections import deque
from sortedcontainers import SortedList
class Solution:
    def solve(self, heights, k):
        
        d = deque()
        sl = SortedList()

        heightIter = 0
        while heightIter < k:
            if heightIter == len(heights):
                break

            d.append(heights[heightIter])
            sl.add(heights[heightIter])
            heightIter+=1

        
        output = []

        while len(d) > 0 or heightIter < len(heights):
            
            if heightIter < len(heights):
                d.append(heights[heightIter])
                sl.add(heights[heightIter])

            person = d.popleft()
            sl.remove(person)

            if (len(sl) > 0 and sl[-1] < person) or len(sl) == 0:
                output.append(heightIter-k)

            heightIter += 1


        return output

