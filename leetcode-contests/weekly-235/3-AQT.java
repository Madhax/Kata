class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        vector<int> srt;
        for(int n : nums1){
            srt.emplace_back(n);
        }
        srt.emplace_back(-1000000);
        srt.emplace_back(1000000);
        sort(srt.begin(), srt.end());
        int mn = 0;
        int tot = 0;
        for(int i = 0; i<nums2.size(); i++){
            int idx = lower_bound(srt.begin(), srt.end(), nums2[i]) - srt.begin();
            mn = min(mn, abs(nums2[i] - srt[idx]) - abs(nums1[i] - nums2[i]));
            mn = min(mn, abs(nums2[i] - srt[idx-1]) - abs(nums1[i] - nums2[i]));
            tot += abs(nums1[i] - nums2[i]);
            tot %= 1000000007;
        }
        tot += mn;
        tot += 1000000007;
        tot %= 1000000007;
        return tot;
    }
};
