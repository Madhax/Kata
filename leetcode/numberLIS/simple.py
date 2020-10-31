class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = [1] * len(nums)
        count = [1] * len(nums)
        max_len = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]
        max_length = max(length)
        return sum([count[i] for i in range(len(nums)) if length[i] == max_length]) 