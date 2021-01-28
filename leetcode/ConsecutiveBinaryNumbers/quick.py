    
class Solution:
    ansList =[0,1]
    mod = 10**9+7
    ans = 1
    fast = 4
    carry = 2
    for num in range(2,100001):
        if num==fast:
            fast*=2
            carry+=1
        ans = ((ans<<carry)+num)%mod
        ansList.append(ans)
    def concatenatedBinary(self, n: int) -> int:
        return Solution.ansList[n]