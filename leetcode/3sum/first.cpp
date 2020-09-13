class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int> > output;
        vector<int> row;
        std::sort(nums.begin(), nums.end());
        set<vector<int>> myset;
        for(int z = 0; z < nums.size(); z++) {
            int left = z+1;
            int right = nums.size()-1;
            while(left<right) 
            {
                int value = nums[z] + nums[left] + nums[right];
                bool found = false;
                if(value == 0) 
                {
                    row.push_back(nums[z]);
                    row.push_back(nums[left]);
                    row.push_back(nums[right]);
                    myset.insert(row);
                    row.clear();
                    left++;
                    right--;
                }
                else if(value > 0) 
                {
                    right--;
                }
                else 
                {
                    left++;
                }
            }
        }
        for(auto iterator = myset.begin(); iterator!=myset.end(); iterator++) {
            output.push_back(*iterator);
        }
        return output;
    }
};
