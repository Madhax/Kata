class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp=0
        c=0
        for i in s:
            if i=='1':
                c+=1
            else:
                dp=min(dp+1,c)
        return dp