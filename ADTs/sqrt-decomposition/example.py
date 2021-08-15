from math import sqrt, ceil

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        n = len(nums)

        self.m = int(sqrt(n))
        self.small_sums = [0] * (ceil(n/self.m))

        for i in range(n):
            self.small_sums[i//self.m] += nums[i]

    def update(self, index, val):
        change = val - self.nums[index]

        self.small_sums[index//self.m] += change
        self.nums[index] = val

    def sumRange(self, left, right):
        result = 0

        s_left = left//self.m
        s_right = right//self.m

        for i in range(s_left, s_right+1):
            result += self.small_sums[i]

        if left % self.m != 0:
            for i in range(s_left*self.m, left):
                result -= self.nums[i]

        right_end = min(len(self.nums), (s_right+1) * self.m)
        for i in range(right+1, right_end):
            result -= self.nums[i]

        return result

            
