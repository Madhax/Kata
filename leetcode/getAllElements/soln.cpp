/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    //void addElements(vector<int>&, TreeNode*);
    void addElements(vector<int>& vals, TreeNode* node) {
        if (node != NULL) {
            vals.push_back(node->val);
            addElements(vals,node->left);
            addElements(vals,node->right);
        }
    }
    
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> vals;
        
        addElements(vals, root1);
        addElements(vals, root2);
        
        std::sort(vals.begin(), vals.end());
        
        return vals;
        
    }
};