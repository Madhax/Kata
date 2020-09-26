class Solution {
public:
    map<int, int> counter;
    vector<int> majorityElement(vector<int>& nums) {
        for(auto& num : nums) {
            if(counter.count(num) == 0) {
                counter[num] = 1;
            }
            else {
                counter[num]++;
            }
        }
        int majority = nums.size()/3;
        vector<int> output;
        for(std::map<int,int>::iterator iter = counter.begin(); iter != counter.end(); ++iter)
        {
            if(iter->second > majority) {
                output.push_back(iter->first);
            }
        }
        return output;
    }
};