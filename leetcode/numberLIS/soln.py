class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def binary_search(k):
            (a,b)=(-1,len(data))
            while((b-a)>1):
                piv=(a+b)//2
                if (n<=data[piv][0]):
                    b=piv
                else:
                    a=piv
            return(a)
       
        big=1111111
        data=[[-big,{-big:1}]]
        # data[j]=== [minEndVal,{v:multiplicity for v in endvals}]
        for n in nums:
            new_len = binary_search(n)+1
            keylist = list(data[new_len-1][1].keys())
            for key in keylist:
                if (key>=n):
                    del data[new_len-1][1][key]
            if (new_len==len(data)):
                data.append([n,{n:sum(data[-1][1].values())}])
            else:
                data[new_len][1][n] = data[new_len][1].get(n,0) + sum(data[new_len-1][1].values())
                data[new_len][0] = min(n,data[new_len][0])
        return(sum(data[-1][1].values()) if nums else 0) 
