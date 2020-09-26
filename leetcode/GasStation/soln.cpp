class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int min = INT_MAX;
        int curMin = INT_MAX;
        int minLocation;
        int prevMin;
        for(int x = 0; x < gas.size(); x++) {
            curMin = gas[x] - cost[x];
            if(x > 0)  {
                curMin += prevMin;
            }
            if(curMin < min) {
                minLocation = x;
                min = curMin;
            }
            prevMin = curMin;
        }
        if(curMin >= 0) {
            return ((minLocation+1) >= (gas.size())) ? 0 : minLocation+1;
        }
        return -1;
    }
};