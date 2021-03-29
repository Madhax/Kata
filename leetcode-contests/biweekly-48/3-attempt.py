class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ctr = 1
        print(coins)
        for coin in coins:
            print(ctr, coin)
            if coin > ctr:
                break
            ctr += coin
            
        
        return ctr
        
        
        
        """class Solution {
    public int getMaximumConsecutive(int[] A) {
        Arrays.sort(A);
        int res=1;
        for(int i=0;i<A.length;i++){
            if(A[i]>res)break;
            res+=A[i];
        }
        
        return res;
        
    }
}"""