class Solution {
public:
   
    struct size_less
    {
        template<class T> bool operator()(T const &a, T const &b) const
        { return a.size() < b.size(); }
    };

    static size_t max_line_length(std::vector<std::string> const &lines)
    {
        if(lines.size() == 0) return 0;
        return std::max_element(lines.begin(), lines.end(), size_less())->size();
    }
   
   
    bool allEqual(vector<string>& strs, int index) {
        if(strs.size() == 0) return false;
        if(strs[0].size() <= index) return false;
        char c = strs[0][index];
        for(auto str: strs) {
            if(str.size() <= index) return false;
            if(str[index] != c) return false;
        }
        return true;
    }
   
    string longestCommonPrefix(vector<string>& strs) {
        int x;
        if(strs.size() == 0) return "";
        for(x = 0; x < max_line_length(strs); x++) {
            if(!allEqual(strs, x)) break;
        }
        return strs[0].substr(0, x);
    }
};