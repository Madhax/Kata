class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums[:]
        self.l = nums[:]
        self.X = 123456789
        self.Y = 362436069
        self.Z = 521288629
        self.W = 88675123

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.l = self.orig[:]
        return self.l

    def randbelow(self, x) -> int:
        t = self.X ^ (self.X << 11)
        self.X = self.Y
        self.Y = self.Z
        self.Z = self.W
        self.W = self.W ^ (self.W >> 19) ^ t ^ (t >> 8)
        return self.W % x

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        #self.l[:] = self.orig
        for i in reversed(range(1, len(self.l))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = self.randbelow(i + 1)
            self.l[i], self.l[j] = self.l[j], self.l[i]
            
        return self.l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()