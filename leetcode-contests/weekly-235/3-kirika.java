typedef long long lint;
class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size();
        vector<int>s(nums1);
        sort(s.begin(),s.end());
        lint m=0,d=0;
        for(int i=0;i<n;i++){
            d+=abs(nums1[i]-nums2[i]);
        }
        m=d;
        for(int i=0;i<n;i++){
            lint tmp=-abs(nums1[i]-nums2[i]);
            int j=lower_bound(s.begin(),s.end(),nums2[i])-s.begin();
            if(j>0)m=min(m,d+tmp+abs(s[j-1]-nums2[i]));
            if(j<n)m=min(m,d+tmp+abs(s[j]-nums2[i]));
        }
        return m%1000000007;
    }
};
