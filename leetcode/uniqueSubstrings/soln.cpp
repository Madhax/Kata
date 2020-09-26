class Solution {
public:
    int maximumValue = 1;

    void recursive(set<string>& workingSet, string currentString, int depth) {
        //cout << currentString << "\n";
        if(currentString.size() == 0) return;
        if(workingSet.find(currentString) == workingSet.end() && (depth+1) > maximumValue) {
            maximumValue = depth+1;
            //cout << "new\n";
            //for(auto iter = workingSet.begin(); iter != workingSet.end(); iter++) {
            //    cout << *iter << "\n";
            //}
            //cout << currentString << "\n";
        }
        string token;
        for(int x = 1; x < currentString.size(); x++) {
            token = currentString.substr(0, x);
            if(workingSet.find(token) == workingSet.end()) {
                workingSet.insert(token);
                recursive(workingSet, currentString.substr(x), depth+1);
                workingSet.erase(token);
            }
        }
    }
    
    int maxUniqueSplit(string s) {
        set<string> workingSet;
        string token;
        //if(s.size() == 1) return 0;
        for(int x = 1; x < s.size(); x++) {
            token = s.substr(0, x);
            if(workingSet.find(token) == workingSet.end()) {
                workingSet.insert(token);
                recursive(workingSet, s.substr(x), 1);
                workingSet.erase(token);
            }
        }
        return maximumValue;
    }
}; 