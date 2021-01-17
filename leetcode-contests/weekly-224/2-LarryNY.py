class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = collections.Counter()
        
        N = len(nums)
        for index in range(N):
            for index2 in range(index):
                counts[nums[index] * nums[index2]] += 1
            
        total = 0
        for y in counts.values():
            total += math.comb(y, 2) * 8
        return total