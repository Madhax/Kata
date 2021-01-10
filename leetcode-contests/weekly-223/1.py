class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        output = [first]
        
        for val in encoded:
            output.append(val ^ output[-1])
        
        return output