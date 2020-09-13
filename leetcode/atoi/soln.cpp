class Solution {
public:
    int myAtoi(string str) {
        bool isDigits=false;
        int sigNum = 1;
        string number;
        for(int iter = 0; iter < str.length(); iter++){
            if(str[iter] == ' ' && isDigits==false) continue;
            else if(str[iter] == '+' && isDigits==false) {
                isDigits=true;
            }
            else if(str[iter] == '-' && isDigits == false && number.length() == 0) {
                isDigits = true;
                sigNum = -1;
            }
            else if(str[iter] >= '0' && str[iter] <= '9') {
                isDigits = true;
                number += str[iter];
            }
            else if (isDigits) {
                break;
            }
            else if(number.length() > 10) {
                break;
            }
            else {
                break;
            }
        }
        
        long long int response = 0;
        for(int iter = 0; iter < number.length(); iter++) {
            response *= 10;
            response += (int) number[iter]-'0';
            if(response*sigNum>INT_MAX) return INT_MAX;
            if(response*sigNum<INT_MIN) return INT_MIN;
        }
        response *= sigNum;
        return response;
    }
};