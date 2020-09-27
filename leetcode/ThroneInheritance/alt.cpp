class ThroneInheritance {
public:
    map<string,vector<string>> g;
    unordered_set<string> dead;
    string kk;
    
    void dfs(vector<string>& res, string at) {
        if (dead.find(at) == dead.end()) {
            res.push_back(at);
        }
        for (string to: g[at]) {
            dfs(res, to);
        }
    }
    ThroneInheritance(string kingName) {
        g[kingName];
        kk = kingName;
    }
    
    void birth(string parentName, string childName) {
        g[parentName].push_back(childName);
    }
    
    void death(string name) {
        dead.insert(name);
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> res;
        dfs(res, kk);
        return res;
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */