# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        dep=1
        stack=[]
        stack.append(root)
        if d==1:
            new_node=TreeNode(v)
            new_node.left=root
            root=new_node
        while dep<d:
            if dep==d-1:
                
                for i in range(len(stack)):
                    new_nodel=TreeNode(v)
                    new_noder=TreeNode(v)
                    if stack[i].left:
                        left=stack[i].left
                    else:
                        left=None
                    if stack[i].right:
                        right=stack[i].right
                    else:
                        right=None
                    stack[i].left=new_nodel
                    stack[i].right=new_noder
                    new_nodel.left=left
                    
                    new_noder.right=right
                break
                    
                
            p=[]
            while len(stack)!=0:
                u=stack.pop()
                if u.left:
                    p.append(u.left)
                if u.right:
                    p.append(u.right)
            stack=p
            dep+=1
        return root
            
                
        