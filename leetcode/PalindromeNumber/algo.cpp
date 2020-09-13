class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x % 10 == 0 && x != 0)) return false;
        //int temp=x,r=0;
        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        //return (x==r)? true:false;
        //return (x==r);
        return x == revertedNumber || x == revertedNumber/10;
    }
};