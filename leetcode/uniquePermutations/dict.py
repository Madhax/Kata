class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        seen = {}
        first = nums[0]
        remainder = nums[1:]
        
        remainder_perms = self.permuteUnique(remainder)
        for remainder_perm in remainder_perms:
            for pos in range(len(nums)):
                curr_perm = remainder_perm.copy()
                curr_perm.insert(pos, first)
                seen[str(curr_perm)] = curr_perm
        return seen.values()