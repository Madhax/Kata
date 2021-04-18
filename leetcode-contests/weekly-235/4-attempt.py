from itertools import chain, combinations




class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums.sort()
        dpset = set()
        def countSubsequences(arr, n):
      
            # Declare a dp 2d array
            dp = [[0 for i in range(1000)] for j in range(n)]

            # Iterate i from 0 to n - 1
            for i in range(n):    
                dp[i][arr[i]] = 1;
                dpset.add(arr[i])
                # Iterate j from i - 1 to 0
                for j in range(i - 1, -1, -1):       
                    if (arr[j] < arr[i]):

                        for k in range(1000):

                            # Find gcd of two number
                            GCD = gcd(arr[i], k);

                            # dp[i][GCD] is summation of
                            # dp[i][GCD] and dp[j][k]
                            val = dp[i][GCD] + dp[j][k];
                            dp[i][GCD] = val
                            if val > 0 and GCD > 0:
                                dpset.add(GCD)
                            
                            

            # Add all elements of dp[i][1]
            #sum = 0;  
            #for i in range(n):  
            #    sum = (sum + dp[i][1]);

            #for row in dp:
            #    print(row)

            return sum;
  
        dpset = set()
        @functools.cache()
        def dp(index, val):
            
            if index == len(nums):
                return 0
            
            for j in range(i - 1, -1, -1):
                if (arr[j] < arr[i]):
                    for k in range(450):
                        GCD = gcd(arr[i], k);

                            # dp[i][GCD] is summation of
                            # dp[i][GCD] and dp[j][k]
                        val = dp[i][GCD] + dp[j][k];
                        dp[i][GCD] = val
                        if val > 0 and GCD > 0:
                            dpset.add(GCD)
            
        n = len(nums)
        countSubsequences(nums,n)
        #print()
        return len(dpset)
        