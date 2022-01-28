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
    int lookingFor;
    bool found = false;
    int foundLevel;
    TreeNode* answer;
    
    bool recurse(TreeNode* node, int level) {
        if (found && foundLevel == level) {
            answer = node;
            return true;
        }
        if (node->val == lookingFor) {
            foundLevel = level;
            found = true;
        }
        if (node->left && recurse(node->left, level+1))
            return true;
            
        if (node->right && recurse(node->right, level+1))
            return true;
        
        return false;
    }
public:
    TreeNode* findNearestRightNode(TreeNode* root, TreeNode* u) {
        lookingFor = u->val;
        recurse(root, 0);
        if (found)
            return answer;
        return 0;
    }
};