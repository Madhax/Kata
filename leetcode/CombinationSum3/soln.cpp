class Solution {
public:
    map<int,bool> hashTable;
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> output;
        map<int,bool> availableDigits{{1,true},
                                      {2,true},
                                      {3,true},
                                      {4,true},
                                      {5,true},
                                      {6,true},
                                      {7,true},
                                      {8,true},
                                      {9,true}};
        recursion(output,  availableDigits, 0, n, k-1, 1);
        return output;
    }
    
    void recursion(vector<vector<int>>& output, map<int,bool>& availableDigits, int currentSum, int targetSum, int level, int product) 
    {
        if(level==0) {
            int complement = targetSum-currentSum;
            if(availableDigits.count(complement) && availableDigits[complement]) {
                auto multi = complement*product;
                //check if set already exists
                if(!hashTable.count(multi)) { 
                    hashTable[multi] = true;
                    vector<int> validSet;
                    availableDigits[complement] = false;
                    for(const auto &myPair : availableDigits) {
                        if(!myPair.second){
                            validSet.push_back(myPair.first);
                        }
                    }
                    availableDigits[complement] = true;
                    output.push_back(validSet);
                }
            }
        }
        else {
            for(const auto &myPair : availableDigits) {
                if (myPair.second && myPair.first + currentSum < targetSum) {
                    availableDigits[myPair.first]=false;
                    recursion(output, availableDigits, myPair.first+currentSum, targetSum, level-1, myPair.first * product);
                    availableDigits[myPair.first]=true;
                }    
            }
        }
        
    }
};