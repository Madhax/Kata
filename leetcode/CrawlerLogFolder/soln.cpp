class Solution {
public:
    int minOperations(vector<string>& logs) {
        int operations = 0;
        for(auto& chdir : logs) {
            if(chdir == "./") continue;
            if(chdir.size() == 3 && chdir[0] == '.' && chdir[1] == '.') {
                if(operations>0) operations--;
            }
            else {operations++;}
        }
        return operations;
    }
};
