class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def _flatten(nested, flat):
            for ni in nested:
                if ni.isInteger():
                    flat.append(ni.getInteger())        
                else:
                    _flatten(ni.getList(), flat)
            return
        self.current = 0
        self.flattened = []
        _flatten(nestedList, self.flattened)
        # print(self.flattened)
    
    def next(self) -> int:
        result = self.flattened[self.current]
        self.current += 1
        return result
        
    
    def hasNext(self) -> bool:
        return self.current < len(self.flattened)