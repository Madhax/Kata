static const auto __ = [](){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    string longestPalindrome(string s) {  
        if(s.size()==1) return s;
        
        int max_index = 0, max_len = 0;
        int i = 0;
        while(i < s.size()){
            int start = i;
            int end = i;
            while(end+1<s.size() && s[end]==s[end+1])   end++;
            i = end+1;
            
            while(start-1>=0 && end+1<s.size() && s[start-1]==s[end+1]){
                start--;
                end++;
            }
            
            int curr_len = end-start+1;
            if(curr_len > max_len){
                max_index = start;
                max_len = curr_len;
            }
            
        }
        
        return s.substr(max_index, max_len);
        
    }
};
