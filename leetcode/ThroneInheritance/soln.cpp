class ThroneInheritance {
public:
    
    string _king;
    map<string, vector<string>> _children;
    map<string, bool> _isDead;
    
    ThroneInheritance(string kingName) {
        _king = kingName; 
    }
    
    void birth(string parentName, string childName) {
        if(_children.count(parentName) == 0) {
            vector<string> seed;
            seed.push_back(childName);
            _children[parentName] = seed;
        } else {
            _children[parentName].push_back(childName);
        }
    }
    
    void death(string name) {
        //iterate over map deleting children
        //for (std::pair<string, vector<string>>& children : _children) {
        //    vec.erase(std::remove(children.second.begin(), children.second.end(), name), children.second.end());
        //}
        if(_isDead.count(name) == 0) {
            _isDead[name] = true;
        }
    }
    
    vector<string> getInheritanceOrder() {
        //build inheritance order
        vector<string> output;
        if(_isDead.count(_king) == 0) {
            output.push_back(_king);
        }
        for(auto& iter : _children[_king]) {
            inheritanceHelper(output, iter);
        }
        return output;
    }
    
    void inheritanceHelper(vector<string>& order, string Name) {
        if(_isDead.count(Name) == 0) {
            order.push_back(Name);
        }
        if(_children.count(Name)) {
            for(auto& iter : _children[Name]) {
                inheritanceHelper(order, iter);
            }
        }
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */
