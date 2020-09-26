class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxDiff = 0;
        int prevY = 0;
        for(int y = prices.size()-1; y >= 1; y--) {
            
            for(int x = y-1; x >= 0; x--) {
                if(prices[x] >= prices[y]) {
                    y = x + 1;
                    break;
                }
                int currentDiff = prices[y] - prices[x];
                if(currentDiff > maxDiff) {
                    maxDiff = currentDiff;
                }
            }
        }
        return maxDiff;
    }
};