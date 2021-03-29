class Solution:
    def originalDigits(self, s: str) -> str:
#         names = [
#             'zero', 
#             'one',
#             'two',
#             'three',
#             'four',
#             'five',
#             'six',
#             'seven', 
#             'eight', 
#             'nine'
#         ]
        
#         letters = defaultdict(list)
#         for i in range(10): 
#             for c in names[i]: 
#                 letters[c].append(i)
                
                
        # print(letters)
        
        counts = [0] * 10
        counts[0] = s.count('z')
        counts[2] = s.count('w')
        counts[4] = s.count('u')
        counts[6] = s.count('x')
        counts[8] = s.count('g')

        counts[5] = s.count('f') - counts[4]
        
        counts[1] = s.count('o') - counts[0] - counts[2] - counts[4]
        counts[3] = s.count('r') - counts[0] - counts[4]
        counts[7] = s.count('v') - counts[5]

        counts[9] = s.count('i') - counts[5] - counts[6] - counts[8]
        
        res = ''.join(str(i) * counts[i] for i in range(10) if counts[i])
        
        
        
        return res
