class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        int N = tasks.size(), M = workers.size();
        int ok = 0, ng = min(N, M) + 1;
        while (ng - ok > 1) {
            const int c = (ok + ng) / 2;
            
            multiset<int> ms;
            for (int i = 0; i < c; ++i) ms.insert(tasks[i]);
            int rem_p = pills;
            bool good = true;
            for (int w = M - c; w < M; ++w) {
                int p = workers[w];
                if (*ms.begin() <= p) {
                    ms.erase(ms.begin());
                    continue;
                } else {
                    p += strength;
                    rem_p--;
                    auto itr = ms.upper_bound(p);
                    if (itr == ms.begin()) {
                        good = false;
                        break;
                    } else {
                        ms.erase(prev(itr));
                    }
                }
            }
            if (rem_p < 0) good = false;
            (good ? ok : ng) = c;
        }
        return ok;
    }
};