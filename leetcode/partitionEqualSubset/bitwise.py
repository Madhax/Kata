class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_val = 0
        bits = 1
        for num in nums:
            sum_val += num
            bits |= bits << num

        return (not sum_val % 2 == 1) and (bits >> (sum_val // 2)) & 1 == 1
