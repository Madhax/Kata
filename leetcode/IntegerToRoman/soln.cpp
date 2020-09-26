class Solution {
public:
    string intToRoman(int num) {
        string output = "";
        while(num > 0) {
            if(num >= 1000) {
                num -= 1000;
                output += "M";
                continue;
            }
            if(num >= 900) {
                output += "CM";
                num -= 900;
                continue;
            }
            if(num >= 500) {
                output += "D";
                num -= 500;
                continue;
            }
            if(num >= 400) {
                output += "CD";
                num -= 400;
                continue;
            }
            if(num >= 100) {
                output += "C";
                num -= 100;
                continue;
            }
            if(num >= 90) {
                output += "XC";
                num -= 90;
                continue;
            }
            if(num >= 50) {
                output += "L";
                num -= 50;
                continue;
            }
            if(num >= 40) {
                output += "XL";
                num -= 40;
                continue;
            }
            if(num >= 10) {
                output += "X";
                num -= 10;
                continue;
            }
            if(num >= 9) {
                output += "IX";
                num -= 9;
                continue;
            }
            if(num >= 5) {
                output += "V";
                num -= 5;
                continue;
            }
            if(num >= 4) {
                output += "IV";
                num -= 4;
                continue;
            }
            if(num >= 0) {
                output += "I";
                num -= 1;
                continue;
            }
        }
        return output;
    }
};