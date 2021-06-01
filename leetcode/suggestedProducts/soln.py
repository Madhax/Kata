class TreeNode():
    def __init__(self):
        self.children = {}
        self.end = False
        
    def add(self, word):
        if word == "":
            self.end = True
            return
        
        else:
            if word[0] not in self.children:
                self.children[word[0]] = TreeNode()
                
            self.children[word[0]].add(word[1:])
            
    
    def getWords(self, prefix, index):
        if index == len(prefix):
            return sorted(list(self.enum(prefix, set())))[:3]
        
        if prefix[index] not in self.children:
            return []
        
        else:
            return self.children[prefix[index]].getWords(prefix, index+1)
        
        
    def enum(self, prefix, words):
        if self.end == True:
            words.add(prefix)
        
        if len(words) == 3:
            return words 
        
        for c in sorted(self.children.keys()):
            words |= self.children[c].enum(prefix + str(c), words)
            if len(words) == 3:
                return words 
            
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TreeNode()
        for product in products:
            root.add(product)
            
        output = []
        
        for x in range(1, len(searchWord)+1):
            output.append(root.getWords(searchWord[:x], 0))
            
        return output