class LL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None] * 2000
        
    def __hash__(self, val):
        
        return val % 2000
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        #print("put", key, value)
        myhash = self.__hash__(key)
        
        node = self.data[myhash]
        if node is None:
            newnode = LL(key, value)
            self.data[myhash] = newnode
            return
        
        while node:
            if node.key == key:
                node.val = value
                return
            
            node = node.next
        
        newnode = LL(key, value)
        newnode.next = self.data[myhash]
        self.data[myhash] = newnode
        return
    
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        #print("get", key)
        myhash = self.__hash__(key)
        node = self.data[myhash]
        
        while node and node.key != key:
            node = node.next
        
        if node is None:
            return -1
        
        return node.val

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        myhash = self.__hash__(key)
        node = self.data[myhash]
        if node is None:
            return
        
        if node.key == key:
            self.data[myhash] = node.next
            del node
            return
        
        while node.next and node.next.key != key:
            node = node.next
            
        if node.next is None:
            return
        
        backup = node.next
        node.next = node.next.next
        del backup


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)