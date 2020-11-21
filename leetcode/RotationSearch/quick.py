class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0: return False
        end = n - 1
        start = 0
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if not nums[start] != nums[mid]:
                start += 1
                continue
            pivotArray = nums[start] <= nums[mid]
            targetArray = nums[start] <= target
            if pivotArray ^ targetArray:
                if pivotArray:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False