class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        nodeCount = 1
        for c in preorder:
            nodeCount -= 1
            if nodeCount < 0:
                return False
            if c != "#":
                nodeCount += 2
        return nodeCount == 0