class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        if(x<10) return true;
        vector<int> digits;
        int original = x;
        int digit;
        while(x>=1) {
            digit = x % 10;
            digits.push_back(x%10);
            x -= digit;
            x = x / 10;
        }
        long int reversed = 0;
        while(digits.size()) {
            digit = digits.front();
            digits.erase(digits.begin());
            reversed += digit;
            if(digits.size()) reversed*=10;
        }
        return(original==reversed);
    }
};