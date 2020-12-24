class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        pivot = len(nums)-2
        while pivot>=0:
            if nums[pivot]<nums[pivot+1]:
                break
            pivot-=1
        if pivot<0:
            return -1
        for i in range(len(nums)-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        num = int(''.join(nums[:pivot+1]+nums[pivot+1:][::-1]))
        return num if num<2**31-1 else -1