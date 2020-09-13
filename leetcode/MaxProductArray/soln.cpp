class Solution {
public:
    int maxProduct(vector<int>& nums) {
        long long int maxProductResult = INT_MIN;
        vector<int> maxProducts(nums.size());
        vector<int> minProducts(nums.size());
        maxProducts[0] = nums[0];
        minProducts[0] = nums[0];
        for(int iter = 1; iter<nums.size(); iter++) {
            maxProducts[iter] = max(nums[iter],max(maxProducts[iter-1]*nums[iter],nums[iter]*minProducts[iter-1]));
            minProducts[iter] = min(nums[iter],min(maxProducts[iter-1]*nums[iter],nums[iter]*minProducts[iter-1]));
        
        }
        return *(max_element(maxProducts.begin(), maxProducts.end()));
    }
};