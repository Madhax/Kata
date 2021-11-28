class Solution {
    public int minCost(int[] sp, int[] hp, int[] rc, int[] cc) {
        int ans = 0;
        while (sp[0]<hp[0]) {
            ++sp[0];
            ans += rc[sp[0]];
        }
        while (sp[0]>hp[0]) {
            --sp[0];
            ans += rc[sp[0]];
        }
        while (sp[1]<hp[1]) {
            ++sp[1];
            ans += cc[sp[1]];
        }
        while (sp[1]>hp[1]) {
            --sp[1];
            ans += cc[sp[1]];
        }
        return ans;
    }
}