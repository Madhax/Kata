class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxValue = [0]
        
        def dfs(root):
            # returns (sum_value, num_nodes)
            if not root:
                return (0, 0)
            
            
            left_val, left_n = dfs(root.left)
            right_val, right_n = dfs(root.right)
            out = (root.val + left_val + right_val, 1 + left_n + right_n)
            
            maxValue[0] = max(out[0] / out[1], maxValue[0])
            return out
    
        dfs(root)
        return maxValue[0]