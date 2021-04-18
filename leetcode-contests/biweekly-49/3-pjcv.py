class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(x):
            return int(str(x)[::-1])
        
        diffs = [n - rev(n) for n in nums]
        
        count = 0
        counts = collections.Counter()
        for d in diffs:
            count += counts[d]
            counts[d] += 1
        return count % (10 ** 9 + 7)
        