class Solution {
public:
    
    struct TrieNode {
        TrieNode* zero;
        TrieNode* one;
    };
    
    void addNode(TrieNode* node, int val, unsigned int flag) {
        if (flag == 0) {
            return;
        }
        if (val&flag) {
            if (node->one == 0) {
                node->one = new TrieNode();
            }
            addNode(node->one, val, flag>>1);
        }
        else {
            if (node->zero == 0) {
                node->zero = new TrieNode();
            }
            addNode(node->zero, val, flag>>1);
        }
    }
    
    int findInv(TrieNode* node, int val, unsigned int flag) {
         if (flag == 0 || node == 0) {
             return 0;
         }
        
        if (val&flag) {
            if (node->zero) {
                return 0 | findInv(node->zero, val, flag>>1);
            }
            return flag | findInv(node->one, val, flag>>1);
        }
        else {
            //cout << val << " " << flag << "\n";
            if (node->one) {
                return flag | findInv(node->one, val, flag>>1);
            }
            return findInv(node->zero, val, flag>>1);
        }
    }
    
    int findMaximumXOR(vector<int>& nums) {
        int max = 0;
        int cur = 0;
        
        TrieNode* root = new TrieNode();
        
        for (auto& it : nums) {
            addNode(root, it, 1<<31);
        }
        
        for (auto& it: nums) {
            int bestCand = findInv(root, it, 1<<31);
            max = std::max(bestCand^it, max);
            //cout << it << " " << bestCand << "\n";
        }
        
        return max;
    }
};