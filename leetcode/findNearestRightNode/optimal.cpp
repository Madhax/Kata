class Solution {
public:
    TreeNode* nextNode;
    int level = -1;
    
    TreeNode* findNearestRightNode(TreeNode* root, TreeNode* u) {
        dfs(root, u, 0);        
        return nextNode;
    }
    
    void dfs(TreeNode* curr, TreeNode *target, int currLevel)
    {
        if(!curr) return;
        
        if(curr == target)
            level = currLevel;        
        else if(currLevel == level && !nextNode)
            nextNode = curr;
        else
            dfs(curr->left, target, currLevel+1), dfs(curr->right, target, currLevel+1);
    }
};