from collections import *
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numLength = len(nums)
        k = k % numLength
        deck = deque()
        
        for x in range(0, numLength):
            deck.append(nums[x])
            if x >= k:
                val = deck.popleft()
                nums[x] = val
            
        iter = 0
        while len(deck) > 0:
            nums[iter] = deck.popleft()
            iter += 1
            
        return