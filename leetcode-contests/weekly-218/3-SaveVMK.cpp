class Solution {
    public int concatenatedBinary(int n) {
        long ans = 0;
        int cl = 1;
        for (int i = 1; i <= n; ++i) {
            if (i==(1<<cl))
                cl++;
            ans <<= cl;
            ans += i;
            ans %= 1000000007;
        }
        return (int)ans;
    }
}