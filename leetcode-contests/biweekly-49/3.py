class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        
        d = defaultdict(list)
        
        for index, num in enumerate(nums):
            revnum = int(str(num)[::-1])
            
            d[num-revnum].append(index)
            
        output = 0
        
        for key in d.keys():
            if len(d[key]) >= 2:
                output += math.comb(len(d[key]), 2)
        
        return output % (10**9 + 7)
            