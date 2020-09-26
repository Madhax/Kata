// using 1000 stops
    bool carPooling(vector<vector<int>>& trips, int capacity){
        vector<int> stops(1001); 
        for (vector<int>& trip: trips){
            stops[trip[1]] += trip[0]; 
            stops[trip[2]] -= trip[0];
        }

        int n = 0; 
        for (int i = 0; i < 1001; ++i){
            n += stops[i]; 
            if (n > capacity) return false;
        }
        return true; 
    }
    
    
    // intuition
//     bool carPooling(vector<vector<int>>& trips, int capacity) {
//         set<int> stops;
//         unordered_map<int, int> pick, drop; 
//         for (vector<int>& trip: trips){
//             pick[trip[1]] += trip[0]; 
//             drop[trip[2]] += -trip[0];
//             stops.insert(trip[1]); 
//             stops.insert(trip[2]);  
//         }

//         int n = 0; 
//         for (auto stop: stops){
//             if (pick.count(stop)) n += pick[stop]; 
//             if (drop.count(stop)) n += drop[stop]; 
//             if (n > capacity) return false; 
//         }
//         return true; 
//     }
}; 
