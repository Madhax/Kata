class Solution {
public:
    int maximumRequests(int N, vector<vector<int>>& a) {
        int n = a.size();
        vector<int> ind(N, 0);
        int res = 0;
        for (int mask=0; mask<1<<n; mask++) {
            for (int i=0; i<N; i++) ind[i]=0;
            for (int j=0; j<n; j++) {
                if (mask>>j&1) {
                    int from = a[j][0];
                    int to = a[j][1];
                    ind[to]++;
                    ind[from]--;
                }
            }
            bool ok = true;
            for (int x: ind) {
                if (x>0) ok = false;
            }
            if (ok) {
                res = max(res, __builtin_popcount(mask));
            }
        }
        
        return res;
    }
};
