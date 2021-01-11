#using fenwick/BIT 
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        max_num = max(instructions)
        BIT = [0] * (max_num + 1)
        count = [0] * (max_num + 1)
        res = 0
        mod = 10**9 + 7
        
        def update(num):
            while num <= max_num:
                BIT[num] += 1
                num += num & (-num)
            
        def range_sum(num):
            c = 0
            while num > 0 :
                c += BIT[num]
                num -= num & (-num)
            return c
        
        for i,num in enumerate(instructions):
            tmp = range_sum(num)
            res = (res + min(tmp-count[num],i-tmp)) % mod
            update(num)
            count[num] += 1
        
        return res