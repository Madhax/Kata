class Solution:
    def solve(self, nums):
        
        N = len(nums)

        array1 = [x for x in range(1, N+1)]
        array2 = [x for x in range(1, N+1)]
        array2.sort(reverse=True)

        index = nums.index(1)

        shift1 = nums[index:] + nums[:index]
        shift2 = nums[index+1:] + nums[:index+1]

        print(shift2)
        if shift1 == array1 or shift1 == array2:
            return True
        
        if shift2 == array1 or shift2 == array2:
            return True

        return False
