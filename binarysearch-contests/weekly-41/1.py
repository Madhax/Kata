class Solution:
    def solve(self, nums):

        iter = 0
        foundOne = False
        EndOfOne = False
        while iter < len(nums):
            if not EndOfOne and nums[iter] == 1:
                foundOne = True

            elif foundOne and not EndOfOne and nums[iter] != 1:
                EndOfOne = True

            elif nums[iter] == 1 and EndOfOne:
                return False

            iter += 1

        return True
