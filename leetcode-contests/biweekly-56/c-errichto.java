class Solution {
public:
    bool sumGame(string s) {
        int n = s.length();
        int count = 0;
        int diff = 0;
        for(int i = 0; i < n; ++i) {
            if(s[i] == '?') {
                count += (i < n / 2 ? 1 : -1);
            }
            else {
                if(i < n / 2) {
                    diff += s[i] - '0';
                }
                else { 
                    diff -= s[i] - '0';
                }
            }
        }
        if(diff * 2 == -9 * count) {
            return false;
        }
        return true;
    }
};