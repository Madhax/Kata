class Solution {
public:
    
    int dp[2005];
    int tmp[2005];
    
    int minChanges(vector<int>& nums, int k) {
        fill(dp, dp+(1<<10), 100000);
        dp[0] = 0;
        for(int i = 1; i<=k; i++){
            unordered_map<int, int> mp;
            int cnt = 0;
            for(int j = i-1; j<nums.size(); j+=k){
                mp[nums[j]]++;
                cnt++;
            }
            int mn = nums.size();
            for(int x = 0; x<1<<10; x++){
                mn = min(mn, dp[x]);
            }
            for(int x = 0; x<1<<10; x++){
                tmp[x] = mn + cnt;
                for(auto p : mp){
                    //cout << p.first << " " << p.second << endl;
                    tmp[x] = min(tmp[x], dp[x^p.first] + cnt - p.second);
                }
            }
            for(int x = 0; x<1<<10; x++){
                dp[x] = tmp[x];
            }
        }
        return dp[0];
    }
};
