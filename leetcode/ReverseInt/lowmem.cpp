class Solution {
public:
    int reverse(int x) {
        long long int res=0;
        int rem;
        while(x){
            rem=x%10;
            res=res*10+rem;
            if(res>INT_MAX || res<INT_MIN)
                return 0;
            x/=10;
        }
        return res;
        
    }
};