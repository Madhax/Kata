class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        
        i = 0 
        diff = 0
        group = 0
        while i < len(nums) and group != len(groups):
            
            diff = 0
            while diff+i < len(nums) and diff < len(groups[group]):
                
                if groups[group][diff] != nums[i+diff]:
                    break
                    
                else:
                    diff += 1
                    if diff == len(groups[group]):
                        group += 1
                        i += diff -1
                        break
            i += 1
        
        return group == len(groups)
            