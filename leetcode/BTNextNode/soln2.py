class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        tree = dict(level) where it returns array of [val, node ptr]
        populate tree and then recursively fill out next ptr based on current level + value
        """
        if root == None:
            return root
       
        q = []
        q.append([root, 0])
        while q:
            (node, level) = q.pop(0)
            if node.left:
                q.append([node.left, level+1])
               
            if node.right:
                q.append([node.right, level+1])
               
            if len(q) and q[0][1] == level:
                node.next = q[0][0]
            else:
                node.next = None
       
        return root