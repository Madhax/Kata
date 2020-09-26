class Solution {
public:
    int romanToInt(string s) {
        
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            
            char ch = s[i];
            char next = s[i+1];
            
            if (ch == 'I') {
                if (next == 'V'){
                    res += 4;
                    i++;
                } else if (next == 'X') {
                    res += 9;
                    i++;
                } else {
                    res += 1;
                }
            } else if (ch == 'X') {
                if (next == 'L'){
                    res += 40;
                    i++;
                } else if (next == 'C') {
                    res += 90;
                    i++;
                } else {
                    res += 10;
                }
            } else if (ch == 'C') {
                if (next == 'D'){
                    res += 400;
                    i++;
                } else if (next == 'M') {
                    res += 900;
                    i++;
                } else {
                    res += 100;
                }
            } else if (ch == 'V') {
                res += 5;
            } else if (ch == 'L') {
                res += 50;
            } else if (ch == 'D') {
                res += 500;
            } else if (ch == 'M') {
                res += 1000;
            }
            
        }
     
        return res;
    }
};