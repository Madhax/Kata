def makeRange(ci, cj):
    if ci == cj:
        return str(ci)
    else:
        return f"{ci}->{cj}"

class Solution:
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        idx, ci, cj = nums[0]-1, nums[0], nums[0]
        res = []
        
        for n in nums:
            if n != (idx+1):
                res.append(makeRange(ci, cj))
                ci = idx = n
            else:
                idx += 1
            cj = n
        
        res.append(makeRange(ci, cj))
        return res
                
        
