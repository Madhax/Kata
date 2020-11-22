class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if k == n*26:
            return "z"*n
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        zs = "z"*((k-n)//25)
        ayes = "a"*(n-len(zs)-1)
        mid = alpha[(k-n)%25]
        return ayes+mid+zs