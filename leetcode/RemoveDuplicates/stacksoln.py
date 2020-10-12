class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        """
        cdadabcc
        
        01234567
        43131244
        
        1: 2, 4
        2: 5
        3: 1, 3
        4: 0, 6, 7
        
        stack = []
        c d 
        a d b c 
        
        """
        
        last_index = {}
        
        for i, char in enumerate(s):
            last_index[char] = i
            
        stack = []
        used  = set()
        
        i = 0
        while i < len(s):
            curr_char = s[i]
            if curr_char not in used:
                while stack and stack[-1] > curr_char and i < last_index[stack[-1]]:
                    used.discard(stack.pop())
                used.add(curr_char)
                stack.append(curr_char)
            i += 1
        
        return ''.join(stack)