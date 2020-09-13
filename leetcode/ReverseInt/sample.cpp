class Solution {
public:
    int reverse(int x) {
        // return 0 is x is 0
        if(x==0)
            return 0;
        
        long y=0;
        while(x!=0) {
            y = y*10;
            y += x%10;
            x /= 10;
        }
        if(y>INT_MAX || y<INT_MIN)
            return 0;
        return y;
    }
};