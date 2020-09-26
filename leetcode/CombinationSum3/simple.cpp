class Solution {
    vector<int> ans;
public:
    
    void f(int p,int k,int nd, vector<vector<int>> &good, int pref, int target){
        if(p==k) {
            if(pref==target){
                good.push_back(ans);
            }
            return;
        }
        if(p>k) return;
        for(int i=nd+1;i<10;i++){
            ans.push_back(i);
            f(p+1,k, i, good, pref+i, target);
            ans.pop_back();
        }
        return;
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> good;
        
        f(0,k,0,good, 0, n);
        
        
        return good;
    }
};