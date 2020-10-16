class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a = nums[len(nums)-k:]
        a += nums[0: len(nums) - k]
        nums[:] = a