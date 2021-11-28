class LockingTree:

    def __init__(self, parent: List[int]):
        self.parents = defaultdict(set)
        self.children = defaultdict(set)
        self.locks = defaultdict(lambda: None)
        
        for x in range(20):
            for idx, p in enumerate(parent):
                if idx > 0:
                    self.parents[idx].add(p)
                    self.parents[idx] |= self.parents[p]
                
        for x in range(20):    
            for x in range(len(parent)-1, 0, -1):
                self.children[parent[x]].add(x)
                self.children[parent[x]] |= self.children[x]
                    

        #print(self.children) 
        
    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == None:
            self.locks[num] = user
            return True
        
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = None
            return True
        
        return False

    def upgrade(self, num: int, user: int) -> bool:
        canUpgrade = False
        
        #is unlocked
        if self.locks[num] != None:
            #print(num, user, "locked")
            return False
        
        #all parents unlocked
        for p in self.parents[num]:
            if self.locks[p] != None:
                #print(num, user, "parent locked")
                return False
        
        #one locked desc
        for c in self.children[num]:
            if self.locks[c] != None:
                canUpgrade = True
                break
                
        if canUpgrade:
            self.locks[num] = user
            for child in self.children[num]:
                self.locks[child] = None
                
            return True
                
        #print(num, user, "cannot upgrade", self.locks)
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
