class Solution:
    def solve(self, ribbons, k):
        ribbons.sort()

        workingSet = ribbons[-k:]
        minSize = 1
        maxSize = workingSet[-1]
        workingSet.reverse()

        def sizeWork(n, k):
            nonlocal workingSet
            ret = 0
            for val in workingSet:
                ret += val // n
                if ret >= k:
                    return True
            return False

        best = -1
        while maxSize >= minSize:
            
            mid = (maxSize+minSize)//2
            #print(minSize, maxSize, mid, best)
            if(sizeWork(mid, k)):
                if mid >= best:
                    best = mid

                minSize = mid + 1
            else:
                maxSize = mid - 1

        return best
        #binary search for values?

