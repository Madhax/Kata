class Solution {
public:
    static bool comparator(const int & l, const int & r)
    {
        if(l==r) return 0;
        
        if(log10 ((int)l) == log10((int)r)) {
            return l>r;
        }
        else {
            string workingl = to_string(l);
            string workingr = to_string(r);
            
            return (stoll(workingl+workingr) > stoll(workingr+workingl));
            //return (to_string(l) > to_string(r));
        }
    }
    
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), comparator);
        string output = "";
        bool nonZero = false;
        for(auto& iter : nums) {
            if(iter) {
                nonZero = true;
                output += to_string(iter);
            }
            else if(!nonZero && output.size() == 0) {
                output += to_string(iter);
            }
            else if(nonZero) {
                output += to_string(iter);
            }
            
        }
        return output;
    }
};