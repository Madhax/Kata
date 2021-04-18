const int MAX = 2e5 + 1;

bool cnt[MAX];

class Solution {
public:
    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        memset(cnt, 0, sizeof(cnt));
        for (int x : nums)
            cnt[x] = true;
        int ret = 0;
        for (int x=1; x<MAX; x++) {
            int g = 0;
            for (int y=x; y<MAX; y+=x)
                if (cnt[y])
                    g = __gcd(g, y);
            if (g == x)
                ret++;
        }
        return ret;
    }
};