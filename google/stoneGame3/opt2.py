class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        Explanation here:
            https://www.youtube.com/watch?v=CWTjs46kl5U
        
        Dp Problem: 
                -dp[i] stores the BEST difference (aliceScore - bobScore)
                -we loop from the end of array and pick best (aliceScore - bobScore) from three Alice's options 
                -dp[0] if positive, that means Alice could win

        Example:
        [5,6,7]
        alice has 5, bob has 13, diff is -8
        alice has 11, bob has 7, diff 4
        alice has 18, bob has 0, diff is 18
                     0 1 2
        stoneList = [5,  6,  7]
            dp    = [18, 13, 7, 0]
            
            if dp[0]>0 Alice could win 

        
        '''
        
        n=len(stoneValue)
        dp=[0]*(n+1)
        
        for i in reversed(range(n)):
            opt_1 = stoneValue[i]-dp[i+1] # Alice takes one stone
            
            opt_2 = opt_1
            if i<(n-1): 
                opt_2 = (stoneValue[i]+stoneValue[i+1]) - dp[i+2] # Alice takes two stones
            
            opt_3 = opt_2
            if i<(n-2):
                opt_3 = (stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]) - dp[i+3] # Alice takes three stones
            
            
            dp[i]=max(opt_1, opt_2, opt_3)
            
        
        if dp[0]==0:
            return "Tie"
        elif dp[0]>0:
            return "Alice"
        else:
            return "Bob"
          