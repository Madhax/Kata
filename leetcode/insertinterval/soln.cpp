class Solution {
public:
    
    void merge(vector<int>& l, vector<int>& r) {
        l[0] = min(l[0], r[0]);
        l[1] = max(l[1], r[1]);
    }
    
    bool doesOverlap(vector<int>& l, vector<int>& r) {
        //if(l[0] <= r[0] && l[1] >= r[0]) return true;
        //if(l[1] >= r[0] && r[1] >= l[1]) return true;
        if(r[0] <= l[1] && r[1] >= l[1]) return true;
        if(r[1] >= l[0] && r[0] <= l[0]) return true;
        if(r[0] >= l[0] && r[1] <= l[1]) return true;
        if(l[0] >= r[0] && l[1] <= r[1]) return true;
        return false;
    }
    
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        bool inserted = false;
        vector<vector<int>> output;
        if(intervals.size() == 0)
        {
            output.push_back(newInterval);
            return output;
        }
        for(int x = 0; x < intervals.size(); x++) {
            if(doesOverlap(intervals[x], newInterval) && inserted == false) {
                vector<int> merger = intervals[x];
                merge(merger, newInterval);
                int y;
                for(y = x+1; y < intervals.size(); y++)
                {
                    if(doesOverlap(merger, intervals[y]))
                    {
                        merge(merger, intervals[y]);
                    }
                    else {
                        break;
                    }
                }
                output.push_back(merger);
                x=y-1;
                inserted = true;
            }
            //insert at beginning
            else if (newInterval[1] < intervals[x][0] && inserted == false)
            {
                output.push_back(newInterval);
                output.push_back(intervals[x]);
                inserted = true;
            }
            //insert in middle
            else if (x < intervals.size()-1 && intervals[x][1] < newInterval[0] && intervals[x+1][0] > newInterval[1])
            {
                output.push_back(intervals[x]);
                output.push_back(newInterval);
                inserted = true;
            }
            else {
                output.push_back(intervals[x]);
            }
        }
        //insert at end
        if(!inserted) 
        {
            output.push_back(newInterval);
        }
        return output;
    }
};