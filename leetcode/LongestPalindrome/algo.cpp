class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty() || s.size() < 1) return "";
        string res;
        int max_len = 0;
        for (int i = 0; i < s.size(); i++) {
            int l = i, r = i;
            //pgryciuk - slide same character
            while(r + 1 < s.size() && s[r+1] == s[i]) {
                r++;
                i++;
            }
            while(l - 1 >= 0 && r + 1 < s.size() && s[l-1] == s[r+1]) {
                r++;
                l--;
            }
            if (r - l + 1 > max_len) {
                max_len = r - l + 1;
                res = s.substr(l, max_len);
            }
        }
        return res;
    }
   
};