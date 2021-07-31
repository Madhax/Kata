class TrieNode:

    def __init__(self):
        self.val = 0
        self.children = {}
    
    def getSum(self, key):
        if len(key) == 0:
            ret = self.val
            
            for child in self.children.values():
                ret += child.getSum("")
                
            return ret
        
        if key[0] in self.children:
            return self.children[key[0]].getSum(key[1:])
        
        return 0
    
    def add(self, key, val):
        if len(key) == 0:
            self.val = val
            return
        
        if key[0] not in self.children:
            self.children[key[0]] = TrieNode()
            

        self.children[key[0]].add(key[1:], val)
    
            
            
            

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, key, val):
        self.root.add(key, val)
        
    def getSum(self, key):
        return self.root.getSum(key)


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def insert(self, key: str, val: int) -> None:
        self.root.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.root.getSum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)