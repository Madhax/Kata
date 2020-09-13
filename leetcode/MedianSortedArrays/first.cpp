class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> dst;
        std::merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), std::back_inserter(dst));
        double index = dst.size()/2.0;
        if(ceil(index) == index) {
            return (dst[index] + dst[index-1]) / 2.0;
        }
        return dst[floor(index)];
    }
};