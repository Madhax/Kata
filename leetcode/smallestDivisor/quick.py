class Solution:
    def smallestDivisor(self, nums: List[int], t: int) -> int:
        '''
        div, mod = divmod(num, p)
        div += mod!=0
        
        BS:
        FFFFTTTTT
        
        largest valud is max(nums), which gives results len(nums) must <= t, otherwise no solution
        '''
        def getValue(v):
            return sum((num+v-1)//v for num in nums)
            
        i, j = 1, max(nums)
        sol = j
        while i<=j:
            mid = (i+j)>>1
            count = getValue(mid)
            if count<=t:
                sol = mid
                j = mid-1
            else:
                i = mid + 1
        return sol
        