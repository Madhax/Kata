class MapSum:
    def __init__(self):
        self.map = {}
        
    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        s, l = 0, len(prefix)
        for k in self.map.keys():
            if l> len(k): continue
            elif prefix == k[0:l]: s += self.map[k]
        return s 