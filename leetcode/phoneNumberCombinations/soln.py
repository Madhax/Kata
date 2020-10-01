class Solution:
    output = list()
    mapping = dict(
        {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
         )
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        self.output.clear()
        filler = list(" " * len(digits))
        def helper(digits, filler, offset):
            for character in self.mapping[digits[offset]]:
                filler[offset] = character
                if offset == len(digits) - 1:
                    self.output.append("".join(filler))
                else:
                    helper(digits, filler, offset+1)
                    
        helper(digits, filler, 0)
        return self.output
                