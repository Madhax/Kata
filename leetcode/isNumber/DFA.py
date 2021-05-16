'''class Solution:
    def isNumber(self, s: str) -> bool:
        number = re.compile("^[+-]?[0-9]+(\.[0-9]*)?([eE][+-]?[0-9]+)?$|^[+-]?\.[0-9]+([eE][+-]?[0-9]+)?$")
        return number.match(s)'''

class Solution(object):
    def isNumber(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        currentState = 0
        state = [ 
            {'blank': 0, 'sign': 1, 'digit': 2, '.': 3}, 
            {'digit': 2, '.': 3},
            {'digit': 2, '.': 4, 'e': 5, 'blank': 8},
            {'digit': 4},
            {'digit': 4, 'e': 5, 'blank': 8},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7, 'blank': 8},
            {'blank': 8}
        ]
        
        for c in s:
            if c == 'E':
                c = 'e'
            elif c >= '0' and c <= '9':
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [2,4,7,8]:
            return False
        return True