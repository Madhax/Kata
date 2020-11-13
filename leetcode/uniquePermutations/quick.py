class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            # only insert up to the first occurrence rest.index(head)
            # because any slot after the first occurrence can be thought as 
            # the duplicate of the first occurrence as the inserted element 
            # and the slot being the existing one.
            res = [path[:i] + [x] + path[i:] for path in res for i in range((path + [x]).index(x) + 1)]

        return res