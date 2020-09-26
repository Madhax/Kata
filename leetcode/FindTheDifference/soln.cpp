class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> characterInstances;
        for(auto& c : s) {
            if(characterInstances.count(c) == 0) {
                characterInstances[c]=1;
            }
            else {
                characterInstances[c]++;
            }
        }
        for(auto& c : t) {
            if(characterInstances.count(c) == 0) {
                characterInstances[c]=1;
            }
            else {
                characterInstances[c]++;
            }
        }
        for ( const auto &myPair : characterInstances ) {
            if(myPair.second%2) {
                return myPair.first;
            }
        }
        return 'x';
    }
};

