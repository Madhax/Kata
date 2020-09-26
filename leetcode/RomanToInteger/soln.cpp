class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        const char *str = s.c_str();
        while(*str) {
            if(!strncmp(str, "M", 1)) {
                str += 1;
                num += 1000;
                continue;
            }
            if(!strncmp(str, "CM", 2)) {
                str += 2;
                num += 900;
                continue;
            }
            if(!strncmp(str, "D", 1)) {
                str += 1;
                num += 500;
                continue;
            }
            if(!strncmp(str, "CD", 2)) {
                str += 2;
                num += 400;
                continue;
            }
            if(!strncmp(str, "C", 1)) {
                str += 1;
                num += 100;
                continue;
            }
            if(!strncmp(str, "XC", 2)) {
                str += 2;
                num += 90;
                continue;
            }
            if(!strncmp(str, "L", 1)) {
                str += 1;
                num += 50;
                continue;
            }
            if(!strncmp(str, "XL", 2)) {
                str += 2;
                num += 40;
                continue;
            }
            if(!strncmp(str, "X", 1)) {
                str += 1;
                num += 10;
                continue;
            }
            if(!strncmp(str, "IX", 2)) {
                str += 2;
                num += 9;
                continue;
            }
            if(!strncmp(str, "V", 1)) {
                str += 1;
                num += 5;
                continue;
            }
            if(!strncmp(str, "IV", 2)) {
                str += 2;
                num += 4;
                continue;
            }
            if(!strncmp(str, "I", 1)) {
                str += 1;
                num += 1;
                continue;
            }
        }
        return num;
    }
};