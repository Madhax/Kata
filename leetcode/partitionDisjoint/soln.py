class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        s = math.inf
        minr = [s := min(s,x) for x in reversed(nums)]
        minr.reverse()
        
        maxl = [s := max(s,x) for x in nums]
        #print(maxl, maxr, minr)
        for x in range(len(nums)-1):
            if maxl[x] <= minr[x+1]:
                return x+1
        #print(maxr)
        return 0