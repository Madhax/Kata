
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()==0)
            return 0;
        if(prices.size()==1)
            return 0;
        int min=prices[0],max=prices[1]-prices[0];
        for(int i=0;i<prices.size();i++) {
            
            if(prices[i]-min>max)
                max = prices[i]-min;
            if(prices[i]<min)
                min=prices[i];
        }
        
        return max;
    }
};


50000/21.14 * 0.12