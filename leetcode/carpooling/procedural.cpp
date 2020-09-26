class Solution {
public:
    vector<vector<int>> events;
   
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int> n(2);
        for(auto& row : trips) {
            n[0] = row[1];
            n[1] = row[0];
            events.push_back(n);
            n[0] = row[2];
            n[1] = row[0]*-1;
            events.push_back(n);
        }  
        sort(events.begin(), events.end());
        int currentCapacity = 0;
        for(int x = 0; x < events.size(); x++) {
            currentCapacity+=events[x][1];
            if(x < events.size()-1 && events[x+1][0] != events[x][0]) {
                if(currentCapacity > capacity) return false;
            }
        }
        if(currentCapacity>capacity) return false;
        /*
        for(auto& row : events) {
            cout << row[0] << " " << row[1] << "\n";
        }*/
       
        return true;
    }
}; 
