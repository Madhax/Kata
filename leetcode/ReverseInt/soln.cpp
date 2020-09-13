class Solution {
public:
    int reverse(int x) {
        //collapse
        long int digits[10];
        long int y; 
        bool isNegative = (x < 0) ? true : false;
        y = x;
        if(isNegative) y = y * -1;
        int iter = 0;
        while(y >= 1) {
            int digit = y % 10;
            digits[iter] = digit;
            y -= digit;
            y /= 10;
            iter++;
        }
        //build
        long long int response=0;
        for(int iter2=0; iter2 < iter; iter2++)
        {
            response = response * 10 + digits[iter2];
        }
        response = (isNegative) ? response * -1 : response;
        return (response > 2147483647 || response < -2147483648) ? 0 : response;
        
    }
};