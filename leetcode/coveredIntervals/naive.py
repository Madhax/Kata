import functools

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def comparePair(item1, item2):
            return (item1[1]-item1[0])-(item2[1]-item2[0])
        
        def isSubset(pair1, pair2):
            #[a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
            
            if pair2[0] <= pair1[0] and pair1[1] <= pair2[1]:
                return True
            return False
        
        intervals.sort(key=functools.cmp_to_key(comparePair))
        x = 0
        while x < len(intervals):
            for y in range(x+1, len(intervals)):
                if isSubset(intervals[x], intervals[y]):
                    intervals.pop(x)
                    x = x - 1
                    break
            x = x + 1
            
        #print(intervals)
        
        return len(intervals)