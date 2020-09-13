class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int>* dst;
        //std::merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), std::back_inserter(dst));
        dst = buildVector(nums1, nums2);
        double index = dst->size()/2.0;
        if(ceil(index) == index) {
            return ((*dst)[index] + (*dst)[index-1]) / 2.0;
        }
        return (*dst)[floor(index)];
    }
    
    vector<int>* buildVector(vector<int>& nums1, vector<int>& nums2) {
        auto it1 = nums1.begin();
        auto it2 = nums2.begin();
        vector<int>* output = new vector<int>();
        while(it1 != nums1.end() || it2 != nums2.end()) 
        {
            if(it1 == nums1.end()) 
            {
                output->push_back(*it2);
                it2++;
                continue;
            }
            if(it2 == nums2.end()) 
            {
                output->push_back(*it1);
                it1++;
                continue;
            }
            if(*it1 > *it2) 
            {
                output->push_back(*it2);
                it2++;
            }
            else 
            {
                output->push_back(*it1);
                it1++;
            }
        }
        return output;
    }
};