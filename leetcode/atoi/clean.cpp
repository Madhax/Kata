lass Solution {
public:
    int myAtoi(string str) {
        long long ans = 0;
        
        // first eliminate whitespaces in the beginning of the string
        int ptr = 0;
        int n = str.size();
        
        while (ptr < n && str[ptr] == ' ') ++ptr;
        
        // now we are at the first non-whitespace character
        // it has to be a number, a '+' or a '-'
        // otherwise return 0
        
        if (!(str[ptr] == '-' || str[ptr] == '+' || (str[ptr] >= '0' && str[ptr] <= '9'))) return 0;
        
        bool isNegative = false;
        if (str[ptr] == '-' || str[ptr] == '+') {
            isNegative = str[ptr] == '-';
            ++ptr;
        }
        
        // now we expect a number
        if (str[ptr] < '0' || str[ptr] > '9') return 0;
        while (ptr < n && str[ptr] >= '0' && str[ptr] <= '9') {
            ans *= 10;
            ans += str[ptr] - '0';
            if (isNegative && -ans < INT_MIN) return INT_MIN;
            if (!isNegative && ans > INT_MAX) return INT_MAX;
            ++ptr;
        }
        
        if (isNegative) ans = -ans;
        return int(ans);
    }
};