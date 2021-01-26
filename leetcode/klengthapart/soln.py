class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        currentZeroes = float("inf")
        for val in nums:
            if val == 1:
                if currentZeroes < k:
                    return False
                currentZeroes = 0
            else:
                currentZeroes += 1
        return True