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

//2

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;

        int orig_x = x, rev_x = 0;
        while (x)
        {
            int digit = x % 10;
            if (rev_x > INT_MAX / 10 ||
                (rev_x == INT_MAX / 10 && digit > INT_MAX % 10))
                return false;

            rev_x = (rev_x * 10) + digit;
            x /= 10;
        }

        if (rev_x == orig_x) return true;

        return false;
    }
};