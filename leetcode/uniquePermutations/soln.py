class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res=[]
        self.answer(nums,[])
        return self.res
        
    def answer(self,nums,path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
                
            self.answer(nums[:i]+nums[i+1:],path+[nums[i]])
            