class Solution {
public:
    unsigned long long limit;

   
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        limit = k;
        if(nums.size() == 0) return 0;
        int numSubArrays = 0;
        int currentProduct = 1;
        int x = 0;
        for(int y = x; y < nums.size(); y++) {
            currentProduct*=nums[y];
                
            while(currentProduct>=limit && x < y) {
                currentProduct/=nums[x++];
            }
                
            if(currentProduct<limit) {
                numSubArrays += y-x+1;
            }
        }
        
        return numSubArrays;
    }
};

